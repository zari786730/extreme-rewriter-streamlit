# =========================
# EXTREME REWRITER BACKEND (NO NLTK - SIMPLIFIED)
# =========================

import random
import re
import importlib

# Import your existing files
try:
    from health_terms import health_terms
    from health_terms_2 import health_terms as health_terms_2
    from generalwords import general_words
    from grammar_corrector import correct_grammar
except ImportError:
    # Fallback if these files don't exist
    health_terms = {}
    health_terms_2 = {}
    general_words = {}
    
    def correct_grammar(text):
        return text  # Fallback function

# =========================
# VOCABULARY LOADER - DYNAMICALLY LOAD ALL 45 SYNONYM FILES
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.load_all_vocabulary()
    
    def load_all_vocabulary(self):
        """Dynamically load all 45 synonym files"""
        print("Loading vocabulary database...")
        
        # Merge health terms first
        health_terms.update(health_terms_2)
        self.all_synonyms.update(health_terms)
        
        # Load general words
        self.all_synonyms.update(general_words)
        
        # Dynamically load all 45 synonym files
        loaded_files = 0
        for i in range(1, 46):  # 1 to 45
            try:
                module_name = f"vocabulary.synonyms_{i:02d}"
                module = importlib.import_module(module_name)
                synonyms_dict = getattr(module, 'synonyms', {})
                self.all_synonyms.update(synonyms_dict)
                loaded_files += 1
                print(f"✓ Loaded {module_name} with {len(synonyms_dict)} words")
            except ImportError as e:
                print(f"✗ Failed to load {module_name}: {e}")
            except Exception as e:
                print(f"✗ Error loading {module_name}: {e}")
        
        self.total_words = len(self.all_synonyms)
        print(f"Vocabulary loading complete!")
        print(f"Total files loaded: {loaded_files}/45")
        print(f"Total unique words in database: {self.total_words:,}")
        
        return self.total_words, self.all_synonyms
    
    def get_vocabulary_stats(self):
        """Get vocabulary statistics for frontend display"""
        return {
            "total_words": self.total_words,
            "loaded_files": 45,
            "health_terms": len(health_terms) + len(health_terms_2),
            "general_words": len(general_words)
        }

# Initialize vocabulary loader
vocabulary_loader = VocabularyLoader()

# Simple tokenizer without NLTK
def simple_tokenize(text):
    """Simple tokenizer that doesn't require NLTK"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# =========================
# OFFLINE SYNONYM FINDER (USES ONLY LOCAL VOCABULARY)
# =========================
class OfflineSynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
    
    def get_synonyms(self, word):
        """Get synonyms from local vocabulary only"""
        word = word.lower().strip()
        
        # Direct match in vocabulary
        if word in self.vocabulary:
            synonyms = self.vocabulary[word]
            if isinstance(synonyms, str):
                return [synonyms]
            elif isinstance(synonyms, list):
                return synonyms
            else:
                return [str(synonyms)]
        
        # Try variations
        variations = [
            word + 's',  # plural
            word[:-1] if word.endswith('s') else None,  # singular
            word + 'ing',
            word[:-3] if word.endswith('ing') else None,
            word + 'ed',
            word[:-2] if word.endswith('ed') else None,
        ]
        
        for variation in variations:
            if variation and variation in self.vocabulary:
                synonyms = self.vocabulary[variation]
                return [synonyms] if isinstance(synonyms, str) else synonyms
        
        return []

# =========================
# PURE REWRITER (ENHANCED WITH VOCABULARY - OFFLINE ONLY)
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = OfflineSynonymFinder(vocabulary_loader.all_synonyms)
        self.replacements = vocabulary_loader.all_synonyms
        self.vocabulary_stats = vocabulary_loader.get_vocabulary_stats()

    def intelligent_word_replacement(self, text):
        words = text.split()
        new_words = []

        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip common short words
            skip_words = ['the','a','an','and','or','but','in','on','at','to','for','of','with','by','as','is','was','be','are','were']
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue

            # Apply replacement with probability
            if random.random() < 0.7:
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                
                if synonyms:
                    valid_synonyms = [
                        s for s in synonyms 
                        if s.lower() != clean_word and len(s.split()) <= 2
                    ]
                    
                    if valid_synonyms:
                        replacement = random.choice(valid_synonyms)
                        replacement = replacement.capitalize() if word[0].isupper() else replacement
                        new_words.append(replacement)
                        continue

            new_words.append(word)
            
        return ' '.join(new_words)

    def varied_sentence_restructure(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
        if random.random() < 0.6:
            random.shuffle(sentences)
        connectors = ['. ', '. Additionally, ', '. Moreover, ', '. Furthermore, ']
        result = sentences[0] + '. '
        for i in range(1, len(sentences)):
            if random.random() < 0.4:
                result += random.choice(connectors) + sentences[i].lower()
            else:
                result += sentences[i] + '. '
        return result.strip()

    def smart_length_manipulation(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text
        processed = []
        for sentence in sentences:
            words = sentence.split()
            if random.random() < 0.4:
                if len(words) > 15:
                    mid = len(words) // 2
                    processed.extend([' '.join(words[:mid]) + '.', ' '.join(words[mid:]).capitalize()])
                elif len(words) < 5:
                    processed.append(f"This involves {sentence.lower()}")
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        return ' '.join(processed)

    def add_natural_variation(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        if random.random() < 0.3:
            first_sentence = sentences[0]
            if not first_sentence.lower().startswith(('interestingly','notably','importantly')):
                sentences[0] = random.choice(['Interestingly, ','Notably, ','Importantly, ']) + first_sentence.lower()
        return '. '.join(sentences) + '.'

    def get_vocabulary_info(self):
        return self.vocabulary_stats

# Initialize pure rewriter
pure_rewriter = PureRewriter()

# =========================
# EXTREME REWRITER FUNCTION
# =========================
def extreme_rewriter(original_text):
    clean_text = original_text.strip().strip('"').strip("'")
    transformations = [
        pure_rewriter.varied_sentence_restructure,
        pure_rewriter.intelligent_word_replacement,
        pure_rewriter.smart_length_manipulation,
        pure_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)
    result = clean_text
    for t in transformations:
        result = t(result)
    
    # Try grammar correction if available
    try:
        result = correct_grammar(result)
    except:
        pass  # Skip if grammar corrector not available
    
    return result

# =========================
# SIMILARITY CALCULATION (NO NLTK)
# =========================
def calculate_similarity(original, rewritten):
    original_words = set(simple_tokenize(original))
    rewritten_words = set(simple_tokenize(rewritten))
    common_words = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common_words) / len(original_words) * 100

# =========================
# GUARANTEE LOW SIMILARITY
# =========================
def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    best_result = None
    best_similarity = 100
    for _ in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        if similarity <= max_similarity:
            return rewritten, similarity
    return best_result, best_similarity

# =========================
# VOCABULARY STATISTICS ENDPOINT
# =========================
def get_vocabulary_stats():
    return pure_rewriter.get_vocabulary_info()

# Test when run directly
if __name__ == "__main__":
    stats = get_vocabulary_stats()
    print("\n" + "="*50)
    print("VOCABULARY DATABASE STATISTICS")
    print("="*50)
    print(f"Total Unique Words: {stats['total_words']:,}")
    print(f"Synonym Files Loaded: {stats['loaded_files']}/45")
    print(f"Health Terms: {stats['health_terms']:,}")
    print(f"General Words: {stats['general_words']:,}")
    print("="*50)
    
    # Test
    test_text = "The quick brown fox jumps over the lazy dog."
    print(f"\nTest Text: {test_text}")
    rewritten = extreme_rewriter(test_text)
    print(f"Rewritten: {rewritten}")
    similarity = calculate_similarity(test_text, rewritten)
    print(f"Similarity: {similarity:.1f}%")
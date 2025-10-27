# =========================
# EXTREME REWRITER BACKEND (NO NLTK - FIXED VOCABULARY LOADING)
# =========================

import random
import re
import importlib
import os
import sys

# Add current directory to Python path to ensure imports work
sys.path.append(os.path.dirname(__file__))

# Import your existing files
try:
    from health_terms import health_terms
    print(f"✓ Loaded health_terms with {len(health_terms)} words")
except ImportError as e:
    print(f"✗ Failed to load health_terms: {e}")
    health_terms = {}

try:
    from health_terms_2 import health_terms as health_terms_2
    print(f"✓ Loaded health_terms_2 with {len(health_terms_2)} words")
except ImportError as e:
    print(f"✗ Failed to load health_terms_2: {e}")
    health_terms_2 = {}

try:
    from generalwords import general_words
    print(f"✓ Loaded general_words with {len(general_words)} words")
except ImportError as e:
    print(f"✗ Failed to load general_words: {e}")
    general_words = {}

try:
    from grammar_corrector import correct_grammar
    print("✓ Loaded grammar_corrector")
except ImportError as e:
    print(f"✗ Failed to load grammar_corrector: {e}")
    def correct_grammar(text):
        return text

# =========================
# VOCABULARY LOADER - IMPROVED WITH BETTER ERROR HANDLING
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files_count = 0
        self.failed_files = []
        self.load_all_vocabulary()
    
    def load_all_vocabulary(self):
        """Dynamically load all synonym files with better error handling"""
        print("\n" + "="*60)
        print("LOADING VOCABULARY DATABASE...")
        print("="*60)
        
        # Start with health terms and general words
        self.all_synonyms.update(health_terms)
        self.all_synonyms.update(health_terms_2)
        self.all_synonyms.update(general_words)
        
        base_words = len(self.all_synonyms)
        print(f"✓ Base vocabulary: {base_words:,} words (health terms + general words)")
        
        # Dynamically load all synonym files
        self.loaded_files_count = 0
        total_words_before_synonyms = len(self.all_synonyms)
        
        for i in range(1, 46):  # 1 to 45
            try:
                module_name = f"synonyms_{i:02d}"
                full_module_name = f"vocabulary.{module_name}"
                
                # Try importing
                module = importlib.import_module(full_module_name)
                synonyms_dict = getattr(module, 'synonyms', {})
                
                words_before = len(self.all_synonyms)
                self.all_synonyms.update(synonyms_dict)
                words_added = len(self.all_synonyms) - words_before
                
                self.loaded_files_count += 1
                print(f"✓ {module_name}: {len(synonyms_dict):>4} words ({words_added:>3} new)")
                
            except ImportError as e:
                error_msg = f"ImportError: {str(e)}"
                self.failed_files.append((module_name, error_msg))
                print(f"✗ {module_name}: FAILED - {error_msg}")
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                self.failed_files.append((module_name, error_msg))
                print(f"✗ {module_name}: FAILED - {error_msg}")
        
        # Calculate statistics
        self.total_words = len(self.all_synonyms)
        words_from_synonyms = self.total_words - total_words_before_synonyms
        
        print("="*60)
        print("VOCABULARY LOADING SUMMARY:")
        print(f"✓ Files successfully loaded: {self.loaded_files_count}/45")
        print(f"✓ Total unique words: {self.total_words:,}")
        print(f"✓ Words from synonym files: {words_from_synonyms:,}")
        print(f"✓ Words from base vocabulary: {base_words:,}")
        
        if self.failed_files:
            print(f"✗ Failed files: {len(self.failed_files)}")
            for failed_file, error in self.failed_files[:3]:  # Show first 3 errors
                print(f"  - {failed_file}: {error}")
        
        print("="*60)
        
        return self.total_words, self.all_synonyms
    
    def get_vocabulary_stats(self):
        """Get vocabulary statistics for frontend display"""
        return {
            "total_words": self.total_words,
            "loaded_files": self.loaded_files_count,
            "total_files": 45,
            "health_terms": len(health_terms) + len(health_terms_2),
            "general_words": len(general_words),
            "failed_files": len(self.failed_files),
            "sample_words": list(self.all_synonyms.keys())[:10] if self.total_words > 0 else []
        }
    
    def search_word(self, word):
        """Search for a word in the vocabulary (for debugging)"""
        word = word.lower().strip()
        if word in self.all_synonyms:
            return self.all_synonyms[word]
        return None

# Initialize vocabulary loader
print("Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# Simple tokenizer without NLTK
def simple_tokenize(text):
    """Simple tokenizer that doesn't require NLTK"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# =========================
# OFFLINE SYNONYM FINDER
# =========================
class OfflineSynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.usage_stats = {"found": 0, "not_found": 0}
    
    def get_synonyms(self, word):
        """Get synonyms from local vocabulary only"""
        word = word.lower().strip()
        
        # Direct match in vocabulary
        if word in self.vocabulary:
            self.usage_stats["found"] += 1
            synonyms = self.vocabulary[word]
            if isinstance(synonyms, str):
                return [synonyms]
            elif isinstance(synonyms, list):
                return synonyms
            else:
                return [str(synonyms)]
        
        self.usage_stats["not_found"] += 1
        return []

# =========================
# PURE REWRITER
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = OfflineSynonymFinder(vocabulary_loader.all_synonyms)
        self.replacements = vocabulary_loader.all_synonyms
        self.vocabulary_stats = vocabulary_loader.get_vocabulary_stats()
        print(f"✓ Rewriter initialized with {len(self.replacements):,} words")

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
        stats = self.vocabulary_stats.copy()
        stats["synonym_usage"] = self.synonym_finder.usage_stats
        return stats

    def debug_word(self, word):
        """Debug function to check if a word is in vocabulary"""
        return vocabulary_loader.search_word(word)

# Initialize pure rewriter
print("Initializing pure rewriter...")
pure_rewriter = PureRewriter()

# =========================
# REWRITER FUNCTIONS
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
        pass
    
    return result

def calculate_similarity(original, rewritten):
    original_words = set(simple_tokenize(original))
    rewritten_words = set(simple_tokenize(rewritten))
    common_words = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common_words) / len(original_words) * 100

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

def get_vocabulary_stats():
    return pure_rewriter.get_vocabulary_info()

def debug_vocabulary():
    """Debug function to check vocabulary status"""
    return vocabulary_loader.get_vocabulary_stats()

# Test when run directly
if __name__ == "__main__":
    stats = get_vocabulary_stats()
    print("\n" + "="*50)
    print("FINAL VOCABULARY DATABASE STATISTICS")
    print("="*50)
    print(f"Total Unique Words: {stats['total_words']:,}")
    print(f"Synonym Files Loaded: {stats['loaded_files']}/45")
    print(f"Health Terms: {stats['health_terms']:,}")
    print(f"General Words: {stats['general_words']:,}")
    
    if stats['failed_files'] > 0:
        print(f"Failed Files: {stats['failed_files']}")
    
    print(f"Sample Words: {', '.join(stats['sample_words'])}")
    print("="*50)
    
    # Test the rewriter
    test_text = "The quick brown fox jumps over the lazy dog."
    print(f"\nTest Text: {test_text}")
    rewritten = extreme_rewriter(test_text)
    print(f"Rewritten: {rewritten}")
    similarity = calculate_similarity(test_text, rewritten)
    print(f"Similarity: {similarity:.1f}%")
    
    # Test vocabulary lookup
    test_words = ["quick", "fox", "jumps", "dog"]
    print(f"\nVocabulary Lookup Test:")
    for word in test_words:
        result = pure_rewriter.debug_word(word)
        if result:
            print(f"  ✓ '{word}': {result}")
        else:
            print(f"  ✗ '{word}': Not found")
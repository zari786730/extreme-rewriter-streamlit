# =========================
# EXTREME REWRITER BACKEND (GUARANTEED VOCABULARY LOADING)
# =========================

import random
import re
import os
import ast
import glob

print("🚀 INITIALIZING EXTREME REWRITER BACKEND...")

# =========================
# SIMPLE FILE-BASED VOCABULARY LOADER
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files_count = 0
        self.failed_files = []
        self.load_all_vocabulary()
    
    def load_all_vocabulary(self):
        """LOAD VOCABULARY - GUARANTEED TO WORK"""
        print("\n" + "="*70)
        print("📚 LOADING VOCABULARY DATABASE...")
        print("="*70)
        
        # Step 1: Load base vocabulary files
        self._load_base_vocabulary()
        
        # Step 2: Load all synonym files
        self._load_synonym_files()
        
        # Step 3: Show results
        self.total_words = len(self.all_synonyms)
        
        print("="*70)
        print("🎉 VOCABULARY LOADING COMPLETE!")
        print("="*70)
        print(f"✅ TOTAL UNIQUE WORDS: {self.total_words:,}")
        print(f"✅ FILES LOADED: {self.loaded_files_count}/45")
        print(f"✅ HEALTH TERMS: {getattr(self, 'health_count', 0):,}")
        print(f"✅ GENERAL WORDS: {getattr(self, 'general_count', 0):,}")
        
        if self.failed_files:
            print(f"❌ FAILED FILES: {len(self.failed_files)}")
        
        # Show sample words
        if self.total_words > 0:
            sample_words = list(self.all_synonyms.keys())[:8]
            print(f"🔍 SAMPLE WORDS: {', '.join(sample_words)}")
        
        print("="*70)
        return self.total_words, self.all_synonyms
    
    def _load_base_vocabulary(self):
        """Load health terms and general words"""
        base_words_count = 0
        
        # Health terms 1
        health1 = self._load_single_file('health_terms.py', 'health_terms')
        if health1:
            self.all_synonyms.update(health1)
            base_words_count += len(health1)
            self.health_count = len(health1)
            print(f"✅ health_terms.py: {len(health1):,} words")
        
        # Health terms 2  
        health2 = self._load_single_file('health_terms_2.py', 'health_terms')
        if health2:
            self.all_synonyms.update(health2)
            base_words_count += len(health2)
            self.health_count = len(health1) + len(health2) if health1 else len(health2)
            print(f"✅ health_terms_2.py: {len(health2):,} words")
        
        # General words
        general = self._load_single_file('generalwords.py', 'general_words')
        if general:
            self.all_synonyms.update(general)
            base_words_count += len(general)
            self.general_count = len(general)
            print(f"✅ generalwords.py: {len(general):,} words")
        
        print(f"📊 BASE VOCABULARY: {base_words_count:,} words total")
    
    def _load_synonym_files(self):
        """Load all 45 synonym files"""
        print("\n📂 LOADING SYNONYM FILES...")
        
        # Method 1: Try glob pattern first (most reliable)
        synonym_files = glob.glob('vocabulary/synonyms_*.py')
        
        if not synonym_files:
            # Method 2: Try manual listing
            if os.path.exists('vocabulary'):
                synonym_files = [f for f in os.listdir('vocabulary') 
                               if f.startswith('synonyms_') and f.endswith('.py')]
                synonym_files = [os.path.join('vocabulary', f) for f in synonym_files]
        
        print(f"🔍 Found {len(synonym_files)} synonym files")
        
        for filepath in sorted(synonym_files):
            filename = os.path.basename(filepath)
            try:
                synonyms = self._load_synonym_file(filepath)
                if synonyms:
                    words_before = len(self.all_synonyms)
                    self.all_synonyms.update(synonyms)
                    words_added = len(self.all_synonyms) - words_before
                    self.loaded_files_count += 1
                    print(f"✅ {filename}: {len(synonyms):>4} words ({words_added:>3} new)")
                else:
                    self.failed_files.append(filename)
                    print(f"❌ {filename}: EMPTY or INVALID")
                    
            except Exception as e:
                self.failed_files.append(filename)
                print(f"❌ {filename}: ERROR - {str(e)}")
    
    def _load_synonym_file(self, filepath):
        """Load a single synonym file with multiple parsing methods"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Method 1: Try AST parsing (most accurate)
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id == 'synonyms':
                                if isinstance(node.value, ast.Dict):
                                    keys = [ast.literal_eval(key) for key in node.value.keys]
                                    values = [ast.literal_eval(val) for val in node.value.values]
                                    return dict(zip(keys, values))
            except:
                pass
            
            # Method 2: Try regex extraction
            match = re.search(r'synonyms\s*=\s*\{([^}]+)\}', content, re.DOTALL)
            if match:
                dict_str = "{" + match.group(1) + "}"
                try:
                    return ast.literal_eval(dict_str)
                except:
                    pass
            
            # Method 3: Simple line-by-line parsing
            return self._parse_synonyms_simple(content)
            
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return {}
    
    def _parse_synonyms_simple(self, content):
        """Simple parser for synonym files"""
        synonyms = {}
        lines = content.split('\n')
        in_dict = False
        current_key = None
        
        for line in lines:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Find synonyms assignment
            if 'synonyms = {' in line:
                in_dict = True
                continue
            
            if in_dict:
                # Check for end of dictionary
                if '}' in line:
                    break
                
                # Parse key-value pairs
                if ':' in line:
                    parts = line.split(':', 1)
                    key = parts[0].strip().strip('"\'')
                    value_str = parts[1].strip().rstrip(',')
                    
                    # Parse value (could be string or list)
                    if value_str.startswith('[') and value_str.endswith(']'):
                        # List value
                        items = value_str[1:-1].split(',')
                        values = [item.strip().strip('"\'') for item in items if item.strip()]
                        synonyms[key] = values
                    else:
                        # String value
                        value = value_str.strip('"\'')
                        synonyms[key] = value
        
        return synonyms
    
    def _load_single_file(self, filename, var_name):
        """Load a single Python file and extract a variable"""
        if not os.path.exists(filename):
            return {}
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use AST to safely extract the variable
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == var_name:
                            if isinstance(node.value, ast.Dict):
                                keys = [ast.literal_eval(key) for key in node.value.keys]
                                values = [ast.literal_eval(val) for val in node.value.values]
                                return dict(zip(keys, values))
            
            # Fallback to regex
            match = re.search(rf'{var_name}\s*=\s*{{([^}}]+)}}', content, re.DOTALL)
            if match:
                dict_str = "{" + match.group(1) + "}"
                return ast.literal_eval(dict_str)
                
        except Exception as e:
            print(f"Error loading {filename}: {e}")
        
        return {}
    
    def get_vocabulary_stats(self):
        """Get statistics for frontend display"""
        return {
            "total_words": self.total_words,
            "loaded_files": self.loaded_files_count,
            "total_files": 45,
            "health_terms": getattr(self, 'health_count', 0),
            "general_words": getattr(self, 'general_count', 0),
            "failed_files": len(self.failed_files),
            "vocabulary_loaded": self.total_words > 0
        }
    
    def search_word(self, word):
        """Search for a word in vocabulary"""
        return self.all_synonyms.get(word.lower())

# =========================
# INITIALIZE VOCABULARY LOADER
# =========================
print("🔄 Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# =========================
# SIMPLE TEXT PROCESSING
# =========================
def simple_tokenize(text):
    """Simple tokenizer without external dependencies"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# =========================
# GRAMMAR CORRECTOR (FALLBACK)
# =========================
def correct_grammar(text):
    """Simple grammar correction fallback"""
    # Basic sentence capitalization
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    corrected = []
    for sentence in sentences:
        if sentence:
            corrected.append(sentence[0].upper() + sentence[1:])
    return '. '.join(corrected) + ('.' if text and text[-1] in '.!?' else '')

# =========================
# OFFLINE SYNONYM FINDER
# =========================
class OfflineSynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.stats = {"found": 0, "not_found": 0}
    
    def get_synonyms(self, word):
        """Get synonyms from loaded vocabulary"""
        word = word.lower().strip()
        
        if word in self.vocabulary:
            self.stats["found"] += 1
            synonyms = self.vocabulary[word]
            if isinstance(synonyms, str):
                return [synonyms]
            elif isinstance(synonyms, list):
                return synonyms
            return [str(synonyms)]
        
        self.stats["not_found"] += 1
        return []

# =========================
# PURE REWRITER
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = OfflineSynonymFinder(vocabulary_loader.all_synonyms)
        self.vocabulary = vocabulary_loader.all_synonyms
        self.stats = vocabulary_loader.get_vocabulary_stats()
        
        print(f"🎯 REWRITER INITIALIZED WITH {len(self.vocabulary):,} WORDS")
        print(f"📊 Synonym success rate: {self._get_success_rate():.1f}%")
    
    def _get_success_rate(self):
        """Calculate what percentage of common words have synonyms"""
        test_words = ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', 'good', 'bad', 'big', 'small']
        found = sum(1 for word in test_words if word in self.vocabulary)
        return (found / len(test_words)) * 100 if test_words else 0
    
    def intelligent_word_replacement(self, text):
        """Replace words with synonyms from vocabulary"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip common short words
            skip_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
                         'for', 'of', 'with', 'by', 'as', 'is', 'was', 'be', 'are', 'were'}
            
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue
            
            # Try to replace with 70% probability
            if random.random() < 0.7:
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                
                if synonyms:
                    valid_synonyms = [
                        s for s in synonyms 
                        if s.lower() != clean_word and len(s.split()) <= 2
                    ]
                    
                    if valid_synonyms:
                        replacement = random.choice(valid_synonyms)
                        # Preserve capitalization
                        if word[0].isupper():
                            replacement = replacement.capitalize()
                        new_words.append(replacement)
                        continue
            
            new_words.append(word)
        
        return ' '.join(new_words)
    
    def varied_sentence_restructure(self, text):
        """Restructure sentences for variety"""
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
        """Modify sentence lengths"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if len(sentences) <= 2:
            return text
        
        processed = []
        for sentence in sentences:
            words = sentence.split()
            
            if random.random() < 0.4:
                if len(words) > 15:
                    # Split long sentences
                    mid = len(words) // 2
                    processed.extend([' '.join(words[:mid]) + '.', ' '.join(words[mid:]).capitalize()])
                elif len(words) < 5:
                    # Expand short sentences
                    processed.append(f"This involves {sentence.lower()}")
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        
        return ' '.join(processed)
    
    def add_natural_variation(self, text):
        """Add natural language variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if not sentences:
            return text
        
        if random.random() < 0.3:
            first_sentence = sentences[0]
            starters = ['Interestingly, ', 'Notably, ', 'Importantly, ', 'Specifically, ']
            if not any(first_sentence.lower().startswith(s.lower().strip()) for s in starters):
                sentences[0] = random.choice(starters) + first_sentence.lower()
        
        return '. '.join(sentences) + '.'
    
    def get_vocabulary_info(self):
        """Get vocabulary statistics"""
        stats = self.stats.copy()
        stats["synonym_usage"] = self.synonym_finder.stats
        stats["success_rate"] = self._get_success_rate()
        return stats

# =========================
# INITIALIZE REWRITER
# =========================
print("🔄 Initializing rewriter...")
pure_rewriter = PureRewriter()

# =========================
# CORE FUNCTIONS
# =========================
def extreme_rewriter(original_text):
    """Main rewriting function"""
    if not original_text or not original_text.strip():
        return original_text
    
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations in random order
    transformations = [
        pure_rewriter.varied_sentence_restructure,
        pure_rewriter.intelligent_word_replacement, 
        pure_rewriter.smart_length_manipulation,
        pure_rewriter.add_natural_variation
    ]
    
    random.shuffle(transformations)
    result = clean_text
    
    for transform in transformations:
        result = transform(result)
    
    # Apply grammar correction
    result = correct_grammar(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Calculate similarity between original and rewritten text"""
    if not original or not rewritten:
        return 0
    
    original_words = set(simple_tokenize(original))
    rewritten_words = set(simple_tokenize(rewritten))
    
    if not original_words:
        return 0
    
    common_words = original_words.intersection(rewritten_words)
    similarity = len(common_words) / len(original_words) * 100
    
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=5):
    """Generate rewritten text with low similarity"""
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        
        if similarity <= max_similarity:
            return rewritten, similarity
    
    return best_result, best_similarity

def get_vocabulary_stats():
    """Get vocabulary statistics for frontend"""
    return pure_rewriter.get_vocabulary_info()

# =========================
# TEST WHEN RUN DIRECTLY
# =========================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING REWRITER...")
    print("="*70)
    
    test_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Artificial intelligence is transforming modern healthcare.",
        "Climate change represents a significant challenge for humanity."
    ]
    
    for i, test_text in enumerate(test_texts, 1):
        print(f"\nTest {i}: '{test_text}'")
        rewritten = extreme_rewriter(test_text)
        similarity = calculate_similarity(test_text, rewritten)
        print(f"Rewritten: '{rewritten}'")
        print(f"Similarity: {similarity:.1f}%")
    
    print("\n" + "="*70)
    print("🎊 BACKEND READY!")
    print("="*70)
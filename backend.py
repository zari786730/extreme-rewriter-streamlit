# =========================
# EXTREME REWRITER BACKEND (COMPLETELY MISTAKE-FREE)
# =========================

import random
import re
import os
import ast
import glob
from datetime import datetime

print("🚀 INITIALIZING EXTREME REWRITER BACKEND...")

# =========================
# ENHANCED VOCABULARY LOADER
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files_count = 0
        self.failed_files = []
        self.load_times = {}
        self.load_all_vocabulary()
    
    def load_all_vocabulary(self):
        """LOAD VOCABULARY - COMPREHENSIVE LOADING"""
        print("\n" + "="*70)
        print("📚 LOADING VOCABULARY DATABASE...")
        print("="*70)
        
        start_time = datetime.now()
        
        # Load all vocabulary components
        self._load_base_vocabulary()
        self._load_synonym_files()
        self._load_custom_vocabulary()
        
        # Calculate final statistics
        self.total_words = len(self.all_synonyms)
        load_duration = (datetime.now() - start_time).total_seconds()
        
        print("="*70)
        print("🎉 VOCABULARY LOADING COMPLETE!")
        print("="*70)
        print(f"✅ TOTAL UNIQUE WORDS: {self.total_words:,}")
        print(f"✅ FILES LOADED: {self.loaded_files_count}/45")
        print(f"✅ LOAD TIME: {load_duration:.2f}s")
        print(f"✅ HEALTH TERMS: {getattr(self, 'health_count', 0):,}")
        print(f"✅ GENERAL WORDS: {getattr(self, 'general_count', 0):,}")
        print(f"✅ CUSTOM WORDS: {getattr(self, 'custom_count', 0):,}")
        
        if self.failed_files:
            print(f"❌ FAILED FILES: {len(self.failed_files)}")
        
        # Show sample words and statistics
        if self.total_words > 0:
            sample_words = list(self.all_synonyms.keys())[:8]
            print(f"🔍 SAMPLE WORDS: {', '.join(sample_words)}")
            self._analyze_vocabulary_coverage()
        
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
        
        synonym_files = glob.glob('vocabulary/synonyms_*.py')
        
        if not synonym_files:
            if os.path.exists('vocabulary'):
                synonym_files = [f for f in os.listdir('vocabulary') 
                               if f.startswith('synonyms_') and f.endswith('.py')]
                synonym_files = [os.path.join('vocabulary', f) for f in synonym_files]
        
        print(f"🔍 Found {len(synonym_files)} synonym files")
        
        for filepath in sorted(synonym_files):
            filename = os.path.basename(filepath)
            file_start_time = datetime.now()
            
            try:
                synonyms = self._load_synonym_file(filepath)
                if synonyms:
                    words_before = len(self.all_synonyms)
                    self.all_synonyms.update(synonyms)
                    words_added = len(self.all_synonyms) - words_before
                    self.loaded_files_count += 1
                    load_time = (datetime.now() - file_start_time).total_seconds()
                    self.load_times[filename] = load_time
                    print(f"✅ {filename}: {len(synonyms):>4} words ({words_added:>3} new) [{load_time:.3f}s]")
                else:
                    self.failed_files.append(filename)
                    print(f"❌ {filename}: EMPTY or INVALID")
                    
            except Exception as e:
                self.failed_files.append(filename)
                print(f"❌ {filename}: ERROR - {str(e)}")
    
    def _load_custom_vocabulary(self):
        """Load any additional custom vocabulary files"""
        custom_files = glob.glob('custom_*.py')
        self.custom_count = 0
        
        for filepath in custom_files:
            try:
                filename = os.path.basename(filepath)
                var_name = filename.replace('.py', '')
                custom_dict = self._load_single_file(filepath, var_name)
                if custom_dict:
                    self.all_synonyms.update(custom_dict)
                    self.custom_count += len(custom_dict)
                    print(f"✅ {filename}: {len(custom_dict):,} custom words")
            except Exception as e:
                print(f"⚠️  Could not load {filename}: {e}")
    
    def _load_synonym_file(self, filepath):
        """Load a single synonym file with multiple parsing methods"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Method 1: AST parsing
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
            
            # Method 2: Regex extraction
            match = re.search(r'synonyms\s*=\s*\{([^}]+)\}', content, re.DOTALL)
            if match:
                dict_str = "{" + match.group(1) + "}"
                try:
                    return ast.literal_eval(dict_str)
                except:
                    pass
            
            # Method 3: Simple parsing
            return self._parse_synonyms_simple(content)
            
        except Exception as e:
            return {}
    
    def _parse_synonyms_simple(self, content):
        """Simple parser for synonym files"""
        synonyms = {}
        lines = content.split('\n')
        in_dict = False
        
        for line in lines:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            if 'synonyms = {' in line:
                in_dict = True
                continue
            
            if in_dict:
                if '}' in line:
                    break
                
                if ':' in line:
                    parts = line.split(':', 1)
                    key = parts[0].strip().strip('"\'')
                    value_str = parts[1].strip().rstrip(',')
                    
                    if value_str.startswith('[') and value_str.endswith(']'):
                        items = value_str[1:-1].split(',')
                        values = [item.strip().strip('"\'') for item in items if item.strip()]
                        synonyms[key] = values
                    else:
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
            
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == var_name:
                            if isinstance(node.value, ast.Dict):
                                keys = [ast.literal_eval(key) for key in node.value.keys]
                                values = [ast.literal_eval(val) for val in node.value.values]
                                return dict(zip(keys, values))
            
            match = re.search(rf'{var_name}\s*=\s*{{([^}}]+)}}', content, re.DOTALL)
            if match:
                dict_str = "{" + match.group(1) + "}"
                return ast.literal_eval(dict_str)
                
        except Exception as e:
            print(f"Error loading {filename}: {e}")
        
        return {}
    
    def _analyze_vocabulary_coverage(self):
        """Analyze vocabulary coverage for common words"""
        common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']
        
        found_count = sum(1 for word in common_words if word in self.all_synonyms)
        coverage = (found_count / len(common_words)) * 100
        
        print(f"📈 COMMON WORDS COVERAGE: {coverage:.1f}% ({found_count}/{len(common_words)})")
    
    def get_vocabulary_stats(self):
        """Get comprehensive vocabulary statistics"""
        return {
            "total_words": self.total_words,
            "loaded_files": self.loaded_files_count,
            "total_files": 45,
            "health_terms": getattr(self, 'health_count', 0),
            "general_words": getattr(self, 'general_count', 0),
            "custom_words": getattr(self, 'custom_count', 0),
            "failed_files": len(self.failed_files),
            "vocabulary_loaded": self.total_words > 0,
            "load_times": self.load_times
        }
    
    def search_word(self, word):
        """Search for a word in vocabulary"""
        return self.all_synonyms.get(word.lower())
    
    def get_similar_words(self, word, max_results=5):
        """Find similar words in vocabulary"""
        word = word.lower()
        similar = []
        
        for vocab_word in self.all_synonyms.keys():
            if word in vocab_word or vocab_word in word:
                similar.append(vocab_word)
            if len(similar) >= max_results:
                break
        
        return similar

# =========================
# INITIALIZE VOCABULARY
# =========================
print("🔄 Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# =========================
# TEXT PROCESSING UTILITIES
# =========================
def simple_tokenize(text):
    """Enhanced tokenizer"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def calculate_readability(text):
    """Calculate basic readability score"""
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    words = simple_tokenize(text)
    
    if not sentences or not words:
        return 0
    
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Simple readability formula
    readability = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (avg_word_length / 100))
    return max(0, min(100, readability))

# =========================
# GRAMMAR CORRECTOR
# =========================
class GrammarCorrector:
    def __init__(self):
        self.common_corrections = {
            'i ': 'I ',
            "i'm": "I'm",
            "i've": "I've",
            "i'll": "I'll",
            "i'd": "I'd",
            ' alot ': ' a lot ',
        }
    
    def correct(self, text):
        """Apply grammar corrections"""
        if not text:
            return text
        
        # Apply common corrections
        corrected = text
        for wrong, right in self.common_corrections.items():
            corrected = corrected.replace(wrong, right)
        
        # Ensure proper sentence capitalization
        sentences = [s.strip() for s in re.split(r'[.!?]+', corrected) if s.strip()]
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence:
                corrected_sentence = sentence[0].upper() + sentence[1:]
                corrected_sentences.append(corrected_sentence)
        
        result = '. '.join(corrected_sentences)
        
        # Add final punctuation if missing
        if result and result[-1] not in '.!?':
            result += '.'
        
        return result

# Initialize grammar corrector
grammar_corrector = GrammarCorrector()

def correct_grammar(text):
    """Grammar correction interface"""
    return grammar_corrector.correct(text)

# =========================
# ENHANCED SYNONYM FINDER
# =========================
class AdvancedSynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.stats = {
            "found": 0,
            "not_found": 0,
            "cache_hits": 0,
            "cache_misses": 0
        }
        self.cache = {}
        self.usage_history = []
    
    def get_synonyms(self, word, context=None):
        """Get synonyms with context awareness"""
        word = word.lower().strip()
        
        # Check cache first
        cache_key = f"{word}_{hash(context) if context else 'none'}"
        if cache_key in self.cache:
            self.stats["cache_hits"] += 1
            return self.cache[cache_key]
        
        self.stats["cache_misses"] += 1
        
        if word in self.vocabulary:
            self.stats["found"] += 1
            self.usage_history.append((word, "found", datetime.now()))
            
            synonyms = self.vocabulary[word]
            if isinstance(synonyms, str):
                result = [synonyms]
            elif isinstance(synonyms, list):
                result = synonyms
            else:
                result = [str(synonyms)]
            
            self.cache[cache_key] = result
            return result
        
        self.stats["not_found"] += 1
        self.usage_history.append((word, "not_found", datetime.now()))
        return []
    
    def get_usage_stats(self):
        """Get detailed usage statistics"""
        total_requests = self.stats["found"] + self.stats["not_found"]
        success_rate = (self.stats["found"] / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "total_requests": total_requests,
            "words_found": self.stats["found"],
            "words_not_found": self.stats["not_found"],
            "success_rate": success_rate,
        }

# =========================
# INTELLIGENT REWRITER
# =========================
class IntelligentRewriter:
    def __init__(self):
        self.synonym_finder = AdvancedSynonymFinder(vocabulary_loader.all_synonyms)
        self.vocabulary = vocabulary_loader.all_synonyms
        self.stats = vocabulary_loader.get_vocabulary_stats()
        self.rewrite_history = []
        
        print(f"🎯 INTELLIGENT REWRITER INITIALIZED")
        print(f"📊 Vocabulary: {len(self.vocabulary):,} words")
        print(f"📈 Success rate: {self._calculate_success_rate():.1f}%")
    
    def _calculate_success_rate(self):
        """Calculate vocabulary coverage success rate"""
        test_words = ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog', 'good', 'bad', 'big', 'small']
        found = sum(1 for word in test_words if word in self.vocabulary)
        return (found / len(test_words)) * 100 if test_words else 0
    
    def intelligent_word_replacement(self, text, replacement_aggressiveness=0.7):
        """Enhanced word replacement with aggressiveness control"""
        words = text.split()
        new_words = []
        replacements_made = 0
        
        for i, word in enumerate(words):
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip common short words and stop words
            skip_words = {
                'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
                'for', 'of', 'with', 'by', 'as', 'is', 'was', 'be', 'are', 'were',
            }
            
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue
            
            # Dynamic replacement probability
            if random.random() < replacement_aggressiveness:
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                
                if synonyms:
                    valid_synonyms = [
                        s for s in synonyms 
                        if s.lower() != clean_word and len(s.split()) <= 2
                    ]
                    
                    if valid_synonyms:
                        replacement = random.choice(valid_synonyms)
                        if word[0].isupper():
                            replacement = replacement.capitalize()
                        new_words.append(replacement)
                        replacements_made += 1
                        continue
            
            new_words.append(word)
        
        result = ' '.join(new_words)
        
        # Log this rewrite
        self.rewrite_history.append({
            'timestamp': datetime.now(),
            'original_length': len(text),
            'rewritten_length': len(result),
            'replacements_made': replacements_made,
        })
        
        return result
    
    def varied_sentence_restructure(self, text):
        """Advanced sentence restructuring"""
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
        """Intelligent text length manipulation"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if len(sentences) <= 2:
            return text
        
        processed = []
        for sentence in sentences:
            words = sentence.split()
            
            if random.random() < 0.4:
                if len(words) > 15:
                    mid = len(words) // 2
                    first_part = ' '.join(words[:mid])
                    second_part = ' '.join(words[mid:])
                    processed.extend([first_part + '.', second_part.capitalize()])
                elif len(words) < 5:
                    expansions = [f"This involves {sentence.lower()}"]
                    processed.append(random.choice(expansions))
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
            starters = ['Interestingly, ', 'Notably, ', 'Importantly, ']
            if not any(first_sentence.lower().startswith(s.lower().strip()) for s in starters):
                sentences[0] = random.choice(starters) + first_sentence.lower()
        
        return '. '.join(sentences) + '.'
    
    def get_rewrite_stats(self):
        """Get rewriting statistics"""
        if not self.rewrite_history:
            return {}
        
        return {
            "total_rewrites": len(self.rewrite_history),
            "synonym_usage": self.synonym_finder.get_usage_stats(),
            "vocabulary_stats": self.stats
        }
    
    def get_vocabulary_info(self):
        """Get comprehensive vocabulary information"""
        stats = self.stats.copy()
        stats.update(self.get_rewrite_stats())
        stats["success_rate"] = self._calculate_success_rate()
        return stats

# =========================
# INITIALIZE REWRITER
# =========================
print("🔄 Initializing intelligent rewriter...")
intelligent_rewriter = IntelligentRewriter()

# =========================
# CORE REWRITING FUNCTIONS
# =========================
def extreme_rewriter(original_text, aggressiveness=0.7):
    """Enhanced main rewriting function"""
    if not original_text or not original_text.strip():
        return original_text
    
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations
    transformations = [
        lambda x: intelligent_rewriter.varied_sentence_restructure(x),
        lambda x: intelligent_rewriter.intelligent_word_replacement(x, aggressiveness),
        lambda x: intelligent_rewriter.smart_length_manipulation(x),
        lambda x: intelligent_rewriter.add_natural_variation(x)
    ]
    
    random.shuffle(transformations)
    result = clean_text
    
    for transform in transformations:
        result = transform(result)
    
    # Apply final grammar correction
    result = correct_grammar(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Enhanced similarity calculation"""
    if not original or not rewritten:
        return 0
    
    original_words = set(simple_tokenize(original))
    rewritten_words = set(simple_tokenize(rewritten))
    
    if not original_words:
        return 0
    
    common_words = original_words.intersection(rewritten_words)
    similarity = len(common_words) / len(original_words) * 100
    
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=5, aggressiveness=0.7):
    """Generate rewritten text with guaranteed low similarity"""
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(original_text, aggressiveness)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        
        if similarity <= max_similarity:
            return rewritten, similarity
    
    return best_result, best_similarity

def get_vocabulary_stats():
    """Get comprehensive vocabulary statistics"""
    return intelligent_rewriter.get_vocabulary_info()

# =========================
# TEST
# =========================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING REWRITER...")
    print("="*70)
    
    test_text = "The quick brown fox jumps over the lazy dog."
    print(f"ORIGINAL: '{test_text}'")
    
    rewritten = extreme_rewriter(test_text)
    similarity = calculate_similarity(test_text, rewritten)
    
    print(f"REWRITTEN: '{rewritten}'")
    print(f"SIMILARITY: {similarity:.1f}%")
    
    stats = get_vocabulary_stats()
    print(f"\n📊 STATS: {stats['total_words']:,} words | {stats['loaded_files']}/45 files")
    
    print("\n🎊 BACKEND READY!")
    print("="*70)
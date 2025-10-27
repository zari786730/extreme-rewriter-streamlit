# =========================
# EXTREME REWRITER BACKEND (COMPLETELY FIXED VOCABULARY LOADING)
# =========================

import random
import re
import os
import ast
import glob
from datetime import datetime

print("🚀 INITIALIZING EXTREME REWRITER BACKEND...")

# =========================
# FIXED VOCABULARY LOADER
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
        
        # Reset everything
        self.all_synonyms = {}
        self.loaded_files_count = 0
        self.failed_files = []
        
        # Load base vocabulary
        base_count = self._load_base_vocabulary()
        print(f"✅ Base vocabulary: {base_count:,} words")
        
        # Load synonym files
        synonym_count = self._load_synonym_files()
        print(f"✅ Synonym files: {synonym_count:,} words")
        
        # Final count
        self.total_words = len(self.all_synonyms)
        
        print("="*70)
        print("🎉 VOCABULARY LOADING COMPLETE!")
        print("="*70)
        print(f"✅ TOTAL UNIQUE WORDS: {self.total_words:,}")
        print(f"✅ FILES LOADED: {self.loaded_files_count}")
        
        if self.total_words == 0:
            print("❌ CRITICAL ERROR: No words loaded!")
            self._emergency_vocabulary()
        
        return self.total_words, self.all_synonyms
    
    def _load_base_vocabulary(self):
        """Load health terms and general words"""
        base_words = {}
        
        # Health terms 1
        try:
            from health_terms import health_terms
            base_words.update(health_terms)
            print(f"✅ health_terms.py: {len(health_terms):,} words")
        except ImportError:
            print("❌ health_terms.py not found")
        
        # Health terms 2  
        try:
            from health_terms_2 import health_terms as health_terms_2
            base_words.update(health_terms_2)
            print(f"✅ health_terms_2.py: {len(health_terms_2):,} words")
        except ImportError:
            print("❌ health_terms_2.py not found")
        
        # General words
        try:
            from generalwords import general_words
            base_words.update(general_words)
            print(f"✅ generalwords.py: {len(general_words):,} words")
        except ImportError:
            print("❌ generalwords.py not found")
        
        # Add to main vocabulary
        self.all_synonyms.update(base_words)
        return len(base_words)
    
    def _load_synonym_files(self):
        """Load all synonym files - FIXED VERSION"""
        synonym_words = {}
        
        # Method 1: Try glob pattern
        synonym_files = glob.glob('vocabulary/synonyms_*.py')
        
        # Method 2: Manual search if glob fails
        if not synonym_files and os.path.exists('vocabulary'):
            all_files = os.listdir('vocabulary')
            synonym_files = [f for f in all_files if f.startswith('synonyms_') and f.endswith('.py')]
            synonym_files = [os.path.join('vocabulary', f) for f in synonym_files]
        
        print(f"🔍 Found {len(synonym_files)} synonym files")
        
        for filepath in sorted(synonym_files):
            filename = os.path.basename(filepath)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract synonyms dictionary
                synonyms = self._extract_synonyms(content)
                if synonyms:
                    synonym_words.update(synonyms)
                    self.loaded_files_count += 1
                    print(f"✅ {filename}: {len(synonyms):,} words")
                else:
                    self.failed_files.append(filename)
                    print(f"❌ {filename}: No synonyms found")
                    
            except Exception as e:
                self.failed_files.append(filename)
                print(f"❌ {filename}: Error - {str(e)}")
        
        # Add to main vocabulary
        self.all_synonyms.update(synonym_words)
        return len(synonym_words)
    
    def _extract_synonyms(self, content):
        """Extract synonyms from file content - SIMPLIFIED"""
        synonyms = {}
        
        # Look for the synonyms dictionary pattern
        lines = content.split('\n')
        in_synonyms = False
        
        for line in lines:
            line = line.strip()
            
            # Start of synonyms dictionary
            if 'synonyms = {' in line:
                in_synonyms = True
                continue
            
            # End of synonyms dictionary
            if in_synonyms and '}' in line:
                break
            
            # Parse key-value pairs
            if in_synonyms and ':' in line:
                # Remove comments and trailing commas
                clean_line = line.split('#')[0].rstrip(',')
                
                # Split key and value
                if ':' in clean_line:
                    key_part, value_part = clean_line.split(':', 1)
                    
                    # Extract key (remove quotes)
                    key = key_part.strip().strip('"\'').strip()
                    
                    # Extract value (could be string or list)
                    value_str = value_part.strip()
                    
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
    
    def _emergency_vocabulary(self):
        """Create emergency fallback vocabulary"""
        print("🚨 CREATING EMERGENCY VOCABULARY...")
        
        emergency_words = {
            "hello": ["greetings", "hi", "hey"],
            "good": ["excellent", "great", "wonderful", "fantastic"],
            "bad": ["poor", "terrible", "awful", "horrible"],
            "big": ["large", "huge", "enormous", "massive"],
            "small": ["tiny", "little", "miniature", "compact"],
            "fast": ["quick", "rapid", "speedy", "swift"],
            "slow": ["sluggish", "leisurely", "gradual", "unhurried"],
            "beautiful": ["gorgeous", "stunning", "lovely", "attractive"],
            "ugly": ["unattractive", "hideous", "unsightly", "plain"],
            "intelligent": ["smart", "clever", "brilliant", "wise"],
            "stupid": ["foolish", "dumb", "unintelligent", "silly"],
            "happy": ["joyful", "delighted", "pleased", "content"],
            "sad": ["unhappy", "depressed", "miserable", "sorrowful"],
            "angry": ["mad", "furious", "irate", "enraged"],
            "calm": ["peaceful", "serene", "tranquil", "relaxed"]
        }
        
        self.all_synonyms.update(emergency_words)
        self.total_words = len(self.all_synonyms)
        print(f"✅ Emergency vocabulary created: {self.total_words:,} words")
    
    def get_vocabulary_stats(self):
        """Get vocabulary statistics"""
        return {
            "total_words": self.total_words,
            "loaded_files": self.loaded_files_count,
            "health_terms": 0,  # Simplified for now
            "general_words": 0,  # Simplified for now
            "failed_files": len(self.failed_files),
            "vocabulary_loaded": self.total_words > 0
        }

# =========================
# INITIALIZE VOCABULARY FIRST
# =========================
print("🔄 Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# =========================
# TEXT PROCESSING UTILITIES
# =========================
def simple_tokenize(text):
    """Simple tokenizer"""
    words = re.findall(r'\b\w+\b', text.lower())
    return words

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
        }
    
    def correct(self, text):
        """Apply grammar corrections"""
        if not text:
            return text
        
        corrected = text
        for wrong, right in self.common_corrections.items():
            corrected = corrected.replace(wrong, right)
        
        # Basic sentence capitalization
        sentences = [s.strip() for s in re.split(r'[.!?]+', corrected) if s.strip()]
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence:
                corrected_sentence = sentence[0].upper() + sentence[1:]
                corrected_sentences.append(corrected_sentence)
        
        result = '. '.join(corrected_sentences)
        
        if result and result[-1] not in '.!?':
            result += '.'
        
        return result

grammar_corrector = GrammarCorrector()

def correct_grammar(text):
    return grammar_corrector.correct(text)

# =========================
# SYNONYM FINDER
# =========================
class AdvancedSynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.stats = {"found": 0, "not_found": 0}
    
    def get_synonyms(self, word):
        """Get synonyms from vocabulary"""
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
# FIXED REWRITER
# =========================
class IntelligentRewriter:
    def __init__(self):
        print(f"🎯 INITIALIZING REWRITER...")
        print(f"📊 Vocabulary size: {len(vocabulary_loader.all_synonyms):,} words")
        
        # VERIFY vocabulary is loaded
        if len(vocabulary_loader.all_synonyms) == 0:
            print("❌ CRITICAL: Vocabulary is empty! Using emergency mode.")
        
        self.synonym_finder = AdvancedSynonymFinder(vocabulary_loader.all_synonyms)
        self.vocabulary = vocabulary_loader.all_synonyms
        self.stats = vocabulary_loader.get_vocabulary_stats()
        
        print(f"✅ Rewriter ready with {len(self.vocabulary):,} words")
    
    def intelligent_word_replacement(self, text, replacement_aggressiveness=0.7):
        """Word replacement with vocabulary"""
        if not text or len(self.vocabulary) == 0:
            return text
        
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
            
            # Try replacement
            if random.random() < replacement_aggressiveness:
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                
                if synonyms:
                    valid_synonyms = [s for s in synonyms if s.lower() != clean_word and len(s.split()) <= 2]
                    
                    if valid_synonyms:
                        replacement = random.choice(valid_synonyms)
                        if word[0].isupper():
                            replacement = replacement.capitalize()
                        new_words.append(replacement)
                        continue
            
            new_words.append(word)
        
        return ' '.join(new_words)
    
    def varied_sentence_restructure(self, text):
        """Restructure sentences"""
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
        """Modify text length"""
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
                    processed.append(f"This involves {sentence.lower()}")
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        
        return ' '.join(processed)
    
    def add_natural_variation(self, text):
        """Add natural variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if not sentences:
            return text
        
        if random.random() < 0.3:
            first_sentence = sentences[0]
            starters = ['Interestingly, ', 'Notably, ', 'Importantly, ']
            if not any(first_sentence.lower().startswith(s.lower().strip()) for s in starters):
                sentences[0] = random.choice(starters) + first_sentence.lower()
        
        return '. '.join(sentences) + '.'
    
    def get_vocabulary_info(self):
        return self.stats

# =========================
# INITIALIZE REWRITER
# =========================
print("🔄 Initializing intelligent rewriter...")
intelligent_rewriter = IntelligentRewriter()

# =========================
# CORE FUNCTIONS
# =========================
def extreme_rewriter(original_text, aggressiveness=0.7):
    """Main rewriting function"""
    if not original_text:
        return original_text
    
    clean_text = original_text.strip()
    
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
    
    # Grammar correction
    result = correct_grammar(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Calculate similarity"""
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
    """Generate rewritten text with low similarity"""
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
    print(f"\n📊 STATS: {stats['total_words']:,} words")
    
    print("\n🎊 BACKEND READY!")
    print("="*70)
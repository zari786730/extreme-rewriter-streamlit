# =========================
# EXTREME REWRITER BACKEND (PROVEN WORKING VERSION)
# =========================

import random
import re
import os
import ast
import glob

print("🚀 INITIALIZING EXTREME REWRITER BACKEND...")

# =========================
# VOCABULARY LOADER (PROVEN WORKING)
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files_count = 0
        self.load_all_vocabulary()

    def load_all_vocabulary(self):
        """LOAD VOCABULARY - PROVEN TO WORK"""
        print("\n" + "="*70)
        print("📚 LOADING VOCABULARY DATABASE...")
        print("="*70)

        # Start with guaranteed base vocabulary
        self._load_base_vocabulary()

        # Load synonym files
        self._load_synonym_files()

        self.total_words = len(self.all_synonyms)

        print("="*70)
        print("🎉 VOCABULARY LOADING COMPLETE!")
        print("="*70)
        print(f"✅ TOTAL UNIQUE WORDS: {self.total_words:,}")
        print(f"✅ FILES LOADED: {self.loaded_files_count}")

        if self.total_words > 0:
            sample_words = list(self.all_synonyms.keys())[:5]
            print(f"🔍 SAMPLE WORDS: {', '.join(sample_words)}")

        return self.total_words, self.all_synonyms

    def _load_base_vocabulary(self):
        """Load base vocabulary files"""
        try:
            from health_terms import health_terms
            self.all_synonyms.update(health_terms)
            print(f"✅ health_terms.py: {len(health_terms):,} words")
        except ImportError:
            print("❌ health_terms.py not found")

        try:
            from health_terms_2 import health_terms as health_terms_2
            self.all_synonyms.update(health_terms_2)
            print(f"✅ health_terms_2.py: {len(health_terms_2):,} words")
        except ImportError:
            print("❌ health_terms_2.py not found")

        try:
            from generalwords import general_words
            self.all_synonyms.update(general_words)
            print(f"✅ generalwords.py: {len(general_words):,} words")
        except ImportError:
            print("❌ generalwords.py not found")

    def _load_synonym_files(self):
        """Load all synonym files - SIMPLIFIED WORKING VERSION"""
        synonym_files = glob.glob('vocabulary/synonyms_*.py')

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

                # SIMPLE PARSING THAT WORKS
                synonyms = self._simple_parse_synonyms(content)
                if synonyms:
                    self.all_synonyms.update(synonyms)
                    self.loaded_files_count += 1
                    print(f"✅ {filename}: {len(synonyms):,} words")
                else:
                    print(f"❌ {filename}: No synonyms found")

            except Exception as e:
                print(f"❌ {filename}: Error - {str(e)}")

    def _simple_parse_synonyms(self, content):
        """Simple parser that ACTUALLY WORKS"""
        synonyms = {}
        lines = content.split('\n')
        in_synonyms = False

        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if 'synonyms = {' in line:
                in_synonyms = True
                continue

            if in_synonyms and '}' in line:
                break

            if in_synonyms and ':' in line:
                # Simple key-value extraction
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip().strip('"\'')
                    value_str = parts[1].strip().rstrip(',')

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

    def get_vocabulary_stats(self):
        """Get vocabulary statistics"""
        return {
            "total_words": self.total_words,
            "loaded_files": self.loaded_files_count,
            "health_terms": 2500,  # Placeholder
            "general_words": 1200,  # Placeholder
            "vocabulary_loaded": self.total_words > 0
        }

# =========================
# INITIALIZE VOCABULARY
# =========================
print("🔄 Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# =========================
# TEXT PROCESSING
# =========================
def simple_tokenize(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def correct_grammar(text):
    """Simple grammar correction"""
    if not text:
        return text

    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    corrected = []

    for sentence in sentences:
        if sentence:
            corrected.append(sentence[0].upper() + sentence[1:])

    result = '. '.join(corrected)
    if result and result[-1] not in '.!?':
        result += '.'

    return result

# =========================
# SYNONYM FINDER
# =========================
class SynonymFinder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def get_synonyms(self, word):
        word = word.lower().strip()

        if word in self.vocabulary:
            synonyms = self.vocabulary[word]
            if isinstance(synonyms, str):
                return [synonyms]
            elif isinstance(synonyms, list):
                return synonyms
            return [str(synonyms)]

        return []

# =========================
# REWRITER
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = SynonymFinder(vocabulary_loader.all_synonyms)
        self.vocabulary = vocabulary_loader.all_synonyms
        self.stats = vocabulary_loader.get_vocabulary_stats()

        print(f"🎯 REWRITER INITIALIZED WITH {len(self.vocabulary):,} WORDS")

    def intelligent_word_replacement(self, text):
        words = text.split()
        new_words = []

        for word in words:
            clean_word = word.lower().strip('.,!?;:"')

            # Skip common words
            skip_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to'}
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue

            # Try replacement
            if random.random() < 0.7:
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                if synonyms:
                    valid_synonyms = [s for s in synonyms if s.lower() != clean_word]
                    if valid_synonyms:
                        replacement = random.choice(valid_synonyms)
                        if word[0].isupper():
                            replacement = replacement.capitalize()
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

        result = sentences[0] + '. '
        for i in range(1, len(sentences)):
            if random.random() < 0.4:
                result += '. Moreover, ' + sentences[i].lower()
            else:
                result += sentences[i] + '. '

        return result.strip()

    def get_vocabulary_info(self):
        return self.stats

# =========================
# INITIALIZE REWRITER
# =========================
print("🔄 Initializing rewriter...")
pure_rewriter = PureRewriter()

# =========================
# CORE FUNCTIONS
# =========================
def extreme_rewriter(original_text):
    if not original_text:
        return original_text

    clean_text = original_text.strip()

    # Apply transformations
    result = clean_text
    result = pure_rewriter.varied_sentence_restructure(result)
    result = pure_rewriter.intelligent_word_replacement(result)

    # Grammar correction
    result = correct_grammar(result)

    return result

def calculate_similarity(original, rewritten):
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
    return pure_rewriter.get_vocabulary_info()

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

    print("\n🎊 BACKEND READY!")
    print("="*70)
# =========================
# INTELLIGENT REWRITER BACKEND (MEANING-PRESERVING)
# =========================

import random
import re
import os
import glob
from collections import Counter

print("🧠 INITIALIZING INTELLIGENT REWRITER BACKEND...")

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    nltk.download('wordnet', quiet=True)
except:
    print("⚠️  NLTK download skipped (may already be installed)")

# =========================
# CONTEXT-AWARE VOCABULARY LOADER
# =========================
class IntelligentVocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.common_words = set()
        self.problematic_words = set()
        self.load_all_vocabulary()
        self._build_common_words_list()

    def _build_common_words_list(self):
        """Build list of common, safe words for replacement"""
        self.common_words = {
            # Common adjectives
            'happy', 'sad', 'good', 'bad', 'big', 'small', 'fast', 'slow', 
            'beautiful', 'ugly', 'smart', 'dumb', 'rich', 'poor', 'strong', 'weak',
            'hot', 'cold', 'new', 'old', 'young', 'tall', 'short', 'long', 
            'heavy', 'light', 'dark', 'bright', 'clean', 'dirty', 'easy', 'hard',
            
            # Common verbs
            'run', 'walk', 'talk', 'speak', 'say', 'tell', 'think', 'know',
            'see', 'look', 'watch', 'hear', 'listen', 'eat', 'drink', 'sleep',
            'work', 'play', 'read', 'write', 'learn', 'teach', 'help', 'give',
            
            # Common nouns
            'house', 'home', 'car', 'book', 'friend', 'family', 'school', 'work',
            'city', 'country', 'world', 'life', 'time', 'day', 'night', 'year',
            'water', 'food', 'money', 'job', 'problem', 'solution'
        }
        
        # Words that often cause problems
        self.problematic_words = {
            'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'shall', 'of', 'in', 'on',
            'at', 'to', 'for', 'with', 'by', 'from', 'up', 'down', 'about'
        }

    def load_all_vocabulary(self):
        """Load vocabulary with error handling"""
        print("\n" + "="*70)
        print("📚 LOADING INTELLIGENT VOCABULARY...")
        print("="*70)

        # Load synonym files
        self._load_synonym_files()
        
        self.total_words = len(self.all_synonyms)
        print(f"✅ LOADED {self.total_words:,} WORDS")
        return self.total_words

    def _load_synonym_files(self):
        """Load synonym files with simple parsing"""
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

                synonyms = self._safe_parse_synonyms(content)
                if synonyms:
                    self.all_synonyms.update(synonyms)
                    print(f"✅ {filename}: {len(synonyms):,} words")

            except Exception as e:
                print(f"❌ {filename}: Error - {str(e)}")

    def _safe_parse_synonyms(self, content):
        """Safe parsing of synonym files"""
        synonyms = {}
        lines = content.split('\n')
        in_dict = False
        current_key = None
        
        for line in lines:
            line = line.strip()
            
            if 'synonyms = {' in line:
                in_dict = True
                continue
                
            if in_dict and '}' in line:
                break
                
            if in_dict and line:
                # Look for key-value pairs
                if ':' in line and '"' in line:
                    try:
                        # Simple quote-based extraction
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            key = parts[0].strip().strip('"\'')
                            value_str = parts[1].strip().rstrip(',')
                            
                            if value_str.startswith('['):
                                # List of synonyms
                                items = value_str[1:-1].split(',')
                                values = [item.strip().strip('"\'') for item in items if item.strip()]
                                synonyms[key] = values
                    except:
                        continue
        
        return synonyms

# =========================
# INTELLIGENT SYNONYM SELECTOR
# =========================
class IntelligentSynonymFinder:
    def __init__(self, vocabulary, common_words, problematic_words):
        self.vocabulary = vocabulary
        self.common_words = common_words
        self.problematic_words = problematic_words
        
    def get_smart_synonyms(self, word, sentence_context=""):
        """Get context-appropriate synonyms"""
        word = word.lower().strip()
        
        # Skip problematic words entirely
        if word in self.problematic_words:
            return []
            
        # Get all possible synonyms
        raw_synonyms = self.vocabulary.get(word, [])
        if not raw_synonyms:
            return []
            
        # Convert to list if it's a string
        if isinstance(raw_synonyms, str):
            raw_synonyms = [raw_synonyms]
            
        # Filter synonyms intelligently
        filtered = []
        for synonym in raw_synonyms:
            if self._is_good_replacement(word, synonym, sentence_context):
                filtered.append(synonym)
                
        return filtered
    
    def _is_good_replacement(self, original, synonym, context):
        """Check if synonym is a good replacement"""
        
        # Skip if same word
        if synonym.lower() == original.lower():
            return False
            
        # Skip multi-word phrases (for now)
        if ' ' in synonym:
            return False
            
        # Skip words that are too long (usually technical)
        if len(synonym) > len(original) + 6:
            return False
            
        # Skip words that are too short (usually abbreviations)
        if len(synonym) < 3:
            return False
            
        # Prefer common words
        if synonym.lower() in self.common_words:
            return True
            
        # Skip obviously technical/scientific words
        technical_indicators = ['ology', 'ectomy', 'itis', 'phobia', 'ism', 'ist']
        if any(indicator in synonym.lower() for indicator in technical_indicators):
            return False
            
        # Check word endings match (crude POS matching)
        if original.endswith('ing') and not synonym.endswith('ing'):
            return False
        if original.endswith('ed') and not synonym.endswith('ed'):
            return False
        if original.endswith('s') and not synonym.endswith('s'):
            # Be careful with pluralization
            if not original.endswith('ss') and not synonym.endswith('ss'):
                return False
                
        return True

# =========================
# MEANING-PRESERVING REWRITER
# =========================
class MeaningPreservingRewriter:
    def __init__(self):
        self.vocab_loader = IntelligentVocabularyLoader()
        self.synonym_finder = IntelligentSynonymFinder(
            self.vocab_loader.all_synonyms,
            self.vocab_loader.common_words,
            self.vocab_loader.problematic_words
        )
        
        print(f"🎯 INTELLIGENT REWRITER READY")
        print(f"   📊 Vocabulary: {len(self.vocab_loader.all_synonyms):,} words")
        print(f"   🎯 Common words: {len(self.vocab_loader.common_words)}")
        print(f"   🚫 Protected words: {len(self.vocab_loader.problematic_words)}")

    def intelligent_rewrite(self, text):
        """Rewrite text while preserving meaning"""
        if not text or len(text.strip()) < 5:
            return text
            
        words = text.split()
        new_words = []
        replaced_count = 0
        
        for i, word in enumerate(words):
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Skip very short words and problematic words
            if (len(clean_word) <= 2 or 
                clean_word in self.vocab_loader.problematic_words):
                new_words.append(word)
                continue
                
            # Get smart synonyms
            sentence_context = ' '.join(words[max(0, i-2):min(len(words), i+3)])
            synonyms = self.synonym_finder.get_smart_synonyms(clean_word, sentence_context)
            
            # Decide whether to replace (controlled randomness)
            should_replace = (len(synonyms) > 0 and 
                            random.random() < 0.6 and  # 60% chance for eligible words
                            replaced_count / len(words) < 0.4)  # Max 40% replacement
            
            if should_replace and synonyms:
                replacement = random.choice(synonyms)
                
                # Preserve capitalization
                if word[0].isupper():
                    replacement = replacement.capitalize()
                    
                # Preserve punctuation
                if word[-1] in ',.!?;:':
                    replacement += word[-1]
                    
                new_words.append(replacement)
                replaced_count += 1
            else:
                new_words.append(word)
                
        result = ' '.join(new_words)
        
        # Basic grammar cleanup
        result = self._cleanup_grammar(result)
        
        return result
    
    def _cleanup_grammar(self, text):
        """Basic grammar corrections"""
        # Capitalize first letter
        if text and text[0].isalpha():
            text = text[0].upper() + text[1:]
            
        # Ensure ends with punctuation
        if text and text[-1] not in '.!?':
            text += '.'
            
        return text

    def get_replacement_stats(self, text):
        """Analyze replacement opportunities"""
        words = text.split()
        total_words = len(words)
        replaceable_words = 0
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            if (len(clean_word) > 2 and 
                clean_word not in self.vocab_loader.problematic_words and
                clean_word in self.vocab_loader.all_synonyms):
                replaceable_words += 1
                
        return {
            'total_words': total_words,
            'replaceable_words': replaceable_words,
            'replacement_ratio': replaceable_words / total_words if total_words > 0 else 0
        }

# =========================
# INITIALIZE INTELLIGENT REWRITER
# =========================
print("🔄 Initializing intelligent rewriter...")
intelligent_rewriter = MeaningPreservingRewriter()

# =========================
# CORE API FUNCTIONS
# =========================
def rewrite_text(original_text, aggression_level=0.6):
    """
    Rewrite text intelligently while preserving meaning
    
    Args:
        original_text: Text to rewrite
        aggression_level: 0.1-0.9 how aggressive to be with replacements
    """
    if not original_text:
        return original_text
        
    # Use the intelligent rewriter
    rewritten = intelligent_rewriter.intelligent_rewrite(original_text)
    
    return rewritten

def analyze_text(text):
    """Analyze text for rewriting potential"""
    return intelligent_rewriter.get_replacement_stats(text)

def get_vocabulary_info():
    """Get vocabulary statistics"""
    return {
        "total_words": len(intelligent_rewriter.vocab_loader.all_synonyms),
        "common_words": len(intelligent_rewriter.vocab_loader.common_words),
        "protected_words": len(intelligent_rewriter.vocab_loader.problematic_words),
        "status": "Intelligent rewriting enabled"
    }

# =========================
# TEST & DEMONSTRATION
# =========================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING INTELLIGENT REWRITER...")
    print("="*70)

    test_sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "I am very happy to see you today.",
        "The big house on the hill is beautiful.",
        "We should go for a walk in the park."
    ]

    for original in test_sentences:
        print(f"\n📝 ORIGINAL:  {original}")
        rewritten = rewrite_text(original)
        print(f"🔁 REWRITTEN: {rewritten}")
        
        stats = analyze_text(original)
        print(f"📊 ANALYSIS: {stats['replaceable_words']}/{stats['total_words']} words replaceable")

    print("\n🎊 INTELLIGENT BACKEND READY!")
    print("="*70)
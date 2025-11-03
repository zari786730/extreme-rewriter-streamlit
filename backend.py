# =========================
# UNIVERSAL INTELLIGENT REWRITER BACKEND
# =========================

import random
import re
import os
import glob

print("🌐 INITIALIZING UNIVERSAL INTELLIGENT REWRITER...")

# =========================
# UNIVERSAL VOCABULARY LOADER
# =========================
class UniversalVocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.load_all_vocabulary()

    def load_all_vocabulary(self):
        """Load all synonym files"""
        print("\n" + "="*70)
        print("📚 LOADING VOCABULARY DATABASE...")
        print("="*70)

        synonym_files = []
        
        # Check multiple possible locations
        possible_locations = [
            'vocabulary/',
            'Library/',
            '',
            'synonyms/'
        ]
        
        for location in possible_locations:
            pattern = os.path.join(location, 'synonyms_*.py')
            files = glob.glob(pattern)
            synonym_files.extend(files)

        # Remove duplicates
        synonym_files = list(set(synonym_files))
        
        print(f"🔍 Found {len(synonym_files)} synonym files")

        for filepath in sorted(synonym_files):
            filename = os.path.basename(filepath)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                synonyms = self._parse_synonyms(content)
                if synonyms:
                    self.all_synonyms.update(synonyms)
                    print(f"✅ {filename}: {len(synonyms):,} words")

            except Exception as e:
                print(f"❌ {filename}: Error - {str(e)}")

        self.total_words = len(self.all_synonyms)
        print(f"🎯 TOTAL VOCABULARY: {self.total_words:,} words")
        return self.total_words

    def _parse_synonyms(self, content):
        """Simple and reliable synonym parsing"""
        synonyms = {}
        lines = content.split('\n')
        in_dict = False
        
        for line in lines:
            line = line.strip()
            
            if 'synonyms = {' in line:
                in_dict = True
                continue
                
            if in_dict and '}' in line:
                break
                
            if in_dict and ':' in line:
                try:
                    # Extract key and value
                    key_part, value_part = line.split(':', 1)
                    key = key_part.strip().strip('"\'')
                    
                    # Clean value
                    value_str = value_part.strip().rstrip(',')
                    if value_str.startswith('[') and value_str.endswith(']'):
                        items = value_str[1:-1].split(',')
                        values = [item.strip().strip('"\'') for item in items if item.strip()]
                        synonyms[key] = values
                except:
                    continue
        
        return synonyms

# =========================
# UNIVERSAL CONTEXT ANALYZER
# =========================
class UniversalContextAnalyzer:
    def __init__(self):
        self.never_change_words = self._get_never_change_words()
        self.safe_to_change_words = self._get_safe_to_change_words()
    
    def _get_never_change_words(self):
        """Words that should NEVER be changed"""
        return {
            # Articles and basic connectors
            'a', 'an', 'the', 'and', 'or', 'but', 'if', 'of', 'in', 'on', 'at', 
            'to', 'for', 'with', 'by', 'from', 'up', 'down', 'about', 'over', 
            'under', 'through', 'during', 'before', 'after', 'between',
            
            # Common verbs (too fundamental)
            'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
            'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            
            # Pronouns
            'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
            'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their',
            
            # Basic question words
            'what', 'when', 'where', 'why', 'how', 'which', 'who', 'whom'
        }
    
    def _get_safe_to_change_words(self):
        """Word categories that are SAFE to change"""
        return {
            # Common adjectives
            'happy', 'sad', 'good', 'bad', 'big', 'small', 'fast', 'slow',
            'beautiful', 'ugly', 'smart', 'dumb', 'rich', 'poor', 'strong', 'weak',
            'hot', 'cold', 'new', 'old', 'young', 'tall', 'short', 'long',
            'heavy', 'light', 'dark', 'bright', 'clean', 'dirty', 'easy', 'hard',
            'simple', 'complex', 'important', 'funny', 'serious', 'quiet', 'loud',
            
            # Common verbs (action-oriented)
            'run', 'walk', 'talk', 'speak', 'say', 'tell', 'think', 'know',
            'see', 'look', 'watch', 'hear', 'listen', 'eat', 'drink', 'sleep',
            'work', 'play', 'read', 'write', 'learn', 'teach', 'help', 'give',
            'take', 'make', 'create', 'build', 'break', 'fix', 'buy', 'sell',
            'start', 'stop', 'begin', 'end', 'open', 'close',
            
            # Common nouns
            'house', 'home', 'car', 'book', 'friend', 'family', 'school', 'work',
            'city', 'country', 'world', 'life', 'time', 'day', 'night', 'year',
            'water', 'food', 'money', 'job', 'problem', 'solution', 'idea',
            'person', 'man', 'woman', 'child', 'people', 'place', 'thing'
        }
    
    def can_change_word(self, word, is_first_word=False):
        """
        UNIVERSAL DECISION: Can this word be safely changed?
        Returns: True (safe), False (never change), None (use default rules)
        """
        word_lower = word.lower()
        clean_word = re.sub(r'[^\w]', '', word_lower)
        
        # NEVER change these words
        if clean_word in self.never_change_words:
            return False
        
        # ALWAYS safe to change these words
        if clean_word in self.safe_to_change_words:
            return True
        
        # Default rules for unknown words
        return self._default_word_rules(word, clean_word, is_first_word)
    
    def _default_word_rules(self, word, clean_word, is_first_word):
        """Default rules for words not in our lists"""
        # Don't change very short words
        if len(clean_word) <= 2:
            return False
        
        # Don't change words that look technical/scientific
        if self._looks_technical(word, clean_word):
            return False
        
        # Don't change proper nouns (except first word of sentence)
        if word[0].isupper() and not is_first_word:
            return False
        
        # Don't change acronyms
        if word.isupper() and len(word) <= 5:
            return False
        
        # Don't change words with numbers or hyphens
        if any(c in word for c in '-0123456789'):
            return False
        
        # Safe to change common-looking words
        if len(clean_word) <= 8 and clean_word.isalpha():
            return True
        
        # Default: don't change unknown words
        return False
    
    def _looks_technical(self, word, clean_word):
        """Check if word looks technical/scientific"""
        # Long words often technical
        if len(clean_word) > 10:
            return True
        
        # Words with scientific suffixes
        technical_suffixes = {'ology', 'itis', 'ectomy', 'phobia', 'ism', 'zyme'}
        if any(clean_word.endswith(suffix) for suffix in technical_suffixes):
            return True
        
        # Words with scientific prefixes
        technical_prefixes = {'bio', 'chem', 'neuro', 'psych', 'electro'}
        if any(clean_word.startswith(prefix) for prefix in technical_prefixes):
            return True
        
        return False

# =========================
# UNIVERSAL REWRITER ENGINE
# =========================
class UniversalRewriterEngine:
    def __init__(self, vocabulary_loader):
        self.vocabulary = vocabulary_loader.all_synonyms
        self.context_analyzer = UniversalContextAnalyzer()
        
        print(f"🚀 UNIVERSAL REWRITER ENGINE READY")
        print(f"   📊 Vocabulary: {len(self.vocabulary):,} words")

    def rewrite_text(self, text, replacement_rate=0.3):
        """
        Universal text rewriting that works on ANY content
        replacement_rate: 0.1-0.9 how aggressive to be (default: 30%)
        """
        if not text or len(text.strip()) < 5:
            return text
            
        words = text.split()
        new_words = []
        replaced_count = 0
        total_changeable = 0
        
        for i, word in enumerate(words):
            is_first_word = (i == 0)
            
            # Check if we can change this word
            change_decision = self.context_analyzer.can_change_word(word, is_first_word)
            
            if change_decision is True:  # Safe to change
                total_changeable += 1
                
                # Decide whether to actually replace it
                should_replace = (
                    random.random() < replacement_rate and
                    replaced_count / max(1, total_changeable) < 0.5  # Max 50% of changeable words
                )
                
                if should_replace:
                    new_word = self._get_replacement(word)
                    if new_word != word:
                        new_words.append(new_word)
                        replaced_count += 1
                        continue
            
            # Keep original word
            new_words.append(word)
            
        result = ' '.join(new_words)
        return self._cleanup_text(result)
    
    def _get_replacement(self, original_word):
        """Get a replacement word that makes sense"""
        clean_original = re.sub(r'[^\w]', '', original_word.lower())
        synonyms = self.vocabulary.get(clean_original, [])
        
        if not synonyms:
            return original_word
        
        # Filter good replacements
        good_replacements = []
        for synonym in synonyms:
            if self._is_good_replacement(clean_original, synonym):
                good_replacements.append(synonym)
        
        if not good_replacements:
            return original_word
        
        # Choose a replacement
        replacement = random.choice(good_replacements)
        
        # Preserve original formatting
        if original_word[0].isupper():
            replacement = replacement.capitalize()
        
        # Preserve trailing punctuation
        if not original_word[-1].isalnum():
            replacement += original_word[-1]
            
        return replacement
    
    def _is_good_replacement(self, original, synonym):
        """Check if synonym is a good replacement"""
        # Don't replace with same word
        if synonym.lower() == original.lower():
            return False
        
        # Don't use multi-word phrases
        if ' ' in synonym:
            return False
        
        # Don't use much longer words
        if len(synonym) > len(original) + 4:
            return False
        
        # Don't use much shorter words
        if len(synonym) < len(original) - 3:
            return False
        
        return True
    
    def _cleanup_text(self, text):
        """Basic text cleanup"""
        # Fix spacing around punctuation
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        text = re.sub(r'([.,!?;])(\w)', r'\1 \2', text)
        
        # Ensure first letter is capitalized
        if text and text[0].isalpha():
            text = text[0].upper() + text[1:]
            
        return text

    def analyze_text(self, text):
        """Analyze what would be changed"""
        words = text.split()
        analysis = {
            'total_words': len(words),
            'never_change': [],
            'safe_to_change': [],
            'unknown': []
        }
        
        for i, word in enumerate(words):
            is_first_word = (i == 0)
            decision = self.context_analyzer.can_change_word(word, is_first_word)
            
            if decision is False:
                analysis['never_change'].append(word)
            elif decision is True:
                analysis['safe_to_change'].append(word)
            else:
                analysis['unknown'].append(word)
                
        return analysis

# =========================
# INITIALIZE UNIVERSAL REWRITER
# =========================
print("🔄 Loading vocabulary...")
vocab_loader = UniversalVocabularyLoader()
print("🔄 Initializing rewriter engine...")
universal_rewriter = UniversalRewriterEngine(vocab_loader)

# =========================
# CORE API FUNCTIONS
# =========================
def rewrite_text_universal(original_text, aggression=0.3):
    """
    Universal text rewriting - works on ANY content
    Args:
        original_text: Text to rewrite
        aggression: 0.1-0.9 how aggressive to be with replacements
    """
    return universal_rewriter.rewrite_text(original_text, aggression)

def analyze_text_content(text):
    """See what would be protected vs changed"""
    return universal_rewriter.analyze_text(text)

def get_system_info():
    """Get system information"""
    return {
        "vocabulary_size": len(universal_rewriter.vocabulary),
        "rewriter_type": "Universal Context-Aware",
        "status": "Ready",
        "capabilities": [
            "Automatic technical term protection",
            "Safe word replacement only",
            "Universal content handling",
            "Meaning preservation"
        ]
    }

# =========================
# TEST WITH VARIOUS CONTENT
# =========================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING UNIVERSAL REWRITER...")
    print("="*70)

    test_cases = [
        "The quick brown fox jumps over the lazy dog.",
        "DNA replication occurs during cell division in living organisms.",
        "The company reported strong financial results this quarter.",
        "Machine learning algorithms can process large datasets efficiently."
    ]

    for original in test_cases:
        print(f"\n📝 ORIGINAL:  {original}")
        
        analysis = analyze_text_content(original)
        print(f"🔍 ANALYSIS: {len(analysis['safe_to_change'])} safe, {len(analysis['never_change'])} protected")
        
        rewritten = rewrite_text_universal(original)
        print(f"🔁 REWRITTEN: {rewritten}")

    print("\n🎊 UNIVERSAL REWRITER BACKEND READY!")
    print("="*70)
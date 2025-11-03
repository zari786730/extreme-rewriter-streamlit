# =========================
# UNIVERSALLY INTELLIGENT REWRITER BACKEND
# =========================

import random
import re
import os
import glob

print("🌍 INITIALIZING UNIVERSALLY INTELLIGENT REWRITER...")

# =========================
# AUTOMATIC TERM DETECTION
# =========================
class IntelligentTermDetector:
    def __init__(self):
        self.common_words = self._load_common_words()
        self.problematic_suffixes = {
            'ology', 'itis', 'ectomy', 'phobia', 'ism', 'ist', 'genic', 'nomic',
            'lysis', 'zyme', 'some', 'blast', 'cyte', 'phage', 'troph'
        }
        
    def _load_common_words(self):
        """Load the most common English words"""
        return {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
            'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
            'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
            'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me',
            'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take',
            'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see',
            'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
            'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work',
            'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these',
            'give', 'day', 'most', 'us'
        }
    
    def should_protect_term(self, word, context_words=None):
        """Intelligently decide if a word should be protected from changes"""
        word_lower = word.lower()
        
        # 1. Always protect very common words (they're usually correct as-is)
        if word_lower in self.common_words:
            return True
            
        # 2. Protect words with scientific-looking suffixes
        if any(word_lower.endswith(suffix) for suffix in self.problematic_suffixes):
            return True
            
        # 3. Protect capitalized proper nouns (except sentence starters)
        if (word[0].isupper() and len(word) > 3 and 
            not (context_words and context_words[0] == word)):
            return True
            
        # 4. Protect words with numbers or special formats
        if any(char.isdigit() for char in word):
            return True
            
        # 5. Protect hyphenated words (often technical terms)
        if '-' in word:
            return True
            
        # 6. Protect very long words (often technical)
        if len(word) > 12:
            return True
            
        # 7. Protect acronyms (all caps)
        if word.isupper() and len(word) <= 5:
            return True
            
        return False

# =========================
# CONTEXT-AWARE VOCABULARY LOADER
# =========================
class UniversalVocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.term_detector = IntelligentTermDetector()
        self.load_all_vocabulary()

    def load_all_vocabulary(self):
        """Load vocabulary from all available files"""
        print("\n" + "="*70)
        print("📚 LOADING UNIVERSAL VOCABULARY...")
        print("="*70)

        self._load_synonym_files()
        
        self.total_words = len(self.all_synonyms)
        print(f"✅ LOADED {self.total_words:,} WORDS")
        return self.total_words

    def _load_synonym_files(self):
        """Load synonym files from multiple locations"""
        possible_paths = [
            'vocabulary/synonyms_*.py',
            'synonyms_*.py', 
            'Library/synonyms_*.py',
            '*.py'  # Fallback
        ]
        
        synonym_files = []
        for pattern in possible_paths:
            files = glob.glob(pattern)
            synonym_files.extend([f for f in files if 'synonyms_' in f])
        
        # Remove duplicates
        synonym_files = list(set(synonym_files))
        
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
        
        for line in lines:
            line = line.strip()
            
            if 'synonyms = {' in line:
                in_dict = True
                continue
                
            if in_dict and '}' in line:
                break
                
            if in_dict and ':' in line:
                try:
                    # Extract key-value pair
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
# UNIVERSAL INTELLIGENT REWRITER
# =========================
class UniversalIntelligentRewriter:
    def __init__(self):
        self.vocab_loader = UniversalVocabularyLoader()
        self.term_detector = IntelligentTermDetector()
        
        print(f"🎯 UNIVERSAL REWRITER READY")
        print(f"   📊 Vocabulary: {len(self.vocab_loader.all_synonyms):,} words")

    def universal_rewrite(self, text):
        """Intelligently rewrite ANY text while preserving meaning and technical terms"""
        if not text or len(text.strip()) < 5:
            return text
            
        sentences = self._split_sentences(text)
        rewritten_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                rewritten = self._rewrite_sentence(sentence)
                rewritten_sentences.append(rewritten)
        
        result = ' '.join(rewritten_sentences)
        return self._cleanup_text(result)
    
    def _split_sentences(self, text):
        """Split text into sentences"""
        # Simple sentence splitting
        sentences = []
        current = ""
        
        for char in text:
            current += char
            if char in '.!?':
                sentences.append(current.strip())
                current = ""
        
        if current.strip():
            sentences.append(current.strip())
            
        return sentences

    def _rewrite_sentence(self, sentence):
        """Rewrite a single sentence intelligently"""
        words = re.findall(r"[\w']+|[.,!?;]", sentence)
        new_words = []
        replaced_count = 0
        
        for i, word in enumerate(words):
            # Skip punctuation
            if word in '.!?;,':
                new_words.append(word)
                continue
                
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Get context for intelligent decision
            context_words = words[max(0, i-2):min(len(words), i+2)]
            
            # INTELLIGENT DECISION: Should we protect this word?
            if self.term_detector.should_protect_term(word, context_words):
                new_words.append(word)
                continue
                
            # Get synonyms for non-protected words
            synonyms = self.vocab_loader.all_synonyms.get(clean_word, [])
            if isinstance(synonyms, str):
                synonyms = [synonyms]
                
            # Filter good synonyms
            good_synonyms = [s for s in synonyms if self._is_good_replacement(clean_word, s)]
            
            # Decide whether to replace
            should_replace = (
                good_synonyms and 
                random.random() < 0.5 and  # 50% chance
                replaced_count / len([w for w in words if w not in '.!?;,']) < 0.3  # Max 30% replacement
            )
            
            if should_replace:
                replacement = random.choice(good_synonyms)
                
                # Preserve original formatting
                if word[0].isupper():
                    replacement = replacement.capitalize()
                    
                new_words.append(replacement)
                replaced_count += 1
            else:
                new_words.append(word)
                
        return ' '.join(new_words)

    def _is_good_replacement(self, original, synonym):
        """Check if synonym is appropriate"""
        # Don't replace with same word
        if synonym.lower() == original.lower():
            return False
            
        # Don't replace with multi-word phrases
        if ' ' in synonym:
            return False
            
        # Don't replace with much longer words
        if len(synonym) > len(original) + 5:
            return False
            
        # Don't replace with very short words
        if len(synonym) < 3:
            return False
            
        return True

    def _cleanup_text(self, text):
        """Clean up the final text"""
        # Ensure proper spacing around punctuation
        text = re.sub(r'\s+([.,!?])', r'\1', text)
        text = re.sub(r'([.,!?])(\w)', r'\1 \2', text)
        
        # Capitalize first letter
        if text and text[0].isalpha():
            text = text[0].upper() + text[1:]
            
        return text

    def analyze_text(self, text):
        """Analyze what the rewriter would protect/change"""
        words = re.findall(r"[\w']+", text)
        analysis = {
            'total_words': len(words),
            'protected_words': [],
            'changeable_words': []
        }
        
        for i, word in enumerate(words):
            context = words[max(0, i-2):min(len(words), i+2)]
            if self.term_detector.should_protect_term(word, context):
                analysis['protected_words'].append(word)
            else:
                analysis['changeable_words'].append(word)
                
        return analysis

# =========================
# INITIALIZE UNIVERSAL REWRITER
# =========================
print("🔄 Initializing universal rewriter...")
universal_rewriter = UniversalIntelligentRewriter()

# =========================
# CORE API FUNCTIONS
# =========================
def rewrite_text_intelligent(original_text):
    """
    Universal intelligent text rewriting
    - Automatically detects and protects technical terms
    - Only changes appropriate words
    - Preserves meaning and readability
    """
    return universal_rewriter.universal_rewrite(original_text)

def analyze_text_intelligent(text):
    """See what would be protected vs changed"""
    return universal_rewriter.analyze_text(text)

def get_rewriter_stats():
    return {
        "vocabulary_size": len(universal_rewriter.vocab_loader.all_synonyms),
        "type": "Universal Intelligent Rewriter",
        "capabilities": [
            "Automatic technical term detection",
            "Scientific term protection", 
            "Context-aware replacements",
            "Meaning preservation"
        ]
    }

# =========================
# TEST WITH YOUR DNA TEXT
# =========================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING UNIVERSAL REWRITER...")
    print("="*70)

    dna_text = "Deoxyribonucleic acid, commonly known as DNA, is the hereditary material that carries the genetic instructions."
    
    print("🔍 ANALYSIS:")
    analysis = analyze_text_intelligent(dna_text)
    print(f"Protected: {analysis['protected_words']}")
    print(f"Changeable: {analysis['changeable_words']}")
    
    print(f"\n📝 ORIGINAL: {dna_text}")
    rewritten = rewrite_text_intelligent(dna_text)
    print(f"🔁 REWRITTEN: {rewritten}")
    
    print("\n🎊 UNIVERSAL INTELLIGENT BACKEND READY!")
    print("="*70)
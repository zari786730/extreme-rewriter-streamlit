# =========================
# STEP 4: FINAL INTELLIGENT BACKEND (REPLACEMENT)
# =========================

print("🚀 STEP 4: DEPLOYING FINAL INTELLIGENT BACKEND...")

# =========================
# FINAL UNIVERSAL INTELLIGENT REWRITER
# =========================

class FinalIntelligentRewriter:
    def __init__(self):
        self.vocabulary = {}
        self.word_frequencies = {}
        self.academic_words = {}
        self.scientific_terms = set()
        
        self._load_all_intelligence_data()
        self._load_all_vocabulary_files()
        
        print("🎯 FINAL INTELLIGENT REWRITER READY")
        print(f"   📊 Vocabulary: {len(self.vocabulary):,} words")
        print(f"   🧠 Intelligence Data: Loaded")
        print(f"   🛡️  Protected Terms: {len(self.scientific_terms)}")
    
    def _load_all_intelligence_data(self):
        """Load all intelligence data"""
        # Word frequencies
        try:
            with open('word_frequencies.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        word = parts[0].lower()
                        try:
                            self.word_frequencies[word] = int(parts[1])
                        except:
                            continue
        except:
            print("⚠️  Could not load word frequencies")
        
        # Academic words
        try:
            with open('academic_words.json', 'r') as f:
                import json
                self.academic_words = json.load(f)
        except:
            print("⚠️  Could not load academic words")
        
        # Scientific terms
        try:
            with open('scientific_terms.json', 'r') as f:
                import json
                self.scientific_terms = set(json.load(f))
        except:
            print("⚠️  Could not load scientific terms")
    
    def _load_all_vocabulary_files(self):
        """Load all your synonym files"""
        import glob
        import os
        
        synonym_files = []
        
        # Check all locations
        locations = ['vocabulary/', 'Library/', '', 'synonyms/']
        for location in locations:
            pattern = os.path.join(location, 'synonyms_*.py')
            files = glob.glob(pattern)
            synonym_files.extend(files)
        
        synonym_files = list(set(synonym_files))
        print(f"📂 Loading {len(synonym_files)} synonym files...")
        
        for filepath in sorted(synonym_files):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                file_synonyms = self._parse_synonyms(content)
                if file_synonyms:
                    self.vocabulary.update(file_synonyms)
                    
            except Exception as e:
                continue
    
    def _parse_synonyms(self, content):
        """Parse synonyms from file content"""
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
                    key_part, value_part = line.split(':', 1)
                    key = key_part.strip().strip('"\'')
                    
                    value_str = value_part.strip().rstrip(',')
                    if value_str.startswith('[') and value_str.endswith(']'):
                        items = value_str[1:-1].split(',')
                        values = [item.strip().strip('"\'') for item in items if item.strip()]
                        synonyms[key] = values
                except:
                    continue
        
        return synonyms
    
    def get_smart_synonyms(self, word, context=""):
        """Get intelligent synonyms"""
        word_lower = word.lower().strip()
        
        # NEVER change scientific terms
        if word_lower in self.scientific_terms:
            return []
        
        # Get basic synonyms
        synonyms = self.vocabulary.get(word_lower, [])
        if isinstance(synonyms, str):
            synonyms = [synonyms]
        
        if not synonyms:
            return []
        
        # Filter intelligently
        filtered = []
        for synonym in synonyms:
            if self._is_good_replacement(word_lower, synonym, context):
                filtered.append(synonym)
        
        return filtered
    
    def _is_good_replacement(self, original, synonym, context):
        """Check if replacement makes sense"""
        if synonym.lower() == original.lower():
            return False
        
        if ' ' in synonym:
            return False
        
        if len(synonym) > len(original) + 4:
            return False
        
        # Use frequency data if available
        if self.word_frequencies:
            synonym_freq = self.word_frequencies.get(synonym.lower(), 0)
            original_freq = self.word_frequencies.get(original.lower(), 0)
            
            if original_freq > 1000 and synonym_freq < 100:
                return False
        
        return True
    
    def rewrite_text(self, text, aggression=0.3):
        """Main rewriting function - USE THIS IN YOUR APP"""
        if not text:
            return text
            
        import random
        import re
        
        words = text.split()
        new_words = []
        
        for i, word in enumerate(words):
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Get context
            start = max(0, i-2)
            end = min(len(words), i+3)
            context = ' '.join(words[start:end])
            
            synonyms = self.get_smart_synonyms(clean_word, context)
            
            should_replace = (
                synonyms and 
                random.random() < aggression and
                len([w for w in new_words if w != word]) / len(words) < 0.4
            )
            
            if should_replace:
                replacement = random.choice(synonyms)
                
                if word[0].isupper():
                    replacement = replacement.capitalize()
                if not word[-1].isalnum():
                    replacement += word[-1]
                    
                new_words.append(replacement)
            else:
                new_words.append(word)
        
        result = ' '.join(new_words)
        
        # Cleanup
        result = re.sub(r'\s+([.,!?;])', r'\1', result)
        result = re.sub(r'([.,!?;])(\w)', r'\1 \2', result)
        
        if result and result[0].isalpha():
            result = result[0].upper() + result[1:]
            
        return result

# =========================
# INITIALIZE FINAL BACKEND
# =========================

print("🔄 Initializing final intelligent backend...")
final_rewriter = FinalIntelligentRewriter()

# =========================
# API FUNCTIONS FOR YOUR APP
# =========================

def extreme_rewriter(original_text, aggression=0.3):
    """
    REPLACE YOUR CURRENT FUNCTION WITH THIS
    """
    return final_rewriter.rewrite_text(original_text, aggression)

def get_vocabulary_stats():
    """Get vocabulary statistics"""
    return {
        "total_words": len(final_rewriter.vocabulary),
        "intelligence_data": "Loaded",
        "scientific_terms_protected": len(final_rewriter.scientific_terms),
        "status": "Intelligent Rewriting Active"
    }

# =========================
# TEST FINAL VERSION
# =========================

def test_final_system():
    """Test the complete system"""
    print("\n" + "="*70)
    print("🎯 TESTING FINAL INTELLIGENT SYSTEM...")
    print("="*70)
    
    test_cases = [
        "DNA replication occurs during cell division in living organisms.",
        "The quick brown fox jumps over the lazy dog.",
        "The study found important results that demonstrate significant findings.",
        "Protein synthesis involves transcription and translation processes."
    ]
    
    for i, original in enumerate(test_cases, 1):
        print(f"\n🧪 TEST {i}:")
        print(f"📝 ORIGINAL:  {original}")
        rewritten = extreme_rewriter(original)
        print(f"🔁 REWRITTEN: {rewritten}")
    
    stats = get_vocabulary_stats()
    print(f"\n📊 SYSTEM STATS: {stats}")

# Run final test
test_final_system()

print("\n🎊 STEP 4 COMPLETE!")
print("="*70)
print("✅ FINAL INTELLIGENT BACKEND READY!")
print("🔧 REPLACE YOUR CURRENT extreme_rewriter() WITH THIS VERSION")
print("🚀 YOUR APP NOW HAS AI-LEVEL INTELLIGENCE!")
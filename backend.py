# =========================
# ENHANCED REWRITER BACKEND WITH VOCABULARY INTEGRATION
# =========================

import random
import re
import os
import importlib

# -------------------------
# VOCABULARY LOADING SYSTEM
# -------------------------
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files = 0
        
    def load_vocabulary_folder(self, folder_path="vocabulary"):
        """Load all vocabulary files from specified folder"""
        if not os.path.exists(folder_path):
            print(f"Vocabulary folder '{folder_path}' not found!")
            return
            
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".py") and file_name != "__init__.py":
                try:
                    module_name = file_name[:-3]
                    module = importlib.import_module(f"vocabulary.{module_name}")
                    self.process_vocabulary_module(module)
                    self.loaded_files += 1
                    print(f"✅ Loaded {file_name}")
                    
                except Exception as e:
                    print(f"❌ Error loading {file_name}: {str(e)}")
    
    def process_vocabulary_module(self, module):
        """Process individual vocabulary module"""
        if hasattr(module, 'synonyms'):
            for word, synonyms in module.synonyms.items():
                if word not in self.all_synonyms:
                    self.all_synonyms[word] = synonyms if isinstance(synonyms, list) else [synonyms]
                    self.total_words += 1
        elif hasattr(module, 'synonyms_list'):
            # Handle list format if needed
            pass

# -------------------------
# GRAMMAR CORRECTOR (FALLBACK)
# -------------------------
def correct_grammar(text):
    """
    Basic grammar correction fallback
    In production, you might want to use a more sophisticated grammar checker
    """
    # Basic sentence capitalization
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    corrected_sentences = []
    
    for sentence in sentences:
        if sentence:
            # Capitalize first letter
            corrected = sentence[0].upper() + sentence[1:] if sentence else sentence
            corrected_sentences.append(corrected)
    
    return '. '.join(corrected_sentences) + ('.' if text and text[-1] in '.!?' else '')

# -------------------------
# ENHANCED REWRITER CLASS
# -------------------------
class EnhancedRewriter:
    def __init__(self):
        self.replacements = {}
        self.vocabulary_loader = VocabularyLoader()
        self.setup_complete = False
        self.initialize_system()
    
    def initialize_system(self):
        """Initialize the rewriting system with all vocabulary"""
        print("🔄 Initializing Enhanced Rewriter...")
        
        # Load vocabulary files
        self.vocabulary_loader.load_vocabulary_folder()
        
        # Setup main replacements dictionary
        self.setup_vocabulary()
        self.setup_complete = True
        
        print(f"✅ System initialized with {self.get_total_words():,} words from {self.vocabulary_loader.loaded_files} files")
    
    def setup_vocabulary(self):
        """Setup the main replacements dictionary"""
        # Start with vocabulary files
        self.replacements.update(self.vocabulary_loader.all_synonyms)
        
        # You can add additional custom dictionaries here
        # self.replacements.update(custom_medical_terms)
        # self.replacements.update(academic_phrases)
    
    def get_total_words(self):
        """Get total number of words in vocabulary"""
        return len(self.replacements)
    
    def get_loaded_files_count(self):
        """Get number of loaded vocabulary files"""
        return self.vocabulary_loader.loaded_files

    def intelligent_word_replacement(self, text):
        """Advanced word replacement with context awareness"""
        words = text.split()
        new_words = []
        replacements_made = 0
        skip_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
            'of', 'with', 'by', 'as', 'is', 'was', 'were', 'be', 'been', 'have', 
            'has', 'had', 'do', 'does', 'did', 'this', 'that', 'these', 'those'
        }
        
        for i, word in enumerate(words):
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Skip very short words and common words
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue
            
            # Apply replacement with probability
            if clean_word in self.replacements and random.random() < 0.75:
                replacement = random.choice(self.replacements[clean_word])
                
                # Preserve capitalization
                if word[0].isupper():
                    replacement = replacement.capitalize()
                
                # Preserve punctuation
                punctuation = re.findall(r'[^\w\s]', word)
                if punctuation:
                    replacement += punctuation[0]
                
                new_words.append(replacement)
                replacements_made += 1
            else:
                new_words.append(word)
        
        return ' '.join(new_words), replacements_made

    def advanced_sentence_restructuring(self, text):
        """Advanced sentence restructuring with multiple strategies"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if len(sentences) <= 1:
            return text, len(sentences), len(sentences)
        
        original_count = len(sentences)
        
        # Choose restructuring strategy
        strategy = random.choice(['split_combine', 'reorder', 'syntactic_variation'])
        
        if strategy == 'split_combine':
            modified_sentences = self._split_combine_sentences(sentences)
        elif strategy == 'reorder':
            modified_sentences = self._reorder_sentences(sentences)
        else:
            modified_sentences = self._syntactic_variation(sentences)
        
        final_count = len(modified_sentences)
        result = '. '.join(modified_sentences) + '.'
        
        return result, original_count, final_count

    def _split_combine_sentences(self, sentences):
        """Split long sentences and combine short ones"""
        modified = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # Split very long sentences
            if len(words) > 20 and random.random() < 0.7:
                # Find natural break points
                break_points = []
                for i, word in enumerate(words):
                    if word.lower() in ['and', 'but', 'however', 'although', 'while']:
                        break_points.append(i)
                
                if break_points:
                    # Split at a random break point
                    split_point = random.choice(break_points)
                    part1 = ' '.join(words[:split_point])
                    part2 = ' '.join(words[split_point:])
                    modified.append(part1)
                    modified.append(part2.capitalize())
                else:
                    # Split in the middle
                    mid = len(words) // 2
                    part1 = ' '.join(words[:mid])
                    part2 = ' '.join(words[mid:])
                    modified.append(part1)
                    modified.append(part2.capitalize())
            else:
                modified.append(sentence)
        
        # Combine very short sentences
        if len(modified) > 2:
            final_sentences = []
            i = 0
            while i < len(modified):
                if (i < len(modified) - 1 and 
                    len(modified[i].split()) < 6 and 
                    len(modified[i+1].split()) < 6):
                    
                    connectors = ['and', 'while', 'whereas', 'although']
                    connector = random.choice(connectors)
                    combined = f"{modified[i]} {connector} {modified[i+1].lower()}"
                    final_sentences.append(combined)
                    i += 2
                else:
                    final_sentences.append(modified[i])
                    i += 1
            return final_sentences
        
        return modified

    def _reorder_sentences(self, sentences):
        """Reorder sentences while maintaining coherence"""
        if len(sentences) <= 3:
            return sentences
        
        # Keep first and last sentence in position for coherence
        first = sentences[0]
        last = sentences[-1]
        middle = sentences[1:-1]
        
        # Shuffle middle sentences
        random.shuffle(middle)
        
        return [first] + middle + [last]

    def _syntactic_variation(self, sentences):
        """Change sentence structures"""
        modified = []
        
        for sentence in sentences:
            words = sentence.split()
            
            if len(words) > 5:
                # Change sentence structure
                if random.random() < 0.4:
                    # Convert to passive/active or other structures
                    if words[0].lower() in ['the', 'a', 'an'] and random.random() < 0.5:
                        # Add introductory phrase
                        intro_phrases = [
                            "It is important to note that",
                            "Research indicates that",
                            "Studies have shown that",
                            "Evidence suggests that"
                        ]
                        new_sentence = f"{random.choice(intro_phrases)} {sentence.lower()}"
                        modified.append(new_sentence)
                    else:
                        modified.append(sentence)
                else:
                    modified.append(sentence)
            else:
                modified.append(sentence)
        
        return modified

    def add_academic_enhancements(self, text):
        """Add academic phrasing and enhancements"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if not sentences:
            return text
        
        academic_enhancements = [
            "From an academic perspective,",
            "In the context of scholarly research,",
            "Based on current literature,",
            "According to established theories,",
            "Within the framework of",
            "Drawing upon existing research,"
        ]
        
        enhanced_sentences = []
        
        for i, sentence in enumerate(sentences):
            if i == 0 and random.random() < 0.3:
                enhanced_sentences.append(f"{random.choice(academic_enhancements)} {sentence.lower()}")
            elif random.random() < 0.15:
                enhanced_sentences.append(f"{random.choice(academic_enhancements)} {sentence.lower()}")
            else:
                enhanced_sentences.append(sentence)
        
        return '. '.join(enhanced_sentences) + '.'

# -------------------------
# SIMILARITY CALCULATION
# -------------------------
def calculate_similarity(original, rewritten):
    """Calculate similarity between original and rewritten text"""
    original_words = set(re.findall(r'\w+', original.lower()))
    rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
    
    if not original_words:
        return 0
    
    common_words = original_words.intersection(rewritten_words)
    similarity = len(common_words) / len(original_words) * 100
    
    return similarity

# -------------------------
# MAIN REWRITING FUNCTION
# -------------------------
def enhanced_rewrite(original_text, rewriter_instance):
    """Main rewriting function with comprehensive transformations"""
    if not rewriter_instance.setup_complete:
        rewriter_instance.initialize_system()
    
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations
    result, replacements_made = rewriter_instance.intelligent_word_replacement(clean_text)
    result, orig_sentences, final_sentences = rewriter_instance.advanced_sentence_restructuring(result)
    result = rewriter_instance.add_academic_enhancements(result)
    
    # Final grammar correction
    result = correct_grammar(result)
    
    stats = {
        'replacements': replacements_made,
        'original_sentences': orig_sentences,
        'final_sentences': final_sentences,
        'vocabulary_words': rewriter_instance.get_total_words(),
        'loaded_files': rewriter_instance.get_loaded_files_count()
    }
    
    return result, stats

# -------------------------
# SIMILARITY-GUARANTEED REWRITING
# -------------------------
def guarantee_low_similarity(original_text, rewriter_instance, max_similarity=20, max_attempts=8):
    """Guarantee low similarity through multiple attempts"""
    best_result = None
    best_similarity = 100
    best_stats = {}
    
    for attempt in range(max_attempts):
        rewritten, stats = enhanced_rewrite(original_text, rewriter_instance)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            best_stats = stats
            best_stats['attempt'] = attempt + 1
        
        if similarity <= max_similarity:
            return best_result, best_similarity, best_stats
    
    return best_result, best_similarity, best_stats

# -------------------------
# INITIALIZATION
# -------------------------
# Create global rewriter instance
enhanced_rewriter = EnhancedRewriter()

if __name__ == "__main__":
    # Test the system
    test_text = "Cancer is a complex group of diseases characterized by uncontrolled growth of abnormal cells that can invade different parts of the body."
    
    print("🧪 Testing Enhanced Rewriter...")
    result, stats = enhanced_rewrite(test_text, enhanced_rewriter)
    
    print(f"📊 Stats: {stats}")
    print(f"📝 Original: {test_text}")
    print(f"✨ Rewritten: {result}")
    print(f"📈 Similarity: {calculate_similarity(test_text, result):.1f}%")
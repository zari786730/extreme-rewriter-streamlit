# =========================
# FIXED BACKEND REWRITER
# =========================

import random
import re
import os
import importlib.util

class FixedRewriter:
    def __init__(self):
        self.replacements = {}
        self.total_words = 0
        self.loaded_files = 0
        self.load_vocabulary()
    
    def load_vocabulary(self):
        """Load vocabulary files from the vocabulary folder"""
        vocab_folder = "vocabulary"
        
        if not os.path.exists(vocab_folder):
            print("❌ Vocabulary folder not found!")
            return
        
        for file_name in os.listdir(vocab_folder):
            if file_name.endswith(".py") and file_name != "__init__.py":
                try:
                    file_path = os.path.join(vocab_folder, file_name)
                    
                    # Load module manually
                    spec = importlib.util.spec_from_file_location(file_name[:-3], file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Extract synonyms
                    if hasattr(module, 'synonyms'):
                        for word, synonyms in module.synonyms.items():
                            if word not in self.replacements:
                                self.replacements[word] = synonyms if isinstance(synonyms, list) else [synonyms]
                                self.total_words += 1
                    
                    self.loaded_files += 1
                    print(f"✅ Loaded {file_name} with {len(module.synonyms) if hasattr(module, 'synonyms') else 0} words")
                    
                except Exception as e:
                    print(f"❌ Error loading {file_name}: {str(e)}")
        
        print(f"🎯 Total: {self.total_words} words from {self.loaded_files} files")
    
    def rewrite_text(self, text, intensity=0.7):
        """Rewrite text with vocabulary replacements"""
        if not text.strip():
            return text
        
        sentences = re.split(r'[.!?]+', text)
        rewritten_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            words = sentence.strip().split()
            new_words = []
            
            for word in words:
                clean_word = re.sub(r'[^\w]', '', word.lower())
                
                # Skip common short words
                if (len(clean_word) <= 2 or 
                    clean_word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for']):
                    new_words.append(word)
                    continue
                
                # Apply replacement with probability based on intensity
                if (clean_word in self.replacements and 
                    random.random() < intensity):
                    
                    replacement = random.choice(self.replacements[clean_word])
                    
                    # Preserve capitalization
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    
                    # Preserve trailing punctuation
                    punctuation = re.findall(r'[^\w\s]', word)
                    if punctuation:
                        replacement += punctuation[0]
                    
                    new_words.append(replacement)
                else:
                    new_words.append(word)
            
            # Reconstruct sentence
            if new_words:
                new_sentence = ' '.join(new_words)
                rewritten_sentences.append(new_sentence)
        
        # Join sentences with periods
        result = '. '.join(rewritten_sentences) + '.' if rewritten_sentences else ""
        return result
    
    def calculate_similarity(self, original, rewritten):
        """Calculate similarity between original and rewritten text"""
        original_words = set(re.findall(r'\w+', original.lower()))
        rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
        
        if not original_words:
            return 0
        
        common_words = original_words.intersection(rewritten_words)
        similarity = len(common_words) / len(original_words) * 100
        
        return similarity
    
    def guarantee_low_similarity(self, text, max_similarity=20, max_attempts=5):
        """Generate rewritten text with guaranteed low similarity"""
        best_result = text
        best_similarity = 100
        
        for attempt in range(max_attempts):
            # Vary intensity for different attempts
            intensity = 0.5 + (attempt * 0.1)
            rewritten = self.rewrite_text(text, intensity)
            similarity = self.calculate_similarity(text, rewritten)
            
            if similarity < best_similarity:
                best_result = rewritten
                best_similarity = similarity
            
            if similarity <= max_similarity:
                return rewritten, similarity, attempt + 1
        
        return best_result, best_similarity, max_attempts

# Create global instance
fixed_rewriter = FixedRewriter()

# Test function
def test_rewriter():
    test_text = "Cancer is a complex disease characterized by uncontrolled growth of abnormal cells."
    
    print("🧪 Testing Fixed Rewriter...")
    result, similarity, attempts = fixed_rewriter.guarantee_low_similarity(test_text)
    
    print(f"📝 Original: {test_text}")
    print(f"✨ Rewritten: {result}")
    print(f"📈 Similarity: {similarity:.1f}%")
    print(f"🔄 Attempts: {attempts}")
    print(f"📚 Vocabulary: {fixed_rewriter.total_words} words")

if __name__ == "__main__":
    test_rewriter()
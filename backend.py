# =========================
# SIMPLE BACKEND REWRITER
# =========================

import random
import re

class SimpleRewriter:
    def __init__(self):
        self.replacements = {}
        self.setup_vocabulary()
    
    def setup_vocabulary(self):
        """Basic vocabulary setup"""
        self.replacements = {
            "cancer": ["malignancy", "carcinoma", "neoplasm"],
            "disease": ["disorder", "condition", "ailment"],
            "treatment": ["therapy", "intervention", "management"],
            "study": ["research", "investigation", "analysis"],
            "result": ["outcome", "finding", "conclusion"],
            "important": ["significant", "crucial", "essential"],
            "show": ["demonstrate", "indicate", "reveal"],
            "patient": ["individual", "case", "subject"],
            "cell": ["cellular unit", "biological unit"],
            "growth": ["proliferation", "development", "expansion"],
        }
    
    def rewrite_text(self, text):
        """Simple text rewriting"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            if clean_word in self.replacements and random.random() < 0.6:
                replacement = random.choice(self.replacements[clean_word])
                if word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(word)
        
        return ' '.join(new_words)

# Test
if __name__ == "__main__":
    rewriter = SimpleRewriter()
    test_text = "Cancer is a complex disease that requires treatment."
    result = rewriter.rewrite_text(test_text)
    print(f"Original: {test_text}")
    print(f"Rewritten: {result}")
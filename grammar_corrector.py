import re

class IntelligentGrammarCorrector:
    def __init__(self):
        self.grammar_rules = self.setup_grammar_rules()
        self.common_errors = self.setup_common_errors()
    
    def setup_grammar_rules(self):
        """Comprehensive grammar rules without AI"""
        return {
            # Capitalization rules
            r'^([a-z])': lambda m: m.group(1).upper(),
            r'([.!?]\s+)([a-z])': lambda m: m.group(1) + m.group(2).upper(),
            
            # Punctuation fixes
            r',\s*,': ',',
            r'\.\s*\.': '.',
            r'\s+\.': '.',
            r'\s+,': ',',
            r',\s*\.': '.',
            r';\s*;': ';',
            
            # Spacing fixes
            r'\s{2,}': ' ',
            r'\s+([.,!?;])': r'\1',
            r'([.,!?;])([A-Za-z])': r'\1 \2',
            r'\(\s*': '(',
            r'\s*\)': ')',
            
            # Sentence structure
            r'\.([A-Za-z])': r'. \1',
            r'\!([A-Za-z])': r'! \1',
            r'\?([A-Za-z])': r'? \1',
        }
    
    def setup_common_errors(self):
        """Common grammatical errors and their corrections"""
        return {
            r'\bi\s': 'I ',
            r'\balot\b': 'a lot',
            r'\bnoone\b': 'no one',
            r'\beverytime\b': 'every time',
            r'\banytime\b': 'any time',
            r'\bsometime\b': 'some time',
            
            # Verb agreement
            r'\bthey is\b': 'they are',
            r'\bhe are\b': 'he is',
            r'\bshe are\b': 'she is',
            r'\bit are\b': 'it is',
            
            # Common confusions
            r'\byour\b': 'you\'re',
            r'\btheir\b': 'they\'re',
            r'\bits\b': 'it\'s',
            r'\bwhos\b': 'who\'s',
            
            # Double words
            r'\bthe the\b': 'the',
            r'\band and\b': 'and',
            r'\bin in\b': 'in',
            r'\bis is\b': 'is',
        }
    
    def fix_sentence_fragments(self, text):
        """Fix incomplete sentences and fragments"""
        sentences = re.split(r'([.!?]+)', text)
        corrected = []
        
        for i in range(0, len(sentences), 2):
            if i < len(sentences):
                sentence = sentences[i].strip()
                punctuation = sentences[i + 1] if i + 1 < len(sentences) else '.'
                
                if sentence:
                    # Check if sentence is too short to stand alone
                    words = sentence.split()
                    if len(words) < 3 and len(corrected) > 0:
                        # Merge with previous sentence
                        if corrected:
                            corrected[-1] = corrected[-1].rstrip('.,!?') + ', ' + sentence.lower()
                        else:
                            corrected.append(sentence.capitalize() + punctuation)
                    else:
                        corrected.append(sentence.capitalize() + punctuation)
        
        return ' '.join(corrected)
    
    def fix_comma_overuse(self, text):
        """Remove excessive commas while keeping necessary ones"""
        # Remove commas before short words
        text = re.sub(r',\s+(and|or|but)\s+', r' \1 ', text)
        
        # Remove commas in simple lists
        text = re.sub(r'(\w+), (\w+), (\w+)', r'\1, \2 and \3', text)
        
        # Remove commas between very short phrases
        sentences = re.split(r'[.!?]', text)
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                parts = sentence.split(',')
                if len(parts) > 3:  # Too many commas
                    # Keep only necessary commas
                    cleaned = parts[0] + ', ' + ' '.join(parts[1:])
                    corrected_sentences.append(cleaned)
                else:
                    corrected_sentences.append(sentence)
        
        return '. '.join(corrected_sentences) + '.'
    
    def fix_article_agreement(self, text):
        """Fix a/an article usage"""
        text = re.sub(r'\ba ([aeiouAEIOU])', r'an \1', text)
        text = re.sub(r'\ban ([^aeiouAEIOU])', r'a \1', text)
        return text
    
    def fix_repeated_words(self, text):
        """Remove accidentally repeated words"""
        words = text.split()
        corrected_words = []
        
        for i, word in enumerate(words):
            if i == 0 or word.lower() != words[i-1].lower():
                corrected_words.append(word)
        
        return ' '.join(corrected_words)
    
    def fix_capitalization_consistency(self, text):
        """Ensure consistent capitalization in sentences"""
        sentences = re.split(r'([.!?]+\s*)', text)
        corrected = []
        
        for i in range(0, len(sentences), 2):
            if i < len(sentences):
                sentence = sentences[i].strip()
                punctuation = sentences[i + 1] if i + 1 < len(sentences) else ''
                
                if sentence:
                    # Capitalize first letter
                    sentence = sentence[0].upper() + sentence[1:]
                    corrected.append(sentence + punctuation)
        
        return ''.join(corrected)
    
    def fix_spacing_issues(self, text):
        """Fix all spacing problems"""
        # Remove spaces before punctuation
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        
        # Add spaces after punctuation
        text = re.sub(r'([.,!?;])([A-Za-z])', r'\1 \2', text)
        
        # Fix space after commas
        text = re.sub(r',(\S)', r', \1', text)
        
        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def intelligent_grammar_correction(self, text):
        """Main grammar correction function - completely AI-free"""
        if not text or len(text.strip()) < 10:
            return text
        
        # Step 1: Fix basic grammar rules
        for pattern, replacement in self.grammar_rules.items():
            if callable(replacement):
                text = re.sub(pattern, replacement, text)
            else:
                text = re.sub(pattern, replacement, text)
        
        # Step 2: Fix common errors
        for error, correction in self.common_errors.items():
            text = re.sub(error, correction, text, flags=re.IGNORECASE)
        
        # Step 3: Fix article agreement
        text = self.fix_article_agreement(text)
        
        # Step 4: Fix repeated words
        text = self.fix_repeated_words(text)
        
        # Step 5: Fix comma overuse
        text = self.fix_comma_overuse(text)
        
        # Step 6: Fix sentence fragments
        text = self.fix_sentence_fragments(text)
        
        # Step 7: Fix spacing issues
        text = self.fix_spacing_issues(text)
        
        # Step 8: Ensure consistent capitalization
        text = self.fix_capitalization_consistency(text)
        
        # Final cleanup
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

# Create global instance
grammar_corrector = IntelligentGrammarCorrector()

def correct_grammar(text):
    """Simple function to correct grammar"""
    return grammar_corrector.intelligent_grammar_correction(text)











def enhanced_grammar_correction(self, text):
    """More comprehensive grammar correction"""
    if not text or len(text.strip()) < 10:
        return text
    
    # Step 1: Fix basic grammar rules
    for pattern, replacement in self.grammar_rules.items():
        if callable(replacement):
            text = re.sub(pattern, replacement, text)
        else:
            text = re.sub(pattern, replacement, text)
    
    # Step 2: Fix common errors
    for error, correction in self.common_errors.items():
        text = re.sub(error, correction, text, flags=re.IGNORECASE)
    
    # Step 3: Fix sentence fragments
    text = self.fix_sentence_fragments(text)
    
    # Step 4: Fix comma overuse
    text = self.fix_comma_overuse(text)
    
    # Step 5: Fix missing spaces after punctuation
    text = re.sub(r'([.!?])([A-Za-z])', r'\1 \2', text)
    
    # Step 6: Ensure proper sentence endings
    if not text.endswith(('.', '!', '?')):
        text = text + '.'
    
    # Step 7: Final cleanup
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Update the correct_grammar function to use enhanced version
def correct_grammar(text):
    return grammar_corrector.enhanced_grammar_correction(text)
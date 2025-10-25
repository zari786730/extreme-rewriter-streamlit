import re

class IntelligentGrammarCorrector:
    def __init__(self):
        self.grammar_rules = self.setup_grammar_rules()
        self.common_errors = self.setup_common_errors()

    def setup_grammar_rules(self):
        return {
            r'^([a-z])': lambda m: m.group(1).upper(),
            r'([.!?]\s+)([a-z])': lambda m: m.group(1) + m.group(2).upper(),
            r',\s*,': ',', r'\.\s*\.': '.', r'\s+\.': '.', r'\s+,': ',',
            r',\s*\.': '.', r';\s*;': ';', r'\s{2,}': ' ',
            r'\s+([.,!?;])': r'\1', r'([.,!?;])([A-Za-z])': r'\1 \2',
        }

    def setup_common_errors(self):
        return {
            r'\bi\s': 'I ', r'\bit\'s\b': 'its', r'\bthey\'re\b': 'their',
            r'\byour\b': 'you\'re', r'\btheir\b': 'they\'re', r'\bits\b': 'it\'s',
            r'\bwhere\s+it\s+has\b': 'where it has',  # Fix broken phrases
        }

    def fix_broken_sentences(self, text):
        """Fix the specific broken sentences your rewriter creates"""
        # Fix random words at start of sentences
        text = re.sub(r'(Significantly, |Interestingly |Similarly |Accordingly |Consequently |Moreover |Therefore, |Notably |Remarkably, )+', '', text)
        
        # Fix "and" at start of sentences
        text = re.sub(r'\. And ', '. ', text)
        
        # Fix sentence fragments that start with lowercase
        text = re.sub(r'\. ([a-z])', lambda m: '. ' + m.group(1).upper(), text)
        
        # Fix random phrases in middle of sentences
        text = re.sub(r', (revealing how|Methods|Similarly|Accordingly|Consequently|Moreover)', ',', text)
        
        return text

    def fix_sentence_structure(self, text):
        """Fix overall sentence structure"""
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        corrected_sentences = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            words = sentence.split()
            if len(words) < 4:  # Too short, merge with next or previous
                continue
                
            # Capitalize first word
            if words and words[0][0].islower():
                words[0] = words[0].capitalize()
                
            corrected_sentences.append(' '.join(words))
        
        # Join with proper punctuation
        result = '. '.join(corrected_sentences)
        if result and not result.endswith('.'):
            result += '.'
            
        return result

    def remove_repetitive_patterns(self, text):
        """Remove repetitive sentence starters"""
        patterns = [
            r'Significantly, ',
            r'Interestingly, ',
            r'Similarly, ',
            r'Accordingly, ',
            r'Consequently, ',
            r'Moreover, ',
            r'Therefore, ',
            r'Notably, ',
            r'Remarkably, ',
            r'In conclusion, ',
            r'For example, ',
        ]
        
        for pattern in patterns:
            # Remove if it appears more than once in close proximity
            text = re.sub(f'({pattern})+', '', text)
            
        return text

    def enhanced_grammar_correction(self, text):
        """Comprehensive grammar correction for rewriter output"""
        if not text or len(text.strip()) < 10:
            return text

        # Step 1: Fix broken sentences from rewriter
        text = self.fix_broken_sentences(text)
        
        # Step 2: Remove repetitive patterns
        text = self.remove_repetitive_patterns(text)
        
        # Step 3: Fix basic grammar rules
        for pattern, replacement in self.grammar_rules.items():
            if callable(replacement):
                text = re.sub(pattern, replacement, text)
            else:
                text = re.sub(pattern, replacement, text)

        # Step 4: Fix common errors
        for error, correction in self.common_errors.items():
            text = re.sub(error, correction, text, flags=re.IGNORECASE)

        # Step 5: Fix overall sentence structure
        text = self.fix_sentence_structure(text)

        # Step 6: Final cleanup
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'\.\s*\.', '.', text)  # Remove double periods
        
        # Ensure proper ending
        if text and not text.endswith(('.', '!', '?')):
            text += '.'
            
        return text

# Create global instance
grammar_corrector = IntelligentGrammarCorrector()

def correct_grammar(text):
    """Simple function to correct grammar"""
    return grammar_corrector.enhanced_grammar_correction(text)
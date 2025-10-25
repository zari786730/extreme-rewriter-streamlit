import re

class SuperGrammarCorrector:
    def __init__(self):
        self.sentence_starters_to_remove = [
            'Interestingly,', 'Significantly,', 'Similarly,', 'Accordingly,', 
            'Consequently,', 'Moreover,', 'Therefore,', 'Notably,', 'Remarkably,',
            'In conclusion,', 'For example,', 'What explains', 'Why is it meaningful that',
            'revealing how', 'which highlights', 'thereby illustrating'
        ]

    def aggressive_sentence_repair(self, text):
        """Extremely aggressive sentence fixing"""
        if not text:
            return text

        # Step 1: Remove ALL problematic sentence starters
        for starter in self.sentence_starters_to_remove:
            text = text.replace(starter, '')
            text = text.replace(starter.lower(), '')
            text = text.replace(starter.upper(), '')

        # Step 2: Fix broken sentence patterns
        text = re.sub(r'\.\s*([A-Z][a-z]*)\s+to\s+', r', \1 to ', text)  # ". Biofuels to" -> ", biofuels to"
        text = re.sub(r'\.\s+And\s+', r', and ', text)  # ". And " -> ", and "
        text = re.sub(r'\.\s+Plays\s+', r', plays ', text)  # ". Plays " -> ", plays "
        text = re.sub(r'\.\s+Yields\s+', r', yielding ', text)  # ". Yields " -> ", yielding "
        
        # Step 3: Fix random capitalized words mid-sentence
        text = re.sub(r',\s+([A-Z][a-z]+)\s+', lambda m: ', ' + m.group(1).lower() + ' ', text)
        
        # Step 4: Remove duplicate "thereby" phrases
        text = re.sub(r', thereby illustrating.*?, thereby', ', thereby', text)
        
        return text

    def fix_pronouns_and_contractions(self, text):
        """Fix it's/its, they're/their etc."""
        fixes = {
            r'\bit\'s\b': 'its',
            r'\bthey\'re\b': 'their', 
            r'\bwhere\s+it\s+has\b': 'where it has',
            r'\bregardless of it\'s\b': 'despite its',
            r'\bdespite it\'s\b': 'despite its',
        }
        
        for error, correction in fixes.items():
            text = re.sub(error, correction, text, flags=re.IGNORECASE)
            
        return text

    def rebuild_sentences(self, text):
        """Completely rebuild broken sentences"""
        # Split by periods but keep the content
        parts = re.split(r'[.!?]+', text)
        valid_sentences = []
        
        for part in parts:
            part = part.strip()
            words = part.split()
            
            # Only keep reasonable sentences (4+ words, makes sense)
            if len(words) >= 4 and not any(word in ['what', 'why', 'how'] for word in words[:2]):
                # Capitalize first letter
                if words and words[0][0].islower():
                    words[0] = words[0].capitalize()
                valid_sentences.append(' '.join(words))
        
        # Rebuild text with proper punctuation
        if valid_sentences:
            text = '. '.join(valid_sentences) + '.'
        else:
            text = text[0].upper() + text[1:] if text else text
            
        return text

    def remove_garbage_phrases(self, text):
        """Remove nonsensical phrases"""
        garbage_phrases = [
            r'which highlights to clean up pollutants',
            r'revealing how where it has revolutionized',
            r'what explains and environmental',
            r'why is it meaningful that and the potential',
        ]
        
        for phrase in garbage_phrases:
            text = text.replace(phrase, '')
            
        return text

    def correct_grammar_aggressive(self, text):
        """Super aggressive grammar correction"""
        if not text or len(text.strip()) < 10:
            return text

        # Step 1: Remove garbage phrases
        text = self.remove_garbage_phrases(text)
        
        # Step 2: Aggressive sentence repair
        text = self.aggressive_sentence_repair(text)
        
        # Step 3: Fix pronouns
        text = self.fix_pronouns_and_contractions(text)
        
        # Step 4: Rebuild sentences completely
        text = self.rebuild_sentences(text)
        
        # Step 5: Final cleanup
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r',\s*,', ',', text)
        text = re.sub(r'\.\s*\.', '.', text)
        text = text.strip()
        
        # Ensure proper start and end
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
        if text and not text.endswith('.'):
            text += '.'
            
        return text

# Create global instance
grammar_corrector = SuperGrammarCorrector()

def correct_grammar(text):
    """Simple function to correct grammar"""
    return grammar_corrector.correct_grammar_aggressive(text)
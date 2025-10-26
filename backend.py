# =========================
# EXTREME REWRITER BACKEND (NO NLTK)
# =========================

import random
import re
import requests

# Import your existing files
try:
    from health_terms import health_terms
    from health_terms_2 import health_terms as health_terms_2
    from generalwords import general_words
    from grammar_corrector import correct_grammar
    # Merge health terms
    health_terms.update(health_terms_2)
except ImportError:
    # Fallback empty dictionaries if files not found
    health_terms = {}
    general_words = {}
    
    # Fallback grammar corrector
    def correct_grammar(text):
        return text

# =========================
# PURE INTERNET SYNONYM FINDER
# =========================
class PureInternetSynonymFinder:
    def __init__(self):
        self.cache = {}

    def get_synonyms(self, word):
        word = word.lower().strip()
        if word in self.cache:
            return self.cache[word]

        try:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=3)
            if response.status_code == 200:
                data = response.json()
                synonyms = []
                for meaning in data[0].get('meanings', []):
                    for definition in meaning.get('definitions', []):
                        synonyms.extend(definition.get('synonyms', []))

                clean_synonyms = [
                    s for s in synonyms
                    if s.isalpha() and s.lower() != word and len(s.split()) <= 2
                ]
                unique_synonyms = list(set(clean_synonyms))[:6]
                if unique_synonyms:
                    self.cache[word] = unique_synonyms
                    return unique_synonyms
        except:
            pass
        return []

# =========================
# PURE REWRITER
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = PureInternetSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()

    def setup_vocabulary(self):
        # Load health terms
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement

        # Load general words
        for word, replacement in general_words.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement

    def intelligent_word_replacement(self, text):
        words = text.split()
        new_words = []

        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            if len(clean_word) <= 2 or clean_word in ['the','a','an','and','or','but','in','on','at']:
                new_words.append(word)
                continue

            if random.random() < 0.8:
                # Library replacement
                if clean_word in self.replacements:
                    replacement = random.choice(self.replacements[clean_word])
                    replacement = replacement.capitalize() if word[0].isupper() else replacement
                    new_words.append(replacement)
                    continue

                # Internet synonyms
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                if synonyms:
                    self.replacements[clean_word] = synonyms
                    replacement = random.choice(synonyms)
                    replacement = replacement.capitalize() if word[0].isupper() else replacement
                    new_words.append(replacement)
                    continue

            new_words.append(word)
        return ' '.join(new_words)

    def varied_sentence_restructure(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
        if random.random() < 0.6:
            random.shuffle(sentences)
        connectors = ['. ', '. Additionally, ', '. Moreover, ', '. Furthermore, ']
        result = sentences[0] + '. '
        for i in range(1, len(sentences)):
            if random.random() < 0.4:
                result += random.choice(connectors) + sentences[i].lower()
            else:
                result += sentences[i] + '. '
        return result.strip()

    def smart_length_manipulation(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text
        processed = []
        for sentence in sentences:
            words = sentence.split()
            if random.random() < 0.4:
                if len(words) > 15:
                    mid = len(words) // 2
                    processed.extend([' '.join(words[:mid]) + '.', ' '.join(words[mid:]).capitalize()])
                elif len(words) < 5:
                    processed.append(f"This involves {sentence.lower()}")
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        return ' '.join(processed)

    def add_natural_variation(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        if random.random() < 0.3:
            first_sentence = sentences[0]
            if not first_sentence.lower().startswith(('interestingly','notably','importantly')):
                sentences[0] = random.choice(['Interestingly, ','Notably, ','Importantly, ']) + first_sentence.lower()
        return '. '.join(sentences) + '.'

# Initialize pure rewriter
pure_rewriter = PureRewriter()

# =========================
# EXTREME REWRITER FUNCTION
# =========================
def extreme_rewriter(original_text):
    clean_text = original_text.strip().strip('"').strip("'")
    transformations = [
        pure_rewriter.varied_sentence_restructure,
        pure_rewriter.intelligent_word_replacement,
        pure_rewriter.smart_length_manipulation,
        pure_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)
    result = clean_text
    for t in transformations:
        result = t(result)
    result = correct_grammar(result)
    return result

# =========================
# SIMILARITY CALCULATION
# =========================
def calculate_similarity(original, rewritten):
    def simple_tokenize(text):
        return re.findall(r'\b\w+\b', text.lower())
    
    original_words = set(simple_tokenize(original))
    rewritten_words = set(simple_tokenize(rewritten))
    common_words = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common_words) / len(original_words) * 100

# =========================
# GUARANTEE LOW SIMILARITY
# =========================
def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    best_result = None
    best_similarity = 100
    for _ in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        if similarity <= max_similarity:
            return rewritten, similarity
    return best_result, best_similarity
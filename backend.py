# =========================
# EXTREME REWRITER BACKEND
# =========================

import random
import re
import requests
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# --- IMPORT YOUR LIBRARIES ---
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# --- PURE INTERNET SYNONYM FINDER ---
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
                    syn for syn in synonyms
                    if syn.lower() != word and len(syn.split()) <= 2 and syn.isalpha()
                ]
                unique_synonyms = list(set(clean_synonyms))[:6]
                if unique_synonyms:
                    self.cache[word] = unique_synonyms
                    return unique_synonyms
        except:
            return []
        return []

# --- PURE REWRITER ---
class PureRewriter:
    def __init__(self):
        self.synonym_finder = PureInternetSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()
    
    def setup_vocabulary(self):
        """Load your existing libraries"""
        for d in [health_terms, general_words]:
            for word, replacement in d.items():
                self.replacements[word.lower()] = [replacement] if isinstance(replacement, str) else replacement

    def pos_to_wordnet(self, tag):
        """Convert POS tag to WordNet format for synonym selection"""
        if tag.startswith('J'): return wordnet.ADJ
        if tag.startswith('V'): return wordnet.VERB
        if tag.startswith('N'): return wordnet.NOUN
        if tag.startswith('R'): return wordnet.ADV
        return None

    def intelligent_word_replacement(self, text):
        """Replace words intelligently with synonyms or library words"""
        tokens = word_tokenize(text)
        tags = pos_tag(tokens)
        new_tokens = []

        for token, tag in tags:
            clean_token = token.lower()
            wn_tag = self.pos_to_wordnet(tag)

            # Skip short/common words
            if len(clean_token) <= 2 or clean_token in ['the','a','an','and','or','but','in','on','at']:
                new_tokens.append(token)
                continue

            replaced = False
            if random.random() < 0.85:  # 85% chance replacement
                # Library-based
                if clean_token in self.replacements:
                    rep = random.choice(self.replacements[clean_token])
                    if token[0].isupper(): rep = rep.capitalize()
                    new_tokens.append(rep)
                    replaced = True
                else:
                    # Internet synonym
                    synonyms = self.synonym_finder.get_synonyms(clean_token)
                    if synonyms:
                        rep = random.choice(synonyms)
                        if token[0].isupper(): rep = rep.capitalize()
                        new_tokens.append(rep)
                        self.replacements[clean_token] = synonyms
                        replaced = True

            if not replaced:
                new_tokens.append(token)

        return ' '.join(new_tokens)

    def sentence_restructure(self, text):
        """Restructure sentences intelligently without losing meaning"""
        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text)]
        if len(sentences) <= 1:
            return text

        # Reorder some sentences
        if random.random() < 0.5:
            random.shuffle(sentences)

        # Merge or split sentences
        merged = []
        for s in sentences:
            words = s.split()
            if len(words) > 18 and random.random() < 0.5:
                mid = len(words)//2
                merged.extend([' '.join(words[:mid])+'.', ' '.join(words[mid:]).capitalize()])
            elif len(words) < 6 and random.random() < 0.4:
                merged.append("This relates to " + s.lower())
            else:
                merged.append(s)
        return ' '.join(merged)

    def add_natural_variation(self, text):
        """Add variation like 'Importantly', 'Interestingly' for natural flow"""
        sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text)]
        if not sentences: return text

        if random.random() < 0.3:
            variations = ['Interestingly, ', 'Notably, ', 'Importantly, ']
            if not sentences[0].lower().startswith(tuple(v.lower() for v in variations)):
                sentences[0] = random.choice(variations) + sentences[0].lower()

        return ' '.join(sentences)

# Initialize rewriter
pure_rewriter = PureRewriter()

# --- EXTREME REWRITER ---
def extreme_rewriter(text):
    text = text.strip()
    transformations = [
        pure_rewriter.intelligent_word_replacement,
        pure_rewriter.sentence_restructure,
        pure_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)
    for t in transformations:
        text = t(text)
    return correct_grammar(text)

# --- SIMILARITY CALCULATION ---
def calculate_similarity(original, rewritten):
    orig_words = set(re.findall(r'\b\w+\b', original.lower()))
    rew_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common = orig_words & rew_words
    return (len(common) / len(orig_words) * 100) if orig_words else 0

# --- GUARANTEE LOW SIMILARITY ---
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
            break
    return best_result, best_similarity
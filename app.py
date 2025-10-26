import random
import re
import streamlit as st
import requests

# Import your existing files
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

st.write("✓ Health terms loaded:", len(health_terms))
st.write("✓ General words loaded:", len(general_words))
st.write("✓ Grammar corrector loaded")

# =========================
# PURE INTERNET SYNONYM FINDER
# =========================
class PureInternetSynonymFinder:
    def __init__(self):
        self.cache = {}
    
    def get_synonyms(self, word):
        """Get synonyms ONLY from internet API"""
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
                
                # Filter and clean synonyms
                clean_synonyms = []
                for synonym in synonyms:
                    if (synonym.lower() != word and 
                        len(synonym.split()) <= 2 and  # Avoid long phrases
                        synonym.isalpha()):  # Only alphabetic words
                        clean_synonyms.append(synonym)
                
                unique_synonyms = list(set(clean_synonyms))[:6]  # Limit to 6
                
                if unique_synonyms:
                    self.cache[word] = unique_synonyms
                    return unique_synonyms
                    
        except Exception as e:
            pass
        
        return []

# =========================
# PURE REWRITER - ONLY YOUR LIBRARIES + INTERNET
# =========================
class PureRewriter:
    def __init__(self):
        self.synonym_finder = PureInternetSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()
        st.write("🔄 Pure rewriter activated - Only your libraries + internet")
    
    def setup_vocabulary(self):
        """Setup vocabulary from your existing files ONLY"""
        # Add health terms from your files
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        # Add general words from your files
        for word, replacement in general_words.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        st.write(f"📚 Loaded {len(self.replacements)} words from your libraries")

    def intelligent_word_replacement(self, text):
        """Word replacement using ONLY your libraries + internet"""
        if not text:
            return text
            
        words = text.split()
        new_words = []
        
        for word in words:
            original_word = word
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip very short/common words
            if len(clean_word) <= 2 or clean_word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at']:
                new_words.append(original_word)
                continue
            
            # 80% chance of replacement
            if random.random() < 0.8:
                # First check your existing libraries
                if clean_word in self.replacements:
                    replacement = random.choice(self.replacements[clean_word])
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    continue
                
                # If not in libraries, try internet
                synonyms = self.synonym_finder.get_synonyms(clean_word)
                if synonyms:
                    # Add to replacements for future use
                    self.replacements[clean_word] = synonyms
                    replacement = random.choice(synonyms)
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    continue
            
            # Keep original if no replacement found
            new_words.append(original_word)
        
        return ' '.join(new_words)

    def varied_sentence_restructure(self, text):
        """Sentence restructuring without hardcoded patterns"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if len(sentences) <= 1:
            return text
        
        # Simple sentence shuffling
        if random.random() < 0.6:
            random.shuffle(sentences)
        
        # Simple connector addition
        connectors = ['. ', '. Additionally, ', '. Moreover, ', '. Furthermore, ']
        result = sentences[0] + '. '
        
        for i in range(1, len(sentences)):
            if random.random() < 0.4:
                result += random.choice(connectors) + sentences[i].lower()
            else:
                result += sentences[i] + '. '
        
        return result.strip()

    def smart_length_manipulation(self, text):
        """Basic length management"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text

        processed = []
        for sentence in sentences:
            words = sentence.split()
            if random.random() < 0.4:
                if len(words) > 15:
                    # Simple split at middle
                    mid = len(words) // 2
                    part1 = ' '.join(words[:mid])
                    part2 = ' '.join(words[mid:])
                    processed.extend([part1 + '.', part2.capitalize()])
                elif len(words) < 5:
                    # Simple expansion
                    expanded = f"This involves {sentence.lower()}"
                    processed.append(expanded)
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)

        return ' '.join(processed)

    def add_natural_variation(self, text):
        """Simple natural variation"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text

        if random.random() < 0.3:
            # Simple variation without hardcoded patterns
            first_sentence = sentences[0]
            if not first_sentence.lower().startswith(('interestingly', 'notably', 'importantly')):
                variations = ['Interestingly, ', 'Notably, ', 'Importantly, ']
                sentences[0] = random.choice(variations) + first_sentence.lower()

        return '. '.join(sentences) + '.'

# Initialize pure rewriter
pure_rewriter = PureRewriter()

def extreme_rewriter(original_text):
    """Pure rewriting using ONLY your libraries + internet"""
    clean_text = original_text.strip().strip('"').strip("'")

    # Apply transformations in random order
    transformations = [
        pure_rewriter.varied_sentence_restructure,
        pure_rewriter.intelligent_word_replacement, 
        pure_rewriter.smart_length_manipulation,
        pure_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)

    result = clean_text
    for transform in transformations:
        result = transform(result)

    # Final grammar correction from your file
    result = correct_grammar(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Calculate text similarity"""
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)

    if not original_words:
        return 0

    similarity = len(common_words) / len(original_words) * 100
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    """Keep generating until similarity is below threshold"""
    best_result = None
    best_similarity = 100

    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)

        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity

        if similarity <= max_similarity:
            return rewritten, similarity

    return best_result, best_similarity

# =========================
# YOUR EXISTING STREAMLIT UI
# =========================
st.title("🔁 Pure Text Rewriter")
st.write("Using ONLY your libraries + internet synonyms")

text_input = st.text_area("Enter text to rewrite:", height=200)

if st.button("Rewrite Text"):
    if text_input:
        with st.spinner("Rewriting with pure approach..."):
            rewritten, similarity = guarantee_low_similarity(text_input)
            
            st.subheader("Original Text:")
            st.write(text_input)
            
            st.subheader("Rewritten Text:")
            st.write(rewritten)
            
            st.subheader("Similarity Score:")
            st.write(f"{similarity:.1f}%")
            
            if similarity > 20:
                st.warning("Similarity is higher than target. Try running again.")
    else:
        st.error("Please enter some text")
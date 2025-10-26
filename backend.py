# =========================
# ENHANCED REWRITER BACKEND WITH LOCAL FILES INTEGRATION
# =========================

import streamlit as st
import random
import re
import math

import os
import importlib

vocab_modules = []
vocab_folder = "vocabulary"  # GitHub folder with all 45 files

for file in os.listdir(vocab_folder):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]
        module = importlib.import_module(f"vocabulary.{module_name}")
        vocab_modules.append(module)

# Example: print first 5 words from each file
for module in vocab_modules:
    print(module.synonyms_list[:5])

# -------------------------
# IMPORT YOUR LOCAL FILES
# -------------------------
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# -------------------------
# ENHANCED REWRITER CLASS
# -------------------------
class EnhancedRewriter:
    def __init__(self):
        self.replacements = {}
        self.total_words_accessed = 0
        self.setup_vocabulary()
        
    def setup_vocabulary(self):
        """Integrate local dictionary files and count total words"""
        # Load health terms
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
            self.total_words_accessed += 1
        
        # Load general words
        for word, replacement in general_words.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
                self.total_words_accessed += 1
        
        st.sidebar.info(f"📚 Total words in dictionary: {self.total_words_accessed}")

    def intelligent_word_replacement(self, text):
        """Replace words using local dictionaries"""
        words = text.split()
        new_words = []
        replacements_made = 0

        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip very short common words
            if len(clean_word) <= 2 or clean_word in ['the','a','an','and','or','but','in','on','at','to','for','of','with','by','as','is','was','were','be','been','have','has','had','do','does','did']:
                new_words.append(word)
                continue

            # Apply replacement from local dictionaries
            if clean_word in self.replacements and random.random() < 0.7:
                replacement = random.choice(self.replacements[clean_word])
                replacement = replacement.capitalize() if word[0].isupper() else replacement
                new_words.append(replacement)
                replacements_made += 1
            else:
                new_words.append(word)
        
        st.sidebar.info(f"🔄 Words replaced: {replacements_made}")
        return ' '.join(new_words)

    def sentence_length_manipulation(self, text):
        """Change number of sentences - increase or decrease"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        original_sentence_count = len(sentences)
        
        if original_sentence_count <= 1:
            return text
            
        # Decide whether to increase or decrease sentence count
        change_direction = random.choice(['increase', 'decrease'])
        
        if change_direction == 'increase' and original_sentence_count < 10:
            # Split long sentences to increase count
            modified_sentences = []
            for sentence in sentences:
                words = sentence.split()
                if len(words) > 15 and random.random() < 0.6:
                    # Split into two sentences
                    mid = len(words) // 2
                    first_part = ' '.join(words[:mid])
                    second_part = ' '.join(words[mid:])
                    modified_sentences.append(first_part + '.')
                    modified_sentences.append(second_part.capitalize())
                else:
                    modified_sentences.append(sentence)
            sentences = modified_sentences
        elif change_direction == 'decrease' and original_sentence_count > 2:
            # Combine short sentences to decrease count
            modified_sentences = []
            i = 0
            while i < len(sentences):
                if i < len(sentences) - 1 and len(sentences[i].split()) < 8 and len(sentences[i+1].split()) < 8:
                    # Combine two short sentences
                    combined = sentences[i] + ' and ' + sentences[i+1].lower()
                    modified_sentences.append(combined)
                    i += 2
                else:
                    modified_sentences.append(sentences[i])
                    i += 1
            sentences = modified_sentences
        
        final_sentence_count = len(sentences)
        st.sidebar.info(f"📊 Sentences: {original_sentence_count} → {final_sentence_count}")
        
        return '. '.join(sentences) + '.'

    def word_count_manipulation(self, text):
        """Change word count in each sentence - increase or decrease"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        modified_sentences = []
        total_original_words = 0
        total_modified_words = 0
        
        for sentence in sentences:
            words = sentence.split()
            original_word_count = len(words)
            total_original_words += original_word_count
            
            if original_word_count <= 5:
                # Expand very short sentences
                expanders = [
                    "This process involves",
                    "It is important to note that",
                    "Clinically, this means",
                    "From a medical perspective,"
                ]
                expanded = random.choice(expanders) + " " + sentence.lower()
                modified_sentences.append(expanded)
                total_modified_words += len(expanded.split())
                
            elif original_word_count > 20 and random.random() < 0.6:
                # Reduce very long sentences
                reduction_strategy = random.choice(['remove_adjectives', 'simplify_phrases'])
                if reduction_strategy == 'remove_adjectives':
                    # Remove some adjectives
                    simplified_words = []
                    for word in words:
                        if not (word.endswith('ing') or word.endswith('ed') or word.endswith('ful')) or random.random() < 0.7:
                            simplified_words.append(word)
                    if len(simplified_words) >= original_word_count * 0.6:  # Keep at least 60% of words
                        modified_sentences.append(' '.join(simplified_words))
                        total_modified_words += len(simplified_words)
                    else:
                        modified_sentences.append(sentence)
                        total_modified_words += original_word_count
                else:
                    # Simplify by taking core parts
                    if original_word_count > 8:
                        # Keep beginning and end, remove middle
                        keep_start = words[:3]
                        keep_end = words[-3:]
                        simplified = keep_start + ['...'] + keep_end
                        modified_sentences.append(' '.join(simplified))
                        total_modified_words += len(simplified)
                    else:
                        modified_sentences.append(sentence)
                        total_modified_words += original_word_count
            else:
                # Moderate expansion for medium sentences
                if random.random() < 0.4 and original_word_count < 15:
                    expanders = [
                        "Specifically,",
                        "In particular,",
                        "Notably,",
                        "Importantly,"
                    ]
                    expanded = random.choice(expanders) + " " + sentence.lower()
                    modified_sentences.append(expanded)
                    total_modified_words += len(expanded.split())
                else:
                    modified_sentences.append(sentence)
                    total_modified_words += original_word_count
        
        st.sidebar.info(f"📝 Words: {total_original_words} → {total_modified_words}")
        
        return '. '.join(modified_sentences) + '.'

    def varied_sentence_restructure(self, text):
        """Restructure sentences with varied patterns"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
            
        # Different restructuring strategies
        strategy = random.choice(['shuffle', 'reverse', 'interleave'])
        
        if strategy == 'shuffle':
            random.shuffle(sentences)
        elif strategy == 'reverse':
            sentences.reverse()
        elif strategy == 'interleave':
            if len(sentences) >= 4:
                mid = len(sentences) // 2
                first_half = sentences[:mid]
                second_half = sentences[mid:]
                sentences = []
                for i in range(max(len(first_half), len(second_half))):
                    if i < len(first_half):
                        sentences.append(first_half[i])
                    if i < len(second_half):
                        sentences.append(second_half[i])
        
        # Add varied connectors
        connectors = [
            '. ', '. Additionally, ', '. Moreover, ', '. Furthermore, ',
            '. Consequently, ', '. Therefore, ', '. Specifically, '
        ]
        
        result = sentences[0] + '.'
        for i in range(1, len(sentences)):
            if random.random() < 0.5:
                result += random.choice(connectors) + sentences[i].lower()
            else:
                result += '. ' + sentences[i]
        
        return result

    def add_natural_variation(self, text):
        """Add natural language variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
            
        # Add introductory phrases to some sentences
        introductory_phrases = [
            'From a clinical standpoint,',
            'In medical terms,',
            'Biologically speaking,',
            'Pathologically,',
            'Therapeutically,',
            'Diagnostically,',
            'Prognostically,'
        ]
        
        modified_sentences = []
        for i, sentence in enumerate(sentences):
            if i == 0 and random.random() < 0.3:
                modified_sentences.append(random.choice(introductory_phrases) + ' ' + sentence.lower())
            elif random.random() < 0.2:
                modified_sentences.append(random.choice(introductory_phrases) + ' ' + sentence.lower())
            else:
                modified_sentences.append(sentence)
        
        return '. '.join(modified_sentences) + '.'

# Initialize enhanced rewriter
enhanced_rewriter = EnhancedRewriter()

# -------------------------
# ENHANCED REWRITER FUNCTION
# -------------------------
def enhanced_rewrite(original_text):
    """Main rewriting function with all enhancements"""
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations in varied order
    transformations = [
        enhanced_rewriter.sentence_length_manipulation,
        enhanced_rewriter.word_count_manipulation,
        enhanced_rewriter.intelligent_word_replacement,
        enhanced_rewriter.varied_sentence_restructure,
        enhanced_rewriter.add_natural_variation
    ]
    
    # Shuffle transformation order for variety
    random.shuffle(transformations)
    
    result = clean_text
    for transformation in transformations:
        result = transformation(result)
    
    # Final grammar correction
    result = correct_grammar(result)
    
    return result

# -------------------------
# SIMILARITY CALCULATION
# -------------------------
def calculate_similarity(original, rewritten):
    original_words = set(re.findall(r'\w+', original.lower()))
    rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common_words) / len(original_words) * 100

# -------------------------
# GUARANTEE LOW SIMILARITY
# -------------------------
def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=8):
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = enhanced_rewrite(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            
        if similarity <= max_similarity:
            st.sidebar.success(f"✅ Attempt {attempt + 1}: Similarity = {similarity:.1f}%")
            return rewritten, similarity
        else:
            st.sidebar.warning(f"🔄 Attempt {attempt + 1}: Similarity = {similarity:.1f}%")
    
    st.sidebar.error(f"⚠️ Best achieved: {best_similarity:.1f}% similarity")
    return best_result, best_similarity

# =========================
# STREAMLIT FRONTEND INTEGRATION
# =========================

# Add this to your existing Streamlit app
def main():
    st.title("🧬 Enhanced Medical Text Rewriter")
    
    # Input area
    input_text = st.text_area("Enter medical text to rewrite:", height=150, 
                             value="Cancer is a complex and devastating group of diseases characterized by uncontrolled growth of abnormal cells...")
    
    # Settings
    col1, col2 = st.columns(2)
    with col1:
        target_similarity = st.slider("Target Similarity %", 5, 40, 15)
    with col2:
        max_attempts = st.slider("Max Attempts", 1, 15, 8)
    
    # Rewrite button
    if st.button("🚀 Enhanced Rewrite"):
        if not input_text.strip():
            st.warning("⚠️ Please enter some text first!")
        else:
            with st.spinner("Rewriting with enhanced algorithms..."):
                rewritten, similarity = guarantee_low_similarity(input_text, target_similarity, max_attempts)
            
            # Display results
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Original Text")
                st.info(input_text)
            with col2:
                st.markdown("### Rewritten Text")
                st.success(rewritten)
            
            # Similarity indicator
            if similarity <= 15:
                st.balloons()
                st.success(f"🎉 Excellent! Similarity: {similarity:.1f}%")
            elif similarity <= 25:
                st.warning(f"⚠️ Good! Similarity: {similarity:.1f}%")
            else:
                st.error(f"❌ High similarity: {similarity:.1f}% - Try again!")

if __name__ == "__main__":
    main()
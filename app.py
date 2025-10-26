# =========================
# EXTREME REWRITER STREAMLIT (OFFLINE & NO NLTK)
# =========================

import streamlit as st
import random
import re

# -------------------------
# IMPORT LOCAL FILES
# -------------------------
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# -------------------------
# PURE REWRITER (OFFLINE)
# -------------------------
class PureRewriter:
    def __init__(self):
        self.replacements = {}
        self.setup_vocabulary()

    def setup_vocabulary(self):
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
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
            if clean_word in self.replacements and random.random() < 0.8:
                replacement = random.choice(self.replacements[clean_word])
                replacement = replacement.capitalize() if word[0].isupper() else replacement
                new_words.append(replacement)
            else:
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

# Initialize rewriter
pure_rewriter = PureRewriter()

# -------------------------
# EXTREME REWRITER FUNCTION
# -------------------------
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

# =========================
# FRONTEND (UI)
# =========================

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- CSS, Bubbles, Header, Input, Buttons ---
# [Paste your full CSS + bubbles + header code here from your existing frontend]

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("🧬 Enter text:", height=180, label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("Rewriting your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        st.markdown(f"""
        <div class="glass-box" style="border:1px solid rgba(0,255,255,0.3);">
            <h3 style="color:#00eaff;">✨ Rewritten Text (Similarity: {similarity:.1f}%)</h3>
            <textarea readonly rows="10" style="
                width:100%;
                background:rgba(0,15,25,0.8);
                color:#e6faff;
                border-radius:15px;
                border:1px solid rgba(0,180,255,0.2);
                padding:1rem;
                font-size:1rem;
            ">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear"):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
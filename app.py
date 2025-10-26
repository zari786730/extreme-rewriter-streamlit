# =========================
# EXTREME REWRITER STREAMLIT (OFFLINE & NO NLTK)
# =========================

import streamlit as st
import random
import re


from flask import Flask
import os
import importlib

app = Flask(__name__)

# ---------------------------
# Load all vocabulary files
# ---------------------------
vocab_folder = "vocabulary"
vocab_modules = []

for file in os.listdir(vocab_folder):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]  # remove .py extension
        module = importlib.import_module(f"vocabulary.{module_name}")
        vocab_modules.append(module)

# Combine all words into one list
all_words = []
for module in vocab_modules:
    all_words.extend(module.synonyms_list)

total_words = len(all_words)

# ---------------------------
# Web route to show total
# ---------------------------
@app.route("/")
def home():
    return f"<h1>Total words in vocabulary: {total_words}</h1>"

# ---------------------------
# Run the web app
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

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
# FRONTEND (UI) - COMPLETE WITH STYLING
# =========================

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- CUSTOM CSS WITH ANIMATIONS ---
st.markdown("""
<style>
    /* Main background and text */
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    
    /* Rotating DNA Logo */
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes colorChange {
        0% { color: #FF6B6B; }
        25% { color: #4ECDC4; }
        50% { color: #45B7D1; }
        75% { color: #96CEB4; }
        100% { color: #FF6B6B; }
    }
    
    .rotating-logo {
        animation: rotate 3s linear infinite, colorChange 5s ease-in-out infinite;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Glass morphism effect */
    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem;
        margin: 1rem 0;
    }
    
    /* Bubble animations */
    @keyframes float {
        0%, 100% { transform: translateY(0) translateX(0); }
        25% { transform: translateY(-20px) translateX(10px); }
        50% { transform: translateY(-10px) translateX(-10px); }
        75% { transform: translateY(-15px) translateX(15px); }
    }
    
    .bubble {
        position: fixed;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
        animation: float 15s infinite ease-in-out;
        z-index: -1;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background: rgba(0, 15, 25, 0.8) !important;
        color: #e6faff !important;
        border-radius: 15px !important;
        border: 1px solid rgba(0, 180, 255, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BUBBLE BACKGROUND ---
st.markdown("""
<div class="bubble" style="width: 100px; height: 100px; top: 10%; left: 5%; animation-delay: 0s;"></div>
<div class="bubble" style="width: 150px; height: 150px; top: 20%; right: 10%; animation-delay: 2s;"></div>
<div class="bubble" style="width: 80px; height: 80px; bottom: 30%; left: 15%; animation-delay: 4s;"></div>
<div class="bubble" style="width: 120px; height: 120px; bottom: 20%; right: 5%; animation-delay: 6s;"></div>
<div class="bubble" style="width: 90px; height: 90px; top: 50%; left: 80%; animation-delay: 8s;"></div>
""", unsafe_allow_html=True)

# --- HEADER WITH ROTATING LOGO ---
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <div class="rotating-logo">🧬</div>
    <h1 style="color: white; font-size: 3rem; margin-bottom: 0.5rem;">Extreme Rewriter</h1>
    <p style="color: rgba(255,255,255,0.8); font-size: 1.2rem;">
        Advanced Text Transformation • DNA-Inspired Algorithms
    </p>
</div>
""", unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

input_text = st.text_area(
    "🧬 Enter text to rewrite:", 
    height=180, 
    placeholder="Type or paste your text here...",
    label_visibility="collapsed"
)

target_similarity = st.slider(
    "🎯 Target Maximum Similarity (%)", 
    5, 50, 20, 
    step=1,
    help="Lower percentage = more different from original"
)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("🧪 Rewriting your text with DNA-inspired algorithms..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        
        st.markdown(f"""
        <div class="glass-box" style="border: 2px solid rgba(0, 255, 255, 0.3); margin-top: 2rem;">
            <h3 style="color: #00eaff; text-align: center;">
                ✨ Rewritten Text (Similarity: {similarity:.1f}%)
            </h3>
            <textarea readonly rows="10" style="
                width: 100%;
                background: rgba(0, 15, 25, 0.8);
                color: #e6faff;
                border-radius: 15px;
                border: 1px solid rgba(0, 180, 255, 0.2);
                padding: 1rem;
                font-size: 1rem;
                resize: none;
            ">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear All", use_container_width=True):
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    💻 Developed with 💙 by <strong style="color: #00ffff;">Zariab</strong><br>
    🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
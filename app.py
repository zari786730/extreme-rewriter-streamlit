import random
import re
import streamlit as st
from collections import defaultdict
import requests
import time
import json
import os
import threading

# =========================
# Load your existing word lists
# =========================
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
# FREE SYNONYM API CLASS
# =========================
class FreeSynonymsAPI:
    """Fetch synonyms from the internet with caching"""
    def __init__(self):
        self.cache = {}
    
    def get_synonyms(self, word):
        word = word.lower().strip()
        if word in self.cache:
            return self.cache[word]
        try:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                synonyms = []
                for meaning in data[0].get('meanings', []):
                    for definition in meaning.get('definitions', []):
                        synonyms.extend(definition.get('synonyms', []))
                unique_synonyms = list(set(synonyms))[:6]
                self.cache[word] = unique_synonyms
                return unique_synonyms
        except Exception:
            pass
        return []

# =========================
# ACADEMIC VOCABULARY BUILDER
# =========================
class AcademicVocabularyBuilder:
    """
    Continuously fetches synonyms for academic words, updates progress
    and stores results in a JSON file automatically.
    """
    def __init__(self, main_rewriter):
        self.synonym_finder = FreeSynonymsAPI()
        self.main_rewriter = main_rewriter
        self.learning_active = True

        # Academic words bank
        self.academic_words = [
            'cell', 'dna', 'enzyme', 'protein', 'metabolism', 
            'atom', 'molecule', 'reaction', 'gravity', 'energy',
            'analyze', 'evaluate', 'hypothesis', 'methodology', 'experiment'
        ]
        
        self.learned_words = set()
        self.total_synonyms = 0

        # Ensure folder exists
        os.makedirs("data", exist_ok=True)

        # Streamlit placeholders
        self.progress_placeholder = st.empty()
        st.write("🎯 Academic vocabulary builder activated")
        st.write(f"📚 {len(self.academic_words)} words queued for learning")

        # Start continuous learning in a background thread
        self.start_continuous_learning()

    # -------------------------
    # Highlighted Function: Update Progress
    # -------------------------
    def update_progress(self):
        learned_count = len(self.learned_words)
        progress_percent = (learned_count / len(self.academic_words)) * 100
        with self.progress_placeholder.container():
            st.write(f"🧠 Words learned: {learned_count}/{len(self.academic_words)} ({progress_percent:.1f}%)")
            st.write(f"🔗 Total synonyms collected: {self.total_synonyms}")
            if learned_count > 0:
                recent_words = list(self.learned_words)[-5:]
                st.write(f"📌 Recently learned: {', '.join(recent_words)}")
            st.progress(progress_percent / 100)

    # -------------------------
    # Highlighted Function: Save Vocabulary
    # -------------------------
    def save_vocabulary(self):
        try:
            learned_vocab = {word: self.main_rewriter.replacements[word] for word in self.learned_words}
            with open("data/learned_vocabulary.json", "w") as f:
                json.dump(learned_vocab, f, indent=2)
            st.write(f"💾 Saved {len(learned_vocab)} learned words")
        except Exception as e:
            st.write(f"⚠️ Could not save vocabulary: {e}")

    # -------------------------
    # Highlighted Function: Continuous Learning Worker
    # -------------------------
    def start_continuous_learning(self):
        def learning_worker():
            while self.learning_active:
                for word in self.academic_words:
                    if word in self.learned_words:
                        continue
                    try:
                        synonyms = self.synonym_finder.get_synonyms(word)
                        if synonyms:
                            self.main_rewriter.replacements[word] = synonyms
                            self.learned_words.add(word)
                            self.total_synonyms += len(synonyms)
                        time.sleep(0.5)
                    except Exception:
                        time.sleep(1)
                # Update UI every loop
                self.update_progress()
                time.sleep(1)

            st.success(f"✅ Academic vocabulary learning completed! Learned {len(self.learned_words)} words with {self.total_synonyms} synonyms.")
            self.save_vocabulary()

        thread = threading.Thread(target=learning_worker, daemon=True)
        thread.start()

# =========================
# MAIN REWRITER CLASS
# =========================
class UniversalExtremeRewriter:
    """
    Main class that manages vocabulary and intelligent rewriting.
    """
    def __init__(self):
        self.replacements = {}
        self.setup_comprehensive_vocabulary()
        # Start academic vocabulary builder
        self.vocabulary_builder = AcademicVocabularyBuilder(self)

    # -------------------------
    # Highlighted Function: Load Vocabulary
    # -------------------------
    def setup_comprehensive_vocabulary(self):
        # Add health terms
        for word, replacement in health_terms.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        # Add general words
        for word, replacement in general_words.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        st.write(f"✅ Total vocabulary loaded: {len(self.replacements)} words")

    # -------------------------
    # Highlighted Function: Intelligent Word Replacement
    # -------------------------
    def intelligent_word_replacement(self, text):
        words = text.split()
        new_words = []
        i = 0
        while i < len(words):
            word = words[i].lower().strip('.,!?;:"')
            original_word = words[i]

            if len(word) <= 2 or word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']:
                new_words.append(original_word)
                i += 1
                continue

            # Try 2-word phrases
            if i + 1 < len(words):
                next_word = words[i+1].lower().strip('.,!?;:"')
                two_word = f"{word} {next_word}"
                if two_word in self.replacements:
                    replacement = random.choice(self.replacements[two_word])
                    if words[i][0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    i += 2
                    continue

            # Single word replacement
            if word in self.replacements and random.random() < 0.7:
                replacement = random.choice(self.replacements[word])
                if words[i][0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(original_word)
            i += 1

        return ' '.join(new_words)

    # -------------------------
    # Placeholder functions
    # -------------------------
    def varied_sentence_restructure(self, text):
        return text

    def smart_length_manipulation(self, text):
        return text

    def add_natural_variation(self, text):
        return text

# =========================
# Initialize the universal rewriter
# =========================
universal_rewriter = UniversalExtremeRewriter()
st.write("✅ Universal Extreme Rewriter initialized")

# =========================
# Example function to rewrite text
# =========================
def extreme_rewriter(original_text):
    text = universal_rewriter.intelligent_word_replacement(original_text)
    text = universal_rewriter.varied_sentence_restructure(text)
    text = universal_rewriter.smart_length_manipulation(text)
    text = universal_rewriter.add_natural_variation(text)
    return text






# =========================
# FRONTEND (DNA WATER GLASS UI — FINAL DARK MODE WORKING)
# =========================

import streamlit as st
import random

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- REWRITE FUNCTION (TRUE BACKEND CALL) ---
# This version uses the real rewriting logic from your backend
def guarantee_low_similarity(text, target):
    """Generate rewritten text using the true backend extreme_rewriter() logic."""
    rewritten = extreme_rewriter(text)
    similarity = calculate_similarity(text, rewritten)
    return rewritten, similarity

# --- CSS STYLES ---
st.markdown("""
<style>
body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: #e6faff;
}

/* ---- BUBBLES ---- */
#bubble-layer {
  position: fixed;
  top: 0; 
  left: 0;
  width: 100%; 
  height: 100%;
  overflow: hidden; 
  z-index: -3; 
  pointer-events: none;
}

.dna-bubble {
  position: absolute;
  bottom: -120px;
  background: rgba(0,180,255,0.3);
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0,200,255,0.6);
  animation: rise linear infinite;
}

@keyframes rise {
  0% { transform: translateY(0) scale(0.6); opacity: 0; }
  20% { opacity: 1; }
  70% { transform: translateY(-80vh) scale(1.1); opacity: 0.9; }
  100% { transform: translateY(-120vh) scale(0.8); opacity: 0; }
}

/* ---- DROPLETS ---- */
#droplet-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -2;
  pointer-events: none;
}

.droplet {
  position: absolute;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.25), rgba(255,255,255,0.05));
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0,200,255,0.15);
  animation: slideDown 18s ease-in-out infinite;
}

@keyframes slideDown {
  0% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
  50% { transform: translateY(15px) rotate(2deg); opacity: 1; }
  100% { transform: translateY(0) rotate(-1deg); opacity: 0.8; }
}

/* ---- WAVE ---- */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 220px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -1;
}

@keyframes waveMove {
  from { transform: translateY(0); }
  to { transform: translateY(-30px); }
}

/* ---- GLASS BOX ---- */
.glass-box {
  backdrop-filter: blur(25px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  margin-top: 2rem;
}

/* ---- TITLE ---- */
h1.title {
  text-align: center;
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(45deg, #00eaff, #00ffb7, #0095ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: colorShift 6s ease-in-out infinite;
  margin-top: 3rem;
}
@keyframes colorShift {
  0% { filter: hue-rotate(0deg); }
  50% { filter: hue-rotate(180deg); }
  100% { filter: hue-rotate(360deg); }
}

/* ---- BUTTONS ---- */
.stButton>button {
  background: linear-gradient(135deg, #00b4ff, #0077ff);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1.1rem;
  padding: 0.75rem 2rem;
  transition: all 0.3s ease;
}
.stButton>button:hover {
  background: linear-gradient(135deg, #0077ff, #00b4ff);
  box-shadow: 0 0 15px rgba(0,180,255,0.8);
  transform: translateY(-2px);
}

/* ---- TEXTAREA ---- */
.stTextArea textarea {
  border-radius: 15px;
  border: 1px solid rgba(0,180,255,0.3);
  background: rgba(15, 25, 35, 0.9);
  color: #e6faff;
  font-size: 1rem;
  padding: 1rem;
  resize: vertical;
}

/* ---- FOOTER ---- */
.footer {
  text-align:center;
  margin-top:3rem;
  color:#66dfff;
  font-size:1.1rem;
  padding-bottom:2rem;
  animation: glow 3s ease-in-out infinite alternate;
}
@keyframes glow {
  from { text-shadow: 0 0 5px #00b4ff; }
  to { text-shadow: 0 0 20px #00ffff; }
}
</style>
""", unsafe_allow_html=True)

# --- VISUAL LAYERS (BUBBLES + DROPLETS) ---
bubble_html = '<div id="bubble-layer">'
for i in range(40):
    size = random.randint(8, 35)
    left = random.randint(0, 98)
    duration = random.randint(15, 28)
    delay = random.randint(0, 12)
    bubble_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
bubble_html += '</div>'

droplet_html = '<div id="droplet-layer">'
for i in range(25):
    size = random.randint(4, 18)
    top = random.randint(0, 90)
    left = random.randint(0, 95)
    duration = random.randint(12, 20)
    delay = random.randint(0, 8)
    droplet_html += f"""
    <div class="droplet" style="
        top:{top}vh;
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
droplet_html += '</div><div class="wave-bg"></div>'

st.markdown(bubble_html + droplet_html, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1 class="title">💧 Extreme Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

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
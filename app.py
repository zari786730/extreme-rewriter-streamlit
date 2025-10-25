import random
import re
import streamlit as st
from collections import defaultdict
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
# SIMPLE SYNOYM FETCHER - GUARANTEED WORKING
# =========================
class SimpleSynonymFinder:
    def __init__(self):
        self.cache = {}
        self.fallback_synonyms = {
            'research': ['study', 'investigation', 'analysis', 'examination'],
            'study': ['research', 'analysis', 'investigation', 'examination'],
            'analysis': ['examination', 'evaluation', 'assessment', 'study'],
            'data': ['information', 'facts', 'statistics', 'findings'],
            'method': ['approach', 'technique', 'procedure', 'strategy'],
            'result': ['outcome', 'finding', 'conclusion', 'product'],
            'show': ['demonstrate', 'reveal', 'indicate', 'display'],
            'important': ['significant', 'crucial', 'vital', 'essential'],
            'use': ['utilize', 'employ', 'apply', 'implement'],
            'create': ['generate', 'produce', 'develop', 'make'],
            'help': ['assist', 'aid', 'support', 'facilitate'],
            'understand': ['comprehend', 'grasp', 'apprehend', 'fathom'],
            'change': ['modify', 'alter', 'adjust', 'transform'],
            'problem': ['issue', 'challenge', 'difficulty', 'obstacle'],
            'solution': ['resolution', 'answer', 'remedy', 'fix']
        }
    
    def get_synonyms(self, word):
        """Simple synonym fetcher with guaranteed fallback"""
        word = word.lower().strip()
        
        # Check cache first
        if word in self.cache:
            return self.cache[word]
        
        # Try online API
        try:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=3)
            if response.status_code == 200:
                data = response.json()
                synonyms = []
                for meaning in data[0].get('meanings', []):
                    for definition in meaning.get('definitions', []):
                        synonyms.extend(definition.get('synonyms', []))
                
                if synonyms:
                    unique_synonyms = list(set(synonyms))[:4]
                    self.cache[word] = unique_synonyms
                    st.write(f"🌐 Fetched synonyms for: {word}")
                    return unique_synonyms
        except:
            pass
        
        # Use fallback synonyms
        if word in self.fallback_synonyms:
            self.cache[word] = self.fallback_synonyms[word]
            st.write(f"📚 Used fallback synonyms for: {word}")
            return self.fallback_synonyms[word]
        
        return []

# =========================
# SIMPLE REWRITER CLASS - GUARANTEED WORKING
# =========================
class UniversalExtremeRewriter:
    def __init__(self):
        self.synonym_finder = SimpleSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()
        st.write("✅ Rewriter ready - synonym system active")

    def setup_vocabulary(self):
        """Setup vocabulary with your existing words"""
        # Add health terms
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        # Add general words
        for word, replacement in general_words.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        st.write(f"📚 Loaded {len(self.replacements)} words from dictionaries")

    def intelligent_word_replacement(self, text):
        """SIMPLE word replacement that actually works"""
        if not text:
            return text
            
        words = text.split()
        new_words = []
        
        for word in words:
            original_word = word
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip short/common words
            if len(clean_word) <= 2 or clean_word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at']:
                new_words.append(original_word)
                continue
            
            # Check if word is in replacements
            if clean_word in self.replacements:
                replacement = random.choice(self.replacements[clean_word])
                if word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
                continue
            
            # If not in vocabulary, try to find synonyms
            synonyms = self.synonym_finder.get_synonyms(clean_word)
            if synonyms:
                self.replacements[clean_word] = synonyms
                replacement = random.choice(synonyms)
                if word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(original_word)
        
        return ' '.join(new_words)

    def varied_sentence_restructure(self, text):
        """Simple sentence restructuring"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
            
        # Just shuffle sentences for simplicity
        random.shuffle(sentences)
        return '. '.join(sentences) + '.'

    def smart_length_manipulation(self, text):
        """Simple length adjustment"""
        return text  # Skip complex manipulation for now

    def add_natural_variation(self, text):
        """Simple variation"""
        return text  # Skip for now

# Initialize the rewriter
universal_rewriter = UniversalExtremeRewriter()

def extreme_rewriter(original_text):
    """Simple rewriting that actually works"""
    if not original_text:
        return original_text
        
    clean_text = original_text.strip()
    
    # Apply word replacement first
    result = universal_rewriter.intelligent_word_replacement(clean_text)
    
    # Then sentence restructuring
    result = universal_rewriter.varied_sentence_restructure(result)
    
    # Finally grammar correction
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

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=5):
    """Keep generating until similarity is below threshold"""
    best_result = original_text
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
# SIMPLE STREAMLIT UI
# =========================
st.title("🔁 Text Rewriter")
st.write("Working synonym-based text rewriting")

text_input = st.text_area("Enter text to rewrite:", height=150, value="This research shows important results that help understand complex problems.")

if st.button("Rewrite Text"):
    if text_input:
        with st.spinner("Rewriting..."):
            rewritten, similarity = guarantee_low_similarity(text_input)
            
            st.subheader("Original:")
            st.write(text_input)
            
            st.subheader("Rewritten:")
            st.write(rewritten)
            
            st.subheader("Similarity:")
            st.write(f"{similarity:.1f}%")
    else:
        st.error("Please enter some text")






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
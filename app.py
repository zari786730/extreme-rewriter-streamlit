# =========================
# EXTREME REWRITER BACKEND
# =========================

import random
import re
import requests
import nltk
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
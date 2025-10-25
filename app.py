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
# AGGRESSIVE SYNONYM FINDER
# =========================
class AggressiveSynonymFinder:
    def __init__(self):
        self.cache = {}
        # EXPANDED FALLBACK SYNONYMS
        self.fallback_synonyms = {
            'research': ['investigation', 'inquiry', 'exploration', 'examination', 'scrutiny', 'analysis'],
            'study': ['examination', 'analysis', 'scrutiny', 'survey', 'research', 'investigation'],
            'analysis': ['examination', 'evaluation', 'assessment', 'interpretation', 'appraisal', 'scrutiny'],
            'data': ['information', 'facts', 'statistics', 'figures', 'details', 'findings'],
            'method': ['approach', 'technique', 'procedure', 'process', 'system', 'strategy'],
            'result': ['outcome', 'finding', 'conclusion', 'product', 'effect', 'consequence'],
            'show': ['demonstrate', 'reveal', 'indicate', 'display', 'exhibit', 'illustrate'],
            'important': ['significant', 'crucial', 'vital', 'essential', 'critical', 'paramount'],
            'use': ['utilize', 'employ', 'apply', 'implement', 'exercise', 'operate'],
            'create': ['generate', 'produce', 'develop', 'make', 'construct', 'formulate'],
            'help': ['assist', 'aid', 'support', 'facilitate', 'enable', 'guide'],
            'understand': ['comprehend', 'grasp', 'apprehend', 'fathom', 'discern', 'perceive'],
            'change': ['modify', 'alter', 'adjust', 'transform', 'convert', 'adapt'],
            'problem': ['issue', 'challenge', 'difficulty', 'obstacle', 'complication', 'dilemma'],
            'solution': ['resolution', 'answer', 'remedy', 'fix', 'approach', 'method'],
            'this': ['the present', 'the current', 'the existing', 'this particular'],
            'that': ['which', 'the aforementioned', 'the specified', 'the particular'],
            'these': ['the present', 'the current', 'the existing', 'these particular'],
            'those': ['the aforementioned', 'the specified', 'the particular', 'those specific'],
            'very': ['extremely', 'highly', 'exceptionally', 'remarkably', 'particularly'],
            'many': ['numerous', 'multiple', 'several', 'various', 'countless'],
            'some': ['certain', 'various', 'several', 'select', 'particular'],
            'more': ['additional', 'further', 'extra', 'supplementary', 'increased'],
            'most': ['majority', 'bulk', 'predominance', 'largest portion'],
            'all': ['every', 'each', 'entire', 'complete', 'total', 'whole'],
            'has': ['possesses', 'contains', 'includes', 'comprises', 'incorporates'],
            'have': ['possess', 'contain', 'include', 'comprise', 'incorporate'],
            'is': ['represents', 'constitutes', 'forms', 'comprises', 'equals'],
            'are': ['represent', 'constitute', 'form', 'comprise', 'equal'],
            'was': ['represented', 'constituted', 'formed', 'comprised', 'equaled'],
            'were': ['represented', 'constituted', 'formed', 'comprised', 'equaled'],
            'be': ['exist', 'occur', 'transpire', 'materialize', 'manifest'],
            'been': ['existed', 'occurred', 'transpired', 'materialized', 'manifested'],
            'being': ['existing', 'occurring', 'transpiring', 'materializing', 'manifesting']
        }
    
    def get_synonyms(self, word):
        """Get aggressive synonyms"""
        word = word.lower().strip()
        
        if word in self.cache:
            return self.cache[word]
        
        # Try online API
        try:
            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}", timeout=2)
            if response.status_code == 200:
                data = response.json()
                synonyms = []
                for meaning in data[0].get('meanings', []):
                    for definition in meaning.get('definitions', []):
                        synonyms.extend(definition.get('synonyms', []))
                
                if synonyms:
                    unique_synonyms = list(set(synonyms))[:6]
                    self.cache[word] = unique_synonyms
                    return unique_synonyms
        except:
            pass
        
        # Use aggressive fallback
        if word in self.fallback_synonyms:
            return self.fallback_synonyms[word]
        
        return []

# =========================
# AGGRESSIVE REWRITER CLASS
# =========================
class AggressiveRewriter:
    def __init__(self):
        self.synonym_finder = AggressiveSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()
        st.write("🚀 AGGRESSIVE rewriter activated!")

    def setup_vocabulary(self):
        """Setup vocabulary"""
        # Add health terms
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        # Add general words
        for word, replacement in general_words.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        st.write(f"📚 Loaded {len(self.replacements)} base words")

    def aggressive_word_replacement(self, text):
        """VERY AGGRESSIVE word replacement - 90% replacement rate"""
        if not text:
            return text
            
        words = text.split()
        new_words = []
        
        for word in words:
            original_word = word
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip only VERY short words
            if len(clean_word) <= 1:
                new_words.append(original_word)
                continue
            
            # 90% CHANCE OF REPLACEMENT for most words
            if random.random() < 0.9:
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
            else:
                new_words.append(original_word)
        
        return ' '.join(new_words)

    def restructure_sentences(self, text):
        """Aggressive sentence restructuring"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
        
        # Shuffle sentences
        random.shuffle(sentences)
        
        # Add variety to sentence starts
        starters = [
            "Research indicates that", "Studies demonstrate that", "Evidence suggests that",
            "Analysis reveals that", "Findings show that", "Data illustrates that",
            "It is evident that", "One can observe that", "The evidence indicates that"
        ]
        
        restructured = []
        for i, sentence in enumerate(sentences):
            if i == 0 and random.random() < 0.7:
                sentence = random.choice(starters) + " " + sentence.lower()
            restructured.append(sentence)
        
        return '. '.join(restructured) + '.'

    def change_sentence_structure(self, text):
        """Change sentence structure aggressively"""
        # Add prefixes
        prefixes = [
            "From this perspective,", "In this context,", "Within this framework,",
            "Considering these factors,", "Based on the evidence,", "According to the data,"
        ]
        
        if random.random() < 0.6:
            text = random.choice(prefixes) + " " + text.lower()
        
        return text

# Initialize the AGGRESSIVE rewriter
aggressive_rewriter = AggressiveRewriter()

def extreme_rewriter(original_text):
    """AGGRESSIVE rewriting that actually changes text"""
    if not original_text:
        return original_text
        
    clean_text = original_text.strip()
    
    # Apply AGGRESSIVE word replacement
    result = aggressive_rewriter.aggressive_word_replacement(clean_text)
    
    # Apply sentence restructuring
    result = aggressive_rewriter.restructure_sentences(result)
    
    # Change sentence structure
    result = aggressive_rewriter.change_sentence_structure(result)
    
    # Final grammar correction
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

def guarantee_low_similarity(original_text, max_similarity=15, max_attempts=8):
    """Keep generating until similarity is very low"""
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
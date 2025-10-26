import random
import re
import streamlit as st
from collections import defaultdict
import requests
import json
import os

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
# UNIVERSAL SYNONYM FINDER
# =========================
class UniversalSynonymFinder:
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
                if synonyms:
                    unique_synonyms = list(set(synonyms))[:6]
                    self.cache[word] = unique_synonyms
                    return unique_synonyms
        except:
            pass
        return []

# =========================
# SENTENCE-LEVEL REWRITER (YOUR IDEA)
# =========================
class SentenceLevelRewriter:
    def __init__(self):
        self.synonym_finder = UniversalSynonymFinder()
        self.replacements = {}
        self.setup_vocabulary()
    
    def setup_vocabulary(self):
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        for word, replacement in general_words.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement

    def rewrite_sentence_completely(self, sentence):
        """Your idea: completely rewrite sentences"""
        original = sentence.strip()
        if len(original.split()) < 4:
            return original
        
        # Different restructuring strategies
        strategies = [
            self._academic_restructure,
            self._change_sentence_focus,
            self._simplify_complex,
            self._split_combine_ideas
        ]
        
        for strategy in random.sample(strategies, len(strategies)):
            rewritten = strategy(original)
            if rewritten != original:
                return rewritten
        
        return original

    def _academic_restructure(self, sentence):
        patterns = [
            (r'(\w+) is far more than the mere (.+?); it is (.+)', r'Beyond simply \2, \1 fundamentally represents \3'),
            (r'At its core, it encompasses (.+)', r'The fundamental nature involves \1'),
            (r'An effective system seamlessly integrates (.+)', r'A successful framework combines \1'),
            (r'This holistic approach not only (.+?) but also (.+)', r'This comprehensive method both \1 and additionally \2'),
            (r'The true measure of (.+) lies not just in (.+), but in (.+)', r'The actual assessment of \1 depends not only on \2 but fundamentally on \3')
        ]
        for pattern, replacement in patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                return re.sub(pattern, replacement, sentence, flags=re.IGNORECASE)
        return sentence

    def _change_sentence_focus(self, sentence):
        focus_changes = [
            (r'Health care is', 'The healthcare system represents'),
            (r'it is a', 'this constitutes a'),
            (r'it encompasses', 'this includes'),
            (r'An effective system', 'A successful framework'),
        ]
        for old, new in focus_changes:
            if old in sentence.lower():
                return sentence.lower().replace(old, new).capitalize()
        return sentence

    def _simplify_complex(self, sentence):
        if len(sentence.split()) > 20:
            clauses = re.split(r'[,;]', sentence)
            if len(clauses) >= 2:
                main = clauses[0].strip()
                rest = '. '.join([c.strip() for c in clauses[1:] if c.strip()])
                return f"{main}. {rest}."
        return sentence

    def _split_combine_ideas(self, sentence):
        if 'not only' in sentence and 'but also' in sentence:
            parts = sentence.split(' but also ')
            if len(parts) == 2:
                first_part = parts[0].replace(' not only', '')
                second_part = parts[1]
                return f"{first_part}. Additionally, {second_part}"
        return sentence

    def intelligent_word_replacement(self, text):
        """Traditional word replacement as backup"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            if len(clean_word) <= 2 or clean_word in ['the', 'a', 'an', 'and', 'or', 'but']:
                new_words.append(word)
                continue
            
            if clean_word in self.replacements and random.random() < 0.7:
                replacement = random.choice(self.replacements[clean_word])
                if word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(word)
        
        return ' '.join(new_words)

# =========================
# MAIN UNIVERSAL REWRITER CLASS
# =========================
class UniversalExtremeRewriter:
    def __init__(self):
        self.sentence_rewriter = SentenceLevelRewriter()
        self.replacements = self.sentence_rewriter.replacements
        st.write("✅ Universal rewriter activated - Sentence-level + Word-level")

    def intelligent_word_replacement(self, text):
        """Word-level replacement"""
        return self.sentence_rewriter.intelligent_word_replacement(text)

    def varied_sentence_restructure(self, text):
        """Sentence-level restructuring (YOUR IDEA)"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        rewritten_sentences = []
        for sentence in sentences:
            # Use your sentence-level rewriting idea
            rewritten = self.sentence_rewriter.rewrite_sentence_completely(sentence)
            rewritten_sentences.append(rewritten)
        
        # Join with academic connectors
        connectors = ['. ', '. Furthermore, ', '. Moreover, ', '. Additionally, ']
        result = ''
        for i, sentence in enumerate(rewritten_sentences):
            if i > 0 and random.random() < 0.4:
                result += random.choice(connectors) + sentence.lower()
            else:
                result += sentence + '. '
        
        return result.strip()

    def smart_length_manipulation(self, text):
        """Sentence length management"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text

        processed = []
        for sentence in sentences:
            words = sentence.split()
            if random.random() < 0.5:
                if len(words) > 12:
                    mid = len(words) // 2
                    part1 = ' '.join(words[:mid])
                    part2 = ' '.join(words[mid:])
                    processed.extend([part1 + '.', part2.capitalize()])
                elif len(words) < 6:
                    expansions = ["It is evident that", "Research indicates that", "Studies demonstrate that"]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    processed.append(expanded)
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)

        return ' '.join(processed)

    def add_natural_variation(self, text):
        """Add natural writing variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text

        if random.random() < 0.3:
            variations = [
                f"Interestingly, {sentences[0].lower()}",
                f"Notably, {sentences[0].lower()}",
                f"Importantly, {sentences[0].lower()}"
            ]
            sentences[0] = random.choice(variations)

        return '. '.join(sentences) + '.'

# Initialize the universal rewriter
universal_rewriter = UniversalExtremeRewriter()

def extreme_rewriter(original_text):
    """Universal rewriting with sentence-level approach"""
    clean_text = original_text.strip().strip('"').strip("'")

    # Apply transformations in random order
    transformations = [
        universal_rewriter.varied_sentence_restructure,  # YOUR IDEA
        universal_rewriter.intelligent_word_replacement, 
        universal_rewriter.smart_length_manipulation,
        universal_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)

    result = clean_text
    for transform in transformations:
        result = transform(result)

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
# STREAMLIT UI
# =========================
st.title("🔁 Universal Text Rewriter")
st.write("Sentence-level + Word-level rewriting")

text_input = st.text_area("Enter text to rewrite:", height=200)

if st.button("Rewrite Text"):
    if text_input:
        with st.spinner("Rewriting with universal approach..."):
            rewritten, similarity = guarantee_low_similarity(text_input)
            
            st.subheader("Original Text:")
            st.write(text_input)
            
            st.subheader("Rewritten Text:")
            st.write(rewritten)
            
            st.subheader("Similarity Score:")
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
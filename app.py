import random
import re
import streamlit as st
from collections import defaultdict
import requests
import time
import json
import os
import threading

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
# FREE SYNONYM API CLASS
# =========================
class FreeSynonymsAPI:
    def __init__(self):
        self.cache = {}
    
    def get_synonyms(self, word):
        """Get synonyms from free dictionary API"""
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
                
        except Exception as e:
            pass
        
        return []

# =========================
# ACADEMIC VOCABULARY BUILDER - FIXED VERSION
# =========================
class AcademicVocabularyBuilder:
    def __init__(self, main_rewriter):
        self.synonym_finder = FreeSynonymsAPI()
        self.main_rewriter = main_rewriter
        self.learning_active = True
        
        # Academic word banks - EXPANDED
        self.academic_words = [
            # Biology (40 words)
            'cell', 'dna', 'rna', 'protein', 'enzyme', 'metabolism', 'respiration', 
            'photosynthesis', 'mitosis', 'meiosis', 'chromosome', 'gene', 'mutation',
            'evolution', 'ecology', 'ecosystem', 'organism', 'tissue', 'organ',
            'membrane', 'nucleus', 'mitochondria', 'biology', 'biological', 'cellular',
            'genetic', 'molecular', 'microbial', 'physiology', 'anatomy', 'zoology',
            'botany', 'microbiology', 'biochemistry', 'immunology', 'neuroscience',
            'pathology', 'virology', 'bacteriology', 'genomics',
            
            # Chemistry (35 words)
            'atom', 'molecule', 'compound', 'element', 'reaction', 'bond', 
            'solution', 'acid', 'base', 'ph', 'equilibrium', 'catalyst',
            'organic', 'inorganic', 'chemical', 'chemistry', 'synthesis',
            'analysis', 'laboratory', 'experiment', 'formula', 'equation',
            'periodic', 'table', 'atomic', 'molecular', 'compound', 'mixture',
            'solvent', 'solute', 'concentration', 'temperature', 'pressure',
            'volume', 'mass',
            
            # Physics (30 words)
            'force', 'energy', 'velocity', 'acceleration', 'momentum', 'gravity',
            'quantum', 'relativity', 'mechanics', 'optics', 'electricity',
            'magnetism', 'wave', 'particle', 'mass', 'physics', 'physical',
            'motion', 'speed', 'distance', 'time', 'space', 'universe',
            'thermodynamics', 'entropy', 'temperature', 'pressure', 'volume',
            'density', 'weight',
            
            # Academic Writing (25 words)
            'analyze', 'evaluate', 'synthesize', 'interpret', 'demonstrate',
            'illustrate', 'methodology', 'framework', 'paradigm', 'theoretical',
            'empirical', 'hypothesis', 'premise', 'inference', 'validation',
            'argument', 'evidence', 'conclusion', 'discussion', 'analysis',
            'evaluation', 'synthesis', 'interpretation', 'demonstration',
            
            # Research Methods (25 words)
            'methodology', 'protocol', 'procedure', 'sampling', 'population',
            'variable', 'control', 'validity', 'reliability', 'correlation',
            'significance', 'statistic', 'distribution', 'research', 'study',
            'experiment', 'observation', 'data', 'results', 'findings',
            'conclusions', 'recommendations', 'limitations', 'implications',
            
            # Scientific Concepts (25 words)
            'theory', 'law', 'principle', 'concept', 'phenomenon', 'mechanism',
            'process', 'system', 'model', 'experiment', 'observation', 'data',
            'evidence', 'proof', 'measurement', 'science', 'scientific',
            'discovery', 'innovation', 'technology', 'application', 'development',
            'progress', 'advancement', 'breakthrough'
        ]
        
        self.learned_words = set()
        self.progress_placeholder = st.empty()
        
        st.write(f"🎯 Academic vocabulary builder activated")
        st.write(f"📚 {len(self.academic_words)} academic words queued for learning")
        self.start_continuous_learning()
    
    def update_progress(self):
        """Update progress display"""
        learned_count = len(self.learned_words)
        total_count = len(self.academic_words)
        progress_percent = (learned_count / total_count) * 100
        
        with self.progress_placeholder.container():
            st.write(f"**🧠 Learning Progress:** {learned_count}/{total_count} words ({progress_percent:.1f}%)")
            
            # Progress bar
            progress_bar = st.progress(progress_percent / 100)
            
            # Show recently learned words
            if learned_count > 0:
                recent_words = list(self.learned_words)[-5:]  # Last 5 learned words
                st.write(f"**Recently learned:** {', '.join(recent_words)}")
    
    def start_continuous_learning(self):
        """Start background learning thread with proper progress tracking"""
        def learning_worker():
            for word in self.academic_words:
                if not self.learning_active:
                    break
                    
                try:
                    if word not in self.main_rewriter.replacements and word not in self.learned_words:
                        synonyms = self.synonym_finder.get_synonyms(word)
                        if synonyms:
                            self.main_rewriter.replacements[word] = synonyms
                            self.learned_words.add(word)
                            
                            # Update progress every word for better visibility
                            self.update_progress()
                            
                            # Save to file every 10 words
                            if len(self.learned_words) % 10 == 0:
                                self.save_vocabulary()
                    
                    time.sleep(1.5)  # Be nice to the API
                    
                except Exception as e:
                    time.sleep(2)
            
            # Final update when done
            self.update_progress()
            st.success(f"✅ Academic vocabulary learning completed! Learned {len(self.learned_words)} words.")
            self.save_vocabulary()
        
        # Start the thread
        thread = threading.Thread(target=learning_worker, daemon=True)
        thread.start()
    
    def save_vocabulary(self):
        """Save learned vocabulary to file"""
        try:
            learned_vocab = {}
            for word in self.learned_words:
                if word in self.main_rewriter.replacements:
                    learned_vocab[word] = self.main_rewriter.replacements[word]
            
            with open("learned_vocabulary.json", "w") as f:
                json.dump(learned_vocab, f, indent=2)
            
            st.write(f"💾 Saved {len(learned_vocab)} learned words to file")
        except Exception as e:
            st.write(f"⚠️ Could not save vocabulary: {e}")

# =========================
# MAIN REWRITER CLASS
# =========================
class UniversalExtremeRewriter:
    def __init__(self):
        self.replacements = {}
        self.setup_comprehensive_vocabulary()
        
        # Start academic vocabulary builder
        self.vocabulary_builder = AcademicVocabularyBuilder(self)

    def setup_comprehensive_vocabulary(self):
        """EXPANDED vocabulary database for universal use"""
        # Start with your existing replacements
        self.replacements = {}
          
        # Add health terms
        for word, replacement in health_terms.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        # Add general words
        for word, replacement in general_words.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
        
        st.write(f"✅ Total vocabulary loaded: {len(self.replacements)} words")

    def intelligent_word_replacement(self, text):
        """More aggressive and intelligent word replacement"""
        words = text.split()
        new_words = []
        i = 0
        
        while i < len(words):
            word = words[i].lower().strip('.,!?;:"')
            original_word = words[i]

            # Skip very short/common words
            if len(word) <= 2 or word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']:
                new_words.append(original_word)
                i += 1
                continue

            # Try 2-word phrases first
            if i + 1 < len(words):
                next_word = words[i+1].lower().strip('.,!?;:"')
                two_word = f"{word} {next_word}"
                if two_word in self.replacements:
                    replacement = self.replacements[two_word]
                    if isinstance(replacement, list):
                        replacement = random.choice(replacement)
                    if words[i][0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    i += 2
                    continue

            # Single word replacement with high probability
            if word in self.replacements and random.random() < 0.7:
                replacement = self.replacements[word]
                if isinstance(replacement, list):
                    replacement = random.choice(replacement)
                if words[i][0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(original_word)

            i += 1

        return ' '.join(new_words)

    # KEEP ALL YOUR EXISTING METHODS EXACTLY THE SAME
    # varied_sentence_restructure, smart_length_manipulation, add_natural_variation
    def varied_sentence_restructure(self, text):
        # ... your existing code ...
        return text

    def smart_length_manipulation(self, text):
        # ... your existing code ...
        return text

    def add_natural_variation(self, text):
        # ... your existing code ...
        return text

# Initialize the universal rewriter
universal_rewriter = UniversalExtremeRewriter()

# KEEP ALL YOUR EXISTING FUNCTIONS EXACTLY THE SAME
def extreme_rewriter(original_text):
    # ... your existing code ...
    return original_text

def calculate_similarity(original, rewritten):
    # ... your existing code ...
    return 0

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    # ... your existing code ...
    return original_text, 0




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
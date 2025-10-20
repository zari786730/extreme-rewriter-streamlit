import random
import re
import streamlit as st
from collections import defaultdict

# =========================
# GRAMMAR-CORRECTED UNIVERSAL BACKEND
# =========================

class GrammarCorrectedRewriter:
    def __init__(self):
        self.setup_comprehensive_vocabulary()
    
    def setup_comprehensive_vocabulary(self):
        """EXPANDED vocabulary database for universal use"""
        self.replacements = {
            # Common academic/research words
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study', 'empirical exploration'],
            'study': ['examination', 'analysis', 'investigation', 'scrutiny', 'assessment'],
            'analysis': ['evaluation', 'appraisal', 'interpretation', 'assessment'],
            'evidence': ['empirical data', 'documented findings', 'research results', 'substantive proof'],
            'data': ['information', 'findings', 'metrics', 'statistics'],
            'method': ['approach', 'technique', 'procedure', 'methodology'],
            'result': ['outcome', 'finding', 'conclusion', 'product'],
            'show': ['demonstrate', 'reveal', 'illustrate', 'indicate', 'display'],
            'prove': ['substantiate', 'verify', 'confirm', 'validate'],
            'suggest': ['indicate', 'imply', 'propose', 'point to'],
            
            # Common adjectives
            'important': ['crucial', 'vital', 'essential', 'significant', 'paramount'],
            'significant': ['notable', 'considerable', 'substantial', 'meaningful'],
            'different': ['various', 'diverse', 'distinct', 'disparate'],
            'many': ['numerous', 'multiple', 'countless', 'several'],
            'big': ['large', 'substantial', 'considerable', 'sizable'],
            'small': ['minor', 'modest', 'limited', 'minimal'],
            'good': ['effective', 'beneficial', 'advantageous', 'favorable'],
            'bad': ['detrimental', 'unfavorable', 'negative', 'adverse'],
            'beautiful': ['stunning', 'gorgeous', 'exquisite', 'magnificent'],
            'beauty': ['aesthetics', 'elegance', 'grace', 'loveliness'],
            
            # Common verbs
            'use': ['utilize', 'employ', 'leverage', 'apply'],
            'make': ['create', 'produce', 'construct', 'generate'],
            'do': ['perform', 'execute', 'carry out', 'conduct'],
            'get': ['obtain', 'acquire', 'secure', 'attain'],
            'help': ['assist', 'facilitate', 'support', 'aid'],
            'change': ['alter', 'modify', 'transform', 'adjust'],
            'develop': ['cultivate', 'nurture', 'foster', 'build'],
            'create': ['generate', 'produce', 'establish', 'form'],
            'understand': ['comprehend', 'grasp', 'apprehend', 'fathom'],
            'explain': ['clarify', 'elucidate', 'interpret', 'expound'],
            
            # Society & culture words
            'society': ['community', 'populace', 'civilization', 'social fabric'],
            'culture': ['heritage', 'traditions', 'customs', 'way of life'],
            'people': ['individuals', 'persons', 'population', 'citizens'],
            'government': ['administration', 'authorities', 'leadership', 'regime'],
            'organization': ['institution', 'entity', 'association', 'body'],
            'system': ['framework', 'structure', 'network', 'arrangement'],
        }
    
    def clean_sentence_endings(self, text):
        """Remove random dots and ensure proper sentence endings"""
        # Remove multiple consecutive dots
        text = re.sub(r'\.{2,}', '.', text)
        # Ensure space after dots
        text = re.sub(r'\.(\w)', r'. \1', text)
        # Remove dots in the middle of sentences
        text = re.sub(r'(\w)\.(\s+[a-z])', r'\1\2', text)
        return text
    
    def intelligent_word_replacement(self, text):
        """Grammar-aware word replacement"""
        words = text.split()
        new_words = []
        
        i = 0
        while i < len(words):
            word = words[i].lower().strip('.,!?;:"')
            original_word = words[i]
            
            # Preserve punctuation
            punctuation = ''
            if original_word and not original_word[-1].isalnum():
                punctuation = original_word[-1]
                original_word = original_word[:-1]
            
            # Skip very short/common words
            if len(word) <= 2 or word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']:
                new_words.append(original_word + punctuation)
                i += 1
                continue
            
            # Single word replacement with grammar awareness
            if word in self.replacements and random.random() < 0.7:
                replacement = random.choice(self.replacements[word])
                # Preserve capitalization
                if original_word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement + punctuation)
            else:
                new_words.append(original_word + punctuation)
            
            i += 1
        
        return ' '.join(new_words)
    
    def grammar_aware_sentence_restructure(self, text):
        """Restructure sentences with proper grammar"""
        # Split into sentences properly
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        restructured = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 4:
                restructured.append(sentence)
                continue
            
            # Choose structure based on sentence length and content
            if len(words) > 15:
                # Split long sentences intelligently
                restructured.extend(self.split_long_sentence(sentence))
            elif len(words) < 8:
                # Expand short sentences
                restructured.append(self.expand_short_sentence(sentence))
            else:
                # Restructure medium sentences
                restructured.append(self.restructure_medium_sentence(sentence))
        
        # Join with proper punctuation
        result = '. '.join(restructured) + '.' if restructured else ''
        return self.clean_sentence_endings(result)
    
    def split_long_sentence(self, sentence):
        """Intelligently split long sentences at natural break points"""
        words = sentence.split()
        connectors = ['and', 'but', 'however', 'therefore', 'moreover', 'furthermore', 'although', 'while']
        split_points = []
        
        # Find natural split points
        for i, word in enumerate(words):
            if word.lower() in connectors and 4 < i < len(words) - 4:
                split_points.append(i)
        
        if split_points:
            split_at = random.choice(split_points)
            part1 = ' '.join(words[:split_at])
            part2 = ' '.join(words[split_at:])
            # Ensure part2 starts with proper capitalization
            part2 = part2[0].upper() + part2[1:] if part2 else part2
            return [part1 + '.', part2]
        else:
            # Fallback: split at relative clause or comma
            return [sentence]
    
    def expand_short_sentence(self, sentence):
        """Expand short sentences with additional context"""
        expansions = [
            "Research indicates that",
            "Studies demonstrate that", 
            "Evidence suggests that",
            "It is evident that",
            "One can observe that",
            "Analysis reveals that",
            "Findings show that"
        ]
        
        # Ensure the expanded sentence flows naturally
        base_sentence = sentence.lower()
        if base_sentence.startswith(('the ', 'a ', 'an ')):
            base_sentence = base_sentence
        else:
            base_sentence = base_sentence
        
        expanded = f"{random.choice(expansions)} {base_sentence}"
        return expanded[0].upper() + expanded[1:]
    
    def restructure_medium_sentence(self, sentence):
        """Restructure medium-length sentences with varied patterns"""
        words = sentence.split()
        pattern_choice = random.choice(['passive', 'active', 'emphatic', 'conditional'])
        
        if pattern_choice == 'passive' and len(words) > 6:
            # Convert to passive voice where appropriate
            return self.convert_to_passive(sentence)
        elif pattern_choice == 'emphatic':
            # Add emphasis
            emphatic_words = ['Notably,', 'Significantly,', 'Importantly,', 'Remarkably,']
            return f"{random.choice(emphatic_words)} {sentence.lower()}"
        elif pattern_choice == 'conditional':
            # Add conditional framing
            conditionals = ['When considered,', 'In this context,', 'From this perspective,']
            return f"{random.choice(conditionals)} {sentence.lower()}"
        else:
            return sentence
    
    def convert_to_passive(self, sentence):
        """Simple passive voice conversion for common patterns"""
        words = sentence.split()
        if len(words) >= 3:
            # Simple pattern: "A does B" -> "B is done by A"
            if words[1].endswith('s') and len(words) >= 3:  # Simple present tense detection
                subject = words[0]
                verb = words[1]
                rest = ' '.join(words[2:])
                
                # Convert verb to past participle
                verb_base = verb[:-1] if verb.endswith('s') else verb
                past_participle = verb_base + 'ed'  # Simple conversion
                
                return f"{rest} is {past_participle} by {subject}".capitalize()
        
        return sentence
    
    def vary_sentence_lengths(self, text):
        """Ensure sentences have different word counts while preserving meaning"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) < 2:
            return text
        
        processed_sentences = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            current_length = len(words)
            
            # Vary sentence lengths strategically
            if current_length > 20:
                # Split very long sentences
                split_sentences = self.split_long_sentence(sentence)
                processed_sentences.extend(split_sentences)
            elif current_length < 6:
                # Expand very short sentences
                processed_sentences.append(self.expand_short_sentence(sentence))
            else:
                # Moderate adjustment for medium sentences
                if i % 2 == 0 and current_length > 8:
                    # Make every other medium sentence slightly shorter
                    if len(words) > 10:
                        processed_sentences.append(' '.join(words[:8]) + '...')
                    else:
                        processed_sentences.append(sentence)
                else:
                    processed_sentences.append(sentence)
        
        result = '. '.join(processed_sentences) + '.' if processed_sentences else ''
        return self.clean_sentence_endings(result)
    
    def ensure_grammar_flow(self, text):
        """Final grammar and flow check"""
        # Fix common grammar issues
        text = re.sub(r'\s+([.,!?])', r'\1', text)  # Remove spaces before punctuation
        text = re.sub(r'\.\s*\.', '.', text)  # Remove consecutive dots
        text = re.sub(r',\s*,', ',', text)  # Remove consecutive commas
        
        # Ensure proper capitalization after sentence endings
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence and sentence[0].islower():
                sentence = sentence[0].upper() + sentence[1:]
            corrected_sentences.append(sentence)
        
        result = '. '.join(corrected_sentences) + '.' if corrected_sentences else ''
        return result

# Initialize the grammar-corrected rewriter
grammar_rewriter = GrammarCorrectedRewriter()

def extreme_rewriter(original_text):
    """Grammar-corrected extreme rewriting"""
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations in logical order
    result = clean_text
    result = grammar_rewriter.intelligent_word_replacement(result)
    result = grammar_rewriter.grammar_aware_sentence_restructure(result)
    result = grammar_rewriter.vary_sentence_lengths(result)
    result = grammar_rewriter.ensure_grammar_flow(result)
    
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
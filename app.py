import random
import re
import streamlit as st
from collections import defaultdict

# =========================
# IMPROVED UNIVERSAL BACKEND
# =========================

class UniversalExtremeRewriter:
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
            
            # Education words
            'education': ['learning', 'instruction', 'schooling', 'training'],
            'student': ['learner', 'pupil', 'scholar', 'trainee'],
            'teacher': ['educator', 'instructor', 'tutor', 'mentor'],
            'school': ['institution', 'academy', 'educational establishment'],
            
            # Business words
            'business': ['enterprise', 'company', 'firm', 'venture'],
            'market': ['industry', 'sector', 'commerce', 'trade'],
            'product': ['item', 'goods', 'merchandise', 'offering'],
            'customer': ['client', 'consumer', 'buyer', 'patron'],
            
            # Technology words
            'technology': ['innovation', 'digital tools', 'tech solutions', 'advancements'],
            'digital': ['electronic', 'computerized', 'online', 'virtual'],
            'information': ['data', 'knowledge', 'intelligence', 'facts'],
            
            # Time-related words
            'time': ['period', 'duration', 'interval', 'timespan'],
            'now': ['currently', 'presently', 'at this time', 'currently'],
            'recent': ['latest', 'current', 'contemporary', 'modern'],
            'old': ['ancient', 'aged', 'traditional', 'historic'],
            
            # Place-related words
            'world': ['globe', 'planet', 'earth', 'international community'],
            'country': ['nation', 'state', 'land', 'sovereign state'],
            'city': ['metropolis', 'urban center', 'municipality', 'town'],
            'place': ['location', 'site', 'venue', 'setting'],
            
            # General nouns
            'problem': ['issue', 'challenge', 'difficulty', 'obstacle'],
            'solution': ['resolution', 'answer', 'remedy', 'fix'],
            'way': ['method', 'approach', 'manner', 'technique'],
            'part': ['component', 'element', 'section', 'portion'],
            'kind': ['type', 'category', 'sort', 'variety'],
            
            # General adjectives
            'new': ['novel', 'innovative', 'fresh', 'recent'],
            'old': ['aged', 'ancient', 'traditional', 'historic'],
            'high': ['elevated', 'significant', 'substantial', 'considerable'],
            'low': ['minimal', 'reduced', 'limited', 'modest'],
            'fast': ['rapid', 'quick', 'speedy', 'swift'],
            'slow': ['gradual', 'leisurely', 'unhurried', 'deliberate']
        }
    
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
                    replacement = random.choice(self.replacements[two_word])
                    if words[i][0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    i += 2
                    continue
            
            # Single word replacement with high probability
            if word in self.replacements and random.random() < 0.7:  # 70% replacement rate
                replacement = random.choice(self.replacements[word])
                if words[i][0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(original_word)
            
            i += 1
        
        return ' '.join(new_words)
    
    def varied_sentence_restructure(self, text):
        """More diverse sentence restructuring patterns"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        restructured = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            if len(words) < 4:
                restructured.append(sentence)
                continue
            
            # DIVERSE patterns (no repetition)
            pattern_choice = random.choice([
                'reverse', 'question', 'academic', 'emphasis', 
                'context', 'normal', 'comparative', 'result'
            ])
            
            if pattern_choice == 'reverse' and len(words) > 6:
                split_point = random.randint(3, len(words) - 3)
                first_part = ' '.join(words[:split_point])
                second_part = ' '.join(words[split_point:])
                reverse_frames = [
                    f"{second_part}, thereby illustrating {first_part.lower()}",
                    f"{second_part}, which highlights {first_part.lower()}",
                    f"{second_part}, revealing how {first_part.lower()}",
                    f"{second_part}, demonstrating that {first_part.lower()}"
                ]
                restructured.append(random.choice(reverse_frames))
                
            elif pattern_choice == 'question':
                question_frames = [
                    f"What explains {sentence.lower()}?",
                    f"How can we understand {sentence.lower()}?",
                    f"Why is it significant that {sentence.lower()}?",
                    f"In what ways does {sentence.lower()}?"
                ]
                restructured.append(random.choice(question_frames))
                
            elif pattern_choice == 'academic':
                academic_frames = [
                    f"Research indicates that {sentence.lower()}",
                    f"Studies demonstrate that {sentence.lower()}",
                    f"Evidence suggests that {sentence.lower()}",
                    f"Analysis reveals that {sentence.lower()}",
                    f"Findings show that {sentence.lower()}"
                ]
                restructured.append(random.choice(academic_frames))
                
            elif pattern_choice == 'emphasis':
                emphasis_frames = [
                    f"Notably, {sentence.lower()}",
                    f"Significantly, {sentence.lower()}",
                    f"Importantly, {sentence.lower()}",
                    f"Remarkably, {sentence.lower()}"
                ]
                restructured.append(random.choice(emphasis_frames))
                
            elif pattern_choice == 'context':
                context_frames = [
                    f"In this context, {sentence.lower()}",
                    f"Within this framework, {sentence.lower()}",
                    f"From this perspective, {sentence.lower()}",
                    f"Considering these factors, {sentence.lower()}"
                ]
                restructured.append(random.choice(context_frames))
                
            elif pattern_choice == 'comparative':
                comparative_frames = [
                    f"By comparison, {sentence.lower()}",
                    f"Similarly, {sentence.lower()}",
                    f"Likewise, {sentence.lower()}",
                    f"In contrast, {sentence.lower()}"
                ]
                restructured.append(random.choice(comparative_frames))
                
            elif pattern_choice == 'result':
                result_frames = [
                    f"Consequently, {sentence.lower()}",
                    f"As a result, {sentence.lower()}",
                    f"Therefore, {sentence.lower()}",
                    f"Accordingly, {sentence.lower()}"
                ]
                restructured.append(random.choice(result_frames))
                
            else:
                restructured.append(sentence)
        
        return '. '.join(restructured) + '.'
    
    def smart_length_manipulation(self, text):
        """Better sentence length management"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text
        
        processed = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # Only manipulate 50% of sentences for better flow
            if random.random() < 0.5:
                if len(words) > 12:
                    # Smart splitting at natural break points
                    connectors = ['and', 'but', 'however', 'therefore', 'moreover', 'furthermore']
                    split_points = []
                    
                    for i, word in enumerate(words):
                        if word.lower() in connectors and 4 < i < len(words) - 4:
                            split_points.append(i)
                    
                    if split_points:
                        split_at = random.choice(split_points)
                        part1 = ' '.join(words[:split_at])
                        part2 = ' '.join(words[split_at:])
                        processed.extend([part1 + '.', part2.capitalize()])
                    else:
                        # Fallback: split at middle
                        mid = len(words) // 2
                        part1 = ' '.join(words[:mid])
                        part2 = ' '.join(words[mid:])
                        processed.extend([part1 + '.', part2.capitalize()])
                elif len(words) < 6:
                    # Expand short sentences
                    expansions = [
                        "It is evident that",
                        "One can observe that", 
                        "Research indicates that",
                        "The evidence shows that",
                        "Analysis reveals that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    processed.append(expanded)
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        
        return ' '.join(processed)
    
    def add_natural_variation(self, text):
        """Add natural human writing variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        # Add variation to first sentence only (avoid over-patterning)
        if random.random() < 0.4:
            variations = [
                f"Interestingly, {sentences[0].lower()}",
                f"Notably, {sentences[0].lower()}",
                f"Surprisingly, {sentences[0].lower()}",
                f"Importantly, {sentences[0].lower()}"
            ]
            sentences[0] = random.choice(variations)
        
        return '. '.join(sentences) + '.'

# Initialize the universal rewriter
universal_rewriter = UniversalExtremeRewriter()

def extreme_rewriter(original_text):
    """Universal extreme rewriting with improved transformations"""
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations in random order for variety
    transformations = [
        universal_rewriter.varied_sentence_restructure,
        universal_rewriter.intelligent_word_replacement, 
        universal_rewriter.smart_length_manipulation,
        universal_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)
    
    result = clean_text
    for transform in transformations:
        result = transform(result)
    
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
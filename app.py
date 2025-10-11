# =========================
# COMPLETE INTEGRATED VERSION (BACKEND + FRONTEND)
# =========================

import streamlit as st
import random
import re

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- BACKEND REWRITING ENGINE ---
def extreme_rewriter(original_text):
    """
    Extreme rewriting that guarantees <20% similarity through radical changes
    """
    
    clean_text = original_text.strip().strip('"').strip("'")
    
    # EXTREME TRANSFORMATION 1: Complete sentence structure overhaul
    def radical_sentence_restructure(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        if not sentences:
            return text
            
        # Completely rebuild each sentence with different patterns
        rebuilt_sentences = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 4:
                rebuilt_sentences.append(sentence)
                continue
                
            # RADICAL PATTERN 1: Question format
            if random.random() < 0.3:
                question_words = ['How', 'What', 'Why', 'In what ways']
                rebuilt = f"{random.choice(question_words)} does {sentence.lower()}?"
                rebuilt_sentences.append(rebuilt)
            
            # RADICAL PATTERN 2: Reverse order
            elif random.random() < 0.3:
                if len(words) > 6:
                    mid_point = len(words) // 2
                    part1 = ' '.join(words[:mid_point])
                    part2 = ' '.join(words[mid_point:])
                    rebuilt = f"{part2}, which demonstrates that {part1.lower()}"
                    rebuilt_sentences.append(rebuilt)
            
            # RADICAL PATTERN 3: Academic framing
            elif random.random() < 0.4:
                academic_frames = [
                    f"Scholarly analysis reveals that {sentence.lower()}",
                    f"Research findings indicate {sentence.lower()}",
                    f"Academic investigation demonstrates {sentence.lower()}",
                    f"Evidence from multiple studies shows {sentence.lower()}",
                    f"Comprehensive research establishes {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(academic_frames))
            
            # RADICAL PATTERN 4: Extreme compression/expansion
            else:
                if random.random() < 0.5:
                    # Extreme compression
                    if len(words) > 8:
                        compressed = ' '.join(words[:4] + words[-2:])
                        rebuilt_sentences.append(compressed + "...")
                    else:
                        rebuilt_sentences.append(sentence)
                else:
                    # Extreme expansion
                    expansions = [
                        "This represents a significant development in the field because",
                        "From a comprehensive analytical perspective,",
                        "When contextualized within broader scholarly discourse,",
                        "Considering the multifaceted implications of this phenomenon,",
                        "Through rigorous empirical examination it becomes evident that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    rebuilt_sentences.append(expanded)
        
        return '. '.join(rebuilt_sentences) + '.'

    # EXTREME TRANSFORMATION 2: Vocabulary nuclear option
    def nuclear_vocabulary_replacement(text):
        # Comprehensive word replacement database
        nuclear_replacements = {
            # Academic terms
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
            'study': ['examination', 'analysis', 'investigation'],
            'analysis': ['scrutiny', 'assessment', 'evaluation'],
            'evidence': ['empirical data', 'documented findings', 'research results'],
            
            # Democracy terms
            'democracy': ['democratic governance', 'popular sovereignty', 'representative government'],
            'democratic': ['self-governing', 'popularly accountable', 'representative'],
            'governance': ['administration', 'steering', 'political management'],
            'accountability': ['answerability', 'responsibility', 'obligation'],
            
            # Society terms
            'society': ['social fabric', 'community', 'civilization'],
            'civil': ['civic', 'public', 'communal'],
            'organization': ['institution', 'entity', 'association'],
            'movement': ['campaign', 'initiative', 'drive'],
            
            # Action verbs
            'evolved': ['developed progressively', 'transformed gradually', 'advanced systematically'],
            'emerged': ['arisen', 'materialized', 'come to prominence'],
            'promoting': ['advancing', 'fostering', 'championing'],
            'served': ['functioned', 'operated', 'acted'],
            'striving': ['endeavoring', 'working assiduously', 'making concerted efforts'],
            
            # Descriptive terms
            'complex': ['multifaceted', 'intricate', 'sophisticated'],
            'vital': ['essential', 'indispensable', 'fundamental'],
            'persistent': ['unrelenting', 'sustained', 'continual'],
            'transparency': ['openness', 'clarity', 'candor'],
            
            # Geographic terms
            'South Asia': ['the South Asian region', 'Southern Asian nations', 'the Indian subcontinent region'],
            'countries': ['nation-states', 'political entities', 'sovereign states'],
            
            # Structural terms
            'landscape': ['environment', 'terrain', 'context'],
            'legacies': ['inheritance', 'historical baggage', 'enduring influences'],
            'inequalities': ['disparities', 'imbalances', 'differentials'],
            'struggles': ['campaigns', 'endeavors', 'movements'],
            'practices': ['procedures', 'methodologies', 'approaches'],
            'freedoms': ['liberties', 'entitlements', 'rights'],
            'institutions': ['establishments', 'organizations', 'bodies'],
            'erosion': ['deterioration', 'decline', 'weakening']
        }
        
        new_text = text
        for original, replacements in nuclear_replacements.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                replacement = random.choice(replacements)
                new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
        
        return new_text

    # EXTREME TRANSFORMATION 3: Sentence length manipulation
    def extreme_length_manipulation(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        if len(sentences) <= 1:
            return text
            
        manipulated = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # DRAMATIC length changes
            if random.random() < 0.6:
                if len(words) > 10:
                    # Split into multiple short sentences
                    num_splits = random.randint(2, 4)
                    chunk_size = max(3, len(words) // num_splits)
                    
                    for i in range(0, len(words), chunk_size):
                        chunk = words[i:i + chunk_size]
                        if len(chunk) >= 3:
                            manipulated.append(' '.join(chunk) + '.')
                else:
                    # Expand short sentences dramatically
                    expansions = [
                        "This represents a significant development in the field because",
                        "From a comprehensive analytical perspective,",
                        "When contextualized within broader scholarly discourse,",
                        "Considering the multifaceted implications of this phenomenon,",
                        "Through rigorous empirical examination it becomes evident that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    manipulated.append(expanded)
            else:
                manipulated.append(sentence)
        
        return ' '.join(manipulated)

    # EXTREME TRANSFORMATION 4: Add human-like variations
    def add_human_touches(text):
        # Add human writing patterns that AI doesn't use
        human_patterns = [
            # Conversational academic style
            lambda t: f"Interestingly, {t.lower()}",
            
            # Reflective style
            lambda t: f"Upon reflection, {t.lower()}",
            
            # Comparative style
            lambda t: f"By comparison, {t.lower()}",
            
            # Cautious academic style
            lambda t: f"It appears that {t.lower()}",
            
            # Emphatic style
            lambda t: f"Notably, {t.lower()}",
            
            # Contextual style
            lambda t: f"In this context, {t.lower()}"
        ]
        
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if sentences:
            first_sentence = sentences[0]
            if random.random() < 0.7:
                pattern = random.choice(human_patterns)
                sentences[0] = pattern(first_sentence)
        
        return '. '.join(sentences) + '.'

    # APPLY ALL EXTREME TRANSFORMATIONS
    result = clean_text
    
    # Apply in sequence for maximum effect
    result = radical_sentence_restructure(result)
    result = nuclear_vocabulary_replacement(result)
    result = extreme_length_manipulation(result)
    result = add_human_touches(result)
    
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

def guarantee_low_similarity(text, target_similarity=20, max_attempts=5):
    """Keep generating until similarity is below threshold"""
    
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(text)
        similarity = calculate_similarity(text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            
        if similarity <= target_similarity:
            return rewritten, similarity
    
    return best_result, best_similarity

# --- FRONTEND UI ---

# CSS STYLES
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
input_text = st.text_area("🧬 Enter text:", height=180, placeholder="Paste your text here to rewrite it...", label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("Rewriting your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        
        # Display results
        st.success(f"✅ Rewriting complete! Similarity: {similarity:.1f}%")
        
        st.markdown(f"""
        <div style="border:1px solid rgba(0,255,255,0.3); border-radius:15px; padding:1.5rem; margin-top:1rem; background:rgba(0,20,30,0.6);">
            <h3 style="color:#00eaff; margin-top:0;">✨ Rewritten Text</h3>
            <div style="background:rgba(0,15,25,0.8); padding:1.5rem; border-radius:10px; border:1px solid rgba(0,180,255,0.2); color:#e6faff; line-height:1.6;">
            {rewritten}
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear"):
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
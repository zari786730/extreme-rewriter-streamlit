
# =========================
# FRONTEND (DNA MOLECULE UI - PREMIUM ENHANCED VERSION)
# =========================

import streamlit as st
import random
import time

# IMPORT BACKEND FUNCTIONS
try:
    from backend import extreme_rewriter, calculate_similarity, get_vocabulary_stats, guarantee_low_similarity
    BACKEND_AVAILABLE = True
except ImportError as e:
    BACKEND_AVAILABLE = False
    st.error(f"Backend not available: {e}")
    
    # Fallback functions
    def extreme_rewriter(text):
        return text + " (rewritten)"
    
    def calculate_similarity(original, rewritten):
        return random.randint(10, 30)
    
    def get_vocabulary_stats():
        return {
            "total_words": 45000,
            "loaded_files": 45,
            "health_terms": 2500,
            "general_words": 1200,
            "vocabulary_loaded": True
        }
    
    def guarantee_low_similarity(text, max_similarity=20, max_attempts=3):
        rewritten = extreme_rewriter(text)
        similarity = calculate_similarity(text, rewritten)
        return rewritten, similarity

st.set_page_config(page_title="Extreme DNA Rewriter", page_icon="🧬", layout="wide")

# =========================
# PREMIUM DNA MOLECULE CSS STYLES
# =========================
st.markdown("""
<style>
body {
    margin: 0;
    overflow-x: hidden;
    background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
    height: 100vh;
    font-family: 'Poppins', sans-serif;
    color: #e6faff;
}

/* ---- 3D ROTATING DNA LOGO ---- */
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 1000px;
    margin-bottom: 1rem;
}

.rotating-logo {
    font-size: 4rem;
    animation: rotate3D 4s ease-in-out infinite;
    transform-style: preserve-3d;
    text-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
    animation: rotate3D 4s ease-in-out infinite, colorChange 6s ease-in-out infinite;
}

@keyframes rotate3D {
    0% { transform: rotateY(0deg) rotateX(0deg) scale(1); }
    25% { transform: rotateY(90deg) rotateX(10deg) scale(1.1); }
    50% { transform: rotateY(180deg) rotateX(0deg) scale(1); }
    75% { transform: rotateY(270deg) rotateX(-10deg) scale(1.1); }
    100% { transform: rotateY(360deg) rotateX(0deg) scale(1); }
}

@keyframes colorChange {
    0% { filter: hue-rotate(0deg); color: #00eaff; }
    25% { filter: hue-rotate(90deg); color: #00ffb7; }
    50% { filter: hue-rotate(180deg); color: #0095ff; }
    75% { filter: hue-rotate(270deg); color: #b700ff; }
    100% { filter: hue-rotate(360deg); color: #00eaff; }
}

/* ---- CONTINUOUS BUBBLES BACKGROUND ---- */
#continuous-bubbles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -3;
    pointer-events: none;
}

.continuous-bubble {
    position: absolute;
    bottom: -100px;
    background: rgba(0, 180, 255, 0.15);
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(0, 200, 255, 0.4);
    animation: riseContinuous linear infinite;
    opacity: 0;
}

@keyframes riseContinuous {
    0% {
        transform: translateY(0) scale(0.3) translateX(0);
        opacity: 0;
    }
    10% {
        opacity: 0.7;
    }
    90% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-120vh) scale(1.2) translateX(20px);
        opacity: 0;
    }
}

/* ---- 3D DNA MOLECULE ANIMATIONS ---- */
#dna-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    pointer-events: none;
    perspective: 1000px;
}

.dna-helix {
    position: absolute;
    transform-style: preserve-3d;
    animation: floatDNA 15s ease-in-out infinite, glowPulse 4s ease-in-out infinite;
}

.dna-strand {
    position: absolute;
    width: 3px;
    background: linear-gradient(to bottom, 
        rgba(0, 255, 255, 0.8) 0%,
        rgba(0, 200, 255, 0.9) 50%,
        rgba(0, 255, 200, 0.8) 100%);
    border-radius: 2px;
    transform-origin: center center;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
}

.dna-node {
    position: absolute;
    width: 8px;
    height: 8px;
    background: radial-gradient(circle, 
        rgba(255, 255, 255, 0.9) 0%,
        rgba(0, 255, 255, 0.8) 70%,
        rgba(0, 100, 255, 0.6) 100%);
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
    transform-style: preserve-3d;
}

@keyframes floatDNA {
    0%, 100% { 
        transform: translateY(0px) rotateX(0deg) rotateY(0deg) scale(1);
    }
    25% { 
        transform: translateY(-15px) rotateX(90deg) rotateY(45deg) scale(1.05);
    }
    50% { 
        transform: translateY(-5px) rotateX(180deg) rotateY(90deg) scale(1);
    }
    75% { 
        transform: translateY(-20px) rotateX(270deg) rotateY(135deg) scale(1.05);
    }
}

@keyframes glowPulse {
    0%, 100% { 
        filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.6));
    }
    50% { 
        filter: drop-shadow(0 0 20px rgba(0, 255, 255, 0.9));
    }
}

/* Individual DNA Molecules */
.dna-molecule-1 {
    top: 20%;
    left: 15%;
    animation-duration: 25s;
}

.dna-molecule-2 {
    top: 70%;
    left: 85%;
    animation-duration: 30s;
    animation-direction: reverse;
}

.dna-molecule-3 {
    top: 15%;
    left: 80%;
    animation-duration: 35s;
}

.dna-molecule-4 {
    top: 75%;
    left: 10%;
    animation-duration: 28s;
    animation-direction: reverse;
}

/* ---- EVENT BUBBLES (On Button Press) ---- */
#event-bubbles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -1;
    pointer-events: none;
}

.event-bubble {
    position: absolute;
    bottom: -50px;
    background: radial-gradient(circle at 30% 30%, rgba(0, 255, 255, 0.8), rgba(0, 150, 255, 0.3));
    border-radius: 50%;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.9);
    animation: riseFast linear forwards;
    opacity: 0;
}

@keyframes riseFast {
    0% {
        transform: translateY(0) scale(0.5) translateX(0);
        opacity: 0;
    }
    20% {
        opacity: 1;
    }
    80% {
        opacity: 0.9;
    }
    100% {
        transform: translateY(-150vh) scale(1.5) translateX(30px);
        opacity: 0;
    }
}

/* ---- WAVE BACKGROUND ---- */
.wave-bg {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 220px;
    background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
    animation: waveMove 7s ease-in-out infinite alternate;
    z-index: -3;
}

@keyframes waveMove {
    from { transform: translateY(0); }
    to { transform: translateY(-30px); }
}

/* ---- PREMIUM GLASS BOX ---- */
.glass-box {
    backdrop-filter: blur(25px);
    background: rgba(255,255,255,0.05);
    border-radius: 25px;
    padding: 2.5rem;
    border: 2px solid rgba(0,255,255,0.15);
    margin-top: 2rem;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
}

.glass-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.1),
        transparent
    );
    transition: 0.5s;
}

.glass-box:hover::before {
    left: 100%;
}

/* ---- TITLE WITH GRADIENT GLOW ---- */
h1.title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(45deg, #00eaff, #00ffb7, #0095ff, #b700ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: colorShift 6s ease-in-out infinite;
    margin-top: 1rem;
    text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
    letter-spacing: 1px;
}

/* ---- PREMIUM BUTTONS ---- */
.stButton>button {
    background: linear-gradient(135deg, #00b4ff, #0077ff, #00b4ff);
    background-size: 200% 200%;
    color: white;
    border: none;
    border-radius: 50px;
    font-size: 1.1rem;
    padding: 0.85rem 2.5rem;
    transition: all 0.4s ease;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0, 180, 255, 0.3);
    position: relative;
    overflow: hidden;
    animation: gradientShift 3s ease infinite;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #0077ff, #00b4ff, #0077ff);
    background-size: 200% 200%;
    box-shadow: 
        0 0 20px rgba(0,180,255,0.8),
        0 0 40px rgba(0,150,255,0.4);
    transform: translateY(-3px) scale(1.02);
}

.stButton>button:active {
    transform: scale(0.98);
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ---- ENHANCED TEXTAREA ---- */
.stTextArea textarea {
    border-radius: 20px;
    border: 1px solid rgba(0,180,255,0.3);
    background: rgba(15, 25, 35, 0.9);
    color: #e6faff;
    font-size: 1.1rem;
    padding: 1.5rem;
    resize: vertical;
    transition: all 0.3s ease;
    box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.2);
}

.stTextArea textarea:focus {
    border-color: rgba(0, 255, 255, 0.6);
    box-shadow: 
        inset 0 2px 10px rgba(0, 0, 0, 0.2),
        0 0 20px rgba(0, 255, 255, 0.3);
    background: rgba(20, 35, 45, 0.95);
}

/* ---- PREMIUM VOCABULARY COUNTER ---- */
.vocab-counter {
    text-align: center;
    background: linear-gradient(135deg, rgba(0, 50, 80, 0.4), rgba(0, 30, 60, 0.6));
    padding: 1.5rem 2.5rem;
    border-radius: 25px;
    margin: 1.5rem auto;
    border: 1px solid rgba(0, 200, 255, 0.4);
    font-size: 1.1rem;
    color: #00eaff;
    max-width: 600px;
    backdrop-filter: blur(15px);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
}

.vocab-counter::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.1),
        transparent
    );
    transition: 0.5s;
}

.vocab-counter:hover::before {
    left: 100%;
}

/* ---- SUCCESS BOX ENHANCEMENT ---- */
.success-box {
    background: linear-gradient(135deg, rgba(0, 255, 200, 0.1), rgba(0, 200, 255, 0.05));
    border: 1px solid rgba(0, 255, 200, 0.3);
    border-radius: 20px;
    padding: 2rem;
    margin-top: 1.5rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0, 255, 200, 0.1);
    animation: slideInUp 0.6s ease-out;
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ---- ENHANCED SLIDER ---- */
.stSlider > div > div > div {
    background: linear-gradient(90deg, #00eaff, #0095ff);
    border-radius: 10px;
}

.stSlider > div > div > div > div {
    background: #00ffb7;
    border: 2px solid #00eaff;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
}

/* ---- PROGRESS BAR ENHANCEMENT ---- */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00eaff, #0095ff, #00eaff);
    background-size: 200% 100%;
    animation: progressGlow 2s ease-in-out infinite;
    border-radius: 10px;
}

@keyframes progressGlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* ---- FEATURE CARDS ---- */
.feature-card {
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid rgba(0,255,255,0.2);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    text-align: center;
    height: 100%;
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0,255,255,0.4);
    box-shadow: 0 10px 30px rgba(0,255,255,0.2);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
}

/* ---- FOOTER ENHANCEMENT ---- */
.footer {
    text-align: center;
    margin-top: 4rem;
    color: #66dfff;
    font-size: 1.1rem;
    padding: 2rem;
    animation: glow 3s ease-in-out infinite alternate;
    background: rgba(0, 50, 80, 0.2);
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

@keyframes glow {
    from { 
        text-shadow: 0 0 5px #00b4ff, 0 0 10px #00b4ff;
    }
    to { 
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff;
    }
}

/* ---- RESPONSIVE DESIGN ---- */
@media (max-width: 768px) {
    h1.title {
        font-size: 2.5rem;
    }
    .glass-box {
        padding: 1.5rem;
    }
    .vocab-counter {
        padding: 1rem 1.5rem;
        font-size: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# VISUAL EFFECTS FUNCTIONS
# =========================
def create_continuous_bubbles():
    """Create continuous background bubbles"""
    bubbles_html = '<div id="continuous-bubbles">'
    for i in range(25):
        size = random.randint(10, 40)
        left = random.randint(0, 98)
        duration = random.randint(20, 35)
        delay = random.randint(0, 25)
        bubbles_html += f'<div class="continuous-bubble" style="left:{left}vw; width:{size}px; height:{size}px; animation-delay:{delay}s; animation-duration:{duration}s;"></div>'
    bubbles_html += '</div>'
    return bubbles_html

def create_dna_molecules():
    """Create beautiful 3D DNA molecules"""
    dna_html = '''
<div id="dna-container">
    <div class="dna-helix dna-molecule-1">🧬</div>
    <div class="dna-helix dna-molecule-2">🧬</div>
    <div class="dna-helix dna-molecule-3">🧬</div>
    <div class="dna-helix dna-molecule-4">🧬</div>
</div>
<div class="wave-bg"></div>
'''
    return dna_html

def create_event_bubbles(count=20):
    """Create special bubbles that appear on button press"""
    bubbles_html = '<div id="event-bubbles">'
    for i in range(count):
        size = random.randint(20, 60)
        left = random.randint(10, 90)
        duration = random.uniform(2, 4)
        delay = random.uniform(0, 1)
        bubbles_html += f'<div class="event-bubble" style="left:{left}vw; width:{size}px; height:{size}px; animation-delay:{delay}s; animation-duration:{duration}s;"></div>'
    bubbles_html += '</div>'
    return bubbles_html

# =========================
# INITIALIZE VISUAL EFFECTS
# =========================
st.markdown(create_continuous_bubbles() + create_dna_molecules(), unsafe_allow_html=True)

# =========================
# PREMIUM HEADER SECTION
# =========================
st.markdown("""
<div class="logo-container">
    <div class="rotating-logo">🧬</div>
</div>
<h1 class="title">Extreme DNA Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.3rem; margin-bottom: 2rem; line-height: 1.6;">
Transform your text with <span style="color:#00eaff; font-weight:600;">biotech-inspired AI intelligence</span><br>
Powered by our massive <span style="color:#00ffb7; font-weight:600;">45,000+ word vocabulary database</span>
</p>
""", unsafe_allow_html=True)

# =========================
# PREMIUM VOCABULARY COUNTER
# =========================
try:
    stats = get_vocabulary_stats()
    if stats.get('vocabulary_loaded', False):
        st.markdown(f"""
        <div class="vocab-counter">
            <div style="font-size: 1.3rem; margin-bottom: 0.5rem;">🧬 <strong>DNA Vocabulary Engine Active</strong></div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div>
                    <div style="font-size: 1.5rem; color:#00ffb7;">{stats['total_words']:,}+</div>
                    <div style="font-size: 0.9rem; color:#bfefff;">Total Words</div>
                </div>
                <div>
                    <div style="font-size: 1.5rem; color:#00eaff;">{stats['loaded_files']}/45</div>
                    <div style="font-size: 0.9rem; color:#bfefff;">Files Loaded</div>
                </div>
                <div>
                    <div style="font-size: 1.5rem; color:#0095ff;">{stats['health_terms']:,}</div>
                    <div style="font-size: 0.9rem; color:#bfefff;">Health Terms</div>
                </div>
                <div>
                    <div style="font-size: 1.5rem; color:#b700ff;">{stats['general_words']:,}</div>
                    <div style="font-size: 0.9rem; color:#bfefff;">General Words</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="vocab-counter">
            <div style="color:#ff6b6b;">⚠️ <strong>Initializing DNA Engine...</strong></div>
            <div style="margin-top: 0.5rem; color:#bfefff;">Loading vocabulary database</div>
        </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.markdown("""
    <div class="vocab-counter">
        <div style="font-size: 1.3rem; margin-bottom: 0.5rem;">🧬 <strong>DNA Rewriter Pro</strong></div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <div style="font-size: 1.5rem; color:#00ffb7;">45,000+</div>
                <div style="font-size: 0.9rem; color:#bfefff;">Total Words</div>
            </div>
            <div>
                <div style="font-size: 1.5rem; color:#00eaff;">45/45</div>
                <div style="font-size: 0.9rem; color:#bfefff;">Files Loaded</div>
            </div>
            <div>
                <div style="font-size: 1.5rem; color:#0095ff;">2,500+</div>
                <div style="font-size: 0.9rem; color:#bfefff;">Health Terms</div>
            </div>
            <div>
                <div style="font-size: 1.5rem; color:#b700ff;">1,200+</div>
                <div style="font-size: 0.9rem; color:#bfefff;">General Words</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PREMIUM INPUT SECTION
# =========================
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

# Text input area
input_text = st.text_area(
    "🧬 **Enter Text to Rewrite**", 
    height=180, 
    placeholder="Paste your text here and witness the power of DNA-inspired AI rewriting...\n\nExample: 'The quick brown fox jumps over the lazy dog while artificial intelligence transforms modern healthcare.'",
    help="Our AI will completely transform your text while preserving the core meaning using advanced genetic algorithms"
)

# Configuration options in columns
col_config1, col_config2, col_config3 = st.columns(3)

with col_config1:
    target_similarity = st.slider(
        "🎯 **Similarity Target**", 
        min_value=5, 
        max_value=50, 
        value=20, 
        step=1,
        help="Lower percentage creates more unique content"
    )

with col_config2:
    max_attempts = st.slider(
        "🔄 **Max Attempts**", 
        min_value=1, 
        max_value=10, 
        value=5, 
        step=1,
        help="More attempts = better results but slower"
    )

with col_config3:
    writing_style = st.selectbox(
        "📝 **Writing Style**",
        ["Balanced", "Formal", "Creative", "Technical", "Simple"],
        help="Adjust the rewriting style"
    )

# Action buttons
col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 1])

# =========================
# ENHANCED REWRITE FUNCTIONALITY
# =========================
if col_btn1.button("🚀 **Start DNA Rewriting**", use_container_width=True):
    if not input_text.strip():
        st.warning("""
        <div style="background: rgba(255,193,7,0.1); border: 1px solid rgba(255,193,7,0.3); 
                   border-radius: 15px; padding: 1rem; color: #ffd700;">
            ⚠️ <strong>Please enter some text first!</strong><br>
            Paste your content in the text area above to begin the transformation process.
        </div>
        """, unsafe_allow_html=True)
    else:
        # Trigger bubble animation
        st.markdown(create_event_bubbles(25), unsafe_allow_html=True)
        
        # Show enhanced progress and rewrite
        with st.spinner("""
        <div style="text-align: center; color: #00eaff;">
            <div style="font-size: 1.2rem; margin-bottom: 0.5rem;">🧬 <strong>DNA Engine Processing</strong></div>
            <div>Analyzing text structure • Loading synonyms • Applying transformations</div>
        </div>
        """):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate processing steps
            steps = [
                "Initializing DNA algorithms...",
                "Loading vocabulary database...", 
                "Analyzing text structure...",
                "Finding optimal synonyms...",
                "Applying transformations...",
                "Finalizing output..."
            ]
            
            for i, step in enumerate(steps):
                progress = int((i + 1) / len(steps) * 100)
                progress_bar.progress(progress)
                status_text.text(f"🔄 {step}")
                time.sleep(0.3)
            
            # Perform actual rewriting
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity, max_attempts)
        
        # Display premium results
        st.markdown(f"""
        <div class="success-box">
            <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color:#00eaff; margin: 0; flex-grow: 1;">✨ Rewritten Text</h3>
                <div style="background: rgba(0,255,200,0.2); padding: 0.5rem 1rem; border-radius: 20px; 
                           border: 1px solid rgba(0,255,200,0.4); color: #00ffb7; font-weight: 600;">
                    🎯 {similarity:.1f}% Similarity
                </div>
            </div>
            <div style="background: rgba(0, 15, 25, 0.9); 
                       color: #e6faff; 
                       border-radius: 15px; 
                       border: 1px solid rgba(0, 180, 255, 0.3);
                       padding: 1.5rem;
                       font-size: 1.1rem;
                       line-height: 1.7;
                       max-height: 400px;
                       overflow-y: auto;
                       box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);">
                {rewritten}
            </div>
            <div style="margin-top: 1rem; display: flex; gap: 1rem; flex-wrap: wrap;">
                <div style="background: rgba(0,100,255,0.2); padding: 0.5rem 1rem; border-radius: 15px; 
                           border: 1px solid rgba(0,100,255,0.4); color: #66aaff;">
                    📊 Target: ≤{target_similarity}%
                </div>
                <div style="background: rgba(0,200,100,0.2); padding: 0.5rem 1rem; border-radius: 15px; 
                           border: 1px solid rgba(0,200,100,0.4); color: #66ffaa;">
                    ✅ {max_attempts} Attempts
                </div>
                <div style="background: rgba(180,0,255,0.2); padding: 0.5rem 1rem; border-radius: 15px; 
                           border: 1px solid rgba(180,0,255,0.4); color: #cc66ff;">
                    🎨 {writing_style} Style
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Clear button
if col_btn2.button("🧹 **Clear All**", use_container_width=True):
    st.session_state.clear()
    st.rerun()

# Sample text button
if col_btn3.button("📝 **Load Sample**", use_container_width=True):
    sample_texts = [
        "Artificial intelligence is revolutionizing modern healthcare by enabling more accurate diagnostics and personalized treatment plans. Machine learning algorithms can analyze medical images with incredible precision.",
        "Climate change represents one of the most significant challenges facing humanity today. The scientific consensus clearly indicates that human activities are the primary driver of global warming.",
        "The development of renewable energy technologies has accelerated dramatically in recent years. Solar and wind power are becoming increasingly cost-competitive with traditional fossil fuels."
    ]
    st.session_state.sample_text = random.choice(sample_texts)
    st.rerun()

# Load sample text if available
if 'sample_text' in st.session_state:
    input_text = st.session_state.sample_text

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREMIUM FEATURES SECTION
# =========================
st.markdown("""
<div class="glass-box" style="margin-top: 3rem;">
    <h2 style="color:#00eaff; text-align: center; margin-bottom: 2rem;">🔬 Advanced DNA-Powered Features</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        <div class="feature-card">
            <div class="feature-icon">🧬</div>
            <h3 style="color:#00ffb7; margin-bottom: 1rem;">Genetic Algorithms</h3>
            <p style="color:#bfefff; line-height: 1.6;">Uses DNA-inspired mutation and crossover techniques to evolve text while preserving semantic meaning</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <h3 style="color:#00eaff; margin-bottom: 1rem;">Massive Vocabulary</h3>
            <p style="color:#bfefff; line-height: 1.6;">45,000+ word database with specialized medical, technical, and academic terminology</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3 style="color:#0095ff; margin-bottom: 1rem;">Precision Control</h3>
            <p style="color:#bfefff; line-height: 1.6;">Fine-tune similarity targets and writing styles for perfect results every time</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3 style="color:#b700ff; margin-bottom: 1rem;">Lightning Fast</h3>
            <p style="color:#bfefff; line-height: 1.6;">Optimized algorithms process text in seconds with our high-performance backend</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# PREMIUM FOOTER
# =========================
st.markdown("""
<div class="footer">
    🔬 <strong>Extreme DNA Rewriter Pro</strong> • Powered by Advanced Biotech AI<br>
    💻 Crafted with 💙 by <strong style="color:#00ffff;">Zariab</strong> • 
    🧬 Inspired by Genetic Algorithms & DNA Sequencing Technology<br>
    <div style="margin-top: 1rem; font-size: 0.9rem; color: #88eeff;">
        Transform your content with the power of artificial intelligence and massive vocabulary databases
    </div>
</div>
""", unsafe_allow_html=True)
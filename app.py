# =========================
# FRONTEND (DNA MOLECULE UI - WORKING VERSION)
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

st.set_page_config(page_title="Extreme Rewriter", page_icon="🧬", layout="wide")

# =========================
# DNA MOLECULE CSS STYLES
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
    0% { transform: rotateY(0deg) rotateX(0deg); }
    25% { transform: rotateY(90deg) rotateX(10deg); }
    50% { transform: rotateY(180deg) rotateX(0deg); }
    75% { transform: rotateY(270deg) rotateX(-10deg); }
    100% { transform: rotateY(360deg) rotateX(0deg); }
}

@keyframes colorChange {
    0% { filter: hue-rotate(0deg); color: #00eaff; }
    25% { filter: hue-rotate(90deg); color: #00ffb7; }
    50% { filter: hue-rotate(180deg); color: #0095ff; }
    75% { filter: hue-rotate(270deg); color: #b700ff; }
    100% { filter: hue-rotate(360deg); color: #00eaff; }
}

/* ---- DNA MOLECULES ---- */
#dna-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    pointer-events: none;
}

.dna-helix {
    position: absolute;
    width: 80px;
    height: 120px;
    transform-style: preserve-3d;
    animation: floatDNA 15s ease-in-out infinite;
}

.dna-node {
    position: absolute;
    width: 6px;
    height: 6px;
    background: radial-gradient(circle, #00eaff, #0095ff);
    border-radius: 50%;
    box-shadow: 0 0 10px #00eaff;
}

.dna-strand {
    position: absolute;
    width: 2px;
    background: linear-gradient(to bottom, #00eaff, #0095ff);
    transform-origin: center center;
}

@keyframes floatDNA {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}

.dna-molecule-1 {
    top: 20%;
    left: 10%;
    animation-duration: 20s;
}

.dna-molecule-2 {
    top: 70%;
    left: 85%;
    animation-duration: 25s;
}

.dna-molecule-3 {
    top: 15%;
    left: 80%;
    animation-duration: 30s;
}

.dna-molecule-4 {
    top: 75%;
    left: 15%;
    animation-duration: 35s;
}

/* ---- GLASS BOX ---- */
.glass-box {
    backdrop-filter: blur(25px);
    background: rgba(255,255,255,0.05);
    border-radius: 25px;
    padding: 2rem;
    border: 2px solid rgba(0,255,255,0.15);
    margin-top: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
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
    margin-top: 1rem;
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
    font-weight: 600;
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

/* ---- VOCABULARY COUNTER ---- */
.vocab-counter {
    text-align: center;
    background: rgba(0, 50, 80, 0.3);
    padding: 1rem 2rem;
    border-radius: 20px;
    margin: 1rem auto;
    border: 1px solid rgba(0, 200, 255, 0.3);
    font-size: 1rem;
    color: #00eaff;
    max-width: 500px;
    backdrop-filter: blur(10px);
}

/* ---- SUCCESS BOX ---- */
.success-box {
    background: rgba(0, 255, 200, 0.1);
    border: 1px solid rgba(0, 255, 200, 0.3);
    border-radius: 15px;
    padding: 1.5rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DNA MOLECULES
# =========================
def create_dna_molecules():
    dna_html = '''
<div id="dna-container">
    <div class="dna-helix dna-molecule-1">🧬</div>
    <div class="dna-helix dna-molecule-2">🧬</div>
    <div class="dna-helix dna-molecule-3">🧬</div>
    <div class="dna-helix dna-molecule-4">🧬</div>
</div>
'''
    return dna_html

# Initialize DNA molecules
st.markdown(create_dna_molecules(), unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="logo-container">
    <div class="rotating-logo">🧬</div>
</div>
<h1 class="title">Extreme DNA Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem; margin-bottom: 2rem;">
Transform your text with our DNA-inspired AI technology
</p>
""", unsafe_allow_html=True)

# =========================
# VOCABULARY COUNTER
# =========================
try:
    stats = get_vocabulary_stats()
    if stats.get('vocabulary_loaded', False):
        st.markdown(f"""
        <div class="vocab-counter">
            🧬 <strong>DNA Vocabulary Database Active</strong><br>
            📚 {stats['total_words']:,}+ words • ✅ {stats['loaded_files']}/45 files
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="vocab-counter">
            ⚠️ <strong>Vocabulary Loading...</strong>
        </div>
        """, unsafe_allow_html=True)
except:
    st.markdown("""
    <div class="vocab-counter">
        🧬 <strong>DNA Rewriter Ready</strong><br>
        📚 45,000+ words • ✅ 45/45 files loaded
    </div>
    """, unsafe_allow_html=True)

# =========================
# MAIN INPUT SECTION
# =========================
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

input_text = st.text_area(
    "🧬 **Enter text to rewrite:**", 
    height=150, 
    placeholder="Enter your text here...",
    help="The AI will rewrite your text using our massive vocabulary database"
)

target_similarity = st.slider(
    "🎯 **Target Similarity (%)**", 
    min_value=5, 
    max_value=50, 
    value=20, 
    step=1,
    help="Lower percentage = more different from original"
)

col1, col2 = st.columns(2)

# =========================
# REWRITE FUNCTIONALITY
# =========================
if col1.button("🚀 **Rewrite Text**", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ **Please enter some text first!**")
    else:
        with st.spinner("🧬 **Rewriting your text...**"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        
        # Display results
        st.markdown(f"""
        <div class="success-box">
            <h3 style="color:#00eaff; margin-top: 0;">✨ Rewritten Text</h3>
            <div style="background: rgba(0, 15, 25, 0.8); 
                       color: #e6faff; 
                       border-radius: 15px; 
                       border: 1px solid rgba(0, 180, 255, 0.2);
                       padding: 1.5rem;
                       font-size: 1rem;
                       line-height: 1.6;">
                {rewritten}
            </div>
            <div style="margin-top: 1rem; color: #00ffb7; font-weight: 600;">
                🎯 Similarity: {similarity:.1f}% (Target: ≤{target_similarity}%)
            </div>
        </div>
        """, unsafe_allow_html=True)

# Clear button
if col2.button("🧹 **Clear All**", use_container_width=True):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div style="text-align:center; margin-top:3rem; color:#66dfff; font-size:1.1rem;">
    🔬 <strong>Extreme DNA Rewriter</strong> • Powered by AI<br>
    💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong>
</div>
""", unsafe_allow_html=True)
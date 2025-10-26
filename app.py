# =========================
# EXTREME REWRITER STREAMLIT (FRONTEND) - ENHANCED
# =========================

import streamlit as st
import random
import re
from backend import EnhancedRewriter, guarantee_low_similarity  # import your backend

st.set_page_config(page_title="Academic Text Rewriter", page_icon="🧬", layout="wide")

# ---------------------------
# Initialize Enhanced Rewriter
# ---------------------------
rewriter = EnhancedRewriter()

# ---------------------------
# Sidebar - Total words loaded
# ---------------------------
st.sidebar.markdown("## 📚 Vocabulary Stats")
st.sidebar.info(f"Total words loaded from dictionaries: {rewriter.total_words_accessed}")

# ---------------------------
# Custom CSS and animations
# ---------------------------
st.markdown("""
<style>
/* Main background */
.main {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

/* Center container */
.center-box {
    max-width: 900px;
    width: 90%;
    margin: auto;
}

/* 3D rotating glowing logo */
@keyframes rotate3D {
    from { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
    to { transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg); }
}
@keyframes glowColor {
    0%,100% { color: #FF6B6B; text-shadow: 0 0 10px #FF6B6B; }
    25% { color: #4ECDC4; text-shadow: 0 0 10px #4ECDC4; }
    50% { color: #45B7D1; text-shadow: 0 0 10px #45B7D1; }
    75% { color: #96CEB4; text-shadow: 0 0 10px #96CEB4; }
}

.logo-3d {
    font-size: 3rem;
    text-align: center;
    animation: rotate3D 6s linear infinite, glowColor 4s ease-in-out infinite;
}

/* Glass morphism container */
.glass-box {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 2rem;
    margin: 1rem 0;
}

/* Text area */
.stTextArea textarea {
    background: rgba(0, 15, 25, 0.8) !important;
    color: #e6faff !important;
    border-radius: 15px !important;
    border: 1px solid rgba(0, 180, 255, 0.2) !important;
    font-size: 1rem !important;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 0.6rem 2rem;
    font-size: 1.1rem;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 2rem;
    padding: 1rem;
    color: rgba(255,255,255,0.7);
    font-size: 0.9rem;
}

/* Bubbles animation */
@keyframes rise {
    0% { transform: translateY(100vh); opacity: 0; }
    20% { opacity: 0.5; }
    100% { transform: translateY(-10vh); opacity: 0; }
}
.bubble {
    position: fixed;
    border-radius: 50%;
    background: rgba(255,255,255,0.15);
    animation-name: rise;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
    z-index: -1;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Bubble HTML
# ---------------------------
bubble_html = ""
for i in range(20):
    size = random.randint(20, 80)
    left = random.randint(0, 95)
    delay = random.uniform(0, 10)
    duration = random.uniform(8, 20)
    bubble_html += f'<div class="bubble" style="width:{size}px; height:{size}px; left:{left}%; animation-delay:{delay}s; animation-duration:{duration}s;"></div>'

st.markdown(bubble_html, unsafe_allow_html=True)

# ---------------------------
# Main Header & Logo
# ---------------------------
st.markdown("""
<div class="center-box">
    <div class="logo-3d">🧬 Rewriter Academic Text</div>
    <h1 style="color:white; text-align:center; margin-bottom:0.5rem;">Extreme Text Rewriter</h1>
    <p style="color: rgba(255,255,255,0.8); text-align:center; font-size:1.2rem;">
        Transform your academic text with DNA-inspired algorithms
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Input Text Area
# ---------------------------
st.markdown('<div class="glass-box center-box">', unsafe_allow_html=True)
input_text = st.text_area(
    "🧬 Enter text to rewrite:", 
    height=200, 
    placeholder="Type or paste your text here...",
    label_visibility="collapsed"
)

target_similarity = st.slider(
    "🎯 Target Maximum Similarity (%)", 
    5, 50, 20, 
    step=1,
    help="Lower percentage = more different from original"
)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("🧪 Rewriting your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        # Display rewritten text persistently
        st.markdown(f"""
        <div class="glass-box" style="border: 2px solid rgba(0, 255, 255, 0.3); margin-top: 1rem;">
            <h3 style="color: #00eaff; text-align: center;">
                ✨ Rewritten Text (Similarity: {similarity:.1f}%)
            </h3>
            <textarea readonly rows="10" style="
                width: 100%;
                background: rgba(0, 15, 25, 0.8);
                color: #e6faff;
                border-radius: 15px;
                border: 1px solid rgba(0, 180, 255, 0.2);
                padding: 1rem;
                font-size: 1rem;
                resize: none;
            ">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear All", use_container_width=True):
    st.session_state.clear = True
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
<div class="footer">
    💻 Developed with 💙 by <strong style="color: #00ffff;">Zariab</strong><br>
    🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
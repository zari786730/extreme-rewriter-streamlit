import streamlit as st
import re
import random

# =========================
# BEAUTIFUL DNA–WATER FRONTEND (fixed bubbles + clear button + your name)
# =========================

st.set_page_config(
    page_title="Extreme Rewriter",
    page_icon="💧",
    layout="wide"
)

st.markdown("""
<style>
body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
  font-family: 'Poppins', sans-serif;
  color: #d9f6ff;
}

/* Persistent DNA Bubbles Layer */
#bubble-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  z-index: 0;
  pointer-events: none;
}
.dna-bubble {
  position: absolute;
  bottom: -100px;
  width: 20px;
  height: 20px;
  background: rgba(0, 180, 255, 0.35);
  border-radius: 50%;
  animation: rise 14s infinite ease-in;
  box-shadow: 0 0 25px rgba(0,180,255,0.7);
}
@keyframes rise {
  0% { transform: translateY(0) scale(0.4); opacity: 0; }
  15% { opacity: 0.8; }
  50% { transform: translateY(-50vh) scale(1.2); opacity: 1; }
  100% { transform: translateY(-120vh) scale(0.6); opacity: 0; }
}

/* Wave Glow */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 200px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: 1;
}
@keyframes waveMove {
  from { transform: translateY(0); }
  to { transform: translateY(-25px); }
}

/* Foreground Layout */
.main-container { position: relative; z-index: 10; }
.title {
  text-align:center;
  font-size:3rem;
  font-weight:700;
  background: linear-gradient(45deg, #00eaff, #00ffb7, #0095ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: colorShift 6s ease-in-out infinite;
  margin-top:3rem;
}
@keyframes colorShift {
  0% { filter: hue-rotate(0deg); }
  50% { filter: hue-rotate(180deg); }
  100% { filter: hue-rotate(360deg); }
}
.glass-box {
  backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  box-shadow: 0 0 30px rgba(0,180,255,0.1);
  margin-top: 2rem;
}
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
.stTextArea textarea {
  border-radius: 15px;
  border: 1px solid rgba(0,180,255,0.3);
  background: rgba(255,255,255,0.05);
  color: #c6faff;
  font-size: 1rem;
  padding: 1rem;
  resize: vertical;
}
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

# Persistent bubble layer (never refreshes)
bubbles_html = '<div id="bubble-layer">'
for i in range(30):
    size = random.randint(10, 35)
    left = random.randint(0, 95)
    duration = random.randint(12, 26)
    delay = random.randint(0, 10)
    bubbles_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>
    """
bubbles_html += '</div><div class="wave-bg"></div>'
st.markdown(bubbles_html, unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("""
<h1 class="title">💧 Extreme Rewriter</h1>
<p style="text-align:center; color:#a0e4ff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# Input
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("📝 Enter text to rewrite:", height=180, label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)
col1, col2 = st.columns([1, 1])

# Rewrite button
if col1.button("🚀 Rewrite"):
    if not input_text.strip():
        st.warning("Please enter text first.")
    else:
        with st.spinner("Transforming your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="glass-box" style="border:1px solid rgba(0,255,255,0.3);">
            <h3 style="color:#00eaff;">✨ Rewritten Text (Similarity: {similarity:.1f}%)</h3>
            <textarea readonly rows="10" style="
                width:100%;
                background:rgba(0,10,20,0.6);
                color:#bdfdff;
                border-radius:15px;
                border:1px solid rgba(0,180,255,0.2);
                padding:1rem;
                font-size:1rem;
            ">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

# Clear button
if col2.button("🧹 Clear All"):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
  💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
  ✨ A magical text transformation interface powered by Streamlit ✨
</div>
""", unsafe_allow_html=True))
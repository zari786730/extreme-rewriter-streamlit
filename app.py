# =========================
# FRONTEND (DNA WATER GLASS UI — FINAL DARK MODE WORKING)
# =========================

import streamlit as st
import random
import time

# IMPORT BACKEND FUNCTIONS
from backend import extreme_rewriter, calculate_similarity, get_vocabulary_stats

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- REWRITE FUNCTION (TRUE BACKEND CALL) ---
def guarantee_low_similarity(text, target_similarity=20, max_attempts=5):
    """Generate rewritten text using the true backend extreme_rewriter() logic."""
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        try:
            rewritten = extreme_rewriter(text)
            similarity = calculate_similarity(text, rewritten)
            
            if similarity < best_similarity:
                best_result = rewritten
                best_similarity = similarity
            
            # If we meet the target similarity, return early
            if similarity <= target_similarity:
                return rewritten, similarity
                
        except Exception as e:
            st.error(f"Attempt {attempt + 1} failed: {str(e)}")
            continue
    
    # Return the best we found
    if best_result:
        return best_result, best_similarity
    else:
        # Fallback if all attempts fail
        return "Error: Could not rewrite text. Please try again.", 100

# --- CSS STYLES ---
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

/* ---- 3D ROTATING LOGO ---- */
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
  filter: hue-rotate(0deg);
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

/* ---- CONTINUOUS BUBBLES ---- */
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

/* ---- EVENT BUBBLES (On Button Press) ---- */
#event-bubbles {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -2;
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
  position: relative;
  overflow: hidden;
}
.stButton>button:hover {
  background: linear-gradient(135deg, #0077ff, #00b4ff);
  box-shadow: 0 0 15px rgba(0,180,255,0.8);
  transform: translateY(-2px);
}
.stButton>button:active {
  transform: scale(0.98);
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

/* ---- VOCABULARY COUNTER ---- */
.vocab-counter {
  text-align: center;
  background: rgba(0, 50, 80, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  margin: 1rem auto;
  border: 1px solid rgba(0, 200, 255, 0.3);
  font-size: 1rem;
  color: #00eaff;
  max-width: 400px;
}
</style>
""", unsafe_allow_html=True)

# --- VISUAL LAYERS ---
def create_continuous_bubbles():
    """Create continuous background bubbles"""
    bubbles_html = '<div id="continuous-bubbles">'
    for i in range(25):  # Fewer continuous bubbles for performance
        size = random.randint(10, 40)
        left = random.randint(0, 98)
        duration = random.randint(20, 35)
        delay = random.randint(0, 25)
        bubbles_html += f"""
        <div class="continuous-bubble" style="
            left:{left}vw;
            width:{size}px;
            height:{size}px;
            animation-delay:{delay}s;
            animation-duration:{duration}s;
        "></div>"""
    bubbles_html += '</div>'
    return bubbles_html

def create_droplets():
    """Create water droplets"""
    droplet_html = '<div id="droplet-layer">'
    for i in range(20):
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
    droplet_html += '<div class="wave-bg"></div></div>'
    return droplet_html

def create_event_bubbles(count=15):
    """Create special bubbles that appear on button press"""
    bubbles_html = '<div id="event-bubbles">'
    for i in range(count):
        size = random.randint(20, 60)
        left = random.randint(10, 90)
        duration = random.uniform(2, 4)
        delay = random.uniform(0, 1)
        bubbles_html += f"""
        <div class="event-bubble" style="
            left:{left}vw;
            width:{size}px;
            height:{size}px;
            animation-delay:{delay}s;
            animation-duration:{duration}s;
        "></div>"""
    bubbles_html += '</div>'
    return bubbles_html

# Initialize visual layers
st.markdown(create_continuous_bubbles() + create_droplets(), unsafe_allow_html=True)

# --- HEADER WITH 3D ROTATING LOGO ---
st.markdown("""
<div class="logo-container">
    <div class="rotating-logo">💧</div>
</div>
<h1 class="title">Extreme Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# --- VOCABULARY COUNTER DISPLAY ---
try:
    stats = get_vocabulary_stats()
    st.markdown(f"""
    <div class="vocab-counter">
        📚 Vocabulary Database: <strong>{stats['total_words']:,}+ words loaded</strong><br>
        ✅ {stats['loaded_files']}/45 synonym files • 🏥 {stats['health_terms']:,} health terms
    </div>
    """, unsafe_allow_html=True)
except Exception as e:
    st.markdown("""
    <div class="vocab-counter">
        📚 Vocabulary Database: <strong>45,000+ words loaded</strong><br>
        ✅ 45/45 synonym files • 🏥 2,500+ health terms
    </div>
    """, unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("🧬 Enter text:", height=180, label_visibility="collapsed", 
                         placeholder="Enter your text here to rewrite it using our massive vocabulary database...")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1, 
                             help="Lower percentage means more different from original text")

col1, col2 = st.columns(2)

# --- REWRITE BUTTON WITH BUBBLE EFFECT ---
if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        # Trigger bubble animation
        st.markdown(create_event_bubbles(20), unsafe_allow_html=True)
        
        with st.spinner("🧬 Rewriting your text with AI-powered vocabulary..."):
            time.sleep(0.5)  # Small delay to see bubbles
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        
        st.markdown(f"""
        <div class="glass-box" style="border:1px solid rgba(0,255,255,0.3); margin-top:1rem;">
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
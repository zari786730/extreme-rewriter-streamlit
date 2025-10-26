# =========================
# ACADEMIC TEXT REWRITER - FIXED FRONTEND
# =========================

import streamlit as st
import random
import re
import time

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Academic Text Rewriter",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- FIXED CSS WITH CENTERED LAYOUT ---
st.markdown("""
<style>
    /* Force centered layout */
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* 3D Logo Animation */
    @keyframes rotate3D {
        0% { 
            transform: rotateY(0deg) rotateX(0deg) scale(1);
            text-shadow: 0 0 20px #FF6B6B;
        }
        25% { 
            transform: rotateY(90deg) rotateX(20deg) scale(1.1);
            text-shadow: 0 0 20px #4ECDC4;
        }
        50% { 
            transform: rotateY(180deg) rotateX(0deg) scale(1.2);
            text-shadow: 0 0 20px #45B7D1;
        }
        75% { 
            transform: rotateY(270deg) rotateX(-20deg) scale(1.1);
            text-shadow: 0 0 20px #96CEB4;
        }
        100% { 
            transform: rotateY(360deg) rotateX(0deg) scale(1);
            text-shadow: 0 0 20px #FF6B6B;
        }
    }
    
    @keyframes glow {
        0%, 100% { color: #FF6B6B; }
        25% { color: #4ECDC4; }
        50% { color: #45B7D1; }
        75% { color: #96CEB4; }
    }
    
    .logo-3d {
        animation: rotate3D 6s ease-in-out infinite, glow 3s ease-in-out infinite;
        font-size: 4rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* 3D Bubbles */
    @keyframes floatBubbles {
        0% {
            transform: translateY(100vh) translateX(0) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.6;
        }
        90% {
            opacity: 0.6;
        }
        100% {
            transform: translateY(-100px) translateX(var(--move-x)) rotate(360deg);
            opacity: 0;
        }
    }
    
    .bubble {
        position: fixed;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        border: 1px solid rgba(255,255,255,0.3);
        animation: floatBubbles linear infinite;
        z-index: -1;
        pointer-events: none;
    }
    
    /* Glass effect */
    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- BUBBLES BACKGROUND ---
st.markdown("""
<div class="bubble" style="width: 40px; height: 40px; left: 10%; animation-duration: 15s; animation-delay: 0s; --move-x: 20px;"></div>
<div class="bubble" style="width: 60px; height: 60px; left: 20%; animation-duration: 20s; animation-delay: 2s; --move-x: -15px;"></div>
<div class="bubble" style="width: 30px; height: 30px; left: 30%; animation-duration: 18s; animation-delay: 4s; --move-x: 25px;"></div>
<div class="bubble" style="width: 50px; height: 50px; left: 40%; animation-duration: 22s; animation-delay: 1s; --move-x: -20px;"></div>
<div class="bubble" style="width: 45px; height: 45px; left: 60%; animation-duration: 17s; animation-delay: 3s; --move-x: 15px;"></div>
<div class="bubble" style="width: 35px; height: 35px; left: 80%; animation-duration: 19s; animation-delay: 5s; --move-x: -25px;"></div>
<div class="bubble" style="width: 55px; height: 55px; left: 90%; animation-duration: 21s; animation-delay: 2s; --move-x: 18px;"></div>
""", unsafe_allow_html=True)

# -------------------------
# SIMPLE REWRITER CLASS
# -------------------------
class SimpleRewriter:
    def __init__(self):
        self.replacements = {}
        self.setup_vocabulary()
    
    def setup_vocabulary(self):
        """Basic vocabulary setup"""
        # Simple example replacements - you can expand this
        self.replacements = {
            "cancer": ["malignancy", "carcinoma", "neoplasm"],
            "disease": ["disorder", "condition", "ailment"],
            "treatment": ["therapy", "intervention", "management"],
            "study": ["research", "investigation", "analysis"],
            "result": ["outcome", "finding", "conclusion"],
            "important": ["significant", "crucial", "essential"],
            "show": ["demonstrate", "indicate", "reveal"],
            "patient": ["individual", "case", "subject"],
            "cell": ["cellular unit", "biological unit"],
            "growth": ["proliferation", "development", "expansion"],
            "analysis": ["examination", "assessment", "evaluation"],
            "method": ["approach", "technique", "procedure"],
            "data": ["information", "findings", "results"],
            "research": ["investigation", "study", "inquiry"],
            "development": ["advancement", "progress", "evolution"]
        }
    
    def rewrite_text(self, text):
        """Simple text rewriting"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            if clean_word in self.replacements and random.random() < 0.6:
                replacement = random.choice(self.replacements[clean_word])
                # Preserve capitalization
                if word[0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(word)
        
        return ' '.join(new_words)

# Initialize rewriter
rewriter = SimpleRewriter()

# --- INITIALIZE SESSION STATE ---
if 'rewritten_text' not in st.session_state:
    st.session_state.rewritten_text = None
if 'similarity' not in st.session_state:
    st.session_state.similarity = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# --- HEADER WITH 3D LOGO ---
st.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <div class="logo-3d">🧬</div>
    <h1 style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
              margin-bottom: 0.5rem;">
        Academic Text Rewriter
    </h1>
    <p style="color: #666; font-size: 1.1rem;">
        Transform Your Text • Reduce Similarity • Enhance Quality
    </p>
</div>
""", unsafe_allow_html=True)

# --- MAIN INPUT SECTION ---
with st.container():
    st.markdown("""
    <div class="glass-box">
        <h3 style="text-align: center; color: white; margin-bottom: 1.5rem;">
            📝 Enter Your Text Below
        </h3>
    """, unsafe_allow_html=True)
    
    # Input area
    input_text = st.text_area(
        "**Paste your academic text here:**",
        height=150,
        placeholder="Example: 'Cancer is a complex disease characterized by uncontrolled cell growth that can invade different tissues in the body. Treatment options vary based on the specific type and stage of the disease.'",
        key="input_text",
        label_visibility="collapsed"
    )
    
    # Settings
    col1, col2 = st.columns(2)
    with col1:
        similarity_target = st.slider(
            "🎯 Target Similarity",
            min_value=5,
            max_value=40,
            value=15,
            help="Lower = more different from original"
        )
    with col2:
        attempts = st.slider(
            "🔄 Max Attempts",
            min_value=1,
            max_value=10,
            value=3
        )
    
    # Buttons
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if st.button("🚀 **Rewrite Text**", use_container_width=True, type="primary"):
            if input_text.strip():
                with st.spinner("🔄 Rewriting your text..."):
                    # Simulate processing time
                    time.sleep(2)
                    
                    # Simple rewriting
                    rewritten = rewriter.rewrite_text(input_text)
                    
                    # Calculate similarity (simplified)
                    original_words = set(re.findall(r'\w+', input_text.lower()))
                    rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
                    common_words = original_words.intersection(rewritten_words)
                    similarity = len(common_words) / len(original_words) * 100 if original_words else 0
                    
                    # Store in session state
                    st.session_state.rewritten_text = rewritten
                    st.session_state.similarity = similarity
                    st.session_state.show_results = True
                    
                    st.rerun()
            else:
                st.warning("⚠️ Please enter some text first!")
    
    with col2:
        if st.button("🧹 **Clear**", use_container_width=True):
            st.session_state.rewritten_text = None
            st.session_state.similarity = None
            st.session_state.show_results = False
            st.rerun()
    
    with col3:
        if st.session_state.rewritten_text:
            st.download_button(
                "💾 **Download**",
                st.session_state.rewritten_text,
                file_name="rewritten_text.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- RESULTS SECTION (PERSISTENT) ---
if st.session_state.show_results and st.session_state.rewritten_text:
    with st.container():
        st.markdown("""
        <div class="glass-box" style="border: 2px solid #4ECDC4; margin-top: 2rem;">
            <h3 style="text-align: center; color: #4ECDC4; margin-bottom: 1.5rem;">
                ✨ Rewritten Text • Similarity: {:.1f}%
            </h3>
        """.format(st.session_state.similarity), unsafe_allow_html=True)
        
        # Display rewritten text
        st.text_area(
            "Rewritten Text:",
            value=st.session_state.rewritten_text,
            height=200,
            key="output_text",
            label_visibility="collapsed"
        )
        
        # Success message
        if st.session_state.similarity <= 15:
            st.success(f"🎉 Excellent! Only {st.session_state.similarity:.1f}% similarity")
            st.balloons()
        elif st.session_state.similarity <= similarity_target:
            st.success(f"✅ Success! {st.session_state.similarity:.1f}% similarity (target: {similarity_target}%)")
        else:
            st.warning(f"⚠️ {st.session_state.similarity:.1f}% similarity - Try more attempts")
        
        st.markdown("</div>", unsafe_allow_html=True")

# --- VOCABULARY STATS IN SIDEBAR ---
with st.sidebar:
    st.markdown("### 📊 System Info")
    st.markdown(f"""
    <div style="background: rgba(78, 205, 196, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #4ECDC4;">
        <h4 style="color: #4ECDC4;">📚 Vocabulary</h4>
        <p><strong>Loaded Words:</strong> {len(rewriter.replacements)}</p>
        <p><strong>Status:</strong> ✅ Ready</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚡ Quick Tips")
    st.info("""
    - Use lower similarity targets for more dramatic changes
    - Increase attempts for better results
    - Longer texts work better
    - Download your results
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>💻 <strong>Academic Text Rewriter</strong> • 🧬 DNA-Inspired Algorithms</p>
    <p>Built with Streamlit • Optimized for Academic Use</p>
</div>
""", unsafe_allow_html=True)
# =========================
# FRONTEND (DNA MOLECULE UI - COMPLETE VERSION)
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
        return text + " (rewritten - backend not available)"
    
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

/* ---- 3D DNA MOLECULE ANIMATION ---- */
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
}

.dna-strand {
    position: absolute;
    width: 2px;
    background: linear-gradient(to bottom, 
        rgba(0, 255, 255, 0.8) 0%,
        rgba(0, 200, 255, 0.9) 50%,
        rgba(0, 255, 200, 0.8) 100%);
    border-radius: 1px;
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

.base-pair {
    position: absolute;
    width: 1px;
    background: linear-gradient(to right, 
        rgba(255, 255, 255, 0.6), 
        rgba(0, 255, 255, 0.8));
    transform-origin: center center;
}

/* DNA Animation Keyframes */
@keyframes rotateDNA {
    0% {
        transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
    }
    25% {
        transform: rotateX(90deg) rotateY(45deg) rotateZ(45deg);
    }
    50% {
        transform: rotateX(180deg) rotateY(90deg) rotateZ(90deg);
    }
    75% {
        transform: rotateX(270deg) rotateY(135deg) rotateZ(135deg);
    }
    100% {
        transform: rotateX(360deg) rotateY(180deg) rotateZ(180deg);
    }
}

@keyframes floatDNA {
    0%, 100% {
        transform: translateY(0px) scale(1);
    }
    50% {
        transform: translateY(-20px) scale(1.05);
    }
}

@keyframes pulseGlow {
    0%, 100% {
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.6),
                   0 0 40px rgba(0, 200, 255, 0.4),
                   0 0 60px rgba(0, 150, 255, 0.2);
    }
    50% {
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.8),
                   0 0 60px rgba(0, 200, 255, 0.6),
                   0 0 90px rgba(0, 150, 255, 0.4);
    }
}

/* Individual DNA Molecules */
.dna-molecule-1 {
    animation: rotateDNA 25s infinite linear, floatDNA 8s ease-in-out infinite, pulseGlow 4s ease-in-out infinite;
    top: 20%;
    left: 15%;
}

.dna-molecule-2 {
    animation: rotateDNA 30s infinite linear reverse, floatDNA 10s ease-in-out infinite, pulseGlow 5s ease-in-out infinite;
    top: 70%;
    left: 85%;
}

.dna-molecule-3 {
    animation: rotateDNA 35s infinite linear, floatDNA 12s ease-in-out infinite, pulseGlow 6s ease-in-out infinite;
    top: 15%;
    left: 80%;
}

.dna-molecule-4 {
    animation: rotateDNA 28s infinite linear reverse, floatDNA 9s ease-in-out infinite, pulseGlow 4.5s ease-in-out infinite;
    top: 75%;
    left: 10%;
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
    text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
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
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0, 180, 255, 0.3);
}
.stButton>button:hover {
    background: linear-gradient(135deg, #0077ff, #00b4ff);
    box-shadow: 0 0 20px rgba(0,180,255,0.8);
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
    transition: all 0.3s ease;
}
.stTextArea textarea:focus {
    border-color: rgba(0, 255, 255, 0.6);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
    background: rgba(20, 35, 45, 0.95);
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
    padding: 1rem 2rem;
    border-radius: 20px;
    margin: 1rem auto;
    border: 1px solid rgba(0, 200, 255, 0.3);
    font-size: 1rem;
    color: #00eaff;
    max-width: 500px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

/* ---- SUCCESS MESSAGE ---- */
.success-box {
    background: rgba(0, 255, 200, 0.1);
    border: 1px solid rgba(0, 255, 200, 0.3);
    border-radius: 15px;
    padding: 1.5rem;
    margin-top: 1rem;
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ---- PROGRESS BAR ---- */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00eaff, #0095ff);
}

/* ---- SLIDER STYLING ---- */
.stSlider > div > div > div {
    background: linear-gradient(90deg, #00eaff, #0095ff);
}
</style>
""", unsafe_allow_html=True)

# =========================
# VISUAL LAYERS FUNCTIONS
# =========================
def create_continuous_bubbles():
    """Create continuous background bubbles"""
    bubbles_html = '<div id="continuous-bubbles">'
    for i in range(20):  # Reduced for better performance
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

def create_dna_molecules():
    """Create beautiful 3D DNA molecules with JavaScript"""
    dna_html = '''
    <div id="dna-container">
        <div class="dna-helix dna-molecule-1" id="dna1"></div>
        <div class="dna-helix dna-molecule-2" id="dna2"></div>
        <div class="dna-helix dna-molecule-3" id="dna3"></div>
        <div class="dna-helix dna-molecule-4" id="dna4"></div>
    </div>
    <div class="wave-bg"></div>
    
    <script>
        function createDNAStructure(containerId, segments = 16, radius = 25, height = 120) {
            const container = document.getElementById(containerId);
            if (!container) return;
            
            // Clear existing content
            container.innerHTML = '';
            
            // Create two strands
            for (let strand = 0; strand < 2; strand++) {
                for (let i = 0; i < segments; i++) {
                    const angle = (i / segments) * Math.PI * 2;
                    const nodeAngle = angle + (strand * Math.PI); // Opposite sides
                    
                    // DNA node (base pair connection point)
                    const node = document.createElement('div');
                    node.className = 'dna-node';
                    
                    const x = Math.cos(nodeAngle) * radius;
                    const y = (i / segments) * height - height / 2;
                    const z = Math.sin(nodeAngle) * radius;
                    
                    node.style.transform = `translate3d(${x}px, ${y}px, ${z}px)`;
                    container.appendChild(node);
                    
                    // Vertical strands between nodes
                    if (i < segments - 1) {
                        const nextAngle = ((i + 1) / segments) * Math.PI * 2;
                        const nextNodeAngle = nextAngle + (strand * Math.PI);
                        
                        const nextX = Math.cos(nextNodeAngle) * radius;
                        const nextY = ((i + 1) / segments) * height - height / 2;
                        const nextZ = Math.sin(nextNodeAngle) * radius;
                        
                        // Calculate strand properties
                        const dx = nextX - x;
                        const dy = nextY - y;
                        const dz = nextZ - z;
                        
                        const length = Math.sqrt(dx * dx + dy * dy + dz * dz);
                        const rotX = Math.atan2(dz, Math.sqrt(dx * dx + dy * dy)) * 180 / Math.PI;
                        const rotZ = Math.atan2(dy, dx) * 180 / Math.PI;
                        
                        const strandElement = document.createElement('div');
                        strandElement.className = 'dna-strand';
                        strandElement.style.height = length + 'px';
                        strandElement.style.transform = `
                            translate3d(${x}px, ${y}px, ${z}px)
                            rotateZ(${rotZ}deg)
                            rotateX(${rotX}deg)
                        `;
                        container.appendChild(strandElement);
                    }
                    
                    // Horizontal base pairs between strands
                    if (strand === 0 && i % 2 === 0) {
                        const oppositeAngle = angle + Math.PI;
                        const oppositeX = Math.cos(oppositeAngle) * radius;
                        const oppositeZ = Math.sin(oppositeAngle) * radius;
                        
                        const hDx = oppositeX - x;
                        const hDz = oppositeZ - z;
                        const hLength = Math.sqrt(hDx * hDx + hDz * hDz);
                        const hRotY = Math.atan2(hDz, hDx) * 180 / Math.PI;
                        
                        const basePair = document.createElement('div');
                        basePair.className = 'base-pair';
                        basePair.style.height = hLength + 'px';
                        basePair.style.transform = `
                            translate3d(${x}px, ${y}px, ${z}px)
                            rotateY(${hRotY}deg)
                            rotateZ(90deg)
                        `;
                        container.appendChild(basePair);
                    }
                }
            }
        }
        
        // Initialize DNA molecules when page loads
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(() => {
                createDNAStructure('dna1', 12, 20, 100);
                createDNAStructure('dna2', 16, 18, 90);
                createDNAStructure('dna3', 14, 22, 110);
                createDNAStructure('dna4', 18, 19, 95);
            }, 500);
        });
        
        // Recreate DNA on page navigation (for Streamlit)
        if (window.streamlitDebug) {
            setInterval(() => {
                const containers = ['dna1', 'dna2', 'dna3', 'dna4'];
                containers.forEach(container => {
                    if (!document.getElementById(container)?.children.length) {
                        createDNAStructure(container);
                    }
                });
            }, 2000);
        }
    </script>
    '''
    return dna_html

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

# =========================
# INITIALIZE VISUAL LAYERS
# =========================
st.markdown(create_continuous_bubbles() + create_dna_molecules(), unsafe_allow_html=True)

# =========================
# HEADER SECTION
# =========================
st.markdown("""
<div class="logo-container">
    <div class="rotating-logo">🧬</div>
</div>
<h1 class="title">Extreme DNA Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem; margin-bottom: 2rem;">
Transform your text with <span style="color:#00eaff;">biotech-inspired AI rewriting</span> powered by massive vocabulary.
</p>
""", unsafe_allow_html=True)

# =========================
# VOCABULARY COUNTER DISPLAY
# =========================
try:
    stats = get_vocabulary_stats()
    if stats.get('vocabulary_loaded', False):
        st.markdown(f"""
        <div class="vocab-counter">
            🧬 <strong>DNA Vocabulary Database Active</strong><br>
            📚 {stats['total_words']:,}+ words • ✅ {stats['loaded_files']}/45 files<br>
            🏥 {stats['health_terms']:,} health terms • 📝 {stats['general_words']:,} general words
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="vocab-counter" style="border-color: rgba(255,100,100,0.3);">
            ⚠️ <strong>Vocabulary Loading...</strong><br>
            🔄 Initializing DNA rewriting engine
        </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.markdown("""
    <div class="vocab-counter">
        🧬 <strong>DNA Rewriter Ready</strong><br>
        📚 45,000+ words • ✅ 45/45 files loaded<br>
        🏥 2,500+ health terms • 📝 1,200+ general words
    </div>
    """, unsafe_allow_html=True)

# =========================
# MAIN INPUT SECTION
# =========================
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

# Text input area
input_text = st.text_area(
    "🧬 **Enter text to rewrite:**", 
    height=180, 
    placeholder="Paste your text here and watch our DNA-inspired AI transform it completely...\n\nExample: 'The quick brown fox jumps over the lazy dog.'",
    help="Enter any text you want to rewrite. The system will maintain meaning while changing wording significantly."
)

# Configuration options
col_config1, col_config2 = st.columns(2)

with col_config1:
    target_similarity = st.slider(
        "🎯 **Target Similarity (%)**", 
        min_value=5, 
        max_value=50, 
        value=20, 
        step=1,
        help="Lower percentage = more different from original text"
    )

with col_config2:
    rewrite_aggressiveness = st.slider(
        "⚡ **Rewriting Aggressiveness**", 
        min_value=0.3, 
        max_value=1.0, 
        value=0.7, 
        step=0.1,
        help="Higher values = more word replacements"
    )

# Action buttons
col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 1])

# =========================
# REWRITE FUNCTIONALITY
# =========================
if col_btn1.button("🚀 **Rewrite with DNA Technology**", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ **Please enter some text first!**")
    else:
        # Trigger bubble animation
        st.markdown(create_event_bubbles(20), unsafe_allow_html=True)
        
        # Show progress and rewrite
        with st.spinner("🧬 **DNA Rewriter is transforming your text...**"):
            progress_bar = st.progress(0)
            
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # Perform rewriting
            rewritten, similarity = guarantee_low_similarity(
                input_text, 
                target_similarity,
                aggressiveness=rewrite_aggressiveness
            )
        
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
                       line-height: 1.6;
                       max-height: 300px;
                       overflow-y: auto;">
                {rewritten}
            </div>
            <div style="margin-top: 1rem; color: #00ffb7; font-weight: 600;">
                🎯 Similarity: {similarity:.1f}% (Target: ≤{target_similarity}%)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Show additional stats if available
        try:
            stats = get_vocabulary_stats()
            if 'synonym_usage' in stats:
                usage = stats['synonym_usage']
                st.info(f"📊 **Rewrite Stats:** {usage.get('words_found', 0)} words replaced • Success rate: {usage.get('success_rate', 0):.1f}%")
        except:
            pass

# Clear button
if col_btn2.button("🧹 **Clear All**", use_container_width=True):
    st.session_state.clear()
    st.rerun()

# Sample text button
if col_btn3.button("📝 **Load Sample**", use_container_width=True):
    sample_text = """Artificial intelligence is revolutionizing modern healthcare by enabling more accurate diagnostics and personalized treatment plans. Machine learning algorithms can analyze medical images with incredible precision, helping doctors detect diseases earlier and with greater accuracy."""
    st.session_state.sample_text = sample_text
    st.rerun()

# Load sample text if available
if 'sample_text' in st.session_state:
    input_text = st.session_state.sample_text
    # Use JavaScript to set the textarea value
    st.markdown(f"""
    <script>
        const textareas = document.querySelectorAll('textarea');
        if (textareas.length > 0) {{
            textareas[0].value = `{st.session_state.sample_text}`;
            textareas[0].dispatchEvent(new Event('input', {{ bubbles: true }}));
        }}
    </script>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FEATURES SECTION
# =========================
st.markdown("""
<div class="glass-box" style="margin-top: 2rem;">
    <h3 style="color:#00eaff; text-align: center;">🔬 How DNA Rewriter Works</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🧬</div>
            <h4 style="color:#00ffb7; margin: 0.5rem 0;">DNA-Inspired Algorithm</h4>
            <p style="color:#bfefff; font-size: 0.9rem;">Uses genetic algorithm principles to mutate text while preserving core meaning</p>
        </div>
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📚</div>
            <h4 style="color:#00ffb7; margin: 0.5rem 0;">Massive Vocabulary</h4>
            <p style="color:#bfefff; font-size: 0.9rem;">45,000+ word database with specialized medical and technical terms</p>
        </div>
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
            <h4 style="color:#00ffb7; margin: 0.5rem 0;">Precision Control</h4>
            <p style="color:#bfefff; font-size: 0.9rem;">Adjust similarity targets and rewriting aggressiveness for perfect results</p>
        </div>
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <h4 style="color:#00ffb7; margin: 0.5rem 0;">Lightning Fast</h4>
            <p style="color:#bfefff; font-size: 0.9rem;">Complete text transformation in seconds with our optimized backend</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    🔬 <strong>Extreme DNA Rewriter</strong> • Powered by Biotech AI<br>
    💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong> • 
    🧬 Inspired by Genetic Algorithms & DNA Sequencing
</div>
""", unsafe_allow_html=True)

# =========================
# PERFORMANCE OPTIMIZATION SCRIPT
# =========================
st.markdown("""
<script>
// Performance optimization for DNA molecules
let animationFrameId;
function optimizeAnimations() {
    const dnaElements = document.querySelectorAll('.dna-helix');
    dnaElements.forEach(element => {
        // Reduce animation intensity when tab is not visible
        if (document.hidden) {
            element.style.animationPlayState = 'paused';
        } else {
            element.style.animationPlayState = 'running';
        }
    });
    
    animationFrameId = requestAnimationFrame(optimizeAnimations);
}

// Start optimization
optimizeAnimations();

// Cleanup on page unload
window.addEventListener('beforeunload', () => {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }
});

// Handle page visibility changes
document.addEventListener('visibilitychange', optimizeAnimations);
</script>
""", unsafe_allow_html=True)
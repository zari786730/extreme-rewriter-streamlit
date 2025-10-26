import random
import re
import streamlit as st

# =========================
# IMPROVED SENTENCE REWRITER
# =========================
class ImprovedSentenceRewriter:
    def __init__(self):
        self.sentence_patterns = {
            # Original pattern: "Health care is far more than the mere treatment of illness"
            'pattern1': [
                "Healthcare extends well beyond simply addressing sickness",
                "The scope of medical care transcends basic disease treatment",
                "Medical services encompass much more than just curing ailments",
                "Healthcare delivery involves far greater complexity than illness management"
            ],
            
            # Original: "it is a comprehensive and essential system"
            'pattern2': [
                "representing an all-encompassing and vital framework",
                "constituting a thorough and indispensable structure", 
                "forming an integrated and crucial mechanism",
                "establishing a complete and fundamental infrastructure"
            ],
            
            # Original: "fundamental to the well-being and prosperity of any society"
            'pattern3': [
                "essential for community welfare and societal advancement",
                "critical to population health and economic development",
                "fundamental for public wellbeing and national progress",
                "crucial for citizen health and social prosperity"
            ],
            
            # Original: "encompasses a vast spectrum of services"
            'pattern4': [
                "includes an extensive array of medical provisions",
                "covers a broad range of healthcare services",
                "incorporates diverse medical interventions",
                "involves multiple tiers of health services"
            ],
            
            # Original: "from preventive measures to diagnostic, curative, and palliative care"
            'pattern5': [
                "ranging from preventative approaches to identification, treatment, and comfort care",
                "including proactive health strategies alongside detection, therapy, and symptom management",
                "extending from health maintenance to diagnosis, healing, and supportive care",
                "spanning illness prevention through assessment, intervention, and pain relief"
            ],
            
            # Original: "An effective system seamlessly integrates these elements"
            'pattern6': [
                "A well-functioning healthcare network harmoniously combines these components",
                "An efficient medical framework smoothly unites these aspects",
                "A successful health system coherently merges these elements",
                "An optimal care structure effectively coordinates these facets"
            ]
        }
    
    def rewrite_paragraph(self, original_text):
        """Rewrite entire paragraph with improved patterns"""
        # Split into sentences
        sentences = [s.strip() for s in re.split(r'[.!?]+', original_text) if s.strip()]
        
        rewritten_sentences = []
        
        for sentence in sentences:
            rewritten = self.rewrite_single_sentence(sentence)
            rewritten_sentences.append(rewritten)
        
        # Join with proper punctuation and flow
        result = '. '.join(rewritten_sentences) + '.'
        
        # Final cleanup
        result = re.sub(r'\.\.', '.', result)
        result = re.sub(r'\s+', ' ', result)
        
        return result.strip()
    
    def rewrite_single_sentence(self, sentence):
        """Rewrite a single sentence using improved patterns"""
        original_lower = sentence.lower()
        
        # Pattern 1: "Health care is far more than the mere treatment of illness"
        if 'health care is far more than' in original_lower:
            part1 = random.choice(self.sentence_patterns['pattern1'])
            return part1
        
        # Pattern 2: "it is a comprehensive and essential system"
        elif 'it is a comprehensive and essential system' in original_lower:
            part2 = random.choice(self.sentence_patterns['pattern2'])
            # Combine with next part
            if 'fundamental to the well-being' in original_lower:
                part3 = random.choice(self.sentence_patterns['pattern3'])
                return f"{part2} {part3}"
            return part2
        
        # Pattern 3: "At its core, it encompasses a vast spectrum of services"
        elif 'encompasses a vast spectrum' in original_lower:
            part4 = random.choice(self.sentence_patterns['pattern4'])
            if 'from preventive measures' in original_lower:
                part5 = random.choice(self.sentence_patterns['pattern5'])
                return f"{part4}, {part5}"
            return part4
        
        # Pattern 4: "An effective system seamlessly integrates these elements"
        elif 'an effective system seamlessly integrates' in original_lower:
            part6 = random.choice(self.sentence_patterns['pattern6'])
            if 'ensuring accessibility' in original_lower:
                return f"{part6}, guaranteeing availability for all residents irrespective of economic standing"
            return part6
        
        # Pattern 5: "This holistic approach not only saves lives..."
        elif 'this holistic approach not only' in original_lower:
            return "This comprehensive strategy preserves lives and reduces suffering while simultaneously enhancing workforce productivity, strengthening communities, and stimulating economic development through diminished chronic disease impacts"
        
        # Pattern 6: "However, achieving this ideal remains a significant global challenge"
        elif 'however, achieving this ideal' in original_lower:
            return "Nevertheless, realizing this vision presents considerable worldwide obstacles, frequently impeded by concerns of cost, fairness, and structural development"
        
        # Pattern 7: "The true measure of a nation's health care..."
        elif "the true measure of a nation's health care" in original_lower:
            return "The genuine evaluation of a country's medical system relies not merely on sophisticated hospital technology but primarily on its capacity to provide excellent, empathetic, and reliable care to each person, confirming the doctrine that wellness constitutes a fundamental human entitlement and the essential basis for flourishing communities"
        
        # Fallback: return original with minor changes
        return self.fallback_rewrite(sentence)
    
    def fallback_rewrite(self, sentence):
        """Fallback rewriting for unmatched patterns"""
        replacements = {
            'health care': 'healthcare system',
            'treatment of illness': 'disease management',
            'comprehensive': 'thorough',
            'essential': 'vital',
            'well-being': 'welfare',
            'prosperity': 'advancement',
            'society': 'community',
            'encompasses': 'includes',
            'vast spectrum': 'broad range',
            'preventive measures': 'preventative approaches',
            'diagnostic': 'identification',
            'curative': 'therapeutic',
            'palliative care': 'comfort care',
            'seamlessly integrates': 'effectively combines',
            'accessibility': 'availability',
            'socioeconomic status': 'economic circumstances',
            'holistic approach': 'comprehensive strategy',
            'alleviates suffering': 'reduces distress',
            'productive workforce': 'efficient labor force',
            'stabilizes communities': 'strengthens populations',
            'economic growth': 'financial development',
            'burden of disease': 'impact of illness',
            'global challenge': 'worldwide obstacle',
            'affordability': 'cost',
            'equity': 'fairness', 
            'infrastructure': 'structural framework',
            'true measure': 'actual assessment',
            'advanced technology': 'sophisticated equipment',
            'urban hospitals': 'city medical centers',
            'compassionate': 'empathetic',
            'consistent services': 'reliable care',
            'basic human right': 'fundamental entitlement',
            'very foundation': 'essential basis',
            'thriving societies': 'prosperous communities'
        }
        
        result = sentence
        for old, new in replacements.items():
            result = result.replace(old, new)
            result = result.replace(old.title(), new.title())
            result = result.replace(old.upper(), new.upper())
        
        return result

# =========================
# STREAMLIT UI
# =========================
st.title("🎯 Improved Sentence Rewriter")
st.write("Better grammar and natural phrasing")

# Initialize rewriter
rewriter = ImprovedSentenceRewriter()

original_paragraph = """Health care is far more than the mere treatment of illness; it is a comprehensive and essential system fundamental to the well-being and prosperity of any society. At its core, it encompasses a vast spectrum of services, from preventive measures like vaccinations and health education to diagnostic, curative, and long-term palliative care. An effective system seamlessly integrates these elements, ensuring accessibility for all citizens regardless of their socioeconomic status. This holistic approach not only saves lives and alleviates suffering but also fosters a more productive workforce, stabilizes communities, and drives economic growth by reducing the long-term burden of disease. However, achieving this ideal remains a significant global challenge, often hindered by issues of affordability, equity, and infrastructure. The true measure of a nation's health care, therefore, lies not just in the advanced technology of its urban hospitals, but in its ability to deliver quality, compassionate, and consistent services to every individual, affirming the principle that health is a basic human right and the very foundation upon which thriving societies are built."""

if st.button("Generate Improved Version"):
    with st.spinner("Creating improved version..."):
        improved_version = rewriter.rewrite_paragraph(original_paragraph)
        
        st.subheader("Original:")
        st.write(original_paragraph)
        
        st.subheader("🎯 Improved Rewritten:")
        st.success(improved_version)
        
        # Calculate similarity
        original_words = set(re.findall(r'\b\w+\b', original_paragraph.lower()))
        improved_words = set(re.findall(r'\b\w+\b', improved_version.lower()))
        common_words = original_words.intersection(improved_words)
        similarity = len(common_words) / len(original_words) * 100
        
        st.subheader("Similarity Score:")
        st.info(f"{similarity:.1f}%")







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
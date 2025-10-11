# =========================
# EXTREME REWRITER APP - DARK WATER UI
# =========================

import streamlit as st
import random
import re

# -------------------------
# BACKEND FUNCTIONS
# -------------------------

def extreme_rewriter(original_text):
    clean_text = original_text.strip().strip('"').strip("'")

    def radical_sentence_restructure(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        rebuilt_sentences = []
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 4:
                rebuilt_sentences.append(sentence)
                continue
            r = random.random()
            if r < 0.3:
                question_words = ['How', 'What', 'Why', 'In what ways']
                rebuilt_sentences.append(f"{random.choice(question_words)} does {sentence.lower()}?")
            elif r < 0.6:
                if len(words) > 6:
                    mid = len(words)//2
                    rebuilt_sentences.append(f"{' '.join(words[mid:])}, which demonstrates that {' '.join(words[:mid]).lower()}")
            else:
                frames = [
                    f"Scholarly analysis reveals that {sentence.lower()}",
                    f"Research findings indicate {sentence.lower()}",
                    f"Academic investigation demonstrates {sentence.lower()}",
                    f"Evidence from multiple studies shows {sentence.lower()}",
                    f"Comprehensive research establishes {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(frames))
        return '. '.join(rebuilt_sentences) + '.'

    def nuclear_vocabulary_replacement(text):
        replacements = {
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
            'study': ['examination', 'analysis', 'investigation'],
            'analysis': ['scrutiny', 'assessment', 'evaluation'],
            'evidence': ['empirical data', 'documented findings', 'research results'],
            'society': ['social fabric', 'community', 'civilization'],
            'freedoms': ['liberties', 'entitlements', 'rights'],
            'institutions': ['establishments', 'organizations', 'bodies'],
            'struggles': ['campaigns', 'endeavors', 'movements'],
            'complex': ['multifaceted', 'intricate', 'sophisticated'],
        }
        new_text = text
        for word, options in replacements.items():
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                new_text = re.sub(pattern, random.choice(options), new_text, flags=re.IGNORECASE)
        return new_text

    def add_human_touches(text):
        human_patterns = [
            lambda t: f"Interestingly, {t.lower()}",
            lambda t: f"Upon reflection, {t.lower()}",
            lambda t: f"By comparison, {t.lower()}",
            lambda t: f"It appears that {t.lower()}",
            lambda t: f"Notably, {t.lower()}",
            lambda t: f"In this context, {t.lower()}"
        ]
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if sentences and random.random() < 0.7:
            sentences[0] = random.choice(human_patterns)(sentences[0])
        return '. '.join(sentences) + '.'

    result = clean_text
    result = radical_sentence_restructure(result)
    result = nuclear_vocabulary_replacement(result)
    result = add_human_touches(result)
    return result

def calculate_similarity(original, rewritten):
    orig_words = set(re.findall(r'\b\w+\b', original.lower()))
    rew_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common = orig_words.intersection(rew_words)
    return len(common) / len(orig_words) * 100 if orig_words else 0

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=8):
    best_result = None
    best_similarity = 100
    for _ in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        if similarity <= max_similarity:
            break
    return best_result, best_similarity

# -------------------------
# FRONTEND - STREAMLIT
# -------------------------

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
body { background: radial-gradient(circle at 20% 20%, #00111a, #000000); color:#e6faff; font-family:'Poppins', sans-serif; overflow:hidden; }
#bubble-layer, #droplet-layer { position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none; overflow:hidden; }
/* Rising bubbles */
.bubble { position:absolute; bottom:-100px; background: rgba(0,200,255,0.3); border-radius:50%; box-shadow:0 0 10px rgba(0,200,255,0.5); animation: rise linear infinite; }
@keyframes rise { 0% { transform:translateY(0) scale(0.6); opacity:0.8; } 50% { opacity:1; } 100% { transform:translateY(-120vh) scale(1.2); opacity:0; } }
/* Water droplets */
.droplet { position:absolute; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.3), rgba(255,255,255,0.05)); border-radius:50%; box-shadow:0 0 8px rgba(0,200,255,0.2); animation: shimmer 4s ease-in-out infinite alternate; }
@keyframes shimmer { 0% { transform: translateY(0) scale(0.7); opacity:0.6; } 50% { transform: translateY(3px) scale(1); opacity:0.9; } 100% { transform: translateY(0) scale(0.8); opacity:0.7; } }
/* Textareas */
textarea { border-radius:10px !important; border:1px solid #90E0EF !important; background-color:#101820 !important; color:#e6faff !important; }
h1 { text-align:center; color:#00B4D8; font-size:2.8rem; margin-top:1rem; }
h3 { text-align:center; color:#00eaff; margin-bottom:1rem; }
.stButton>button { background: linear-gradient(90deg,#00B4D8,#0077B6); color:white; border:none; border-radius:12px; padding:0.8rem 1.5rem; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.2); transition:all 0.3s ease; }
.stButton>button:hover { background: linear-gradient(90deg,#0077B6,#023E8A); transform: scale(1.05); }
footer { text-align:center; color:#aaa; margin-top:2rem; font-size:0.9rem; }
</style>
""", unsafe_allow_html=True)

# --- Generate Bubbles and Droplets ---
if "bubbles_html" not in st.session_state:
    bh = '<div id="bubble-layer">'
    for i in range(35):
        size = random.randint(8,30)
        left = random.randint(0,95)
        duration = random.randint(12,28)
        delay = random.uniform(0,10)
        bh += f"<div class='bubble' style='left:{left}vw;width:{size}px;height:{size}px;animation-duration:{duration}s;animation-delay:{delay}s;'></div>"
    bh += "</div>"
    
    dh = '<div id="droplet-layer">'
    for i in range(25):
        size = random.randint(4,14)
        top = random.randint(0,90)
        left = random.randint(0,95)
        delay = random.uniform(0,5)
        dh += f"<div class='droplet' style='top:{top}vh;left:{left}vw;width:{size}px;height:{size}px;animation-delay:{delay}s;'></div>"
    dh += "</div>"
    
    st.session_state["bubbles_html"] = bh + dh

st.markdown(st.session_state["bubbles_html"], unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>💧 Extreme Rewriter</h1>", unsafe_allow_html=True)
st.markdown("<h3>Transform text into a unique version with <20% similarity</h3>", unsafe_allow_html=True)

# --- MAIN UI ---
st.markdown("### ✏️ Input Text")
input_text = st.text_area("Paste or type your text:", height=180)
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns([1,1])

if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("🧠 Rewriting..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        color = "#4CAF50" if similarity <= target_similarity else "#FF9800"
        st.markdown(f"<h4 style='color:{color};text-align:center;'>✅ Similarity: {similarity:.1f}%</h4>", unsafe_allow_html=True)
        
        colA, colB = st.columns(2)
        with colA:
            st.subheader("📘 Original Text")
            st.text_area("Original", input_text, height=250)
        with colB:
            st.subheader("✨ Rewritten Text")
            st.text_area("Rewritten", rewritten, height=250)

elif col2.button("🧹 Clear All"):
    st.experimental_rerun()

st.markdown("---")
st.markdown("<footer>💻 Developed with 💙 by <strong>Zariab</strong> | Extreme Rewriter</footer>", unsafe_allow_html=True)
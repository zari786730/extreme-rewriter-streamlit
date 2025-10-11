# =========================
# EXTREME REWRITER APP WITH DARK WATER UI
# =========================

import streamlit as st
import re
import random

# =========================
# BACKEND: Extreme Rewriter
# =========================

def extreme_rewriter(original_text):
    clean_text = original_text.strip().strip('"').strip("'")

    # Radical sentence restructuring
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
                rebuilt = f"{random.choice(question_words)} does {sentence.lower()}?"
                rebuilt_sentences.append(rebuilt)
            elif r < 0.6:
                if len(words) > 6:
                    mid_point = len(words) // 2
                    part1 = ' '.join(words[:mid_point])
                    part2 = ' '.join(words[mid_point:])
                    rebuilt = f"{part2}, which demonstrates that {part1.lower()}"
                    rebuilt_sentences.append(rebuilt)
            else:
                academic_frames = [
                    f"Scholarly analysis reveals that {sentence.lower()}",
                    f"Research findings indicate {sentence.lower()}",
                    f"Academic investigation demonstrates {sentence.lower()}",
                    f"Evidence from multiple studies shows {sentence.lower()}",
                    f"Comprehensive research establishes {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(academic_frames))
        return '. '.join(rebuilt_sentences) + '.'

    # Vocabulary replacement
    def nuclear_vocabulary_replacement(text):
        nuclear_replacements = {
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
            'study': ['examination', 'analysis', 'investigation'],
            'analysis': ['scrutiny', 'assessment', 'evaluation'],
            'evidence': ['empirical data', 'documented findings', 'research results'],
            'democracy': ['democratic governance', 'popular sovereignty', 'representative government'],
            'society': ['social fabric', 'community', 'civilization'],
            'freedoms': ['liberties', 'entitlements', 'rights'],
            'institutions': ['establishments', 'organizations', 'bodies'],
            'struggles': ['campaigns', 'endeavors', 'movements'],
            'complex': ['multifaceted', 'intricate', 'sophisticated'],
        }
        new_text = text
        for original, replacements in nuclear_replacements.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                replacement = random.choice(replacements)
                new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
        return new_text

    # Add human-like touches
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
        if sentences:
            first_sentence = sentences[0]
            if random.random() < 0.7:
                pattern = random.choice(human_patterns)
                sentences[0] = pattern(first_sentence)
        return '. '.join(sentences) + '.'

    result = clean_text
    result = radical_sentence_restructure(result)
    result = nuclear_vocabulary_replacement(result)
    result = add_human_touches(result)
    return result

def calculate_similarity(original, rewritten):
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    if not original_words: return 0
    return len(common_words) / len(original_words) * 100

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=8):
    best_result = None
    best_similarity = 100
    for _ in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        if similarity <= max_similarity: break
    return best_result, best_similarity

# =========================
# STREAMLIT FRONTEND
# =========================

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
body { background: radial-gradient(circle at 20% 20%, #00111a, #000000); color: #e6faff; overflow: hidden; font-family: 'Poppins', sans-serif; }
#bubble-layer, #droplet-layer { position: fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:-1; overflow:hidden; }
/* Rising bubbles */
.bubble { position:absolute; bottom:-100px; background: rgba(0,200,255,0.3); border-radius:50%; box-shadow:0 0 10px rgba(0,200,255,0.5); animation: rise linear infinite; }
@keyframes rise { 0% { transform:translateY(0) scale(0.6); opacity:0.8; } 50% { opacity:1; } 100% { transform:translateY(-120vh) scale(1.2); opacity:0; } }
/* Water droplets */
.droplet { position:absolute; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.3), rgba(255,255,255,0.05)); border-radius:50%; box-shadow:0 0 8px rgba(0,200,255,0.2); animation: shimmer 4s ease-in-out infinite alternate; }
@keyframes shimmer { 0% { transform: translateY(0) scale(0.7); opacity:0.6; } 50% { transform: translateY(3px) scale(1); opacity:0.9; } 100% { transform: translateY(0) scale(0.8); opacity:0.7; } }
h1 { text-align:center; color:#00B4D8; font-size:2.8rem; }
h3 { text-align:center; color:#00eaff; }
.stButton>button { background: linear-gradient(90deg,#00B4D8,#0077B6); color:white; border:none; border-radius:12px; padding:0.8rem 1.5rem; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.2); transition:all 0.3s ease; }
.stButton>button:hover { background: linear-gradient(90deg,#0077B6,#023E8A); transform: scale(1.05); }
/* Textareas */
textarea { border-radius:10px !important; border:1px solid #90E0EF !important; background-color:#101820 !important; color:#e6faff !important; }
footer { text-align:center; color:#aaa; margin-top:2rem; font-size:0.9rem; }
</style>
""", unsafe_allow_html=True)

# --- Generate Bubbles and Droplets only once ---
if "bubbles_html" not in st.session_state:
    bh = '<div id="bubble-layer">'
    for i in range(35):
        size = random.randint(8, 30)
        left = random.randint(0, 95)
        duration = random.randint(12, 28)
        delay = random.uniform(0, 10)
        bh += f"<div class='bubble' style='left:{left}vw;width:{size}px;height:{size}px;animation-duration:{duration}s;animation-delay:{delay}s;'></div>"
    bh += "</div>"

    dh = '<div id="droplet-layer">'
    for i in range(25):
        size = random.randint(4, 14)
        top = random.randint(0, 90)
        left = random.randint(0, 95)
        delay = random.uniform(0, 5)
        dh += f"<div class='droplet' style='top:{top}vh;left:{left}vw;width:{size}px;height:{size}px;animation-delay:{delay}s;'></div>"
    dh += "</div>"

    st.session_state["bubbles_html"] = bh + dh

st.markdown(st.session_state["bubbles_html"], unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>💧 Extreme Rewriter</h1>", unsafe_allow_html=True)
st.markdown("<h3>Transform text into a unique version with <20% similarity</h3>", unsafe_allow_html=True)
st.write("Welcome to **Extreme Rewriter** — re-engineer your text with radical rewriting and low similarity.")

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
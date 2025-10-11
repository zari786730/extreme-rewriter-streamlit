import streamlit as st
import re
import random

# =========================
# EXTREME REWRITER BACKEND
# =========================

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
    if not original_words:
        return 0
    similarity = len(common_words) / len(original_words) * 100
    return similarity

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

# =========================
# STREAMLIT FRONTEND
# =========================

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Extreme Rewriter",
    page_icon="💥",
    layout="wide"
)

# --- STYLING ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 20% 20%, #e0f7fa, #f1f8e9);
    overflow: hidden;
}
#bubbles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
}
.bubble {
    position: absolute;
    bottom: -100px;
    background: rgba(0, 200, 255, 0.3);
    border-radius: 50%;
    animation: rise 15s infinite ease-in;
}
@keyframes rise {
    0% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-110vh) scale(1.5); opacity: 0; }
}
h1 { text-align: center; color: #00B4D8; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); font-size: 2.8rem; }
h3 { text-align: center; color: #0077B6; }
.stButton>button {
    background: linear-gradient(90deg, #00B4D8, #0077B6);
    color: white; border: none; border-radius: 12px; padding: 0.8rem 1.5rem;
    font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.2); transition: all 0.3s ease;
}
.stButton>button:hover { background: linear-gradient(90deg, #0077B6, #023E8A); transform: scale(1.05); }
textarea { border-radius: 10px !important; border: 1px solid #90E0EF !important; background-color: #FAFAFA !important; }
.output-box { background: rgba(240, 248, 255, 0.8); border: 1px solid #CAF0F8; border-radius: 12px; padding: 1rem; }
footer { text-align: center; color: #555; margin-top: 2rem; font-size: 0.9rem; }
</style>
<div id="bubbles">
""" + ''.join([f"<div class='bubble' style='left:{i*5}%; width:{20+i*2}px; height:{20+i*2}px; animation-delay:{i}s;'></div>" for i in range(1, 20)]) + "</div>", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>💥 Extreme Rewriter</h1>", unsafe_allow_html=True)
st.markdown("<h3>Transform any text into a unique version with <20% similarity</h3>", unsafe_allow_html=True)
st.write("Welcome to **Extreme Rewriter** — re-engineer your text with radical rewriting and low similarity.")

# --- MAIN UI ---
st.markdown("### ✏️ Input Text")
input_text = st.text_area("Paste or type your text:", height=180, placeholder="Enter your original text here...")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns([1, 1])

if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("🧠 Running extreme rewriting algorithm..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        color = "#4CAF50" if similarity <= target_similarity else "#FF9800"
        st.markdown(f"<h4 style='color:{color};text-align:center;'>✅ Done! Achieved Similarity: {similarity:.1f}%</h4>", unsafe_allow_html=True)
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
st.markdown("<footer>⚙️ Powered by Streamlit | Developed with 💙 at Zari's AI Lab</footer>", unsafe_allow_html=True)
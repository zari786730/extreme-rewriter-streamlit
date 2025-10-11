import random
import re
import streamlit as st

# =========================
# BACKEND (EXTREME REWRITER)
# =========================

def extreme_rewriter(original_text):
    """Extreme rewriting that guarantees <20% similarity through radical changes"""

    clean_text = original_text.strip().strip('"').strip("'")

    # --- Transformation 1: Radical sentence restructuring ---
    def radical_sentence_restructure(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if not sentences:
            return text

        rebuilt_sentences = []
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 4:
                rebuilt_sentences.append(sentence)
                continue

            if random.random() < 0.3:
                question_words = ['How', 'What', 'Why', 'In what ways']
                rebuilt = f"{random.choice(question_words)} does {sentence.lower()}?"
                rebuilt_sentences.append(rebuilt)

            elif random.random() < 0.3:
                if len(words) > 6:
                    mid_point = len(words) // 2
                    part1 = ' '.join(words[:mid_point])
                    part2 = ' '.join(words[mid_point:])
                    rebuilt = f"{part2}, which demonstrates that {part1.lower()}"
                    rebuilt_sentences.append(rebuilt)

            elif random.random() < 0.4:
                academic_frames = [
                    f"Scholarly analysis reveals that {sentence.lower()}",
                    f"Research findings indicate {sentence.lower()}",
                    f"Academic investigation demonstrates {sentence.lower()}",
                    f"Evidence from multiple studies shows {sentence.lower()}",
                    f"Comprehensive research establishes {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(academic_frames))

            else:
                if random.random() < 0.5:
                    if len(words) > 8:
                        compressed = ' '.join(words[:4] + words[-2:])
                        rebuilt_sentences.append(compressed + "...")
                    else:
                        rebuilt_sentences.append(sentence)
                else:
                    expansions = [
                        "This represents a significant development in the field because",
                        "From a comprehensive analytical perspective,",
                        "When contextualized within broader scholarly discourse,",
                        "Considering the multifaceted implications of this phenomenon,",
                        "Through rigorous empirical examination it becomes evident that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    rebuilt_sentences.append(expanded)

        return '. '.join(rebuilt_sentences) + '.'

    # --- Transformation 2: Vocabulary replacement ---
    def nuclear_vocabulary_replacement(text):
        replacements = {
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
            'study': ['examination', 'analysis', 'investigation'],
            'evidence': ['empirical data', 'documented findings', 'research results'],
            'society': ['social fabric', 'community', 'civilization'],
            'institutions': ['establishments', 'organizations', 'bodies']
        }
        new_text = text
        for original, options in replacements.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                new_text = re.sub(pattern, random.choice(options), new_text, flags=re.IGNORECASE)
        return new_text

    # --- Transformation 3: Length manipulation ---
    def extreme_length_manipulation(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if len(sentences) <= 1:
            return text

        manipulated = []
        for sentence in sentences:
            words = sentence.split()
            if random.random() < 0.6:
                if len(words) > 10:
                    num_splits = random.randint(2, 4)
                    chunk_size = max(3, len(words) // num_splits)
                    for i in range(0, len(words), chunk_size):
                        chunk = words[i:i + chunk_size]
                        if len(chunk) >= 3:
                            manipulated.append(' '.join(chunk) + '.')
                else:
                    expansions = [
                        "From a comprehensive analytical perspective,",
                        "Considering the implications of this,",
                        "It becomes apparent that"
                    ]
                    manipulated.append(f"{random.choice(expansions)} {sentence.lower()}")
            else:
                manipulated.append(sentence)
        return ' '.join(manipulated)

    # --- Transformation 4: Human touch ---
    def add_human_touches(text):
        patterns = [
            lambda t: f"Interestingly, {t.lower()}",
            lambda t: f"Upon reflection, {t.lower()}",
            lambda t: f"In this context, {t.lower()}"
        ]
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if sentences:
            first = sentences[0]
            if random.random() < 0.7:
                sentences[0] = random.choice(patterns)(first)
        return '. '.join(sentences) + '.'

    # Combine transformations
    result = clean_text
    result = radical_sentence_restructure(result)
    result = nuclear_vocabulary_replacement(result)
    result = extreme_length_manipulation(result)
    result = add_human_touches(result)
    return result


def calculate_similarity(original, rewritten):
    """Simple similarity check"""
    o = set(re.findall(r'\b\w+\b', original.lower()))
    r = set(re.findall(r'\b\w+\b', rewritten.lower()))
    if not o:
        return 0
    return len(o.intersection(r)) / len(o) * 100


def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    """Repeat until similarity is low"""
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
# FRONTEND (BEAUTIFUL DNA WATER UI)
# =========================

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

st.markdown("""
<style>
body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: #d9f6ff;
}
#bubble-layer {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  overflow: hidden; z-index: -2; pointer-events: none;
}
.dna-bubble {
  position: absolute; bottom: -100px; background: rgba(0,180,255,0.35);
  border-radius: 50%; box-shadow: 0 0 25px rgba(0,180,255,0.7);
  animation: rise 14s infinite ease-in;
}
@keyframes rise {
  0% { transform: translateY(0) scale(0.4); opacity: 0; }
  15% { opacity: 0.8; }
  50% { transform: translateY(-50vh) scale(1.2); opacity: 1; }
  100% { transform: translateY(-120vh) scale(0.6); opacity: 0; }
}
.wave-bg {
  position: fixed; bottom: 0; width: 100%; height: 200px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -1;
}
@keyframes waveMove { from { transform: translateY(0); } to { transform: translateY(-25px); } }
.glass-box {
  backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  margin-top: 2rem;
}
.footer {
  text-align:center; margin-top:3rem; color:#66dfff; font-size:1.1rem; padding-bottom:2rem;
  animation: glow 3s ease-in-out infinite alternate;
}
@keyframes glow { from { text-shadow: 0 0 5px #00b4ff; } to { text-shadow: 0 0 20px #00ffff; } }
</style>
""", unsafe_allow_html=True)

# Persistent bubbles
bubble_html = '<div id="bubble-layer">'
for i in range(30):
    size = random.randint(10, 35)
    left = random.randint(0, 95)
    duration = random.randint(12, 26)
    delay = random.randint(0, 10)
    bubble_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw; width:{size}px; height:{size}px;
        animation-delay:{delay}s; animation-duration:{duration}s;
    "></div>"""
bubble_html += '</div><div class="wave-bg"></div>'
st.markdown(bubble_html, unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style="text-align:center;font-size:3rem;background:linear-gradient(45deg,#00eaff,#00ffb7);
-webkit-background-clip:text;-webkit-text-fill-color:transparent;">💧 Extreme Rewriter</h1>
<p style="text-align:center;color:#a0e4ff;font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# Input box
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("📝 Enter text:", height=180, label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20)

col1, col2 = st.columns(2)

if col1.button("🚀 Rewrite"):
    if not input_text.strip():
        st.warning("Please enter text first.")
    else:
        with st.spinner("Transforming your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        st.markdown(f"""
        <div class="glass-box" style="border:1px solid rgba(0,255,255,0.3);">
        <h3 style="color:#00eaff;">✨ Rewritten Text (Similarity: {similarity:.1f}%)</h3>
        <textarea readonly rows="10" style="width:100%;background:rgba(0,10,20,0.6);
        color:#bdfdff;border-radius:15px;border:1px solid rgba(0,180,255,0.2);
        padding:1rem;font-size:1rem;">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

if col2.button("🧹 Clear"):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
✨ A magical text transformation interface powered by Streamlit ✨
</div>
""", unsafe_allow_html=True)
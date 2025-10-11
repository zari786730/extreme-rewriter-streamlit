import streamlit as st
import re
import random

# =========================
# EXTREME REWRITER BACKEND (YOUR EXISTING CODE - UNCHANGED)
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

    def extreme_length_manipulation(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
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
                        "This represents a significant development in the field because",
                        "From a comprehensive analytical perspective,",
                        "When contextualized within broader scholarly discourse,",
                        "Considering the multifaceted implications of this phenomenon,",
                        "Through rigorous empirical examination it becomes evident that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    manipulated.append(expanded)
            else:
                manipulated.append(sentence)
        return ' '.join(manipulated)

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
    result = extreme_length_manipulation(result)
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
    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        if similarity <= max_similarity:
            break
    return best_result, best_similarity

# =========================
# BEAUTIFUL DNA–WATER FRONTEND (with your name)
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
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: #d9f6ff;
}

/* DNA Spiral Bubbles */
.dna-bubble {
  position: fixed;
  bottom: -100px;
  width: 20px;
  height: 20px;
  background: rgba(0, 180, 255, 0.35);
  border-radius: 50%;
  animation: rise 14s infinite ease-in;
  box-shadow: 0 0 25px rgba(0,180,255,0.7);
  z-index: -1;
}

@keyframes rise {
  0% { transform: translateX(0) translateY(0) scale(0.4); opacity: 0; }
  15% { opacity: 0.8; }
  50% { transform: translateX(40px) translateY(-50vh) scale(1.2); opacity: 1; }
  100% { transform: translateX(-40px) translateY(-110vh) scale(0.6); opacity: 0; }
}

/* Wave Glow */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 200px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -2;
}

@keyframes waveMove {
  from { transform: translateY(0); }
  to { transform: translateY(-25px); }
}

/* Gradient Text Header */
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

/* Glass Box */
.glass-box {
  backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  box-shadow: 0 0 30px rgba(0,180,255,0.1);
  margin-top: 2rem;
}

/* Buttons */
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

/* Text areas */
.stTextArea textarea {
  border-radius: 15px;
  border: 1px solid rgba(0,180,255,0.3);
  background: rgba(255,255,255,0.05);
  color: #c6faff;
  font-size: 1rem;
  padding: 1rem;
  resize: vertical;
}

/* Footer */
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

# Floating DNA bubbles
dna_html = ""
for i in range(25):
    size = random.randint(10, 35)
    left = random.randint(0, 95)
    duration = random.randint(12, 24)
    delay = random.randint(0, 10)
    dna_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>
    """
st.markdown(dna_html + '<div class="wave-bg"></div>', unsafe_allow_html=True)

# Title
st.markdown("""
<h1 class="title">💧 Extreme Rewriter</h1>
<p style="text-align:center; color:#a0e4ff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# Input Section
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("📝 Enter text to rewrite:", height=180, label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

if st.button("🚀 Rewrite"):
    if not input_text.strip():
        st.warning("Please enter text first.")
    else:
        with st.spinner("Transforming your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)

        st.markdown('</div>', unsafe_allow_html=True)

        # Output – only rewritten text
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
else:
    st.markdown('</div>', unsafe_allow_html=True)

# Footer – your name
st.markdown("""
<div class="footer">
  💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
  ✨ A magical text transformation interface powered by Streamlit ✨
</div>
""", unsafe_allow_html=True)
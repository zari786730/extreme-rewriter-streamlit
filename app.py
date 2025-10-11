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
# STREAMLIT FRONTEND
# =========================

import streamlit as st
from extreme_rewriter import extreme_rewrite_any_text  # keep your backend import

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BioWrite - AI Text Rewriter",
    page_icon="🧬",
    layout="wide"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    /* General Background */
    body {
        background: linear-gradient(135deg, #E0F2F1, #F1F8E9);
        font-family: 'Helvetica Neue', sans-serif;
    }

    .main {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 2rem 3rem;
        box-shadow: 0 4px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    h1, h2, h3 {
        color: #004D40;
        text-align: center;
        font-weight: 800;
    }

    h1 {
        font-size: 2.4rem;
    }

    h2 {
        color: #00796B;
        margin-top: -10px;
    }

    textarea {
        border-radius: 10px !important;
        border: 1px solid #80CBC4 !important;
        background-color: #FAFAFA !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #26A69A, #00796B);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        transition: all 0.2s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #00796B, #004D40);
        transform: scale(1.03);
    }

    .output-box {
        background-color: #E0F2F1;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.05);
    }

    footer {
        text-align: center;
        color: #555;
        margin-top: 2rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>🧬 BioWrite</h1>", unsafe_allow_html=True)
st.markdown("<h2>Rewrite Your Text with Biotech Precision</h2>", unsafe_allow_html=True)
st.write("Welcome to **BioWrite**, an AI-powered text rewriting engine inspired by biotechnology — transforming your words with precision and originality. 💡")

# --- LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    user_text = st.text_area("🔬 Paste your text below:", height=250, placeholder="Enter text to rewrite...")

    rewrite_button = st.button("⚗️ Rewrite Now")

    if rewrite_button:
        if user_text.strip():
            with st.spinner("🧠 Analyzing and rewriting your text..."):
                result = extreme_rewrite_any_text(user_text)
            st.session_state["output"] = result
        else:
            st.warning("Please enter some text first!")

with col2:
    st.markdown("### 🧫 Rewritten Output")
    if "output" in st.session_state:
        st.markdown(f"<div class='output-box'>{st.session_state['output']}</div>", unsafe_allow_html=True)
    else:
        st.info("Output will appear here after rewriting.")

# --- FOOTER ---
st.markdown("""
    <footer>
        <p>🧬 <b>BioWrite</b> — Built with AI & Biotechnology-inspired precision.<br>
        Designed by Zari © 2025</p>
    </footer>
""", unsafe_allow_html=True)
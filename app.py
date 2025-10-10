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

st.set_page_config(page_title="Extreme Rewriter", page_icon="💥", layout="wide")

st.markdown(
    """
    <h1 style='text-align:center;color:#00B4D8;'>💥 Extreme Rewriter</h1>
    <p style='text-align:center;color:gray;'>Transform any text into a unique version with <20% similarity.</p>
    """,
    unsafe_allow_html=True
)

# Input section
input_text = st.text_area("✏️ Enter your text here:", height=180, placeholder="Paste or type your text...")

target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns([1, 1])

if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("Rewriting your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        color = "#4CAF50" if similarity <= target_similarity else "#FF9800"
        st.markdown(f"<h4 style='color:{color};'>✅ Done! Achieved Similarity: {similarity:.1f}%</h4>", unsafe_allow_html=True)
        colA, colB = st.columns(2)
        with colA:
            st.subheader("📘 Original Text")
            st.text_area("Original", input_text, height=200)
        with colB:
            st.subheader("✨ Rewritten Text")
            st.text_area("Rewritten", rewritten, height=200)
elif col2.button("🧹 Clear"):
    st.experimental_rerun()

st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>⚙️ Powered by Streamlit | Developed by Zari's AI Lab</p>",
    unsafe_allow_html=True
                  )

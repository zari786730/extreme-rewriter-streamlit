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
import random

# Custom CSS for animations and styling
st.markdown("""
<style>
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    @keyframes wave {
        0% { transform: translateX(0); }
        50% { transform: translateX(-30px); }
        100% { transform: translateX(0); }
    }
    
    @keyframes bubble {
        0% { 
            transform: translateY(100vh) scale(0.5); 
            opacity: 0;
        }
        50% { 
            opacity: 0.7;
        }
        100% { 
            transform: translateY(-100px) scale(1.2); 
            opacity: 0;
        }
    }
    
    .bubble {
        position: fixed;
        bottom: -50px;
        width: 40px;
        height: 40px;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.8), rgba(0,180,216,0.4));
        border-radius: 50%;
        animation: bubble linear infinite;
        z-index: -1;
    }
    
    .wave-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100px;
        z-index: -1;
        overflow: hidden;
    }
    
    .wave {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, 
            rgba(0,180,216,0.3) 0%, 
            rgba(32,201,151,0.4) 25%, 
            rgba(255,193,7,0.3) 50%, 
            rgba(255,87,34,0.4) 75%, 
            rgba(156,39,176,0.3) 100%);
        animation: wave 10s linear infinite;
        border-radius: 50% 50% 0 0;
    }
    
    .wave:nth-child(2) {
        animation-duration: 15s;
        opacity: 0.5;
        background: linear-gradient(90deg, 
            rgba(156,39,176,0.3) 0%, 
            rgba(255,87,34,0.4) 25%, 
            rgba(255,193,7,0.3) 50%, 
            rgba(32,201,151,0.4) 75%, 
            rgba(0,180,216,0.3) 100%);
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 3px solid transparent;
        background-clip: padding-box;
        position: relative;
        z-index: 1;
    }
    
    .main-container::before {
        content: '';
        position: absolute;
        top: -3px; left: -3px; right: -3px; bottom: -3px;
        background: linear-gradient(45deg, #00B4D8, #20C997, #FFC107, #FF5722, #9C27B0);
        border-radius: 23px;
        z-index: -1;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(180deg); }
    }
    
    .stButton button {
        background: linear-gradient(45deg, #00B4D8, #20C997);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,180,216,0.4);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,180,216,0.6);
        background: linear-gradient(45deg, #20C997, #00B4D8);
    }
    
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #00B4D8;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #FF5722;
        box-shadow: 0 0 0 2px rgba(255,87,34,0.2);
    }
    
    .slider-container {
        background: linear-gradient(45deg, #E3F2FD, #F3E5F5);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    .success-box {
        background: linear-gradient(45deg, #4CAF50, #8BC34A);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .header-animation {
        background: linear-gradient(45deg, #00B4D8, #FF5722, #9C27B0, #FFC107);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientText 6s ease infinite;
    }
    
    @keyframes gradientText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
</style>
""", unsafe_allow_html=True)

# Create bubbles
bubbles_html = ""
for i in range(15):
    size = random.randint(20, 60)
    left = random.randint(0, 95)
    duration = random.randint(10, 30)
    delay = random.randint(0, 10)
    bubbles_html += f"""
    <div class="bubble" style="
        left: {left}vw; 
        width: {size}px; 
        height: {size}px; 
        animation-duration: {duration}s;
        animation-delay: {delay}s;
        background: radial-gradient(circle at 30% 30%, 
            rgba({random.randint(200,255)},{random.randint(200,255)},{random.randint(200,255)},0.8), 
            rgba({random.randint(0,180)},{random.randint(100,216)},{random.randint(150,255)},0.4));
    "></div>
    """

# Create waves
waves_html = """
<div class="wave-container">
    <div class="wave"></div>
    <div class="wave"></div>
</div>
"""

# Inject bubbles and waves
st.markdown(bubbles_html + waves_html, unsafe_allow_html=True)

# Main content
st.markdown(
    """
    <div class="main-container">
        <h1 class="header-animation" style='text-align:center; font-size:3rem; margin-bottom:0.5rem;'>💥 Extreme Rewriter</h1>
        <p style='text-align:center; color:#666; font-size:1.2rem; margin-bottom:2rem;'>
            Transform any text into a unique version with <span style="color:#FF5722; font-weight:bold;"><20% similarity</span>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input section in main container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    input_text = st.text_area(
        "✏️ **Enter your text here:**", 
        height=180, 
        placeholder="Paste or type your text...",
        help="Enter the text you want to rewrite with low similarity"
    )

    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    target_similarity = st.slider(
        "🎯 **Target Similarity (%)**", 
        5, 50, 20, step=1,
        help="Set your desired maximum similarity percentage"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🚀 **Rewrite Now**", use_container_width=True):
            if not input_text.strip():
                st.warning("⚠️ **Please enter some text first!**")
            else:
                with st.spinner("🔮 **Rewriting your text with magic...**"):
                    # Your backend function call remains the same
                    rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
                
                if similarity <= target_similarity:
                    st.markdown(
                        f'<div class="success-box">'
                        f'<h3>🎉 Success! Achieved Similarity: {similarity:.1f}%</h3>'
                        f'<p>Your text has been transformed below target! ✨</p>'
                        f'</div>', 
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<h4 style='color:#FF9800; text-align:center;'>"
                        f"⚠️ Similarity: {similarity:.1f}% (Target: {target_similarity}%)"
                        f"</h4>", 
                        unsafe_allow_html=True
                    )
                
                colA, colB = st.columns(2)
                with colA:
                    st.subheader("📘 Original Text")
                    st.text_area("Original", input_text, height=200, key="original")
                with colB:
                    st.subheader("✨ Rewritten Text")
                    st.text_area("Rewritten", rewritten, height=200, key="rewritten")
    
    with col3:
        if st.button("🧹 **Clear All**", use_container_width=True):
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:#666; padding:1rem;'>
        <p style='font-size:1.1rem; margin-bottom:0.5rem;'>
            ⚙️ Powered by <span style="color:#00B4D8; font-weight:bold;">Streamlit</span> | 
            🎨 Developed by <span style="color:#FF5722; font-weight:bold;">Zari's AI Lab</span>
        </p>
        <p style='font-size:0.9rem; color:#999;'>
            ✨ Magical text transformation with animated wonders! ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
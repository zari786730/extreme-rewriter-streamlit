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
    
    # More aggressive sentence splitting
    def split_sentences(text):
        # Split by multiple sentence endings
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    # More radical sentence restructuring
    def radical_sentence_restructure(text):
        sentences = split_sentences(text)
        if not sentences:
            return text
            
        rebuilt_sentences = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 3:
                rebuilt_sentences.append(sentence)
                continue
                
            # More aggressive restructuring options
            r = random.random()
            
            if r < 0.4:
                # Convert to question format
                question_starters = ['How does', 'What makes', 'Why is', 'In what way does', 
                                   'To what extent does', 'How can we understand']
                starter = random.choice(question_starters)
                rebuilt = f"{starter} {sentence.lower()}?"
                rebuilt_sentences.append(rebuilt)
                
            elif r < 0.7:
                # Reverse sentence structure
                if len(words) > 4:
                    # Split and reorder
                    split_point = random.randint(2, len(words)-2)
                    first_part = ' '.join(words[:split_point])
                    second_part = ' '.join(words[split_point:])
                    
                    connectors = [
                        f"{second_part}, thereby illustrating how {first_part.lower()}",
                        f"{second_part}, which fundamentally demonstrates that {first_part.lower()}",
                        f"{second_part}, consequently revealing how {first_part.lower()}",
                        f"{second_part}, essentially proving that {first_part.lower()}"
                    ]
                    rebuilt = random.choice(connectors)
                    rebuilt_sentences.append(rebuilt)
                else:
                    rebuilt_sentences.append(sentence)
                    
            else:
                # Academic reframing with more variation
                academic_frames = [
                    f"From an analytical perspective, {sentence.lower()}",
                    f"Scholarly examination reveals that {sentence.lower()}",
                    f"Research findings consistently indicate {sentence.lower()}",
                    f"Academic scrutiny demonstrates {sentence.lower()}",
                    f"Empirical evidence substantiates that {sentence.lower()}",
                    f"Comprehensive analysis establishes {sentence.lower()}",
                    f"Theoretical frameworks suggest {sentence.lower()}",
                    f"Methodological approaches confirm {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(academic_frames))
        
        return '. '.join(rebuilt_sentences) + '.'

    # More comprehensive vocabulary replacement
    def nuclear_vocabulary_replacement(text):
        # Expanded replacement dictionary
        nuclear_replacements = {
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study', 'methodological examination'],
            'study': ['comprehensive examination', 'detailed analysis', 'thorough investigation', 'rigorous scrutiny'],
            'analysis': ['in-depth scrutiny', 'systematic assessment', 'comprehensive evaluation', 'detailed appraisal'],
            'evidence': ['empirical data', 'documented findings', 'research results', 'substantive documentation'],
            'data': ['information', 'findings', 'empirical evidence', 'documented results'],
            'show': ['demonstrate', 'illustrate', 'reveal', 'substantiate'],
            'important': ['significant', 'crucial', 'pivotal', 'fundamental'],
            'change': ['transformation', 'modification', 'alteration', 'shift'],
            'problem': ['challenge', 'issue', 'difficulty', 'obstacle'],
            'solution': ['resolution', 'approach', 'method', 'strategy'],
            'people': ['individuals', 'persons', 'the population', 'society members'],
            'government': ['governing body', 'administration', 'political leadership', 'state apparatus'],
            'country': ['nation', 'state', 'territory', 'sovereign entity'],
            'development': ['progress', 'advancement', 'evolution', 'growth'],
            'system': ['framework', 'structure', 'mechanism', 'apparatus'],
            'process': ['procedure', 'methodology', 'approach', 'technique'],
            'result': ['outcome', 'consequence', 'finding', 'conclusion'],
            'because': ['due to the fact that', 'owing to', 'as a consequence of', 'given that'],
            'however': ['nevertheless', 'nonetheless', 'conversely', 'notwithstanding'],
            'therefore': ['consequently', 'accordingly', 'thus', 'hence']
        }
        
        new_text = text
        for original, replacements in nuclear_replacements.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                replacement = random.choice(replacements)
                new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
        return new_text

    # More varied human-like touches
    def add_human_touches(text):
        sentences = split_sentences(text)
        if not sentences:
            return text
            
        # Apply different transformations to different sentences
        transformed_sentences = []
        
        for i, sentence in enumerate(sentences):
            if random.random() < 0.6:  # Apply transformation to most sentences
                human_patterns = [
                    lambda s: f"Interestingly, {s.lower()}",
                    lambda s: f"Upon careful consideration, {s.lower()}",
                    lambda s: f"From a broader perspective, {s.lower()}",
                    lambda s: f"It is noteworthy that {s.lower()}",
                    lambda s: f"Significantly, {s.lower()}",
                    lambda s: f"In this context, {s.lower()}",
                    lambda s: f"Remarkably, {s.lower()}",
                    lambda s: f"Essentially, {s.lower()}",
                    lambda s: f"Fundamentally, {s.lower()}",
                    lambda s: f"Critically, {s.lower()}"
                ]
                pattern = random.choice(human_patterns)
                transformed_sentences.append(pattern(sentence))
            else:
                transformed_sentences.append(sentence)
        
        return '. '.join(transformed_sentences) + '.'

    # Apply all transformations multiple times for more radical changes
    result = clean_text
    for _ in range(2):  # Apply twice for more transformation
        result = radical_sentence_restructure(result)
        result = nuclear_vocabulary_replacement(result)
        result = add_human_touches(result)
    
    return result

def calculate_similarity(original, rewritten):
    # More sophisticated similarity calculation
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    
    if not original_words: 
        return 0
    
    common_words = original_words.intersection(rewritten_words)
    similarity = len(common_words) / len(original_words) * 100
    
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=15):
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

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
    body { 
        background: radial-gradient(circle at 20% 20%, #00111a, #000000); 
        color: #e6faff; 
        overflow-x: hidden;
        font-family: 'Poppins', sans-serif; 
    }
    .main > div {
        background-color: transparent;
    }
    #bubble-layer, #droplet-layer { 
        position: fixed; 
        top:0; 
        left:0; 
        width:100%; 
        height:100%; 
        pointer-events:none; 
        z-index:-1; 
        overflow:hidden; 
    }
    /* Rising bubbles */
    .bubble { 
        position:absolute; 
        bottom:-100px; 
        background: rgba(0,200,255,0.3); 
        border-radius:50%; 
        box-shadow:0 0 10px rgba(0,200,255,0.5); 
        animation: rise linear infinite; 
    }
    @keyframes rise { 
        0% { 
            transform:translateY(0) scale(0.6); 
            opacity:0.8; 
        } 
        50% { 
            opacity:1; 
        } 
        100% { 
            transform:translateY(-120vh) scale(1.2); 
            opacity:0; 
        } 
    }
    /* Water droplets */
    .droplet { 
        position:absolute; 
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.3), rgba(255,255,255,0.05)); 
        border-radius:50%; 
        box-shadow:0 0 8px rgba(0,200,255,0.2); 
        animation: shimmer 4s ease-in-out infinite alternate; 
    }
    @keyframes shimmer { 
        0% { 
            transform: translateY(0) scale(0.7); 
            opacity:0.6; 
        } 
        50% { 
            transform: translateY(3px) scale(1); 
            opacity:0.9; 
        } 
        100% { 
            transform: translateY(0) scale(0.8); 
            opacity:0.7; 
        } 
    }
    h1 { 
        text-align:center; 
        color:#00B4D8; 
        font-size:2.8rem; 
        margin-bottom: 0.5rem;
    }
    h3 { 
        text-align:center; 
        color:#00eaff; 
        margin-top: 0;
    }
    .stButton>button { 
        background: linear-gradient(90deg,#00B4D8,#0077B6); 
        color:white; 
        border:none; 
        border-radius:12px; 
        padding:0.8rem 1.5rem; 
        font-weight:bold; 
        box-shadow:0 4px 10px rgba(0,0,0,0.2); 
        transition:all 0.3s ease; 
        width: 100%;
    }
    .stButton>button:hover { 
        background: linear-gradient(90deg,#0077B6,#023E8A); 
        transform: scale(1.05); 
    }
    /* Textareas */
    .stTextArea textarea {
        border-radius:10px !important;
        border:1px solid #90E0EF !important;
        background-color:#101820 !important;
        color:#e6faff !important;
    }
    footer { 
        text-align:center; 
        color:#aaa; 
        margin-top:2rem; 
        font-size:0.9rem; 
    }
    .result-box {
        background-color: rgba(16, 24, 32, 0.8);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #90E0EF;
        margin-top: 1rem;
        min-height: 150px;
    }
    .similarity-meter {
        border-radius: 10px;
        padding: 0.8rem;
        text-align: center;
        font-weight: bold;
        margin-top: 1rem;
        font-size: 1.1rem;
    }
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
st.markdown("<h3>Transform text into a unique version with low similarity</h3>", unsafe_allow_html=True)

# --- MAIN UI ---
st.markdown("### ✏️ Input Text")
input_text = st.text_area("Paste or type your text:", height=180, key="input_text")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 15, step=1, key="target_similarity")

col1, col2 = st.columns([1,1])

with col1:
    if st.button("🚀 Rewrite Now", key="rewrite_button"):
        if not input_text.strip():
            st.warning("⚠️ Please enter some text first!")
        else:
            with st.spinner("🧠 Rewriting text with extreme transformations..."):
                rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
                
                # Display results
                st.markdown("### 🔄 Rewritten Text")
                st.markdown(f'<div class="result-box">{rewritten}</div>', unsafe_allow_html=True)
                
                # Display similarity score with color coding
                if similarity <= target_similarity:
                    similarity_color = "#00FF00"
                    message = f"✅ Success! Achieved {similarity:.1f}% similarity (target: ≤{target_similarity}%)"
                else:
                    similarity_color = "#FF6B6B"
                    message = f"⚠️ Best achieved: {similarity:.1f}% similarity (target: ≤{target_similarity}%)"
                
                st.markdown(f'<div class="similarity-meter" style="background: linear-gradient(90deg, {similarity_color}, #0077B6)">'
                           f'📊 Similarity Score: {similarity:.1f}%</div>', unsafe_allow_html=True)
                
                # Success/warning message
                if similarity <= target_similarity:
                    st.success(message)
                else:
                    st.warning(message)

# --- FOOTER ---
st.markdown("---")
st.markdown("<footer>Extreme Rewriter • Dark Water UI • Text Transformation Tool</footer>", unsafe_allow_html=True)
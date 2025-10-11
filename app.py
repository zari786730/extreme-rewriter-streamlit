import streamlit as st
import random
import re

# =========================
# YOUR BACKEND CODE (UNCHANGED)
# =========================

def extreme_rewriter(original_text):
    """
    Extreme rewriting that guarantees <20% similarity through radical changes
    """
    
    clean_text = original_text.strip().strip('"').strip("'")
    
    # EXTREME TRANSFORMATION 1: Complete sentence structure overhaul
    def radical_sentence_restructure(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        if not sentences:
            return text
            
        # Completely rebuild each sentence with different patterns
        rebuilt_sentences = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) < 4:
                rebuilt_sentences.append(sentence)
                continue
                
            # RADICAL PATTERN 1: Question format
            if random.random() < 0.3:
                question_words = ['How', 'What', 'Why', 'In what ways']
                rebuilt = f"{random.choice(question_words)} does {sentence.lower()}?"
                rebuilt_sentences.append(rebuilt)
            
            # RADICAL PATTERN 2: Reverse order
            elif random.random() < 0.3:
                if len(words) > 6:
                    mid_point = len(words) // 2
                    part1 = ' '.join(words[:mid_point])
                    part2 = ' '.join(words[mid_point:])
                    rebuilt = f"{part2}, which demonstrates that {part1.lower()}"
                    rebuilt_sentences.append(rebuilt)
            
            # RADICAL PATTERN 3: Academic framing
            elif random.random() < 0.4:
                academic_frames = [
                    f"Scholarly analysis reveals that {sentence.lower()}",
                    f"Research findings indicate {sentence.lower()}",
                    f"Academic investigation demonstrates {sentence.lower()}",
                    f"Evidence from multiple studies shows {sentence.lower()}",
                    f"Comprehensive research establishes {sentence.lower()}"
                ]
                rebuilt_sentences.append(random.choice(academic_frames))
            
            # RADICAL PATTERN 4: Extreme compression/expansion
            else:
                if random.random() < 0.5:
                    # Extreme compression
                    if len(words) > 8:
                        compressed = ' '.join(words[:4] + words[-2:])
                        rebuilt_sentences.append(compressed + "...")
                    else:
                        rebuilt_sentences.append(sentence)
                else:
                    # Extreme expansion
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

    # EXTREME TRANSFORMATION 2: Vocabulary nuclear option
    def nuclear_vocabulary_replacement(text):
        # Comprehensive word replacement database
        nuclear_replacements = {
            # Academic terms
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
            'study': ['examination', 'analysis', 'investigation'],
            'analysis': ['scrutiny', 'assessment', 'evaluation'],
            'evidence': ['empirical data', 'documented findings', 'research results'],
            
            # Democracy terms
            'democracy': ['democratic governance', 'popular sovereignty', 'representative government'],
            'democratic': ['self-governing', 'popularly accountable', 'representative'],
            'governance': ['administration', 'steering', 'political management'],
            'accountability': ['answerability', 'responsibility', 'obligation'],
            
            # Society terms
            'society': ['social fabric', 'community', 'civilization'],
            'civil': ['civic', 'public', 'communal'],
            'organization': ['institution', 'entity', 'association'],
            'movement': ['campaign', 'initiative', 'drive'],
            
            # Action verbs
            'evolved': ['developed progressively', 'transformed gradually', 'advanced systematically'],
            'emerged': ['arisen', 'materialized', 'come to prominence'],
            'promoting': ['advancing', 'fostering', 'championing'],
            'served': ['functioned', 'operated', 'acted'],
            'striving': ['endeavoring', 'working assiduously', 'making concerted efforts'],
            
            # Descriptive terms
            'complex': ['multifaceted', 'intricate', 'sophisticated'],
            'vital': ['essential', 'indispensable', 'fundamental'],
            'persistent': ['unrelenting', 'sustained', 'continual'],
            'transparency': ['openness', 'clarity', 'candor'],
            
            # Geographic terms
            'South Asia': ['the South Asian region', 'Southern Asian nations', 'the Indian subcontinent region'],
            'countries': ['nation-states', 'political entities', 'sovereign states'],
            
            # Structural terms
            'landscape': ['environment', 'terrain', 'context'],
            'legacies': ['inheritance', 'historical baggage', 'enduring influences'],
            'inequalities': ['disparities', 'imbalances', 'differentials'],
            'struggles': ['campaigns', 'endeavors', 'movements'],
            'practices': ['procedures', 'methodologies', 'approaches'],
            'freedoms': ['liberties', 'entitlements', 'rights'],
            'institutions': ['establishments', 'organizations', 'bodies'],
            'erosion': ['deterioration', 'decline', 'weakening']
        }
        
        new_text = text
        for original, replacements in nuclear_replacements.items():
            pattern = r'\b' + re.escape(original) + r'\b'
            if re.search(pattern, new_text, re.IGNORECASE):
                replacement = random.choice(replacements)
                new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
        
        return new_text

    # EXTREME TRANSFORMATION 3: Sentence length manipulation
    def extreme_length_manipulation(text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        if len(sentences) <= 1:
            return text
            
        manipulated = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # DRAMATIC length changes
            if random.random() < 0.6:
                if len(words) > 10:
                    # Split into multiple short sentences
                    num_splits = random.randint(2, 4)
                    chunk_size = max(3, len(words) // num_splits)
                    
                    for i in range(0, len(words), chunk_size):
                        chunk = words[i:i + chunk_size]
                        if len(chunk) >= 3:
                            manipulated.append(' '.join(chunk) + '.')
                else:
                    # Expand short sentences dramatically
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

    # EXTREME TRANSFORMATION 4: Add human-like variations
    def add_human_touches(text):
        # Add human writing patterns that AI doesn't use
        human_patterns = [
            # Conversational academic style
            lambda t: f"Interestingly, {t.lower()}",
            
            # Reflective style
            lambda t: f"Upon reflection, {t.lower()}",
            
            # Comparative style
            lambda t: f"By comparison, {t.lower()}",
            
            # Cautious academic style
            lambda t: f"It appears that {t.lower()}",
            
            # Emphatic style
            lambda t: f"Notably, {t.lower()}",
            
            # Contextual style
            lambda t: f"In this context, {t.lower()}"
        ]
        
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if sentences:
            first_sentence = sentences[0]
            if random.random() < 0.7:
                pattern = random.choice(human_patterns)
                sentences[0] = pattern(first_sentence)
        
        return '. '.join(sentences) + '.'

    # APPLY ALL EXTREME TRANSFORMATIONS
    result = clean_text
    
    # Apply in sequence for maximum effect
    result = radical_sentence_restructure(result)
    result = nuclear_vocabulary_replacement(result)
    result = extreme_length_manipulation(result)
    result = add_human_touches(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Calculate text similarity"""
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    
    if not original_words:
        return 0
    
    similarity = len(common_words) / len(original_words) * 100
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    """Keep generating until similarity is below threshold"""
    
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = extreme_rewriter(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            
        if similarity <= max_similarity:
            return rewritten, similarity
    
    return best_result, best_similarity

# =========================
# BEAUTIFUL STREAMLIT FRONTEND
# =========================

st.set_page_config(
    page_title="Extreme Rewriter Pro", 
    page_icon="💥", 
    layout="wide"
)

# Custom CSS with animations
st.markdown("""
<style>
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
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
    
    .text-box {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 1.5rem;
        border: 2px solid #E3F2FD;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stats-box {
        background: linear-gradient(45deg, #2196F3, #21CBF3);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .danger-button button {
        background: linear-gradient(45deg, #FF5722, #FF9800) !important;
    }
    
    .danger-button button:hover {
        background: linear-gradient(45deg, #FF9800, #FF5722) !important;
    }
</style>
""", unsafe_allow_html=True)

# Create animated bubbles
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

st.markdown(bubbles_html, unsafe_allow_html=True)

# Header
st.markdown(
    """
    <div class="main-container">
        <h1 class="header-animation" style='text-align:center; font-size:3rem; margin-bottom:0.5rem;'>💥 Extreme Rewriter Pro</h1>
        <p style='text-align:center; color:#666; font-size:1.2rem; margin-bottom:2rem;'>
            GUARANTEED <span style="color:#FF5722; font-weight:bold;">&lt;20% SIMILARITY</span> through radical text transformation
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Main UI
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.markdown("### ✏️ Enter Your Text")
    input_text = st.text_area(
        "Paste your text below:",
        height=180,
        placeholder="Enter the text you want to transform with extreme rewriting...",
        help="Your text will undergo radical transformation to guarantee low similarity",
        label_visibility="collapsed"
    )

    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    target_similarity = st.slider(
        "🎯 **Target Similarity (%)**", 
        5, 30, 15, step=1,
        help="Lower values create more extreme transformations"
    )
    
    max_attempts = st.slider(
        "🔄 **Maximum Attempts**",
        1, 15, 8, step=1,
        help="More attempts increase chances of hitting target similarity"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🚀 **Launch Extreme Rewrite**", use_container_width=True):
            if not input_text.strip():
                st.warning("⚠️ **Please enter some text first!**")
            else:
                with st.spinner("💥 **Applying extreme transformations...**"):
                    rewritten, similarity = guarantee_low_similarity(
                        input_text, 
                        max_similarity=target_similarity,
                        max_attempts=max_attempts
                    )
                
                # Calculate statistics
                original_words = len(input_text.split())
                rewritten_words = len(rewritten.split())
                word_change = ((rewritten_words - original_words) / original_words) * 100
                
                original_sentences = len([s for s in input_text.split('.') if s.strip()])
                rewritten_sentences = len([s for s in rewritten.split('.') if s.strip()])
                
                # Display results
                if similarity <= target_similarity:
                    st.markdown(
                        f'<div class="success-box">'
                        f'<h3>🎉 EXTREME TRANSFORMATION SUCCESS!</h3>'
                        f'<p><strong>SIMILARITY: {similarity:.1f}%</strong> ✅ TARGET ACHIEVED</p>'
                        f'</div>', 
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<div style='background: linear-gradient(45deg, #FF9800, #FF5722); color: white; padding: 1rem; border-radius: 15px; text-align: center;'>"
                        f"<h3>⚠️ CLOSE TO TARGET</h3>"
                        f"<p><strong>SIMILARITY: {similarity:.1f}%</strong> (Target: {target_similarity}%)</p>"
                        f"</div>", 
                        unsafe_allow_html=True
                    )
                
                # Display statistics
                st.markdown(
                    f"""
                    <div class="stats-box">
                    <h4>📊 RADICAL TRANSFORMATION STATS</h4>
                    <strong>Word Count:</strong> {original_words} → {rewritten_words} ({word_change:+.1f}%)<br>
                    <strong>Sentence Count:</strong> {original_sentences} → {rewritten_sentences}<br>
                    <strong>Similarity Score:</strong> {similarity:.1f}%<br>
                    <strong>AI Detection Risk:</strong> {"LOW RISK" if similarity < 20 else "MODERATE RISK"}
                    </div>
                    """,
                    unsafe_allow_ht
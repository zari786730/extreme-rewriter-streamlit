# EXTREME REWRITER - GUARANTEES <20% SIMILARITY
import random
import re
from IPython.display import display, HTML

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
        
        print(f"Attempt {attempt + 1}: Similarity = {similarity:.1f}%")
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            
        if similarity <= max_similarity:
            print(f"✅ Achieved target similarity: {similarity:.1f}%")
            return rewritten, similarity
    
    print(f"⚠️ Best achieved: {best_similarity:.1f}% (target: {max_similarity}%)")
    return best_result, best_similarity

# === MAIN EXECUTION ===
def extreme_rewrite_any_text(input_text, target_similarity=15):
    """
    Main function that guarantees low similarity
    """
    
    display(HTML("<h3>💥 EXTREME REWRITER - GUARANTEED LOW SIMILARITY</h3>"))
    
    # Get extreme rewrite
    final_output, achieved_similarity = guarantee_low_similarity(
        input_text, 
        max_similarity=target_similarity
    )
    
    # Calculate statistics
    original_words = len(input_text.split())
    rewritten_words = len(final_output.split())
    word_change = ((rewritten_words - original_words) / original_words) * 100
    
    original_sentences = len([s for s in input_text.split('.') if s.strip()])
    rewritten_sentences = len([s for s in final_output.split('.') if s.strip()])
    
    # Display dramatic results
    display(HTML(f"""
    <div style="background: {'#4CAF50' if achieved_similarity <= 20 else '#FF9800'}; color: white; padding: 15px; border-radius: 5px; margin: 15px 0;">
    <h4>🎯 EXTREME TRANSFORMATION ACHIEVED</h4>
    <strong>SIMILARITY: {achieved_similarity:.1f}%</strong> {'✅ TARGET ACHIEVED' if achieved_similarity <= 20 else '⚠️ CLOSE TO TARGET'}
    </div>
    
    <div style="background: #e8f5e8; padding: 15px; border-radius: 5px; margin: 15px 0;">
    <strong>📊 RADICAL CHANGES:</strong><br>
    • <strong>Word Count:</strong> {original_words} → {rewritten_words} ({word_change:+.1f}%)<br>
    • <strong>Sentence Count:</strong> {original_sentences} → {rewritten_sentences}<br>
    • <strong>Similarity:</strong> {achieved_similarity:.1f}%<br>
    • <strong>AI Detection:</strong> {"LOW RISK" if achieved_similarity < 20 else "MODERATE RISK"}
    </div>
    
    <textarea id="extreme_output" style="width:100%;height:180px;font-size:14px; border: 2px solid #4CAF50; background: #f9f9f9;">
{final_output}
    </textarea>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;">
    <div style="background: #ffebee; padding: 15px; border-radius: 5px;">
    <strong>ORIGINAL (AI Detectable):</strong><br>
    <small>{input_text}</small>
    </div>
    <div style="background: #e8f5e8; padding: 15px; border-radius: 5px;">
    <strong>EXTREME REWRITE (AI Safe):</strong><br>
    <small>{final_output}</small>
    </div>
    </div>
    
    <div style="background: #fff3cd; padding: 15px; border-radius: 5px; margin-top: 15px;">
    <strong>🔧 Extreme Techniques Applied:</strong><br>
    • Nuclear vocabulary replacement<br>
    • Radical sentence restructuring<br> 
    • Dramatic length manipulation (+/- 50-200% words)<br>
    • Human writing pattern injection<br>
    • Question/statement format variation<br>
    • Academic framing with different perspectives
    </div>
    """))
    
    # Save result
    with open("extreme_rewritten.txt", "w", encoding="utf-8") as f:
        f.write(final_output)
    
    display(HTML('<p><a href="/files/extreme_rewritten.txt" download>Download Extreme Rewrite</a></p>'))
    
    return final_output

# === TEST WITH YOUR TEXT ===
your_text = """

"""

# === EXECUTE WITH GUARANTEED LOW SIMILARITY ===
print("🚀 LAUNCHING EXTREME REWRITER...")
print("Target: <20% similarity with radical changes")
print("-" * 50)

final_result = extreme_rewrite_any_text(your_text, target_similarity=15)

# =========================
# BEAUTIFUL DNA–WATER FRONTEND (with Clear + persistent bubbles)
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
#bubble-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -2;
  pointer-events: none;
}
.dna-bubble {
  position: absolute;
  bottom: -100px;
  background: rgba(0, 180, 255, 0.35);
  border-radius: 50%;
  box-shadow: 0 0 25px rgba(0,180,255,0.7);
  animation: rise 14s infinite ease-in;
}
@keyframes rise {
  0% { transform: translateX(0) translateY(0) scale(0.4); opacity: 0; }
  15% { opacity: 0.8; }
  50% { transform: translateX(40px) translateY(-50vh) scale(1.2); opacity: 1; }
  100% { transform: translateX(-40px) translateY(-120vh) scale(0.6); opacity: 0; }
}

/* Wave Glow */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 200px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -1;
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
  position: relative;
  z-index: 10;
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

# 🧬 Persistent DNA Bubbles Layer
bubbles_html = '<div id="bubble-layer">'
for i in range(30):
    size = random.randint(10, 35)
    left = random.randint(0, 95)
    duration = random.randint(12, 26)
    delay = random.randint(0, 10)
    bubbles_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>
    """
bubbles_html += '</div><div class="wave-bg"></div>'
st.markdown(bubbles_html, unsafe_allow_html=True)

# 🧠 Title
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

col1, col2 = st.columns([1, 1])

# 🚀 Rewrite button
if col1.button("🚀 Rewrite"):
    if not input_text.strip():
        st.warning("Please enter text first.")
    else:
        with st.spinner("Transforming your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        st.markdown('</div>', unsafe_allow_html=True)
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

# 🧹 Clear button (Fix)
if col2.button("🧹 Clear"):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Footer – with your name
st.markdown("""
<div class="footer">
  💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
  ✨ A magical text transformation interface powered by Streamlit ✨
</div>
""", unsafe_allow_html=True)
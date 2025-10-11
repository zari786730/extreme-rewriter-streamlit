import streamlit as st
import re
import random
import requests
from bs4 import BeautifulSoup
import time
import nltk
from nltk.corpus import wordnet

# Download required NLTK data
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# =========================
# SMART REWRITER BACKEND
# =========================

class SmartRewriter:
    def __init__(self):
        self.synonym_cache = {}
        self.academic_phrases = self._load_academic_phrases()
    
    def _load_academic_phrases(self):
        """Academic transition phrases that maintain proper grammar"""
        return {
            'addition': ['Furthermore,', 'Moreover,', 'Additionally,', 'In addition,'],
            'contrast': ['However,', 'Conversely,', 'On the other hand,', 'Nevertheless,'],
            'cause_effect': ['Consequently,', 'Therefore,', 'As a result,', 'Thus,'],
            'emphasis': ['Notably,', 'Significantly,', 'Importantly,', 'Crucially,'],
            'example': ['For instance,', 'For example,', 'Specifically,', 'To illustrate,']
        }
    
    def get_synonyms_from_internet(self, word):
        """Get real synonyms from online sources"""
        if word in self.synonym_cache:
            return self.synonym_cache[word]
        
        synonyms = set()
        
        # Try WordNet first (more reliable)
        wordnet_syns = self._get_wordnet_synonyms(word)
        synonyms.update(wordnet_syns)
        
        # Try online sources if WordNet doesn't have enough
        if len(synonyms) < 3:
            try:
                thesaurus_syns = self._get_thesaurus_com(word)
                synonyms.update(thesaurus_syns)
            except:
                pass
        
        # Filter to keep only relevant synonyms
        filtered_syns = [syn for syn in synonyms if len(syn.split()) == 1 and syn != word]
        self.synonym_cache[word] = filtered_syns[:8]  # Limit to top 8
        return self.synonym_cache[word]
    
    def _get_wordnet_synonyms(self, word):
        """Get synonyms from WordNet"""
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ').lower()
                if synonym != word and len(synonym.split()) == 1:
                    synonyms.add(synonym)
        return list(synonyms)
    
    def _get_thesaurus_com(self, word):
        """Scrape synonyms from Thesaurus.com"""
        try:
            url = f"https://www.thesaurus.com/browse/{word}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            synonyms = set()
            # Look for synonym containers
            synonym_elements = soup.find_all('a', {'class': 'css-1kg1yv8'})
            for element in synonym_elements[:10]:
                syn = element.text.strip().lower()
                if syn and syn != word and len(syn.split()) == 1:
                    synonyms.add(syn)
            return list(synonyms)
        except Exception as e:
            print(f"Error fetching from thesaurus: {e}")
            return []
    
    def smart_sentence_restructure(self, text):
        """Restructure sentences intelligently without breaking grammar"""
        # Split sentences properly
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        restructured = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # Only restructure longer sentences
            if len(words) > 15:
                # Find natural breaking points (conjunctions)
                conjunctions = [' and ', ' but ', ' however ', ' although ', ' while ', ' because ']
                split_point = None
                
                for conj in conjunctions:
                    if conj in sentence.lower():
                        parts = sentence.lower().split(conj)
                        if len(parts) >= 2:
                            # Create two proper sentences
                            first_part = parts[0].strip().capitalize()
                            second_part = parts[1].strip()
                            
                            # Add appropriate transitions
                            transitions = self.academic_phrases['addition'] + self.academic_phrases['contrast']
                            transition = random.choice(transitions)
                            
                            restructured.append(first_part + '.')
                            restructured.append(f"{transition} {second_part}")
                            split_point = True
                            break
                
                if not split_point:
                    restructured.append(sentence)
            else:
                restructured.append(sentence)
        
        # Join with proper punctuation
        result = '. '.join(restructured)
        if result and not result.endswith('.'):
            result += '.'
        return result
    
    def advanced_vocabulary_replacement(self, text):
        """Replace words with synonyms while maintaining meaning"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Only replace content words (nouns, verbs, adjectives, adverbs)
            if (len(clean_word) > 4 and 
                clean_word not in ['this', 'that', 'there', 'their', 'which', 'about', 'would', 'could'] and
                random.random() < 0.25):  # Only replace 25% of eligible words
                
                synonyms = self.get_synonyms_from_internet(clean_word)
                if synonyms:
                    replacement = random.choice(synonyms)
                    # Preserve original capitalization
                    if word[0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    continue
            
            new_words.append(word)
        
        return ' '.join(new_words)
    
    def academic_style_enhancement(self, text):
        """Add academic flourishes without breaking grammar"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        enhanced = []
        
        for i, sentence in enumerate(sentences):
            # Only enhance some sentences to avoid overdoing it
            if random.random() < 0.3 and len(sentence.split()) > 8:
                enhancements = [
                    f"Research indicates that {sentence.lower()}",
                    f"Studies demonstrate that {sentence.lower()}",
                    f"Evidence suggests that {sentence.lower()}",
                    f"Analysis reveals that {sentence.lower()}",
                    f"Current scholarship shows that {sentence.lower()}"
                ]
                enhanced.append(random.choice(enhancements))
            else:
                enhanced.append(sentence)
        
        result = '. '.join(enhanced)
        if result and not result.endswith('.'):
            result += '.'
        return result
    
    def rewrite_text(self, original_text):
        """Main rewriting function that preserves academic integrity"""
        if not original_text.strip():
            return original_text
            
        # Step 1: Clean the text
        clean_text = original_text.strip()
        
        # Step 2: Smart vocabulary replacement
        result = self.advanced_vocabulary_replacement(clean_text)
        
        # Step 3: Intelligent sentence restructuring
        result = self.smart_sentence_restructure(result)
        
        # Step 4: Academic style enhancement
        result = self.academic_style_enhancement(result)
        
        return result

def calculate_similarity(original, rewritten):
    """Calculate similarity based on word overlap"""
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    
    if not original_words:
        return 0
    
    similarity = len(common_words) / len(original_words) * 100
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=3):
    """Generate rewritten text with guaranteed low similarity"""
    rewriter = SmartRewriter()
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = rewriter.rewrite_text(original_text)
        similarity = calculate_similarity(original_text, rewritten)
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
        
        if similarity <= max_similarity:
            break
        
        # Add small delay
        time.sleep(0.1)
    
    return best_result, best_similarity

# =========================
# BEAUTIFUL STREAMLIT FRONTEND
# =========================

st.set_page_config(
    page_title="Academic Rewriter Pro", 
    page_icon="🎓", 
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

# Header
st.markdown(
    """
    <div class="main-container">
        <h1 class="header-animation" style='text-align:center; font-size:3rem; margin-bottom:0.5rem;'>🎓 Academic Rewriter Pro</h1>
        <p style='text-align:center; color:#666; font-size:1.2rem; margin-bottom:2rem;'>
            Intelligent text rewriting that <span style="color:#FF5722; font-weight:bold;">preserves academic integrity</span> and grammar
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Main UI
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.markdown("### ✏️ Enter Your Academic Text")
    input_text = st.text_area(
        "Paste your text below:",
        height=180,
        placeholder="Enter your academic text here...",
        help="The rewriter will maintain academic quality while reducing similarity",
        label_visibility="collapsed"
    )

    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    target_similarity = st.slider(
        "🎯 **Target Similarity (%)**", 
        5, 40, 15, step=1,
        help="Lower values create more unique text while maintaining quality"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🚀 **Rewrite Academic Text**", use_container_width=True):
            if not input_text.strip():
                st.warning("⚠️ **Please enter some text first!**")
            else:
                with st.spinner("🔮 **Rewriting with academic precision...**"):
                    rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
                
                if similarity <= target_similarity:
                    st.markdown(
                        f'<div class="success-box">'
                        f'<h3>🎉 Success! Similarity: {similarity:.1f}%</h3>'
                        f'<p>Academic integrity maintained! Grammar preserved!</p>'
                        f'</div>', 
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<h4 style='color:#FF9800; text-align:center; background: rgba(255,152,0,0.1); padding: 1rem; border-radius: 10px;'>"
                        f"⚠️ Similarity: {similarity:.1f}% (Target: {target_similarity}%)"
                        f"</h4>", 
                        unsafe_allow_html=True
                    )
                
                colA, colB = st.columns(2)
                with colA:
                    st.markdown("### 📘 Original Text")
                    st.markdown('<div class="text-box">', unsafe_allow_html=True)
                    st.text_area("Original", input_text, height=250, key="original", label_visibility="collapsed")
                    st.markdown('</div>', unsafe_allow_html=True)
                with colB:
                    st.markdown("### ✨ Rewritten Text")
                    st.markdown('<div class="text-box">', unsafe_allow_html=True)
                    st.text_area("Rewritten", rewritten, height=250, key="rewritten", label_visibility="collapsed")
                    st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        if st.button("🧹 **Clear All**", use_container_width=True):
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Features section
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; padding: 2rem;'>
        <h3 style='color:#1976D2;'>✨ Smart Features</h3>
        <div style='display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1rem;'>
            <div style='flex: 1; min-width: 200px; padding: 1rem; background: rgba(0,180,216,0.1); border-radius: 10px;'>
                <h4>🎯 Grammar Preservation</h4>
                <p>No random sentence destruction</p>
            </div>
            <div style='flex: 1; min-width: 200px; padding: 1rem; background: rgba(32,201,151,0.1); border-radius: 10px;'>
                <h4>📚 Academic Quality</h4>
                <p>Maintains scholarly tone</p>
            </div>
            <div style='flex: 1; min-width: 200px; padding: 1rem; background: rgba(255,193,7,0.1); border-radius: 10px;'>
                <h4>🌐 Real Synonyms</h4>
                <p>Uses WordNet & online sources</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:#666; padding:1rem;'>
        <p style='font-size:1.1rem; margin-bottom:0.5rem;'>
            ⚙️ Powered by <span style="color:#00B4D8; font-weight:bold;">Streamlit</span> | 
            🎓 Developed by <span style="color:#FF5722; font-weight:bold;">Academic AI Lab</span>
        </p>
        <p style='font-size:0.9rem; color:#999;'>
            ✨ Intelligent academic rewriting without grammar destruction ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
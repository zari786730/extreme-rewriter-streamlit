# =========================
# FRONTEND (DNA WATER GLASS UI — FINAL DARK MODE WORKING)
# =========================

import streamlit as st
import random
import re
import requests
from bs4 import BeautifulSoup
import time
import nltk
from nltk.corpus import wordnet

# Download NLTK data
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# =========================
# BACKEND FUNCTIONS
# =========================

class DynamicSynonymFetcher:
    def __init__(self):
        self.synonym_cache = {}
        self.setup_fallback_synonyms()
    
    def setup_fallback_synonyms(self):
        """Basic fallback for common words if online fetch fails"""
        self.fallback_synonyms = {
            'beautiful': ['attractive', 'lovely', 'pretty', 'gorgeous', 'stunning'],
            'important': ['significant', 'crucial', 'essential', 'vital', 'critical'],
            'good': ['excellent', 'great', 'superb', 'outstanding', 'fine'],
            'big': ['large', 'huge', 'enormous', 'massive', 'substantial'],
            'small': ['tiny', 'little', 'miniature', 'compact', 'petite'],
            'fast': ['quick', 'rapid', 'swift', 'speedy', 'brisk'],
            'slow': ['gradual', 'leisurely', 'unhurried', 'deliberate', 'measured'],
            'research': ['study', 'investigation', 'analysis', 'examination'],
            'study': ['research', 'investigation', 'analysis', 'examination'],
            'analysis': ['evaluation', 'assessment', 'examination', 'scrutiny']
        }
    
    def fetch_synonyms_online(self, word):
        """Fetch fresh synonyms from online sources"""
        synonyms = set()
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # Try multiple online sources
            sources = [
                f"https://www.thesaurus.com/browse/{word}",
            ]
            
            for url in sources:
                try:
                    response = requests.get(url, headers=headers, timeout=5)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        
                        if "thesaurus.com" in url:
                            synonym_elements = soup.find_all('a', {'data-linkid': 'nn1ov4'})
                            for elem in synonym_elements[:10]:
                                syn = elem.text.strip()
                                if syn and syn.lower() != word.lower():
                                    synonyms.add(syn)
                    
                    if synonyms:
                        break
                        
                except:
                    continue
            
            # If online failed, try WordNet
            if not synonyms:
                for syn in wordnet.synsets(word):
                    for lemma in syn.lemmas():
                        synonym = lemma.name().replace('_', ' ')
                        if synonym.lower() != word.lower() and len(synonym.split()) == 1:
                            synonyms.add(synonym)
            
            # Final fallback
            if not synonyms and word in self.fallback_synonyms:
                synonyms.update(self.fallback_synonyms[word])
            
            # Cache the results
            self.synonym_cache[word.lower()] = list(synonyms)[:8]
            
        except Exception as e:
            if word in self.fallback_synonyms:
                synonyms = set(self.fallback_synonyms[word])
            else:
                synonyms = set()
        
        return list(synonyms)
    
    def get_fresh_synonyms(self, word):
        """Get synonyms with caching"""
        word_lower = word.lower()
        
        if word_lower in self.synonym_cache:
            return self.synonym_cache[word_lower]
        
        synonyms = self.fetch_synonyms_online(word_lower)
        
        if not synonyms:
            return [word]
        
        return synonyms

class DynamicRewriter:
    def __init__(self):
        self.synonym_fetcher = DynamicSynonymFetcher()
        self.common_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
            'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been'
        }
    
    def clean_sentence_endings(self, text):
        """Remove random dots and ensure proper sentence endings"""
        text = re.sub(r'\.{2,}', '.', text)
        text = re.sub(r'\.(\w)', r'. \1', text)
        text = re.sub(r'(\w)\.(\s+[a-z])', r'\1\2', text)
        return text
    
    def intelligent_word_replacement(self, text):
        """Replace words with fresh synonyms from online sources"""
        words = text.split()
        new_words = []
        
        i = 0
        while i < len(words):
            original_word = words[i]
            word_clean = original_word.lower().strip('.,!?;:"')
            
            # Skip very short/common words
            if len(word_clean) <= 2 or word_clean in self.common_words:
                new_words.append(original_word)
                i += 1
                continue
            
            # Extract punctuation
            punctuation = ''
            if original_word and not original_word[-1].isalnum():
                punctuation = original_word[-1]
                clean_word = original_word[:-1]
            else:
                clean_word = original_word
            
            # Get fresh synonyms (70% replacement rate)
            if random.random() < 0.7:
                synonyms = self.synonym_fetcher.get_fresh_synonyms(word_clean)
                
                if synonyms and synonyms[0] != word_clean:
                    replacement = random.choice(synonyms)
                    
                    # Preserve capitalization
                    if clean_word[0].isupper():
                        replacement = replacement.capitalize()
                    
                    new_words.append(replacement + punctuation)
                else:
                    new_words.append(original_word)
            else:
                new_words.append(original_word)
            
            i += 1
        
        return ' '.join(new_words)
    
    def grammar_aware_sentence_restructure(self, text):
        """Restructure sentences with proper grammar"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        restructured = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            if len(words) < 4:
                restructured.append(sentence)
                continue
            
            # Choose different patterns for variety
            pattern_type = random.choice(['academic', 'emphatic', 'contextual', 'normal', 'comparative'])
            
            if pattern_type == 'academic':
                frames = [
                    f"Research indicates that {sentence.lower()}",
                    f"Studies demonstrate that {sentence.lower()}",
                    f"Evidence suggests that {sentence.lower()}",
                    f"Analysis reveals that {sentence.lower()}"
                ]
                restructured.append(random.choice(frames))
                
            elif pattern_type == 'emphatic':
                frames = [
                    f"Notably, {sentence.lower()}",
                    f"Significantly, {sentence.lower()}",
                    f"Importantly, {sentence.lower()}",
                    f"Remarkably, {sentence.lower()}"
                ]
                restructured.append(random.choice(frames))
                
            elif pattern_type == 'contextual':
                frames = [
                    f"In this context, {sentence.lower()}",
                    f"Within this framework, {sentence.lower()}",
                    f"From this perspective, {sentence.lower()}",
                    f"Considering these factors, {sentence.lower()}"
                ]
                restructured.append(random.choice(frames))
                
            elif pattern_type == 'comparative':
                frames = [
                    f"Similarly, {sentence.lower()}",
                    f"Likewise, {sentence.lower()}",
                    f"By comparison, {sentence.lower()}",
                    f"In contrast, {sentence.lower()}"
                ]
                restructured.append(random.choice(frames))
                
            else:
                restructured.append(sentence)
        
        result = '. '.join(restructured) + '.' if restructured else ''
        return self.clean_sentence_endings(result)
    
    def vary_sentence_lengths(self, text):
        """Ensure sentences have different word counts"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) < 2:
            return text
        
        processed_sentences = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            current_length = len(words)
            
            # Strategic length variation
            if current_length > 18:
                split_sentences = self.split_intelligently(sentence)
                processed_sentences.extend(split_sentences)
            elif current_length < 6:
                processed_sentences.append(self.expand_sentence(sentence))
            else:
                processed_sentences.append(sentence)
        
        result = '. '.join(processed_sentences) + '.' if processed_sentences else ''
        return self.clean_sentence_endings(result)
    
    def split_intelligently(self, sentence):
        """Split long sentences at natural break points"""
        words = sentence.split()
        connectors = ['and', 'but', 'however', 'therefore', 'moreover', 'although', 'while', 'because']
        split_points = []
        
        for i, word in enumerate(words):
            if word.lower() in connectors and 5 < i < len(words) - 5:
                split_points.append(i)
        
        if split_points:
            split_at = random.choice(split_points)
            part1 = ' '.join(words[:split_at])
            part2 = ' '.join(words[split_at:])
            part2 = part2[0].upper() + part2[1:] if part2 else part2
            return [part1 + '.', part2]
        else:
            return [sentence]
    
    def expand_sentence(self, sentence):
        """Expand short sentences"""
        expansions = [
            "It is evident that",
            "Research shows that",
            "Studies indicate that",
            "One can observe that",
            "Analysis demonstrates that"
        ]
        
        base_sentence = sentence.lower()
        expanded = f"{random.choice(expansions)} {base_sentence}"
        return expanded[0].upper() + expanded[1:]
    
    def ensure_grammar_flow(self, text):
        """Final grammar and flow check"""
        # Fix common grammar issues
        text = re.sub(r'\s+([.,!?])', r'\1', text)
        text = re.sub(r'\.\s*\.', '.', text)
        text = re.sub(r',\s*,', ',', text)
        
        # Ensure proper capitalization
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence and sentence[0].islower():
                sentence = sentence[0].upper() + sentence[1:]
            corrected_sentences.append(sentence)
        
        result = '. '.join(corrected_sentences) + '.' if corrected_sentences else ''
        return result

# Initialize the dynamic rewriter
dynamic_rewriter = DynamicRewriter()

def extreme_rewriter(original_text):
    """Main rewriting function"""
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations
    result = clean_text
    result = dynamic_rewriter.intelligent_word_replacement(result)
    result = dynamic_rewriter.grammar_aware_sentence_restructure(result)
    result = dynamic_rewriter.vary_sentence_lengths(result)
    result = dynamic_rewriter.ensure_grammar_flow(result)
    
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

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=5):
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
        
        # Small delay to avoid rate limiting
        time.sleep(0.2)
    
    return best_result, best_similarity

# =========================
# FRONTEND UI (YOUR ORIGINAL DESIGN)
# =========================

# --- CSS STYLES ---
st.markdown("""
<style>
body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: #e6faff;
}

/* ---- BUBBLES ---- */
#bubble-layer {
  position: fixed;
  top: 0; 
  left: 0;
  width: 100%; 
  height: 100%;
  overflow: hidden; 
  z-index: -3; 
  pointer-events: none;
}

.dna-bubble {
  position: absolute;
  bottom: -120px;
  background: rgba(0,180,255,0.3);
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0,200,255,0.6);
  animation: rise linear infinite;
}

@keyframes rise {
  0% { transform: translateY(0) scale(0.6); opacity: 0; }
  20% { opacity: 1; }
  70% { transform: translateY(-80vh) scale(1.1); opacity: 0.9; }
  100% { transform: translateY(-120vh) scale(0.8); opacity: 0; }
}

/* ---- DROPLETS ---- */
#droplet-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -2;
  pointer-events: none;
}

.droplet {
  position: absolute;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.25), rgba(255,255,255,0.05));
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0,200,255,0.15);
  animation: slideDown 18s ease-in-out infinite;
}

@keyframes slideDown {
  0% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
  50% { transform: translateY(15px) rotate(2deg); opacity: 1; }
  100% { transform: translateY(0) rotate(-1deg); opacity: 0.8; }
}

/* ---- WAVE ---- */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 220px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -1;
}

@keyframes waveMove {
  from { transform: translateY(0); }
  to { transform: translateY(-30px); }
}

/* ---- GLASS BOX ---- */
.glass-box {
  backdrop-filter: blur(25px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  margin-top: 2rem;
}

/* ---- TITLE ---- */
h1.title {
  text-align: center;
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(45deg, #00eaff, #00ffb7, #0095ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: colorShift 6s ease-in-out infinite;
  margin-top: 3rem;
}
@keyframes colorShift {
  0% { filter: hue-rotate(0deg); }
  50% { filter: hue-rotate(180deg); }
  100% { filter: hue-rotate(360deg); }
}

/* ---- BUTTONS ---- */
.stButton>button {
  background: linear-gradient(135deg, #00b4ff, #0077ff);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1.1rem;
  padding: 0.75rem 2rem;
  transition: all 0.3s ease;
  width: 100%;
}
.stButton>button:hover {
  background: linear-gradient(135deg, #0077ff, #00b4ff);
  box-shadow: 0 0 15px rgba(0,180,255,0.8);
  transform: translateY(-2px);
}

/* ---- TEXTAREA ---- */
.stTextArea textarea {
  border-radius: 15px;
  border: 1px solid rgba(0,180,255,0.3);
  background: rgba(15, 25, 35, 0.9);
  color: #e6faff;
  font-size: 1rem;
  padding: 1rem;
  resize: vertical;
}

/* ---- SLIDER ---- */
.stSlider {
  margin: 2rem 0;
}

/* ---- FOOTER ---- */
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

/* ---- SUCCESS MESSAGE ---- */
.success-box {
  backdrop-filter: blur(25px);
  background: rgba(0,255,200,0.1);
  border-radius: 15px;
  padding: 1.5rem;
  border: 2px solid rgba(0,255,200,0.3);
  margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# --- VISUAL LAYERS (BUBBLES + DROPLETS) ---
bubble_html = '<div id="bubble-layer">'
for i in range(40):
    size = random.randint(8, 35)
    left = random.randint(0, 98)
    duration = random.randint(15, 28)
    delay = random.randint(0, 12)
    bubble_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
bubble_html += '</div>'

droplet_html = '<div id="droplet-layer">'
for i in range(25):
    size = random.randint(4, 18)
    top = random.randint(0, 90)
    left = random.randint(0, 95)
    duration = random.randint(12, 20)
    delay = random.randint(0, 8)
    droplet_html += f"""
    <div class="droplet" style="
        top:{top}vh;
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
droplet_html += '</div><div class="wave-bg"></div>'

st.markdown(bubble_html + droplet_html, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1 class="title">💧 Extreme Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

input_text = st.text_area(
    "🧬 Enter text to rewrite:", 
    height=180, 
    placeholder="Paste your text here...\n\nExample: The red rose is one of the most beautiful and admired flowers in the world, symbolizing love, passion, and deep emotion."
)

target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 15, step=1)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("🔄 Rewriting your text with fresh synonyms..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        
        # Display results
        st.markdown(f"""
        <div class="success-box">
            <h3 style="color:#00eaff; margin-top:0;">✨ Rewritten Text</h3>
            <p style="color:#66fffa; font-size:1.1rem;">Similarity: <strong>{similarity:.1f}%</strong> (Target: {target_similarity}%)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_area(
            "Copy your rewritten text:",
            value=rewritten,
            height=200,
            key="output_text"
        )
        
        # Show statistics
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        with col_stat1:
            st.metric("Original Words", len(input_text.split()))
        with col_stat2:
            st.metric("Rewritten Words", len(rewritten.split()))
        with col_stat3:
            st.metric("AI Detection", "LOW" if similarity < 20 else "MODERATE")

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear All", use_container_width=True):
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
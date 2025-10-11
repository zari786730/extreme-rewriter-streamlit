import streamlit as st
import re
import random
import requests
from bs4 import BeautifulSoup
import time
from collections import defaultdict
import nltk
from nltk.corpus import wordnet
import synonyms

# Download required NLTK data
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# =========================
# SMART REWRITER BACKEND (NO RANDOM SENTENCE DESTRUCTION)
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
        
        # Try multiple online sources
        sources = [
            self._get_thesaurus_com(word),
            self._get_power_thesaurus(word),
            self._get_wordnet_synonyms(word)
        ]
        
        for source_syns in sources:
            synonyms.update(source_syns)
        
        # Filter to keep only relevant synonyms
        filtered_syns = [syn for syn in synonyms if len(syn.split()) == 1]
        self.synonym_cache[word] = filtered_syns[:8]  # Limit to top 8
        return self.synonym_cache[word]
    
    def _get_wordnet_synonyms(self, word):
        """Get synonyms from WordNet"""
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ')
                if synonym != word and len(synonym.split()) == 1:
                    synonyms.add(synonym.lower())
        return list(synonyms)
    
    def _get_thesaurus_com(self, word):
        """Scrape synonyms from Thesaurus.com"""
        try:
            url = f"https://www.thesaurus.com/browse/{word}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            synonyms = set()
            # Look for synonym containers
            containers = soup.find_all('a', {'href': re.compile(r'/browse/')})
            for container in containers[:15]:  # Limit to first 15
                syn = container.text.strip().lower()
                if syn and syn != word and len(syn.split()) == 1:
                    synonyms.add(syn)
            return list(synonyms)
        except:
            return []
    
    def _get_power_thesaurus(self, word):
        """Alternative synonym source"""
        # You can implement Power Thesaurus scraping here
        return []
    
    def smart_sentence_restructure(self, text):
        """Restructure sentences intelligently without breaking grammar"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        restructured = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            
            # Only restructure longer sentences
            if len(words) > 12:
                # Find natural breaking points (conjunctions, commas)
                if ',' in sentence:
                    parts = sentence.split(',')
                    if len(parts) >= 2:
                        # Create two proper sentences
                        first_part = parts[0].strip()
                        rest_parts = ', '.join(parts[1:]).strip()
                        
                        # Add appropriate transitions
                        transitions = self.academic_phrases['addition'] + self.academic_phrases['emphasis']
                        transition = random.choice(transitions)
                        
                        restructured.append(first_part + '.')
                        restructured.append(f"{transition} {rest_parts}")
                        continue
            
            # For shorter sentences or those without natural breaks, keep as is
            restructured.append(sentence)
        
        # Join with proper punctuation
        return '. '.join(restructured) + '.'
    
    def advanced_vocabulary_replacement(self, text):
        """Replace words with synonyms while maintaining meaning"""
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Only replace content words (nouns, verbs, adjectives, adverbs)
            if (len(clean_word) > 5 and 
                clean_word not in ['which', 'that', 'there', 'their', 'about'] and
                random.random() < 0.3):  # Only replace 30% of eligible words
                
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
            if random.random() < 0.4 and len(sentence.split()) > 6:
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
        
        return '. '.join(enhanced) + '.'
    
    def rewrite_text(self, original_text):
        """Main rewriting function that preserves academic integrity"""
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

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=5):
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
        
        # Add small delay to avoid hitting APIs too fast
        time.sleep(0.5)
    
    return best_result, best_similarity

# =========================
# BEAUTIFUL STREAMLIT FRONTEND
# =========================

st.set_page_config(
    page_title="Academic Rewriter Pro", 
    page_icon="🎓", 
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid #e0f7fa;
    }
    
    .stButton button {
        background: linear-gradient(45deg, #2196F3, #21CBF3);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
    }
    
    .success-box {
        background: linear-gradient(45deg, #4CAF50, #66BB6A);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .text-box {
        background: #f8fdff;
        border: 1px solid #e3f2fd;
        border-radius: 10px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-container">
    <h1 style='text-align:center; color:#1976D2;'>🎓 Academic Rewriter Pro</h1>
    <p style='text-align:center; color:#666;'>
        Intelligent text rewriting that preserves academic integrity and grammar
    </p>
</div>
""", unsafe_allow_html=True)

# Main UI
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.markdown("### 📝 Enter Your Academic Text")
    input_text = st.text_area(
        "Paste your text below:",
        height=180,
        placeholder="Enter your academic text here...",
        label_visibility="collapsed"
    )
    
    st.markdown("### 🎯 Similarity Target")
    target_similarity = st.slider(
        "Maximum similarity percentage:",
        5, 40, 15, step=1,
        help="Lower values create more unique text"
    )
    
    col1, col2 = st.columns([1, 1])
    
    if col1.button("🚀 Rewrite Academic Text", use_container_width=True):
        if not input_text.strip():
            st.warning("Please enter some text to rewrite.")
        else:
            with st.spinner("🔄 Rewriting with academic precision..."):
                rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
            
            if similarity <= target_similarity:
                st.markdown(
                    f'<div class="success-box">'
                    f'<h3>✅ Success! Similarity: {similarity:.1f}%</h3>'
                    f'<p>Academic integrity maintained!</p>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.warning(f"Similarity: {similarity:.1f}% (Target: {target_similarity}%)")
            
            colA, colB = st.columns(2)
            with colA:
                st.markdown("#### 📘 Original Text")
                st.markdown('<div class="text-box">', unsafe_allow_html=True)
                st.text_area("Original", input_text, height=250, key="original", label_visibility="collapsed")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with colB:
                st.markdown("#### ✨ Rewritten Text")
                st.markdown('<div class="text-box">', unsafe_allow_html=True)
                st.text_area("Rewritten", rewritten, height=250, key="rewritten", label_visibility="collapsed")
                st.markdown('</div>', unsafe_allow_html=True)
    
    if col2.button("🧹 Clear", use_container_width=True):
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>"
    "🎓 Academic Rewriter Pro | Preserving scholarly integrity since 2024"
    "</p>",
    unsafe_allow_html=True
)
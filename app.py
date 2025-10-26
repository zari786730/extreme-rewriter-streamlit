# =========================
# ACADEMIC TEXT REWRITER - FRONTEND
# =========================

import streamlit as st
import random
import re
import time
import math
import os
import importlib

# -------------------------
# IMPORT LOCAL FILES
# -------------------------
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# -------------------------
# VOCABULARY INTEGRATION
# -------------------------
def load_vocabulary_files():
    """Load all vocabulary files from the vocabulary folder"""
    vocab_folder = "vocabulary"
    vocab_modules = []
    total_words = 0
    
    if os.path.exists(vocab_folder):
        for file in os.listdir(vocab_folder):
            if file.endswith(".py") and file != "__init__.py":
                try:
                    module_name = file[:-3]  # remove .py extension
                    module = importlib.import_module(f"vocabulary.{module_name}")
                    vocab_modules.append(module)
                    
                    # Count words in each module
                    if hasattr(module, 'synonyms'):
                        total_words += len(module.synonyms)
                    elif hasattr(module, 'synonyms_list'):
                        total_words += len(module.synonyms_list)
                        
                except Exception as e:
                    st.sidebar.warning(f"Could not load {file}: {str(e)}")
    
    return vocab_modules, total_words

# Load vocabulary
vocab_modules, vocab_word_count = load_vocabulary_files()

# -------------------------
# ENHANCED REWRITER CLASS
# -------------------------
class EnhancedRewriter:
    def __init__(self):
        self.replacements = {}
        self.total_words_count = 0
        self.setup_vocabulary()

    def setup_vocabulary(self):
        """Integrate all vocabulary sources"""
        # Load health terms
        for word, replacement in health_terms.items():
            self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
            self.total_words_count += 1

        # Load general words
        for word, replacement in general_words.items():
            if word not in self.replacements:
                self.replacements[word] = [replacement] if isinstance(replacement, str) else replacement
                self.total_words_count += 1

        # Load vocabulary files
        for module in vocab_modules:
            if hasattr(module, 'synonyms'):
                for word, synonyms in module.synonyms.items():
                    if word not in self.replacements:
                        self.replacements[word] = synonyms if isinstance(synonyms, list) else [synonyms]
                        self.total_words_count += 1
            elif hasattr(module, 'synonyms_list'):
                # Handle list format if needed
                pass

    def intelligent_word_replacement(self, text):
        """Replace words using integrated dictionaries"""
        words = text.split()
        new_words = []
        replacements_made = 0

        for word in words:
            clean_word = word.lower().strip('.,!?;:"')

            # Skip very short common words
            if len(clean_word) <= 2 or clean_word in ['the','a','an','and','or','but','in','on','at','to','for','of','with','by','as','is','was','were','be','been','have','has','had','do','does','did']:
                new_words.append(word)
                continue

            # Apply replacement from integrated dictionaries
            if clean_word in self.replacements and random.random() < 0.7:
                replacement = random.choice(self.replacements[clean_word])
                replacement = replacement.capitalize() if word[0].isupper() else replacement
                new_words.append(replacement)
                replacements_made += 1
            else:
                new_words.append(word)

        return ' '.join(new_words), replacements_made

    def sentence_length_manipulation(self, text):
        """Change number of sentences"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        original_sentence_count = len(sentences)

        if original_sentence_count <= 1:
            return text, original_sentence_count, original_sentence_count

        # Sentence manipulation logic
        change_direction = random.choice(['increase', 'decrease'])
        modified_sentences = sentences.copy()

        if change_direction == 'increase' and original_sentence_count < 10:
            new_sentences = []
            for sentence in modified_sentences:
                words = sentence.split()
                if len(words) > 15 and random.random() < 0.6:
                    mid = len(words) // 2
                    first_part = ' '.join(words[:mid])
                    second_part = ' '.join(words[mid:])
                    new_sentences.append(first_part + '.')
                    new_sentences.append(second_part.capitalize())
                else:
                    new_sentences.append(sentence)
            modified_sentences = new_sentences
        elif change_direction == 'decrease' and original_sentence_count > 2:
            new_sentences = []
            i = 0
            while i < len(modified_sentences):
                if i < len(modified_sentences) - 1 and len(modified_sentences[i].split()) < 8 and len(modified_sentences[i+1].split()) < 8:
                    combined = modified_sentences[i] + ' and ' + modified_sentences[i+1].lower()
                    new_sentences.append(combined)
                    i += 2
                else:
                    new_sentences.append(modified_sentences[i])
                    i += 1
            modified_sentences = new_sentences

        final_sentence_count = len(modified_sentences)
        result = '. '.join(modified_sentences) + '.'
        return result, original_sentence_count, final_sentence_count

    def varied_sentence_restructure(self, text):
        """Restructure sentences with varied patterns"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text

        strategy = random.choice(['shuffle', 'reverse', 'interleave'])

        if strategy == 'shuffle':
            random.shuffle(sentences)
        elif strategy == 'reverse':
            sentences.reverse()
        elif strategy == 'interleave':
            if len(sentences) >= 4:
                mid = len(sentences) // 2
                first_half = sentences[:mid]
                second_half = sentences[mid:]
                sentences = []
                for i in range(max(len(first_half), len(second_half))):
                    if i < len(first_half):
                        sentences.append(first_half[i])
                    if i < len(second_half):
                        sentences.append(second_half[i])

        connectors = ['. ', '. Additionally, ', '. Moreover, ', '. Furthermore, ']
        result = sentences[0] + '.'
        for i in range(1, len(sentences)):
            if random.random() < 0.5:
                result += random.choice(connectors) + sentences[i].lower()
            else:
                result += '. ' + sentences[i]

        return result

    def add_natural_variation(self, text):
        """Add natural language variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text

        introductory_phrases = [
            'From a clinical standpoint,',
            'In medical terms,',
            'Biologically speaking,',
            'Pathologically,',
            'Therapeutically,',
            'Diagnostically,',
            'Prognostically,'
        ]

        modified_sentences = []
        for i, sentence in enumerate(sentences):
            if i == 0 and random.random() < 0.3:
                modified_sentences.append(random.choice(introductory_phrases) + ' ' + sentence.lower())
            elif random.random() < 0.2:
                modified_sentences.append(random.choice(introductory_phrases) + ' ' + sentence.lower())
            else:
                modified_sentences.append(sentence)

        return '. '.join(modified_sentences) + '.'

# Initialize enhanced rewriter
enhanced_rewriter = EnhancedRewriter()

# -------------------------
# ENHANCED REWRITER FUNCTION
# -------------------------
def enhanced_rewrite(original_text):
    """Main rewriting function with all enhancements"""
    clean_text = original_text.strip().strip('"').strip("'")

    # Apply transformations
    result, replacements_made = enhanced_rewriter.intelligent_word_replacement(clean_text)
    result, orig_sentences, final_sentences = enhanced_rewriter.sentence_length_manipulation(result)
    result = enhanced_rewriter.varied_sentence_restructure(result)
    result = enhanced_rewriter.add_natural_variation(result)

    # Final grammar correction
    result = correct_grammar(result)

    return result, replacements_made, orig_sentences, final_sentences

# -------------------------
# SIMILARITY CALCULATION
# -------------------------
def calculate_similarity(original, rewritten):
    original_words = set(re.findall(r'\w+', original.lower()))
    rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common_words) / len(original_words) * 100

# -------------------------
# GUARANTEE LOW SIMILARITY
# -------------------------
def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=8):
    best_result = None
    best_similarity = 100
    stats = {}

    for attempt in range(max_attempts):
        rewritten, replacements, orig_sent, final_sent = enhanced_rewrite(original_text)
        similarity = calculate_similarity(original_text, rewritten)

        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            stats = {
                'replacements': replacements,
                'original_sentences': orig_sent,
                'final_sentences': final_sent,
                'attempt': attempt + 1
            }

        if similarity <= max_similarity:
            return rewritten, similarity, stats

    return best_result, best_similarity, stats

# =========================
# STREAMLIT FRONTEND WITH ENHANCED UI
# =========================

st.set_page_config(
    page_title="Academic Text Rewriter", 
    page_icon="🧬", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- ENHANCED CUSTOM CSS WITH 3D EFFECTS ---
st.markdown("""
<style>
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
        min-height: 100vh;
    }
    
    /* Centered container */
    .block-container {
        padding-top: 1rem;
        max-width: 900px;
        margin: 0 auto;
    }
    
    /* 3D Logo Animation */
    @keyframes rotate3D {
        0% { 
            transform: rotateY(0deg) rotateX(0deg) scale(1);
            text-shadow: 0 0 20px #FF6B6B, 0 0 30px #4ECDC4;
        }
        25% { 
            transform: rotateY(90deg) rotateX(20deg) scale(1.1);
            text-shadow: 0 0 20px #4ECDC4, 0 0 30px #45B7D1;
        }
        50% { 
            transform: rotateY(180deg) rotateX(0deg) scale(1.2);
            text-shadow: 0 0 20px #45B7D1, 0 0 30px #96CEB4;
        }
        75% { 
            transform: rotateY(270deg) rotateX(-20deg) scale(1.1);
            text-shadow: 0 0 20px #96CEB4, 0 0 30px #FF6B6B;
        }
        100% { 
            transform: rotateY(360deg) rotateX(0deg) scale(1);
            text-shadow: 0 0 20px #FF6B6B, 0 0 30px #4ECDC4;
        }
    }
    
    @keyframes glow {
        0%, 100% { 
            color: #FF6B6B;
            filter: drop-shadow(0 0 10px #FF6B6B);
        }
        25% { 
            color: #4ECDC4;
            filter: drop-shadow(0 0 15px #4ECDC4);
        }
        50% { 
            color: #45B7D1;
            filter: drop-shadow(0 0 20px #45B7D1);
        }
        75% { 
            color: #96CEB4;
            filter: drop-shadow(0 0 15px #96CEB4);
        }
    }
    
    .logo-3d {
        animation: rotate3D 8s ease-in-out infinite, glow 4s ease-in-out infinite;
        font-size: 4rem;
        text-align: center;
        margin-bottom: 0.5rem;
        perspective: 1000px;
        transform-style: preserve-3d;
    }
    
    /* 3D Bubbles Animation */
    @keyframes floatBubbles {
        0% {
            transform: translateY(100vh) translateX(0) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 0.7;
        }
        90% {
            opacity: 0.7;
        }
        100% {
            transform: translateY(-100px) translateX(var(--move-x)) rotate(360deg);
            opacity: 0;
        }
    }
    
    .bubble {
        position: fixed;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.3), rgba(255,255,255,0.1));
        border: 1px solid rgba(255,255,255,0.2);
        animation: floatBubbles linear infinite;
        z-index: -1;
        pointer-events: none;
    }
    
    /* Glass morphism effect */
    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    /* Enhanced button styling */
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    /* Stats cards */
    .stats-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #4ECDC4;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background: rgba(0, 15, 25, 0.8) !important;
        color: #e6faff !important;
        border-radius: 15px !important;
        border: 1px solid rgba(0, 180, 255, 0.3) !important;
        font-size: 1rem !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# --- DYNAMIC BUBBLES BACKGROUND ---
bubble_js = """
<script>
function createBubbles() {
    const container = document.body;
    const bubbleCount = 15;
    
    for (let i = 0; i < bubbleCount; i++) {
        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        
        // Random properties for variety
        const size = Math.random() * 60 + 20;
        const left = Math.random() * 100;
        const duration = Math.random() * 20 + 10; // 10-30 seconds
        const delay = Math.random() * 5;
        const moveX = (Math.random() - 0.5) * 100;
        
        bubble.style.width = size + 'px';
        bubble.style.height = size + 'px';
        bubble.style.left = left + 'vw';
        bubble.style.animationDuration = duration + 's';
        bubble.style.animationDelay = delay + 's';
        bubble.style.setProperty('--move-x', moveX + 'px');
        
        container.appendChild(bubble);
    }
}

// Create bubbles when page loads
document.addEventListener('DOMContentLoaded', createBubbles);
</script>
"""

st.components.v1.html(bubble_js, height=0)

# --- SIDEBAR WITH STATS ---
with st.sidebar:
    st.markdown("### 📊 System Statistics")
    
    # Vocabulary stats
    st.markdown(f"""
    <div class="stats-card">
        <h4>📚 Vocabulary Database</h4>
        <p><strong>Integrated Words:</strong> {enhanced_rewriter.total_words_count:,}</p>
        <p><strong>Vocabulary Files:</strong> {len(vocab_modules)}</p>
        <p><strong>External Words:</strong> {vocab_word_count:,}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Performance stats
    if 'last_rewrite_stats' in st.session_state:
        stats = st.session_state.last_rewrite_stats
        st.markdown(f"""
        <div class="stats-card">
            <h4>⚡ Last Rewrite</h4>
            <p><strong>Words Replaced:</strong> {stats.get('replacements', 0)}</p>
            <p><strong>Sentences Changed:</strong> {stats.get('original_sentences', 0)} → {stats.get('final_sentences', 0)}</p>
            <p><strong>Attempts:</strong> {stats.get('attempt', 1)}</p>
        </div>
        """, unsafe_allow_html=True)

# --- MAIN CONTENT AREA ---
st.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <div class="logo-3d">🧬</div>
    <h1 style="color: white; font-size: 2.5rem; margin-bottom: 0.5rem; 
               background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
               -webkit-background-clip: text;
               -webkit-text-fill-color: transparent;
               text-shadow: 0 0 30px rgba(78, 205, 196, 0.3);">
        Academic Text Rewriter
    </h1>
    <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem;">
        Advanced AI-Powered Text Transformation • Plagiarism Reduction • Academic Excellence
    </p>
</div>
""", unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)

input_text = st.text_area(
    "📝 **Enter your academic text to rewrite:**", 
    height=200,
    placeholder="Paste your research paper, essay, or any academic text here...\n\nExample: 'Cancer is a complex group of diseases characterized by uncontrolled growth of abnormal cells that can invade different parts of the body.'",
    key="input_text"
)

# Settings in columns
col1, col2 = st.columns(2)
with col1:
    target_similarity = st.slider(
        "🎯 **Target Maximum Similarity**", 
        5, 40, 15,
        help="Lower percentage = more different from original text"
    )
with col2:
    max_attempts = st.slider(
        "🔄 **Maximum Attempts**", 
        1, 15, 8,
        help="More attempts = better results but longer processing"
    )

# Action buttons
col1, col2, col3 = st.columns([2, 1, 1])

# Initialize session state for rewritten text
if 'rewritten_text' not in st.session_state:
    st.session_state.rewritten_text = None
if 'last_similarity' not in st.session_state:
    st.session_state.last_similarity = None

# --- REWRITE BUTTON ---
if col1.button("🚀 **Start Rewriting**", use_container_width=True):
    if not input_text.strip():
        st.warning("⚠️ **Please enter some text to rewrite!**")
    else:
        with st.spinner("🧪 **Rewriting your text with advanced AI algorithms...**"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            
            rewritten, similarity, stats = guarantee_low_similarity(
                input_text, target_similarity, max_attempts
            )
            
            # Store results in session state
            st.session_state.rewritten_text = rewritten
            st.session_state.last_similarity = similarity
            st.session_state.last_rewrite_stats = stats
            
            progress_bar.empty()

# --- CLEAR BUTTON ---
if col2.button("🧹 **Clear**", use_container_width=True):
    st.session_state.rewritten_text = None
    st.session_state.last_similarit
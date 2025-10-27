# =========================
# ACADEMIC TEXT REWRITER - COMPLETE FRONTEND
# =========================

import streamlit as st
import random
import re
import time
import os
import importlib.util
import glob

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Academic Text Rewriter",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- ENHANCED CSS WITH 3D EFFECTS ---
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 1rem;
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
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #4ECDC4;
    }
</style>
""", unsafe_allow_html=True)

# --- DYNAMIC BUBBLES BACKGROUND ---
bubble_html = """
<div id="bubbles-container">
    <div class="bubble" style="width: 40px; height: 40px; left: 5%; animation-duration: 25s; animation-delay: 0s; --move-x: 30px;"></div>
    <div class="bubble" style="width: 60px; height: 60px; left: 15%; animation-duration: 30s; animation-delay: 3s; --move-x: -25px;"></div>
    <div class="bubble" style="width: 30px; height: 30px; left: 25%; animation-duration: 28s; animation-delay: 6s; --move-x: 35px;"></div>
    <div class="bubble" style="width: 50px; height: 50px; left: 35%; animation-duration: 32s; animation-delay: 2s; --move-x: -30px;"></div>
    <div class="bubble" style="width: 45px; height: 45px; left: 45%; animation-duration: 27s; animation-delay: 8s; --move-x: 25px;"></div>
    <div class="bubble" style="width: 55px; height: 55px; left: 55%; animation-duration: 29s; animation-delay: 4s; --move-x: -35px;"></div>
    <div class="bubble" style="width: 35px; height: 35px; left: 65%; animation-duration: 31s; animation-delay: 10s; --move-x: 30px;"></div>
    <div class="bubble" style="width: 65px; height: 65px; left: 75%; animation-duration: 26s; animation-delay: 1s; --move-x: -25px;"></div>
    <div class="bubble" style="width: 40px; height: 40px; left: 85%; animation-duration: 33s; animation-delay: 7s; --move-x: 35px;"></div>
    <div class="bubble" style="width: 50px; height: 50px; left: 95%; animation-duration: 24s; animation-delay: 5s; --move-x: -30px;"></div>
</div>
"""
st.markdown(bubble_html, unsafe_allow_html=True)

# -------------------------
# VOCABULARY LOADER CLASS
# -------------------------
class VocabularyLoader:
    def __init__(self):
        self.replacements = {}
        self.total_words = 0
        self.loaded_files = 0
        self.failed_files = 0
        self.file_stats = []
        
    def load_all_vocabulary_files(self, folder_path="vocabulary"):
        """Load all vocabulary files from the folder"""
        self.replacements = {}
        self.total_words = 0
        self.loaded_files = 0
        self.failed_files = 0
        self.file_stats = []
        
        if not os.path.exists(folder_path):
            st.error(f"❌ Vocabulary folder '{folder_path}' not found!")
            return False
        
        # Get all Python files in the vocabulary folder
        vocab_files = glob.glob(os.path.join(folder_path, "*.py"))
        vocab_files = [f for f in vocab_files if not f.endswith("__init__.py")]
        
        # Sort files alphabetically
        vocab_files.sort()
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, file_path in enumerate(vocab_files):
            file_name = os.path.basename(file_path)
            progress = (i + 1) / len(vocab_files)
            progress_bar.progress(progress)
            status_text.text(f"📖 Loading {file_name}... ({i + 1}/{len(vocab_files)})")
            
            try:
                # Load the module
                spec = importlib.util.spec_from_file_location(file_name[:-3], file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                words_in_file = 0
                
                # Extract synonyms
                if hasattr(module, 'synonyms'):
                    for word, synonyms in module.synonyms.items():
                        if word and synonyms:
                            if word not in self.replacements:
                                if isinstance(synonyms, str):
                                    self.replacements[word] = [synonyms]
                                elif isinstance(synonyms, list):
                                    self.replacements[word] = synonyms
                                else:
                                    continue
                                self.total_words += 1
                                words_in_file += 1
                
                self.loaded_files += 1
                self.file_stats.append({
                    'file': file_name,
                    'words': words_in_file,
                    'status': '✅ Loaded'
                })
                
            except Exception as e:
                self.failed_files += 1
                self.file_stats.append({
                    'file': file_name,
                    'words': 0,
                    'status': f'❌ Error: {str(e)[:50]}...'
                })
        
        progress_bar.empty()
        status_text.empty()
        
        if self.loaded_files > 0:
            st.success(f"✅ Successfully loaded {self.total_words:,} words from {self.loaded_files} files")
            if self.failed_files > 0:
                st.warning(f"⚠️ Failed to load {self.failed_files} files")
            return True
        else:
            st.error("❌ No vocabulary files could be loaded!")
            return False

# -------------------------
# ENHANCED REWRITER CLASS
# -------------------------
class EnhancedRewriter:
    def __init__(self):
        self.vocab_loader = VocabularyLoader()
        self.replacements = {}
        self.is_loaded = False
        
    def initialize_vocabulary(self):
        """Initialize vocabulary with progress tracking"""
        if not self.is_loaded:
            with st.spinner("🔄 Loading vocabulary database..."):
                success = self.vocab_loader.load_all_vocabulary_files()
                if success:
                    self.replacements = self.vocab_loader.replacements
                    self.is_loaded = True
                    return True
                else:
                    # Fallback to basic vocabulary
                    self.setup_basic_vocabulary()
                    return False
        return True
    
    def setup_basic_vocabulary(self):
        """Setup basic vocabulary as fallback"""
        basic_vocab = {
            "study": ["research", "investigation", "analysis", "examination"],
            "result": ["finding", "outcome", "conclusion", "discovery"],
            "important": ["significant", "crucial", "essential", "vital"],
            "show": ["demonstrate", "indicate", "reveal", "illustrate"],
            "method": ["approach", "technique", "procedure", "strategy"],
            "data": ["information", "findings", "results", "evidence"],
            "analysis": ["examination", "assessment", "evaluation", "study"],
            "research": ["investigation", "study", "inquiry", "exploration"],
            "development": ["advancement", "progress", "evolution", "growth"],
            "treatment": ["therapy", "intervention", "management", "care"],
            "patient": ["individual", "case", "subject", "person"],
            "disease": ["disorder", "condition", "ailment", "illness"],
            "cell": ["cellular unit", "biological unit", "microscopic unit"],
            "growth": ["proliferation", "development", "expansion", "increase"],
            "process": ["procedure", "mechanism", "operation", "method"],
            "system": ["structure", "framework", "network", "organization"],
            "change": ["alteration", "modification", "transformation", "shift"],
            "effect": ["impact", "influence", "consequence", "result"],
            "level": ["degree", "extent", "measure", "amount"],
            "time": ["duration", "period", "interval", "timespan"]
        }
        self.replacements = basic_vocab
        self.is_loaded = True
    
    def intelligent_word_replacement(self, text, intensity=0.7):
        """Advanced word replacement with context awareness"""
        words = text.split()
        new_words = []
        replacements_made = 0
        
        skip_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
            'of', 'with', 'by', 'as', 'is', 'was', 'were', 'be', 'been', 'have', 
            'has', 'had', 'do', 'does', 'did', 'this', 'that', 'these', 'those',
            'it', 'its', 'they', 'them', 'their'
        }
        
        for i, word in enumerate(words):
            # Clean the word from punctuation
            clean_word = re.sub(r'[^\w]', '', word.lower())
            
            # Skip very short words and common words
            if len(clean_word) <= 2 or clean_word in skip_words:
                new_words.append(word)
                continue
            
            # Apply replacement with probability based on intensity
            if clean_word in self.replacements and random.random() < intensity:
                replacement = random.choice(self.replacements[clean_word])
                
                # Preserve capitalization
                if word[0].isupper():
                    replacement = replacement.capitalize()
                
                # Preserve punctuation
                punctuation = re.findall(r'[^\w\s]', word)
                if punctuation:
                    replacement += punctuation[0]
                
                new_words.append(replacement)
                replacements_made += 1
            else:
                new_words.append(word)
        
        result = ' '.join(new_words)
        return result, replacements_made
    
    def restructure_sentences(self, text):
        """Restructure sentences for better flow"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if len(sentences) <= 1:
            return text, len(sentences), len(sentences)
        
        original_count = len(sentences)
        
        # Apply different restructuring strategies
        strategy = random.choice(['shuffle', 'combine', 'split'])
        
        if strategy == 'shuffle' and len(sentences) > 2:
            # Keep first sentence in place for coherence
            first = sentences[0]
            rest = sentences[1:]
            random.shuffle(rest)
            sentences = [first] + rest
            
        elif strategy == 'combine' and len(sentences) > 2:
            # Combine some short sentences
            combined_sentences = []
            i = 0
            while i < len(sentences):
                if (i < len(sentences) - 1 and 
                    len(sentences[i].split()) < 8 and 
                    len(sentences[i+1].split()) < 8):
                    connectors = ['and', 'while', 'whereas', 'although']
                    combined = f"{sentences[i]} {random.choice(connectors)} {sentences[i+1].lower()}"
                    combined_sentences.append(combined)
                    i += 2
                else:
                    combined_sentences.append(sentences[i])
                    i += 1
            sentences = combined_sentences
            
        elif strategy == 'split' and len(sentences) > 1:
            # Split long sentences
            split_sentences = []
            for sentence in sentences:
                words = sentence.split()
                if len(words) > 20 and random.random() < 0.6:
                    # Find natural break points
                    break_words = ['and', 'but', 'however', 'although', 'while', 'whereas']
                    split_point = None
                    for i, word in enumerate(words[5:-5]):  # Avoid splitting at very beginning or end
                        if word.lower() in break_words:
                            split_point = i + 5
                            break
                    
                    if split_point:
                        part1 = ' '.join(words[:split_point])
                        part2 = ' '.join(words[split_point:])
                        split_sentences.append(part1)
                        split_sentences.append(part2.capitalize())
                    else:
                        split_sentences.append(sentence)
                else:
                    split_sentences.append(sentence)
            sentences = split_sentences
        
        final_count = len(sentences)
        result = '. '.join(sentences) + '.'
        return result, original_count, final_count
    
    def add_academic_phrasing(self, text):
        """Add academic-style phrasing"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        if not sentences:
            return text
        
        academic_intros = [
            "From a research perspective,",
            "In the context of academic inquiry,",
            "Based on current scholarly understanding,",
            "According to established literature,",
            "Within the framework of scientific investigation,",
            "Drawing upon empirical evidence,",
            "From an analytical standpoint,",
            "In consideration of theoretical frameworks,"
        ]
        
        enhanced_sentences = []
        
        for i, sentence in enumerate(sentences):
            if i == 0 and random.random() < 0.4:
                # Add academic intro to first sentence
                enhanced_sentences.append(f"{random.choice(academic_intros)} {sentence.lower()}")
            elif random.random() < 0.2:
                # Occasionally add to other sentences
                enhanced_sentences.append(f"{random.choice(academic_intros)} {sentence.lower()}")
            else:
                enhanced_sentences.append(sentence)
        
        return '. '.join(enhanced_sentences) + '.'
    
    def calculate_similarity(self, original, rewritten):
        """Calculate similarity between original and rewritten text"""
        original_words = set(re.findall(r'\w+', original.lower()))
        rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
        
        if not original_words:
            return 0
        
        common_words = original_words.intersection(rewritten_words)
        similarity = len(common_words) / len(original_words) * 100
        
        return similarity
    
    def enhanced_rewrite(self, original_text, intensity=0.7):
        """Main rewriting function"""
        clean_text = original_text.strip()
        
        # Apply transformations
        result, replacements = self.intelligent_word_replacement(clean_text, intensity)
        result, orig_sentences, final_sentences = self.restructure_sentences(result)
        result = self.add_academic_phrasing(result)
        
        stats = {
            'replacements': replacements,
            'original_sentences': orig_sentences,
            'final_sentences': final_sentences,
            'words_changed': replacements
        }
        
        return result, stats
    
    def guarantee_low_similarity(self, text, max_similarity=20, max_attempts=5):
        """Generate multiple versions to achieve low similarity"""
        best_result = text
        best_similarity = 100
        best_stats = {}
        best_attempt = 0
        
        for attempt in range(max_attempts):
            # Vary intensity for different attempts
            intensity = 0.5 + (attempt * 0.1)
            rewritten, stats = self.enhanced_rewrite(text, intensity)
            similarity = self.calculate_similarity(text, rewritten)
            
            if similarity < best_similarity:
                best_result = rewritten
                best_similarity = similarity
                best_stats = stats
                best_attempt = attempt + 1
            
            if similarity <= max_similarity:
                return best_result, best_similarity, best_stats, best_attempt
        
        return best_result, best_similarity, best_stats, best_attempt

# Initialize rewriter
rewriter = EnhancedRewriter()

# --- INITIALIZE SESSION STATE ---
if 'rewritten_text' not in st.session_state:
    st.session_state.rewritten_text = None
if 'similarity' not in st.session_state:
    st.session_state.similarity = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'rewrite_stats' not in st.session_state:
    st.session_state.rewrite_stats = {}
if 'vocab_initialized' not in st.session_state:
    st.session_state.vocab_initialized = False

# --- HEADER WITH 3D LOGO ---
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <div class="logo-3d">🧬</div>
    <h1 style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
              margin-bottom: 0.5rem;
              text-shadow: 0 0 30px rgba(78, 205, 196, 0.3);">
        Academic Text Rewriter
    </h1>
    <p style="color: rgba(255,255,255,0.8); font-size: 1.2rem;">
        Advanced AI-Powered Text Transformation • Plagiarism Reduction • Academic Excellence
    </p>
</div>
""", unsafe_allow_html=True)

# --- INITIALIZE VOCABULARY ---
if not st.session_state.vocab_initialized:
    with st.spinner("🚀 Initializing Academic Rewriter System..."):
        success = rewriter.initialize_vocabulary()
        if success:
            st.session_state.vocab_initialized = True
            st.success("✅ System initialized successfully!")
        else:
            st.warning("⚠️ Using basic vocabulary - some files may not have loaded correctly")

# --- MAIN INPUT SECTION ---
with st.container():
    st.markdown("""
    <div class="glass-box">
        <h3 style="text-align: center; color: white; margin-bottom: 1.5rem;">
            📝 Enter Your Academic Text
        </h3>
    """, unsafe_allow_html=True)
    
    # Input area
    input_text = st.text_area(
        "**Paste your academic text below:**",
        height=180,
        placeholder="Example: 'Cancer research has shown significant advancements in recent years. The development of targeted therapies has improved patient outcomes substantially. However, challenges remain in early detection and personalized treatment approaches.'",
        key="input_text",
        label_visibility="collapsed"
    )
    
    # Settings
    col1, col2, col3 = st.columns(3)
    with col1:
        similarity_target = st.slider(
            "🎯 Target Similarity",
            min_value=5,
            max_value=40,
            value=15,
            help="Lower percentage = more different from original"
        )
    with col2:
        max_attempts = st.slider(
            "🔄 Max Attempts",
            min_value=1,
            max_value=10,
            value=5,
            help="More attempts = better results but longer processing"
        )
    with col3:
        rewrite_intensity = st.slider(
            "⚡ Rewrite Intensity",
            min_value=0.3,
            max_value=1.0,
            value=0.7,
            help="Higher intensity = more aggressive rewriting"
        )
    
    # Action buttons
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if st.button("🚀 **Start Advanced Rewriting**", use_container_width=True, type="primary"):
            if input_text.strip():
                with st.spinner("🧪 Rewriting your text with advanced AI algorithms..."):
                    # Perform rewriting
                    rewritten, similarity, stats, attempts_used = rewriter.guarantee_low_similarity(
                        input_text, similarity_target, max_attempts
                    )
                    
                    # Store results
                    st.session_state.rewritten_text = rewritten
                    st.session_state.similarity = similarity
                    st.session_state.rewrite_stats = stats
                    st.session_state.rewrite_stats['attempts_used'] = attempts_used
                    st.session_state.show_results = True
                    
            else:
                st.warning("⚠️ Please enter some text to rewrite!")
    
    with col2:
        if st.button("🧹 **Clear All**", use_container_width=True):
            st.session_state.rewritten_text = None
            st.session_state.similarity = None
            st.session_state.rewrite_stats = {}
            st.session_state.show_results = False
            st.rerun()
    
    with col3:
        if st.session_state.rewritten_text:
            st.download_button(
                "💾 **Download**",
                st.session_state.rewritten_text,
                file_name="rewritten_academic_text.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- RESULTS SECTION (PERSISTENT) ---
if st.session_state.show_results and st.session_state.rewritten_text:
    with st.container():
        st.markdown("""
        <div class="glass-box" style="border: 2px solid rgba(0, 255, 255, 0.3); margin-top: 2rem;">
            <h3 style="color: #00eaff; text-align: center; margin-bottom: 1.5rem;">
                ✨ Rewritten Academic Text
            </h3>
        """, unsafe_allow_html=True)
        
        # Display performance metrics
        stats = st.session_state.rewrite_stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Similarity", f"{st.session_state.similarity:.1f}%")
        with col2:
            st.metric("Words Replaced", stats.get('replacements', 0))
        with col3:
            st.metric("Sentences", f"{stats.get('original_sentences', 0)} → {stats.get('final_sentences', 0)}")
        with col4:
            st.metric("Attempts Used", stats.get('attempts_used', 1))
        
        # Display rewritten text
        st.text_area(
            "**Rewritten Text:**",
            value=st.session_state.rewritten_text,
            height=250,
            key="output_text",
            label_visibility="collapsed"
        )
        
        # Success indicators
        if st.session_state.similarity <= 10:
            st.success(f"🎉 Outstanding! Only {st.session_state.similarity:.1f}% similarity - Excellent academic rewriting!")
            st.balloons()
        elif st.session_state.similarity <= 15:
            st.success(f"✅ Excellent! {st.session_state.similarity:.1f}% similarity - High-quality academic rewrite")
        elif st.session_state.similarity <= similarity_target:
            st.success(f"👍 Good! {st.session_state.similarity:.1f}% similarity - Within target range")
        else:
            st.warning(f"⚠️ {st.session_state.similarity:.1f}% similarity - Try increasing attempts or intensity")
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- VOCABULARY STATS IN SIDEBAR ---
with st.sidebar:
    st.markdown("### 📊 System Statistics")
    
    # Vocabulary stats
    vocab_stats = rewriter.vocab_loader
    st.markdown(f"""
    <div class="stats-card">
        <h4 style="color: #4ECDC4; margin-bottom: 1rem;">📚 Vocabulary Database</h4>
        <p><strong>Total Files Loaded:</strong> {vocab_stats.loaded_files}</p>
        <p><strong>Total Words:</strong> {vocab_stats.total_words:,}</p>
        <p><strong>Failed Files:</strong> {vocab_stats.failed_files}</p>
        <p><strong>Status:</strong> {'✅ Ready' if st.session_state.vocab_initialized else '⚠️ Basic'}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # File loading details
    with st.expander("📁 File Loading Details", expanded=False):
        if vocab_stats.file_stats:
            # Show summary of loaded files
            loaded_files = [f for f in vocab_stats.file_stats if '✅' in f['status']]
            error_files = [f for f in vocab_stats.file_stats if '❌' in f['status']]
            
            st.write(f"**Loaded Successfully:** {len(loaded_files)} files")
            st.write(f"**With Errors:** {len(error_files)} files")
            
            if error_files:
                st.write("**Files with errors:**")
                for file_stat in error_files[:5]:  # Show first 5 errors
                    st.error(f"{file_stat['file']}: {file_stat['status']}")
    
    st.markdown("---")
    st.markdown("### ⚡ Quick Tips")
    st.info("""
    **🎯 For Best Results:**
    - Use **5-15%** similarity for academic papers
    - Set **5-8 attempts** for optimal balance
    - **Higher intensity** = more creative rewriting
    - **Longer texts** produce better variations
    
    **📊 Similarity Guide:**
    - <10%: Excellent
    - 10-15%: Very Good  
    - 15-25%: Good
    - >25%: Needs improvement
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div class="footer">
    💻 **Developed with 💙 by Zariab**<br>
    🧬 Inspired by DNA & Biotechnology • 🔬 Powered by Advanced AI Algorithms<br>
    📚 {:,} Vocabulary Words • Optimized for Academic and Research Text
</div>
""".format(rewriter.vocab_loader.total_words), unsafe_allow_html=True)
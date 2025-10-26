# =========================
# FIXED EXTREME REWRITER 
# =========================

import streamlit as st
import random
import re

# -------------------------
# ENHANCED REWRITER CLASS
# -------------------------
class FixedRewriter:
    def __init__(self):
        self.replacements = {}
        self.setup_vocabulary()
        
    def setup_vocabulary(self):
        # Enhanced synonym database
        self.replacements = {
            'cancer': ['malignancy', 'carcinogenic condition', 'neoplastic disease'],
            'cells': ['cellular structures', 'biological units', 'tissue components'],
            'growth': ['proliferation', 'expansion', 'development'],
            'abnormal': ['irregular', 'atypical', 'deviant'],
            'tumors': ['neoplasms', 'growths', 'malignant masses'],
            'metastasis': ['disease dissemination', 'cancer spreading', 'secondary growth'],
            'treatment': ['therapy', 'intervention', 'medical management'],
            'diagnosis': ['detection', 'identification', 'medical assessment'],
            'surgery': ['surgical intervention', 'operative procedure', 'resection'],
            'chemotherapy': ['cytotoxic treatment', 'anticancer drugs', 'systemic therapy'],
            'radiation': ['radiotherapy', 'irradiation', 'beam therapy'],
            'genetic': ['hereditary', 'inherited', 'DNA-based'],
            'mutations': ['genetic alterations', 'DNA changes', 'molecular variations'],
            'risk': ['probability', 'likelihood', 'susceptibility'],
            'prevention': ['prophylaxis', 'risk reduction', 'preventive measures']
        }

    def aggressive_sentence_restructuring(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 1:
            return text
            
        # Completely reorder sentences
        random.shuffle(sentences)
        
        # Add varied connectors
        connectors = [
            'From a clinical perspective, ',
            'In medical terms, ',
            'Biologically speaking, ',
            'Pathologically, ',
            'Therapeutically, '
        ]
        
        result = random.choice(connectors) + sentences[0].lower()
        for i in range(1, len(sentences)):
            if random.random() < 0.6:
                connector = random.choice([' Furthermore, ', ' Additionally, ', ' Moreover, '])
                result += connector + sentences[i].lower()
            else:
                result += '. ' + sentences[i]
        
        return result + '.'

    def deep_word_replacement(self, text):
        words = text.split()
        new_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"')
            
            # Skip very short words
            if len(clean_word) <= 3:
                new_words.append(word)
                continue
                
            # Aggressive replacement
            if clean_word in self.replacements and random.random() < 0.9:
                replacement = random.choice(self.replacements[clean_word])
                # Preserve capitalization
                replacement = replacement.capitalize() if word[0].isupper() else replacement
                new_words.append(replacement)
            else:
                new_words.append(word)
                
        return ' '.join(new_words)

    def change_sentence_structure(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        restructured = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) > 8:
                # Split long sentences
                if random.random() < 0.7:
                    mid = len(words) // 2
                    first_part = ' '.join(words[:mid])
                    second_part = ' '.join(words[mid:])
                    restructured.append(first_part + '.')
                    restructured.append(second_part.capitalize())
                else:
                    restructured.append(sentence)
            else:
                # Combine short sentences or add detail
                if len(words) < 6 and random.random() < 0.5:
                    enhanced = f"This process involves {sentence.lower()}"
                    restructured.append(enhanced)
                else:
                    restructured.append(sentence)
                    
        return '. '.join(restructured) + '.'

    def add_medical_paraphrasing(self, text):
        # Medical-specific paraphrasing patterns
        paraphrases = {
            r'uncontrolled growth': 'dysregulated proliferation',
            r'normal cells': 'healthy cellular components',
            r'cancerous cells': 'malignant cellular entities',
            r'spread to distant organs': 'disseminate to remote anatomical sites',
            r'bloodstream or lymphatic system': 'hematogenous or lymphogenous pathways',
            r'early detection': 'timely identification',
            r'effective treatment': 'successful therapeutic intervention',
            r'lifestyle choices': 'behavioral factors',
            r'public health challenge': 'population health concern'
        }
        
        result = text
        for pattern, replacement in paraphrases.items():
            if random.random() < 0.7:
                result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
                
        return result

# Initialize the fixed rewriter
fixed_rewriter = FixedRewriter()

# -------------------------
# WORKING REWRITER FUNCTION
# -------------------------
def working_rewriter(original_text):
    clean_text = original_text.strip()
    
    # Apply multiple aggressive transformations
    result = clean_text
    result = fixed_rewriter.aggressive_sentence_restructuring(result)
    result = fixed_rewriter.deep_word_replacement(result)
    result = fixed_rewriter.change_sentence_structure(result)
    result = fixed_rewriter.add_medical_paraphrasing(result)
    
    return result

# -------------------------
# SIMILARITY CALCULATION (FIXED)
# -------------------------
def calculate_real_similarity(original, rewritten):
    original_words = set(re.findall(r'\w+', original.lower()))
    rewritten_words = set(re.findall(r'\w+', rewritten.lower()))
    
    if not original_words:
        return 0
        
    common_words = original_words.intersection(rewritten_words)
    similarity = len(common_words) / len(original_words) * 100
    
    return similarity

# -------------------------
# GUARANTEE LOW SIMILARITY (FIXED)
# -------------------------
def guarantee_real_rewrite(original_text, target_similarity=20, max_attempts=8):
    best_result = None
    best_similarity = 100
    
    for attempt in range(max_attempts):
        rewritten = working_rewriter(original_text)
        similarity = calculate_real_similarity(original_text, rewritten)
        
        st.write(f"Attempt {attempt + 1}: Similarity = {similarity:.1f}%")
        
        if similarity < best_similarity:
            best_result = rewritten
            best_similarity = similarity
            
        if similarity <= target_similarity:
            return rewritten, similarity
            
    return best_result, best_similarity

# =========================
# TEST WITH YOUR CANCER TEXT
# =========================

# Your original cancer text
cancer_text = """Cancer is a complex and devastating group of diseases characterized by the uncontrolled growth and spread of abnormal cells in the body. Unlike normal cells, which follow a regulated cycle of growth, division, and death, cancerous cells bypass these controls, allowing them to proliferate unchecked. This abnormal growth can form tumors, invade surrounding tissues, and even spread to distant organs through the bloodstream or lymphatic system, a process known as metastasis. There are over 100 different types of cancer, each classified based on the cell type or organ of origin, such as breast cancer, lung cancer, or leukemia."""

# Test the rewriter
if st.button("🚀 Test Fixed Rewriter"):
    with st.spinner("Rewriting with aggressive transformations..."):
        rewritten, similarity = guarantee_real_rewrite(cancer_text, target_similarity=15)
    
    st.markdown("### Original Text")
    st.write(cancer_text)
    
    st.markdown("### Rewritten Text")
    st.write(rewritten)
    
    st.markdown(f"### Similarity: {similarity:.1f}%")
    
    if similarity > 30:
        st.error("Still too similar! The rewriter needs more work.")
    elif similarity > 15:
        st.warning("Getting better, but could be lower.")
    else:
        st.success("Excellent! Low similarity achieved.")
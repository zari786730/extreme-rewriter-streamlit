import random
import re
import os
import zipfile
from pathlib import Path

# Import your custom libraries
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# =========================
# NLTK DATA EXTRACTION (RUNS ONLY ONCE)
# =========================

def setup_nltk_data():
    """Extract NLTK data only once - creates flag file to prevent re-extraction"""
    nltk_base_path = Path("nltk_data")
    extraction_flag = nltk_base_path / ".extracted"
    
    # If already extracted, skip
    if extraction_flag.exists():
        print("✓ NLTK data already extracted")
        return True
    
    if not nltk_base_path.exists():
        print("✗ NLTK data directory not found")
        return False

    print("Extracting NLTK data zip files (first time only)...")
    
    extracted_count = 0
    for root, dirs, files in os.walk(nltk_base_path):
        for file in files:
            if file.endswith('.zip'):
                zip_path = Path(root) / file
                extract_path = Path(root) / file.replace('.zip', '')
                
                # Skip if already extracted
                if extract_path.exists():
                    continue
                    
                extract_path.mkdir(exist_ok=True)
                
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_path)
                    extracted_count += 1
                    print(f"✓ Extracted: {file}")
                except Exception as e:
                    print(f"✗ Failed to extract {file}: {str(e)}")
    
    # Create flag file to prevent future extractions
    if extracted_count > 0:
        extraction_flag.touch()
        print(f"✓ NLTK extraction completed! Extracted {extracted_count} files")
    else:
        print("✓ No new files to extract")
    
    return True

# Run setup once
nltk_ready = setup_nltk_data()

# =========================
# NLTK IMPORTS (AFTER EXTRACTION)
# =========================

try:
    import nltk
    from nltk import pos_tag
    from nltk.corpus import wordnet
    from nltk.tokenize import RegexpTokenizer
    
    # Set NLTK data path
    if Path("nltk_data").exists():
        nltk.data.path.append("nltk_data")
    
    # Initialize tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    
    print("✓ NLTK modules loaded successfully")
    
except ImportError as e:
    print(f"✗ NLTK import failed: {e}")
    # Fallback implementations
    class FallbackTokenizer:
        def tokenize(self, text):
            return re.findall(r'\w+', text)
    
    tokenizer = FallbackTokenizer()
    
    def pos_tag(tokens):
        # Simple fallback POS tagging
        return [(token, 'NN') for token in tokens]
    
    class FallbackWordnet:
        def synsets(self, word, pos=None):
            return []
    
    wordnet = FallbackWordnet()

# =========================
# UTILITY FUNCTIONS
# =========================

def get_wordnet_pos(treebank_tag):
    """Map POS tag to WordNet POS for synonym lookup"""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def get_synonyms(word, pos=None):
    """Fetch synonyms from WordNet filtered by POS"""
    try:
        if not pos:
            syns = wordnet.synsets(word)
        else:
            syns = wordnet.synsets(word, pos=pos)
        
        lemmas = set()
        for syn in syns:
            for lemma in syn.lemmas():
                lemma_name = lemma.name().replace('_', ' ')
                if lemma_name.lower() != word.lower() and len(lemma_name.split()) == 1:
                    lemmas.add(lemma_name)
        return list(lemmas)[:6]  # Limit to 6 synonyms
    except:
        return []

def split_clauses(sentence):
    """Split a sentence into smaller clauses for clause-level rewriting"""
    return re.split(r',|;| - |: ', sentence)

def join_clauses(clauses):
    """Rejoin clauses into a sentence with mild connectors"""
    if not clauses:
        return ""
    sentence = clauses[0].strip().capitalize()
    connectors = [", ", ", and ", ", but ", "; "]
    for clause in clauses[1:]:
        sentence += random.choice(connectors) + clause.strip().lower()
    return sentence

# =========================
# PURE REWRITER
# =========================

class PureRewriter:
    def __init__(self):
        self.replacements = {}
        self.load_libraries()
        print("✓ PureRewriter initialized")

    def load_libraries(self):  
        # Health terms  
        for w, r in health_terms.items():  
            self.replacements[w] = [r] if isinstance(r, str) else r  
        # General words  
        for w, r in general_words.items():  
            self.replacements[w] = [r] if isinstance(r, str) else r  
        print(f"✓ Loaded {len(self.replacements)} words from libraries")

    def synonym_replace_sentence(self, sentence):  
        """Replace nouns, verbs, adjectives, adverbs with synonyms (one pass)"""  
        words = sentence.split()  
        tagged = pos_tag(words)  
        new_words = []  

        for word, tag in tagged:  
            clean_word = word.strip('.,!?;:"')  
            wn_pos = get_wordnet_pos(tag)  

            # Skip very short/common words  
            if len(clean_word) <= 2 or clean_word.lower() in ['the','a','an','and','or','but','in','on','at']:  
                new_words.append(word)  
                continue  

            # Library replacement  
            if clean_word.lower() in self.replacements:  
                replacement = random.choice(self.replacements[clean_word.lower()])  
                replacement = replacement.capitalize() if word[0].isupper() else replacement  
                new_words.append(replacement)  
                continue  

            # WordNet synonym replacement  
            synonyms = get_synonyms(clean_word, wn_pos)  
            if synonyms:  
                replacement = random.choice(synonyms)  
                replacement = replacement.capitalize() if word[0].isupper() else replacement  
                new_words.append(replacement)  
                continue  

            new_words.append(word)  

        return ' '.join(new_words)  

    def multi_pass_synonym_replace(self, sentence, passes=2):  
        """Apply synonym replacement multiple times for better coverage"""  
        result = sentence
        for _ in range(passes):  
            # Clause-level replacement  
            clauses = split_clauses(result)  
            clauses = [self.synonym_replace_sentence(c) for c in clauses]  
            result = join_clauses(clauses)  
        return result  

    def restructure_paragraph(self, text):  
        """Shuffle sentences lightly and add connectors throughout paragraph"""  
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]  
        if len(sentences) <= 1:  
            return text  

        # Shuffle sentences randomly  
        for i in range(len(sentences)):  
            if random.random() < 0.5:  
                swap_idx = random.randint(0, len(sentences)-1)  
                sentences[i], sentences[swap_idx] = sentences[swap_idx], sentences[i]  

        # Add connectors between sentences  
        connectors = ['Furthermore, ', 'Moreover, ', 'In addition, ', 'Notably, ']  
        paragraph = sentences[0]  
        for s in sentences[1:]:  
            if random.random() < 0.4:  
                paragraph += ' ' + random.choice(connectors) + s.lower()  
            else:  
                paragraph += '. ' + s  
        return paragraph + '.'

# Initialize rewriter
rewriter = PureRewriter()

# =========================
# EXTREME REWRITER
# =========================

def extreme_rewriter(text):
    text = text.strip().strip('"').strip("'")

    # Multi-pass synonym replacement on all sentences  
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]  
    sentences = [rewriter.multi_pass_synonym_replace(s, passes=2) for s in sentences]  
    text = '. '.join(sentences)  

    # Paragraph-level restructuring  
    text = rewriter.restructure_paragraph(text)  

    # Final grammar correction  
    text = correct_grammar(text)  

    return text

# =========================
# SIMILARITY CALCULATION
# =========================

def calculate_similarity(original, rewritten):
    original_words = set(tokenizer.tokenize(original.lower()))
    rewritten_words = set(tokenizer.tokenize(rewritten.lower()))
    common = original_words.intersection(rewritten_words)
    if not original_words:
        return 0
    return len(common)/len(original_words)*100

# =========================
# GUARANTEE LOW SIMILARITY
# =========================

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
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

print("✅ Backend loaded successfully!")
=========================

NON-AI EXTREME REWRITER BACKEND (MULTI-PASS & CLAUSE-LEVEL)

=========================

import random
import re
import os
import zipfile
import nltk
from pathlib import Path
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer

# Import your custom libraries
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words
from grammar_corrector import correct_grammar

# Merge health terms
health_terms.update(health_terms_2)

# Initialize tokenizer
tokenizer = RegexpTokenizer(r'\w+')

=========================

NLTK DATA SETUP & EXTRACTION

=========================

def setup_nltk_data():
    """Setup NLTK data path and extract zip files"""
    nltk_base_path = Path("nltk_data")
    
    if not nltk_base_path.exists():
        print("NLTK data directory not found. Creating...")
        nltk_base_path.mkdir(exist_ok=True)
        return
    
    print("Setting up NLTK data...")
    
    # Extract all zip files
    zip_files_found = False
    for root, dirs, files in os.walk(nltk_base_path):
        for file in files:
            if file.endswith('.zip'):
                zip_files_found = True
                zip_path = Path(root) / file
                extract_path = Path(root) / file.replace('.zip', '')
                
                # Create extraction directory if it doesn't exist
                extract_path.mkdir(exist_ok=True)
                
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_path)
                    print(f"✓ Extracted: {zip_path} -> {extract_path}")
                except Exception as e:
                    print(f"✗ Failed to extract {zip_path}: {str(e)}")
    
    if not zip_files_found:
        print("No zip files found in nltk_data directory")
    
    # Add nltk_data path to NLTK's data path
    nltk.data.path.insert(0, str(nltk_base_path))
    
    # Also add all subdirectories to the path
    for root, dirs, files in os.walk(nltk_base_path):
        nltk.data.path.insert(0, root)
    
    print(f"NLTK data paths: {nltk.data.path}")
    print("NLTK data setup completed!")

def verify_nltk_data():
    """Verify that required NLTK data is available"""
    required_data = [
        'taggers/averaged_perceptron_tagger',
        'corpora/wordnet',
        'tokenizers/punkt'
    ]
    
    print("Verifying NLTK data availability...")
    for data_path in required_data:
        try:
            nltk.data.find(data_path)
            print(f"✓ Found: {data_path}")
        except LookupError:
            print(f"✗ Missing: {data_path}")
            # Try to find it in our custom paths
            found = False
            for custom_path in nltk.data.path:
                full_path = Path(custom_path) / data_path
                if full_path.exists():
                    print(f"  Found in custom path: {full_path}")
                    found = True
                    break
            if not found:
                print(f"  WARNING: {data_path} not found in any path")

# Run setup on startup
setup_nltk_data()
verify_nltk_data()

=========================

UTILITY FUNCTIONS

=========================

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
                if lemma_name.lower() != word.lower():
                    lemmas.add(lemma_name)
        return list(lemmas)
    except Exception as e:
        print(f"Error getting synonyms for '{word}': {e}")
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

=========================

PURE REWRITER

=========================

class PureRewriter:
    def __init__(self):
        self.replacements = {}
        self.load_libraries()

    def load_libraries(self):  
        # Health terms  
        for w, r in health_terms.items():  
            self.replacements[w] = [r] if isinstance(r, str) else r  
        # General words  
        for w, r in general_words.items():  
            self.replacements[w] = [r] if isinstance(r, str) else r  

    def synonym_replace_sentence(self, sentence):  
        """Replace nouns, verbs, adjectives, adverbs with synonyms (one pass)"""  
        try:
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
        except Exception as e:
            print(f"Error in synonym_replace_sentence: {e}")
            return sentence

    def multi_pass_synonym_replace(self, sentence, passes=2):  
        """Apply synonym replacement multiple times for better coverage"""  
        try:
            for _ in range(passes):  
                # Clause-level replacement  
                clauses = split_clauses(sentence)  
                clauses = [self.synonym_replace_sentence(c) for c in clauses]  
                sentence = join_clauses(clauses)  
            return sentence
        except Exception as e:
            print(f"Error in multi_pass_synonym_replace: {e}")
            return sentence

    def restructure_paragraph(self, text):  
        """Shuffle sentences lightly and add connectors throughout paragraph"""  
        try:
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
        except Exception as e:
            print(f"Error in restructure_paragraph: {e}")
            return text

# Initialize rewriter
print("Initializing PureRewriter...")
rewriter = PureRewriter()
print("PureRewriter initialized successfully!")

=========================

EXTREME REWRITER

=========================

def extreme_rewriter(text):
    try:
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
    except Exception as e:
        print(f"Error in extreme_rewriter: {e}")
        return text

=========================

SIMILARITY CALCULATION

=========================

def calculate_similarity(original, rewritten):
    try:
        original_words = set(tokenizer.tokenize(original.lower()))
        rewritten_words = set(tokenizer.tokenize(rewritten.lower()))
        common = original_words.intersection(rewritten_words)
        if not original_words:
            return 0
        return len(common)/len(original_words)*100
    except Exception as e:
        print(f"Error in calculate_similarity: {e}")
        return 0

=========================

GUARANTEE LOW SIMILARITY

=========================

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    try:
        best_result = None
        best_similarity = 100
        for attempt in range(max_attempts):
            print(f"Rewriting attempt {attempt + 1}/{max_attempts}")
            rewritten = extreme_rewriter(original_text)
            similarity = calculate_similarity(original_text, rewritten)
            print(f"Attempt {attempt + 1}: Similarity = {similarity:.1f}%")
            
            if similarity < best_similarity:
                best_result = rewritten
                best_similarity = similarity
            if similarity <= max_similarity:
                return rewritten, similarity
        return best_result, best_similarity
    except Exception as e:
        print(f"Error in guarantee_low_similarity: {e}")
        return original_text, 100
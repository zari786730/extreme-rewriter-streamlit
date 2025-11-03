from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nltk
from nltk.corpus import wordnet
import re
import random
import json
from collections import defaultdict
import os

# Download required NLTK data
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)
CORS(app)

class UniversalTextEnhancer:
    def __init__(self):
        self.synonym_cache = {}
        self.scientific_terms = self.load_scientific_terms()
        
    def load_scientific_terms(self):
        """Load domain-specific terminology to preserve accuracy"""
        return {
            # Medical/Scientific terms that should NOT be changed
            'p53': 'p53', 'dna': 'DNA', 'rna': 'RNA', 'apoptosis': 'apoptosis',
            'genome': 'genome', 'protein': 'protein', 'cell': 'cell',
            'tumor': 'tumor', 'cancer': 'cancer', 'gene': 'gene',
            'mutated': 'mutated', 'genetic': 'genetic', 'mutation': 'mutation',
            'therapist': 'therapist', 'medical': 'medical', 'clinical': 'clinical',
            'molecular': 'molecular', 'cellular': 'cellular', 'biological': 'biological',
            
            # Academic terms
            'research': 'research', 'study': 'study', 'analysis': 'analysis',
            'methodology': 'methodology', 'hypothesis': 'hypothesis',
            
            # Technical terms that should be preserved
            'algorithm': 'algorithm', 'programming': 'programming',
            'software': 'software', 'hardware': 'hardware'
        }
    
    def is_protected_term(self, word):
        """Check if word is a protected scientific/technical term"""
        return word.lower() in self.scientific_terms
    
    def get_contextual_synonyms(self, word, pos_tag):
        """Get contextually appropriate synonyms with POS filtering"""
        if self.is_protected_term(word):
            return []
            
        if word in self.synonym_cache:
            return self.synonym_cache[word]
        
        synonyms = set()
        for syn in wordnet.synsets(word):
            # Filter by part of speech
            if self.match_pos(syn.pos(), pos_tag):
                for lemma in syn.lemmas():
                    synonym = lemma.name().replace('_', ' ').lower()
                    if (synonym != word.lower() and 
                        len(synonym.split()) == 1 and
                        len(synonym) > 2 and
                        not any(char.isdigit() for char in synonym)):
                        synonyms.add(synonym)
        
        # Filter to most common synonyms
        filtered = list(synonyms)[:5]
        self.synonym_cache[word] = filtered
        return filtered
    
    def match_pos(self, wordnet_pos, nltk_pos):
        """Match WordNet POS tags with NLTK POS tags"""
        pos_mapping = {
            'n': ['NN', 'NNS', 'NNP', 'NNPS'],  # Nouns
            'v': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],  # Verbs
            'a': ['JJ', 'JJR', 'JJS'],  # Adjectives
            'r': ['RB', 'RBR', 'RBS']   # Adverbs
        }
        
        for wn_pos, nltk_tags in pos_mapping.items():
            if wordnet_pos == wn_pos and nltk_pos in nltk_tags:
                return True
        return False
    
    def enhance_sentence_flow(self, sentence):
        """Improve sentence structure and flow"""
        words = nltk.word_tokenize(sentence)
        if len(words) <= 5:  # Don't change very short sentences
            return sentence
            
        tagged = nltk.pos_tag(words)
        
        enhanced_words = []
        i = 0
        changes_made = 0
        max_changes = max(2, len(words) // 10)  # Limit changes per sentence
        
        while i < len(tagged) and changes_made < max_changes:
            word, pos = tagged[i]
            
            # Only replace common words (not proper nouns, etc.)
            if (pos in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] and
                not self.is_protected_term(word) and
                random.random() < 0.25):  # 25% chance per eligible word
                
                synonyms = self.get_contextual_synonyms(word, pos)
                if synonyms:
                    enhanced_words.append(random.choice(synonyms))
                    changes_made += 1
                    i += 1
                    continue
            
            enhanced_words.append(word)
            i += 1
        
        return ' '.join(enhanced_words)
    
    def restructure_paragraph(self, text):
        """Improve paragraph structure"""
        sentences = nltk.sent_tokenize(text)
        if len(sentences) <= 1:
            return text
        
        enhanced_sentences = []
        
        # Vary sentence starters for middle sentences
        transition_words = [
            'Additionally,', 'Furthermore,', 'Moreover,', 'However,',
            'Therefore,', 'Consequently,', 'Interestingly,', 'Notably,'
        ]
        
        for i, sentence in enumerate(sentences):
            enhanced_sentence = self.enhance_sentence_flow(sentence)
            
            # Add transition words to some sentences (not first, not all)
            if i > 0 and i < len(sentences) - 1 and random.random() < 0.3:
                transition = random.choice(transition_words)
                enhanced_sentence = f"{transition} {enhanced_sentence[0].lower() + enhanced_sentence[1:]}"
            
            enhanced_sentences.append(enhanced_sentence)
        
        return ' '.join(enhanced_sentences)
    
    def fix_grammar_and_punctuation(self, text):
        """Fix common grammar and punctuation issues"""
        # Fix spaces before punctuation
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        
        # Ensure space after punctuation
        text = re.sub(r'([.,!?;])([A-Za-z])', r'\1 \2', text)
        
        # Fix multiple spaces
        text = re.sub(r' +', ' ', text)
        
        # Fix capitalization after punctuation
        sentences = nltk.sent_tokenize(text)
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                # Ensure first character is uppercase
                corrected = sentence[0].upper() + sentence[1:]
                corrected_sentences.append(corrected)
            else:
                corrected_sentences.append(sentence)
        
        return ' '.join(corrected_sentences)
    
    def humanize_text(self, text):
        """Main method to humanize text while preserving meaning"""
        if not text or not text.strip():
            return text
        
        try:
            # Step 1: Restructure paragraphs for better flow
            humanized = self.restructure_paragraph(text)
            
            # Step 2: Fix grammar and punctuation
            humanized = self.fix_grammar_and_punctuation(humanized)
            
            # Step 3: Ensure proper spacing and formatting
            humanized = re.sub(r'\s+', ' ', humanized).strip()
            
            return humanized
            
        except Exception as e:
            # If processing fails, return original with basic cleaning
            print(f"Enhancement error: {e}")
            return self.fix_grammar_and_punctuation(text)

# Initialize the enhancer
enhancer = UniversalTextEnhancer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/enhance', methods=['POST'])
def enhance_text():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'No text provided in request'
            }), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Text cannot be empty'
            }), 400
        
        # Get enhancement parameters
        aggression = data.get('aggression', 0.5)  # 0.1 to 1.0
        preserve_terms = data.get('preserve_terms', True)
        
        # Enhance the text
        enhanced_text = enhancer.humanize_text(text)
        
        # Calculate statistics
        original_words = len(text.split())
        enhanced_words = len(enhanced_text.split())
        change_percentage = abs(enhanced_words - original_words) / original_words * 100
        
        return jsonify({
            'success': True,
            'original_text': text,
            'enhanced_text': enhanced_text,
            'statistics': {
                'original_length': len(text),
                'enhanced_length': len(enhanced_text),
                'original_words': original_words,
                'enhanced_words': enhanced_words,
                'change_percentage': round(change_percentage, 2)
            },
            'message': 'Text enhanced successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Processing error: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Universal Text Enhancer',
        'version': '1.0.0'
    })

@app.route('/api/batch-enhance', methods=['POST'])
def batch_enhance():
    """Enhance multiple texts at once"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        
        if not texts:
            return jsonify({
                'success': False,
                'error': 'No texts provided'
            }), 400
        
        results = []
        for text in texts:
            enhanced = enhancer.humanize_text(text)
            results.append({
                'original': text,
                'enhanced': enhanced
            })
        
        return jsonify({
            'success': True,
            'results': results,
            'total_processed': len(results)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Batch processing error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
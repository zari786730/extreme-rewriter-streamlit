from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.corpus import wordnet
import re
import random
import json
from typing import List, Tuple, Dict
import os

# Download NLTK data
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt', quiet=True)

app = Flask(__name__)
CORS(app)

class UniversalTextEnhancer:
    def __init__(self):
        self.synonym_cache = {}
        self.protected_terms = self._load_protected_terms()
        self.quality_checks = self._load_quality_checks()
        
    def _load_protected_terms(self) -> set:
        """Load terms that should never be changed"""
        protected = {
            # Scientific
            'p53', 'dna', 'rna', 'apoptosis', 'genome', 'protein', 'cell',
            'tumor', 'cancer', 'gene', 'mutated', 'genetic', 'mutation',
            'molecular', 'cellular', 'biological', 'therapy', 'clinical',
            'medical', 'carcinoma', 'sarcoma', 'leukemia', 'lymphoma',
            
            # Technical
            'algorithm', 'software', 'hardware', 'programming', 'database',
            'api', 'framework', 'javascript', 'python', 'java',
            
            # Academic
            'research', 'study', 'analysis', 'methodology', 'hypothesis',
            'theory', 'experiment', 'data', 'results', 'conclusion',
            
            # Business
            'company', 'business', 'market', 'customer', 'product',
            'service', 'revenue', 'profit', 'strategy',
            
            # Common critical words
            'because', 'however', 'moreover', 'therefore', 'although',
            'while', 'since', 'although', 'unless', 'until'
        }
        return {term.lower() for term in protected}
    
    def _load_quality_checks(self) -> Dict:
        """Quality control parameters"""
        return {
            'max_sentence_length': 50,
            'min_sentence_length': 3,
            'max_paragraph_length': 500,
            'synonym_quality_threshold': 0.7,
            'max_changes_per_sentence': 3
        }
    
    def get_high_quality_synonyms(self, word: str, pos: str) -> List[str]:
        """Get only high-quality, context-appropriate synonyms"""
        if word.lower() in self.protected_terms:
            return []
            
        cache_key = f"{word}_{pos}"
        if cache_key in self.synonym_cache:
            return self.synonym_cache[cache_key]
        
        synonyms = set()
        for synset in wordnet.synsets(word):
            # Filter by part of speech and quality
            if self._is_good_synonym(synset, word, pos):
                for lemma in synset.lemmas():
                    synonym = lemma.name().replace('_', ' ').lower()
                    if self._validate_synonym(synonym, word):
                        synonyms.add(synonym)
        
        # Limit and cache results
        result = list(synonyms)[:5]
        self.synonym_cache[cache_key] = result
        return result
    
    def _is_good_synonym(self, synset, original_word: str, pos: str) -> bool:
        """Check if synonym is appropriate"""
        pos_mapping = {
            'n': ['NN', 'NNS', 'NNP', 'NNPS'],
            'v': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
            'a': ['JJ', 'JJR', 'JJS'],
            'r': ['RB', 'RBR', 'RBS']
        }
        
        # Check POS match
        for wn_pos, nltk_tags in pos_mapping.items():
            if synset.pos() == wn_pos and pos in nltk_tags:
                return True
        return False
    
    def _validate_synonym(self, synonym: str, original: str) -> bool:
        """Validate synonym quality"""
        # Basic checks
        if (synonym == original.lower() or
            len(synonym) <= 2 or
            any(char.isdigit() for char in synonym) or
            len(synonym.split()) > 1):
            return False
        
        # Quality checks
        if len(synonym) / len(original) > 2.0:  # Too long
            return False
            
        if len(synonym) / len(original) < 0.5:  # Too short
            return False
            
        return True
    
    def enhance_sentence_structure(self, sentence: str) -> str:
        """Intelligently enhance sentence structure"""
        if len(sentence.split()) < 4:  # Don't change short sentences
            return sentence
            
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        
        enhanced_words = []
        changes_made = 0
        
        for i, (word, pos) in enumerate(tagged):
            # Decide whether to replace this word
            should_replace = (
                random.random() < 0.3 and  # 30% chance
                changes_made < self.quality_checks['max_changes_per_sentence'] and
                pos in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN'] and
                word.lower() not in self.protected_terms and
                len(word) > 3  # Don't replace very short words
            )
            
            if should_replace:
                synonyms = self.get_high_quality_synonyms(word, pos)
                if synonyms:
                    enhanced_words.append(random.choice(synonyms))
                    changes_made += 1
                    continue
            
            enhanced_words.append(word)
        
        return ' '.join(enhanced_words)
    
    def improve_paragraph_flow(self, text: str) -> str:
        """Improve overall paragraph structure and flow"""
        sentences = nltk.sent_tokenize(text)
        
        if len(sentences) <= 1:
            return self.enhance_sentence_structure(text)
        
        enhanced_sentences = []
        transition_words = [
            'Additionally,', 'Furthermore,', 'Moreover,', 'However,',
            'Therefore,', 'Consequently,', 'Interestingly,', 'Notably,',
            'Specifically,', 'Generally,'
        ]
        
        for i, sentence in enumerate(sentences):
            enhanced_sentence = self.enhance_sentence_structure(sentence)
            
            # Add variety to sentence starters (but not to first sentence)
            if i > 0 and random.random() < 0.4:  # 40% chance
                transition = random.choice(transition_words)
                # Ensure proper capitalization after transition
                if enhanced_sentence and enhanced_sentence[0].isupper():
                    enhanced_sentence = enhanced_sentence[0].lower() + enhanced_sentence[1:]
                enhanced_sentence = f"{transition} {enhanced_sentence}"
            
            enhanced_sentences.append(enhanced_sentence)
        
        return ' '.join(enhanced_sentences)
    
    def clean_and_format(self, text: str) -> str:
        """Clean and properly format text"""
        # Fix spacing around punctuation
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        text = re.sub(r'([.,!?;])([A-Za-z])', r'\1 \2', text)
        
        # Fix multiple spaces
        text = re.sub(r' +', ' ', text)
        
        # Ensure proper capitalization
        sentences = nltk.sent_tokenize(text)
        corrected_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                # Capitalize first letter
                corrected = sentence[0].upper() + sentence[1:]
                corrected_sentences.append(corrected)
            else:
                corrected_sentences.append(sentence)
        
        return ' '.join(corrected_sentences).strip()
    
    def calculate_enhancement_metrics(self, original: str, enhanced: str) -> Dict:
        """Calculate enhancement metrics"""
        orig_words = original.split()
        enh_words = enhanced.split()
        
        return {
            'original_length': len(original),
            'enhanced_length': len(enhanced),
            'original_words': len(orig_words),
            'enhanced_words': len(enh_words),
            'change_percentage': round(abs(len(enh_words) - len(orig_words)) / len(orig_words) * 100, 2),
            'readability_score': self.calculate_readability(enhanced)
        }
    
    def calculate_readability(self, text: str) -> float:
        """Simple readability score"""
        sentences = nltk.sent_tokenize(text)
        words = text.split()
        
        if not sentences or not words:
            return 0
            
        avg_sentence_length = len(words) / len(sentences)
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        # Lower score = easier to read
        readability = (avg_sentence_length * 0.4) + (avg_word_length * 0.6)
        return round(readability, 2)
    
    def enhance_text(self, text: str, intensity: float = 0.5) -> Dict:
        """Main enhancement method"""
        if not text or not text.strip():
            return {
                'success': False,
                'error': 'No text provided'
            }
        
        try:
            # Step 1: Clean input
            cleaned_text = self.clean_and_format(text)
            
            # Step 2: Enhance based on intensity
            if intensity < 0.3:
                # Light enhancement - just clean and minor changes
                enhanced_text = self.enhance_sentence_structure(cleaned_text)
            elif intensity > 0.7:
                # Heavy enhancement - full restructuring
                enhanced_text = self.improve_paragraph_flow(cleaned_text)
            else:
                # Moderate enhancement
                enhanced_text = self.improve_paragraph_flow(cleaned_text)
            
            # Step 3: Final cleaning
            final_text = self.clean_and_format(enhanced_text)
            
            # Step 4: Calculate metrics
            metrics = self.calculate_enhancement_metrics(text, final_text)
            
            return {
                'success': True,
                'original_text': text,
                'enhanced_text': final_text,
                'metrics': metrics,
                'message': 'Text enhanced successfully'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Enhancement failed: {str(e)}',
                'original_text': text,
                'enhanced_text': text  # Return original as fallback
            }

# Initialize enhancer
enhancer = UniversalTextEnhancer()

# API Routes
@app.route('/api/enhance', methods=['POST'])
def api_enhance():
    """Main enhancement endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'No text provided'
            }), 400
        
        text = data['text'].strip()
        intensity = min(max(float(data.get('intensity', 0.5)), 0.1), 1.0)
        
        result = enhancer.enhance_text(text, intensity)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'API error: {str(e)}'
        }), 500

@app.route('/api/batch-enhance', methods=['POST'])
def api_batch_enhance():
    """Enhance multiple texts"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        intensity = min(max(float(data.get('intensity', 0.5)), 0.1), 1.0)
        
        if not texts:
            return jsonify({
                'success': False,
                'error': 'No texts provided'
            }), 400
        
        results = []
        for text in texts:
            if isinstance(text, str) and text.strip():
                result = enhancer.enhance_text(text.strip(), intensity)
                results.append(result)
        
        return jsonify({
            'success': True,
            'results': results,
            'total_processed': len(results)
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Batch processing error: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def api_health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Universal Text Enhancer',
        'version': '2.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
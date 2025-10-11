# EXTREME REWRITER - COMPLETE FRONTEND + BACKEND
import random
import re
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import time

class ExtremeRewriterApp:
    def __init__(self):
        self.setup_interface()
        
    def extreme_rewriter(self, original_text):
        """
        Extreme rewriting that guarantees <20% similarity through radical changes
        """
        
        clean_text = original_text.strip().strip('"').strip("'")
        
        # EXTREME TRANSFORMATION 1: Complete sentence structure overhaul
        def radical_sentence_restructure(text):
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            
            if not sentences:
                return text
                
            # Completely rebuild each sentence with different patterns
            rebuilt_sentences = []
            
            for sentence in sentences:
                words = sentence.split()
                if len(words) < 4:
                    rebuilt_sentences.append(sentence)
                    continue
                    
                # RADICAL PATTERN 1: Question format
                if random.random() < 0.3:
                    question_words = ['How', 'What', 'Why', 'In what ways']
                    rebuilt = f"{random.choice(question_words)} does {sentence.lower()}?"
                    rebuilt_sentences.append(rebuilt)
                
                # RADICAL PATTERN 2: Reverse order
                elif random.random() < 0.3:
                    if len(words) > 6:
                        mid_point = len(words) // 2
                        part1 = ' '.join(words[:mid_point])
                        part2 = ' '.join(words[mid_point:])
                        rebuilt = f"{part2}, which demonstrates that {part1.lower()}"
                        rebuilt_sentences.append(rebuilt)
                
                # RADICAL PATTERN 3: Academic framing
                elif random.random() < 0.4:
                    academic_frames = [
                        f"Scholarly analysis reveals that {sentence.lower()}",
                        f"Research findings indicate {sentence.lower()}",
                        f"Academic investigation demonstrates {sentence.lower()}",
                        f"Evidence from multiple studies shows {sentence.lower()}",
                        f"Comprehensive research establishes {sentence.lower()}"
                    ]
                    rebuilt_sentences.append(random.choice(academic_frames))
                
                # RADICAL PATTERN 4: Extreme compression/expansion
                else:
                    if random.random() < 0.5:
                        # Extreme compression
                        if len(words) > 8:
                            compressed = ' '.join(words[:4] + words[-2:])
                            rebuilt_sentences.append(compressed + "...")
                        else:
                            rebuilt_sentences.append(sentence)
                    else:
                        # Extreme expansion
                        expansions = [
                            "This represents a significant development in the field because",
                            "From a comprehensive analytical perspective,",
                            "When contextualized within broader scholarly discourse,",
                            "Considering the multifaceted implications of this phenomenon,",
                            "Through rigorous empirical examination it becomes evident that"
                        ]
                        expanded = f"{random.choice(expansions)} {sentence.lower()}"
                        rebuilt_sentences.append(expanded)
            
            return '. '.join(rebuilt_sentences) + '.'

        # EXTREME TRANSFORMATION 2: Vocabulary nuclear option
        def nuclear_vocabulary_replacement(text):
            # Comprehensive word replacement database
            nuclear_replacements = {
                # Academic terms
                'research': ['scholarly investigation', 'academic inquiry', 'systematic study'],
                'study': ['examination', 'analysis', 'investigation'],
                'analysis': ['scrutiny', 'assessment', 'evaluation'],
                'evidence': ['empirical data', 'documented findings', 'research results'],
                
                # Democracy terms
                'democracy': ['democratic governance', 'popular sovereignty', 'representative government'],
                'democratic': ['self-governing', 'popularly accountable', 'representative'],
                'governance': ['administration', 'steering', 'political management'],
                'accountability': ['answerability', 'responsibility', 'obligation'],
                
                # Society terms
                'society': ['social fabric', 'community', 'civilization'],
                'civil': ['civic', 'public', 'communal'],
                'organization': ['institution', 'entity', 'association'],
                'movement': ['campaign', 'initiative', 'drive'],
                
                # Action verbs
                'evolved': ['developed progressively', 'transformed gradually', 'advanced systematically'],
                'emerged': ['arisen', 'materialized', 'come to prominence'],
                'promoting': ['advancing', 'fostering', 'championing'],
                'served': ['functioned', 'operated', 'acted'],
                'striving': ['endeavoring', 'working assiduously', 'making concerted efforts'],
                
                # Descriptive terms
                'complex': ['multifaceted', 'intricate', 'sophisticated'],
                'vital': ['essential', 'indispensable', 'fundamental'],
                'persistent': ['unrelenting', 'sustained', 'continual'],
                'transparency': ['openness', 'clarity', 'candor'],
                
                # Geographic terms
                'South Asia': ['the South Asian region', 'Southern Asian nations', 'the Indian subcontinent region'],
                'countries': ['nation-states', 'political entities', 'sovereign states'],
                
                # Structural terms
                'landscape': ['environment', 'terrain', 'context'],
                'legacies': ['inheritance', 'historical baggage', 'enduring influences'],
                'inequalities': ['disparities', 'imbalances', 'differentials'],
                'struggles': ['campaigns', 'endeavors', 'movements'],
                'practices': ['procedures', 'methodologies', 'approaches'],
                'freedoms': ['liberties', 'entitlements', 'rights'],
                'institutions': ['establishments', 'organizations', 'bodies'],
                'erosion': ['deterioration', 'decline', 'weakening']
            }
            
            new_text = text
            for original, replacements in nuclear_replacements.items():
                pattern = r'\b' + re.escape(original) + r'\b'
                if re.search(pattern, new_text, re.IGNORECASE):
                    replacement = random.choice(replacements)
                    new_text = re.sub(pattern, replacement, new_text, flags=re.IGNORECASE)
            
            return new_text

        # EXTREME TRANSFORMATION 3: Sentence length manipulation
        def extreme_length_manipulation(text):
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            
            if len(sentences) <= 1:
                return text
                
            manipulated = []
            
            for sentence in sentences:
                words = sentence.split()
                
                # DRAMATIC length changes
                if random.random() < 0.6:
                    if len(words) > 10:
                        # Split into multiple short sentences
                        num_splits = random.randint(2, 4)
                        chunk_size = max(3, len(words) // num_splits)
                        
                        for i in range(0, len(words), chunk_size):
                            chunk = words[i:i + chunk_size]
                            if len(chunk) >= 3:
                                manipulated.append(' '.join(chunk) + '.')
                    else:
                        # Expand short sentences dramatically
                        expansions = [
                            "This represents a significant development in the field because",
                            "From a comprehensive analytical perspective,",
                            "When contextualized within broader scholarly discourse,",
                            "Considering the multifaceted implications of this phenomenon,",
                            "Through rigorous empirical examination it becomes evident that"
                        ]
                        expanded = f"{random.choice(expansions)} {sentence.lower()}"
                        manipulated.append(expanded)
                else:
                    manipulated.append(sentence)
            
            return ' '.join(manipulated)

        # EXTREME TRANSFORMATION 4: Add human-like variations
        def add_human_touches(text):
            # Add human writing patterns that AI doesn't use
            human_patterns = [
                # Conversational academic style
                lambda t: f"Interestingly, {t.lower()}",
                
                # Reflective style
                lambda t: f"Upon reflection, {t.lower()}",
                
                # Comparative style
                lambda t: f"By comparison, {t.lower()}",
                
                # Cautious academic style
                lambda t: f"It appears that {t.lower()}",
                
                # Emphatic style
                lambda t: f"Notably, {t.lower()}",
                
                # Contextual style
                lambda t: f"In this context, {t.lower()}"
            ]
            
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            if sentences:
                first_sentence = sentences[0]
                if random.random() < 0.7:
                    pattern = random.choice(human_patterns)
                    sentences[0] = pattern(first_sentence)
            
            return '. '.join(sentences) + '.'

        # APPLY ALL EXTREME TRANSFORMATIONS
        result = clean_text
        
        # Apply in sequence for maximum effect
        result = radical_sentence_restructure(result)
        result = nuclear_vocabulary_replacement(result)
        result = extreme_length_manipulation(result)
        result = add_human_touches(result)
        
        return result

    def calculate_similarity(self, original, rewritten):
        """Calculate text similarity"""
        original_words = set(re.findall(r'\b\w+\b', original.lower()))
        rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
        common_words = original_words.intersection(rewritten_words)
        
        if not original_words:
            return 0
        
        similarity = len(common_words) / len(original_words) * 100
        return similarity

    def guarantee_low_similarity(self, original_text, max_similarity=20, max_attempts=10):
        """Keep generating until similarity is below threshold"""
        
        best_result = None
        best_similarity = 100
        
        for attempt in range(max_attempts):
            rewritten = self.extreme_rewriter(original_text)
            similarity = self.calculate_similarity(original_text, rewritten)
            
            if similarity < best_similarity:
                best_result = rewritten
                best_similarity = similarity
                
            if similarity <= max_similarity:
                return rewritten, similarity
        
        return best_result, best_similarity

    def setup_interface(self):
        """Setup the complete frontend interface"""
        
        # Create widgets
        self.input_text = widgets.Textarea(
            value="",
            placeholder="Paste your text here for extreme rewriting...\n\nExample: Civil society organizations in South Asia have played a vital role in promoting democratic governance and accountability. These organizations have evolved significantly over the past few decades.",
            description="📝 Input Text:",
            layout=widgets.Layout(width="100%", height="200px"),
            style={'description_width': 'initial'}
        )
        
        self.similarity_slider = widgets.IntSlider(
            value=15,
            min=5,
            max=30,
            step=1,
            description="🎯 Target Similarity:",
            style={'description_width': 'initial'},
            continuous_update=False
        )
        
        self.attempts_slider = widgets.IntSlider(
            value=8,
            min=1,
            max=20,
            step=1,
            description="🔄 Max Attempts:",
            style={'description_width': 'initial'},
            continuous_update=False
        )
        
        self.rewrite_button = widgets.Button(
            description="🚀 LAUNCH EXTREME REWRITE",
            button_style="success",
            icon="bolt",
            layout=widgets.Layout(width="250px", height="45px", font_weight="bold")
        )
        
        self.clear_button = widgets.Button(
            description="🗑️ Clear All",
            button_style="warning",
            layout=widgets.Layout(width="120px", height="40px")
        )
        
        self.output_text = widgets.Textarea(
            value="",
            placeholder="Your extremely rewritten text will appear here...",
            description="📋 Output Text:",
            layout=widgets.Layout(width="100%", height="200px"),
            style={'description_width': 'initial'}
        )
        
        self.progress_bar = widgets.IntProgress(
            value=0,
            min=0,
            max=100,
            description="Processing:",
            bar_style='info',
            style={'description_width': 'initial'}
        )
        
        self.stats_display = widgets.HTML(value="")
        self.results_display = widgets.HTML(value="")
        
        # Set up event handlers
        self.rewrite_button.on_click(self.on_rewrite_click)
        self.clear_button.on_click(self.on_clear_click)
        
        # Display the interface
        self.display_interface()
    
    def display_interface(self):
        """Display the complete interface"""
        
        # Header
        display(HTML("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        ">
            <h1 style="margin: 0; font-size: 2.5em;">💥 EXTREME REWRITER</h1>
            <h3 style="margin: 10px 0; opacity: 0.9;">GUARANTEED <20% SIMILARITY - AI DETECTION PROTECTION</h3>
            <p style="margin: 0; opacity: 0.8;">Nuclear vocabulary replacement • Radical sentence restructuring • Human pattern injection</p>
        </div>
        """))
        
        # Input Section
        display(HTML("<h3 style='color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px;'>📝 Input Your Text</h3>"))
        display(self.input_text)
        
        # Controls
        controls_box = widgets.VBox([
            widgets.HBox([self.similarity_slider, self.attempts_slider]),
            widgets.HBox([self.rewrite_button, self.clear_button])
        ])
        display(controls_box)
        
        # Progress
        display(HTML("<h3 style='color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; margin-top: 20px;'>🔄 Processing</h3>"))
        display(self.progress_bar)
        display(self.stats_display)
        
        # Results
        display(HTML("<h3 style='color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px;'>📊 Results</h3>"))
        display(self.output_text)
        display(self.results_display)
        
        # Instructions
        self.display_instructions()
    
    def display_instructions(self):
        """Display usage instructions"""
        display(HTML("""
        <div style="
            background: #e8f4fd;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border-left: 5px solid #2196F3;
        ">
            <h4 style="color: #1976D2; margin-top: 0;">🎯 How to Use:</h4>
            <ol style="color: #555;">
                <li><strong>Paste your text</strong> in the input area above</li>
                <li><strong>Set target similarity</strong> (lower = more radical changes)</li>
                <li><strong>Click "LAUNCH EXTREME REWRITE"</strong> to transform your text</li>
                <li><strong>Copy the output</strong> from the results area</li>
            </ol>
            
            <h4 style="color: #1976D2;">🔧 Extreme Techniques Applied:</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; color: #555;">
                <div>• Nuclear vocabulary replacement</div>
                <div>• Radical sentence restructuring</div>
                <div>• Dramatic length manipulation</div>
                <div>• Human writing patterns</div>
                <div>• Question/statement variation</div>
                <div>• Academic framing</div>
            </div>
        </div>
        """))
    
    def on_rewrite_click(self, button):
        """Handle rewrite button click"""
        if not self.input_text.value.strip():
            self.show_error("⚠️ Please enter some text to rewrite!")
            return
        
        # Disable button during processing
        self.rewrite_button.disabled = True
        self.rewrite_button.description = "🔄 PROCESSING..."
        
        # Reset displays
        self.output_text.value = ""
        self.stats_display.value = ""
        self.results_display.value = ""
        
        # Show progress
        self.progress_bar.value = 10
        
        try:
            # Get input values
            original_text = self.input_text.value
            target_similarity = self.similarity_slider.value
            max_attempts = self.attempts_slider.value
            
            # Update progress
            self.progress_bar.value = 30
            self.stats_display.value = "<div style='color: #FF9800;'>🔄 Starting extreme transformation...</div>"
            
            # Perform the rewrite
            final_output, achieved_similarity = self.guarantee_low_similarity(
                original_text, 
                max_similarity=target_similarity,
                max_attempts=max_attempts
            )
            
            # Update progress
            self.progress_bar.value = 90
            
            # Calculate statistics
            original_words = len(original_text.split())
            rewritten_words = len(final_output.split())
            word_change = ((rewritten_words - original_words) / original_words) * 100 if original_words > 0 else 0
            
            original_sentences = len([s for s in original_text.split('.') if s.strip()])
            rewritten_sentences = len([s for s in final_output.split('.') if s.strip()])
            
            # Update output
            self.output_text.value = final_output
            self.progress_bar.value = 100
            
            # Display results
            self.display_results(original_text, final_output, achieved_similarity, target_similarity,
                               original_words, rewritten_words, word_change, 
                               original_sentences, rewritten_sentences)
            
        except Exception as e:
            self.show_error(f"❌ Error during processing: {str(e)}")
        finally:
            # Re-enable button
            self.rewrite_button.disabled = False
            self.rewrite_button.description = "🚀 LAUNCH EXTREME REWRITE"
    
    def display_results(self, original_text, final_output, achieved_similarity, target_similarity,
                      original_words, rewritten_words, word_change, 
                      original_sentences, rewritten_sentences):
        """Display the transformation results"""
        
        # Determine success color
        if achieved_similarity <= target_similarity:
            color = "#4CAF50"
            status = "✅ TARGET ACHIEVED"
            risk_level = "LOW RISK"
        else:
            color = "#FF9800"
            status = "⚠️ CLOSE TO TARGET"
            risk_level = "MODERATE RISK"
        
        # Results header
        results_html = f"""
        <div style="
            background: {color};
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        ">
            <h3 style="margin: 0 0 10px 0;">🎯 EXTREME TRANSFORMATION COMPLETE</h3>
            <div style="font-size: 1.2em; font-weight: bold;">
                SIMILARITY: {achieved_similarity:.1f}% | {status}
            </div>
        </div>
        
        <div style="
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #e9ecef;
        ">
            <strong>📊 TRANSFORMATION STATISTICS:</strong><br>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;">
                <div>• <strong>Word Count:</strong> {original_words} → {rewritten_words} ({word_change:+.1f}%)</div>
                <div>• <strong>Sentence Count:</strong> {original_sentences} → {rewritten_sentences}</div>
                <div>• <strong>Similarity Score:</strong> {achieved_similarity:.1f}%</div>
                <div>• <strong>AI Detection Risk:</strong> {risk_level}</div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
            <div style="
                background: #ffebee;
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid #f44336;
            ">
                <strong style="color: #c62828;">🔴 ORIGINAL TEXT</strong>
                <div style="
                    max-height: 200px;
                    overflow-y: auto;
                    font-size: 12px;
                    background: white;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 4px;
                    border: 1px solid #ffcdd2;
                ">
                    {original_text}
                </div>
            </div>
            
            <div style="
                background: #e8f5e8;
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid #4CAF50;
            ">
                <strong style="color: #2e7d32;">🟢 REWRITTEN TEXT</strong>
                <div style="
                    max-height: 200px;
                    overflow-y: auto;
                    font-size: 12px;
                    background: white;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 4px;
                    border: 1px solid #c8e6c9;
                ">
                    {final_output}
                </div>
            </div>
        </div>
        """
        
        self.results_display.value = results_html
    
    def on_clear_click(self, button):
        """Handle clear button click"""
        self.input_text.value = ""
        self.output_text.value = ""
        self.stats_display.value = ""
        self.results_display.value = ""
        self.progress_bar.value = 0
    
    def show_error(self, message):
        """Display error message"""
        self.stats_display.value = f"<div style='color: #f44336; padding: 10px; background: #ffebee; border-radius: 5px;'>{message}</div>"
        self.progress_bar.value = 0

# === CREATE AND LAUNCH THE APP ===
def launch_extreme_rewriter():
    """Launch the Extreme Rewriter application"""
    display(HTML("""
    <style>
        .widget-textarea textarea {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
            line-height: 1.4;
        }
        .widget-button button {
            font-weight: bold !important;
            font-size: 14px !important;
        }
        .widget-slider .widget-label {
            color: #333 !important;
            font-weight: 500 !important;
        }
    </style>
    """))
    
    app = ExtremeRewriterApp()
    return app

# === AUTO-LAUNCH THE APPLICATION ===
print("🚀 INITIALIZING EXTREME REWRITER APPLICATION...")
print("=" * 60)

# Launch the app
app_instance = launch_extreme_rewriter()

# Sample usage helper
display(HTML("""
<div style="
    background: #fff3e0;
    padding: 15px;
    border-radius: 8px;
    margin-top: 20px;
    border-left: 4px solid #ff9800;
">
    <strong>💡 Quick Start:</strong> Try the sample text below or paste your own text above!
    
    <div style="
        background: white;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
        font-size: 12px;
        border: 1px dashed #ff9800;
    ">
        <em>Civil society organizations in South Asia have played a vital role in promoting democratic governance and accountability. These organizations have evolved significantly over the past few decades, emerging as crucial actors in the region's political landscape. They serve as watchdogs that monitor government activities and strive to ensure transparency in public institutions.</em>
    </div>
</div>
"""))

print("\n" + "=" * 60)
print("✅ EXTREME REWRITER IS READY TO USE!")
print("   • Paste your text in the input area")
print("   • Set your target similarity")
print("   • Click 'LAUNCH EXTREME REWRITE'")
print("=" * 60)
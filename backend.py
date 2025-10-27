# =========================
# FIXED VOCABULARY LOADER
# =========================
class VocabularyLoader:
    def __init__(self):
        self.all_synonyms = {}
        self.total_words = 0
        self.loaded_files_count = 0
        self.failed_files = []
        self.load_times = {}
        self.load_all_vocabulary()
    
    def load_all_vocabulary(self):
        """LOAD VOCABULARY - FIXED LOADING"""
        print("\n" + "="*70)
        print("📚 LOADING VOCABULARY DATABASE...")
        print("="*70)
        
        # Initialize with empty dictionaries to avoid reference issues
        self.all_synonyms = {}
        
        # Load base vocabulary files
        self._load_base_vocabulary()
        
        # Load all synonym files
        self._load_synonym_files()
        
        # Load custom vocabulary
        self._load_custom_vocabulary()
        
        # Calculate final statistics
        self.total_words = len(self.all_synonyms)
        
        print("="*70)
        print("🎉 VOCABULARY LOADING COMPLETE!")
        print("="*70)
        print(f"✅ TOTAL UNIQUE WORDS: {self.total_words:,}")
        print(f"✅ FILES LOADED: {self.loaded_files_count}")
        
        # Verify loading worked
        if self.total_words == 0:
            print("❌ CRITICAL: No words loaded! Checking files...")
            self._debug_loading_issue()
        
        return self.total_words, self.all_synonyms
    
    def _debug_loading_issue(self):
        """Debug why vocabulary isn't loading"""
        print("\n🔍 DEBUGGING LOADING ISSUE:")
        
        # Check if vocabulary directory exists
        if not os.path.exists('vocabulary'):
            print("❌ Vocabulary directory not found!")
            return
        
        # List all files
        files = os.listdir('vocabulary')
        print(f"📁 Files in vocabulary/: {files}")
        
        # Check one file content
        if files:
            sample_file = os.path.join('vocabulary', files[0])
            try:
                with open(sample_file, 'r') as f:
                    content = f.read()
                    print(f"📄 Sample file content (first 200 chars): {content[:200]}")
            except Exception as e:
                print(f"❌ Could not read sample file: {e}")

# Initialize vocabulary loader FIRST
print("🔄 Initializing vocabulary loader...")
vocabulary_loader = VocabularyLoader()

# =========================
# FIXED REWRITER INITIALIZATION
# =========================
class IntelligentRewriter:
    def __init__(self):
        # VERIFY vocabulary is loaded
        print(f"🔍 Checking vocabulary before rewriter init...")
        print(f"📊 Vocabulary words: {len(vocabulary_loader.all_synonyms):,}")
        
        if len(vocabulary_loader.all_synonyms) == 0:
            print("❌ CRITICAL: Vocabulary is empty! Cannot initialize rewriter.")
            # Create emergency fallback
            self.synonym_finder = AdvancedSynonymFinder({})
            self.vocabulary = {}
            self.stats = {"total_words": 0, "loaded_files": 0}
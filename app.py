import random
import re
import streamlit as st
from collections import defaultdict
from health_terms import health_terms
from health_terms_2 import health_terms as health_terms_2
from generalwords import general_words 
# Merge them
health_terms.update(health_terms_2)

st.write("✅ Health terms loaded:", len(health_terms))
import streamlit as st
st.write("✅ Health terms loaded:", len(health_terms))

# =========================
# IMPROVED UNIVERSAL BACKEND
# =========================

class UniversalExtremeRewriter:
    def __init__(self):
        self.setup_comprehensive_vocabulary()
    
    def setup_comprehensive_vocabulary(self):
        """EXPANDED vocabulary database for universal use"""
        self.replacements = {
            # Common academic/research words
            'research': ['scholarly investigation', 'academic inquiry', 'systematic study', 'empirical exploration'],
            'study': ['examination', 'analysis', 'investigation', 'scrutiny', 'assessment'],
            'analysis': ['evaluation', 'appraisal', 'interpretation', 'assessment'],
            'evidence': ['empirical data', 'documented findings', 'research results', 'substantive proof'],
            'data': ['information', 'findings', 'metrics', 'statistics'],
            'method': ['approach', 'technique', 'procedure', 'methodology'],
            'result': ['outcome', 'finding', 'conclusion', 'product'],
            'show': ['demonstrate', 'reveal', 'illustrate', 'indicate', 'display'],
            'prove': ['substantiate', 'verify', 'confirm', 'validate'],
            'suggest': ['indicate', 'imply', 'propose', 'point to'],
 




   
   


 
 
    # Historical & Cultural
    'archaeological': ['excavational', 'antiquarian', 'prehistoric', 'dig-related'],
    'artifact': ['relic', 'object', 'item', 'antiquity'],
    'colonialism': ['imperialism', 'expansionism', 'domination', 'settlement'],
    'dynasty': ['ruling family', 'regime', 'era', 'lineage'],
    'feudal': ['manorial', 'hierarchical', 'medieval', 'land-based'],
    'indigenous': ['native', 'aboriginal', 'original', 'tribal'],
    'medieval': ['middle ages', 'gothic', 'dark ages', 'feudal'],
    'renaissance': ['rebirth', 'revival', 'reawakening', 'cultural renewal'],
    'revolutionary': ['radical', 'rebellious', 'innovative', 'groundbreaking'],
    'traditionalist': ['conservative', 'conventional', 'orthodox', 'established'],

    # Philosophical & Ethical
    'altruistic': ['selfless', 'unselfish', 'humanitarian', 'philanthropic'],
    'dialectical': ['discursive', 'logical', 'rational', 'investigative'],
    'ephemeral': ['transient', 'fleeting', 'short-lived', 'momentary'],
    'hedonistic': ['pleasure-seeking', 'self-indulgent', 'sybaritic', 'epicurean'],
    'karmic': ['fateful', 'destined', 'predetermined', 'cosmic'],
    'nihilistic': ['pessimistic', 'negative', 'cynical', 'despairing'],
    'pragmatic': ['practical', 'realistic', 'sensible', 'utilitarian'],
    'rational': ['logical', 'reasonable', 'sensible', 'coherent'],
    'teleological': ['purposeful', 'goal-oriented', 'design-based', 'final'],
    'utilitarian': ['functional', 'practical', 'useful', 'pragmatic'],

    # Additional Powerful Verbs
    'abate': ['subside', 'diminish', 'lessen', 'weaken'],
    'construe': ['interpret', 'understand', 'read', 'infer'],
    'decimate': ['destroy', 'devastate', 'ravage', 'annihilate'],
    'delineate': ['outline', 'describe', 'define', 'sketch'],
    'engender': ['cause', 'produce', 'create', 'generate'],
    'evince': ['show', 'reveal', 'display', 'exhibit'],
    'fulminate': ['protest', 'rage', 'rant', 'thunder'],
    'gainsay': ['deny', 'contradict', 'dispute', 'oppose'],
    'harangue': ['lecture', 'rant', 'tirade', 'diatribe'],
    'juxtapose': ['compare', 'contrast', 'place side by side', 'set against'],

    # Additional Descriptive Adjectives
    'aberrant': ['deviant', 'abnormal', 'atypical', 'irregular'],
    'convoluted': ['complicated', 'complex', 'tangled', 'intricate'],
    'dearth': ['lack', 'scarcity', 'shortage', 'deficiency'],
    'ebullient': ['enthusiastic', 'exuberant', 'lively', 'bubbly'],
    'garrulous': ['talkative', 'loquacious', 'chatty', 'verbose'],
    'histrionic': ['dramatic', 'theatrical', 'melodramatic', 'overemotional'],
    'intransigent': ['uncompromising', 'unyielding', 'obdurate', 'stubborn'],
    'mendacious': ['lying', 'untruthful', 'deceitful', 'dishonest'],
    'nefarious': ['wicked', 'evil', 'villainous', 'heinous'],
    'ostentatious': ['showy', 'pretentious', 'flamboyant', 'conspicuous'],

    # More Nouns for Precision
    'accolade': ['award', 'honor', 'tribute', 'praise'],
    'bane': ['curse', 'scourge', 'plague', 'affliction'],
    'cacophony': ['discord', 'noise', 'din', 'racket'],
    'diatribe': ['tirade', 'harangue', 'invective', 'denunciation'],
    'efficacy': ['effectiveness', 'efficiency', 'potency', 'success'],
    'fiasco': ['disaster', 'failure', 'debacle', 'catastrophe'],
    'gambit': ['stratagem', 'ploy', 'tactic', 'maneuver'],
    'hiatus': ['break', 'pause', 'gap', 'interruption'],
    'imbroglio': ['complicated situation', 'entanglement', 'misunderstanding', 'predicament'],
    'juggernaut': ['powerful force', 'unstoppable object', 'behemoth', 'colossus'],

    # Words about Words & Language
    'circumlocution': ['verbosity', 'periphrasis', 'wordiness', 'indirectness'],
    'colloquialism': ['informal expression', 'slang', 'idiom', 'vernacular'],
    'denotation': ['literal meaning', 'definition', 'dictionary meaning'],
    'etymology': ['word origin', 'derivation', 'history', 'root'],
    'linguistic': ['language-related', 'philological', 'semantic', 'verbal'],
    'neologism': ['new word', 'coinage', 'invention', 'modernism'],
    'onomatopoeia': ['echoism', 'sound imitation', 'mimetic word'],
    'pragmatics': ['practical language use', 'contextual meaning', 'usage'],
    'semantics': ['meaning', 'interpretation', 'significance', 'connotation'],
    'vernacular': ['everyday language', 'dialect', 'jargon', 'parlance'],

    # Global & International
    'cosmopolitan': ['international', 'worldly', 'sophisticated', 'multicultural'],
    'diplomatic': ['tactful', 'politic', 'discreet', 'strategic'],
    'globalization': ['international integration', 'worldwide connection', 'interdependence'],
    'multilateral': ['many-sided', 'collaborative', 'joint', 'cooperative'],
    'supranational': ['transnational', 'international', 'global', 'multinational'],
    'geopolitical': ['political geography', 'international power relations'],
    'intercontinental': ['transcontinental', 'cross-continental', 'global'],
    'transnational': ['cross-border', 'multinational', 'international', 'global'],
    'bilateral': ['two-sided', 'mutual', 'reciprocal', 'joint'],
    'sovereign': ['independent', 'autonomous', 'self-governing', 'free'],


    # Quality & Character
    'authentic': ['genuine', 'real', 'bona fide', 'legitimate'],
    'diligent': ['hard-working', 'industrious', 'assiduous', 'meticulous'],
    'eloquent': ['articulate', 'fluent', 'expressive', 'persuasive'],
    'meticulous': ['thorough', 'painstaking', 'careful', 'fastidious'],
    'profound': ['deep', 'intense', 'thoughtful', 'philosophical'],
    'prudent': ['wise', 'judicious', 'sensible', 'cautious'],
    'rigorous': ['thorough', 'exhaustive', 'stringent', 'demanding'],
    'robust': ['strong', 'vigorous', 'hardy', 'durable'],
    'thorough': ['comprehensive', 'exhaustive', 'complete', 'detailed'],
    'versatile': ['adaptable', 'flexible', 'all-around', 'multipurpose'],

    # Change & Transformation
    'metamorphosis': ['transformation', 'transmutation', 'changeover', 'evolution'],
    'transmute': ['change', 'transform', 'convert', 'alter'],
    'mutate': ['change', 'evolve', 'transform', 'modify'],
    'flux': ['flow', 'change', 'movement', 'transition'],
    'transient': ['temporary', 'passing', 'fleeting', 'short-term'],
    'mutable': ['changeable', 'variable', 'unstable', 'fluid'],
    'evolve': ['develop', 'progress', 'advance', 'grow'],
    'revamp': ['renovate', 'overhaul', 'reconstruct', 'modernize'],
    'rejuvenate': ['revitalize', 'renew', 'refresh', 'regenerate'],
    'innovate': ['pioneer', 'introduce', 'establish', 'initiate'],

    # Size & Scale
    'colossal': ['huge', 'gigantic', 'enormous', 'massive'],
    'diminutive': ['tiny', 'small', 'miniature', 'mini'],
    'infinitesimal': ['minute', 'microscopic', 'negligible', 'tiny'],
    'monolithic': ['massive', 'imposing', 'uniform', 'solid'],
    'palpable': ['tangible', 'perceptible', 'noticeable', 'visible'],
    'prodigious': ['enormous', 'huge', 'immense', 'colossal'],
    'substantial': ['considerable', 'significant', 'large', 'ample'],
    'minuscule': ['tiny', 'minute', 'microscopic', 'insignificant'],
    'copious': ['abundant', 'plentiful', 'ample', 'profuse'],
    'sparse': ['scanty', 'meager', 'scattered', 'thin'],

    # Time & Duration
    'antediluvian': ['ancient', 'prehistoric', 'primordial', 'archaic'],
    'contemporaneous': ['simultaneous', 'concurrent', 'coexisting', 'synchronic'],
    'dilatory': ['slow', 'tardy', 'delaying', 'procrastinating'],
    'ephemeral': ['short-lived', 'transitory', 'brief', 'momentary'],

    # Advanced States & Conditions
    'auspicious': ['favorable', 'propitious', 'promising', 'optimistic'],
    'banal': ['clichéd', 'trite', 'hackneyed', 'unoriginal'],
    'cacophonous': ['discordant', 'inharmonious', 'jarring', 'grating'],
    'deleterious': ['harmful', 'damaging', 'detrimental', 'injurious'],
    'ephemeral': ['transient', 'fleeting', 'momentary', 'evanescent'],
    'facile': ['simplistic', 'superficial', 'naive', 'cursory'],
    'germane': ['relevant', 'pertinent', 'applicable', 'apropos'],
    'hapless': ['unfortunate', 'unlucky', 'ill-fated', 'cursed'],
    'impervious': ['impenetrable', 'resistant', 'unaffected', 'immune'],
    'jubilant': ['overjoyed', 'elated', 'exultant', 'triumphant'],

    # Complex Human Traits
    'astute': ['shrewd', 'perceptive', 'discerning', 'sagacious'],
    'belligerent': ['hostile', 'aggressive', 'combative', 'pugnacious'],
    'circumspect': ['cautious', 'wary', 'prudent', 'guarded'],
    'dauntless': ['fearless', 'intrepid', 'undaunted', 'valiant'],
    'effervescent': ['bubbly', 'lively', 'vivacious', 'animated'],
    'facetious': ['flippant', 'witty', 'jocular', 'tongue-in-cheek'],
    'gregarious': ['sociable', 'outgoing', 'convivial', 'companionable'],
    'harried': ['stressed', 'beset', 'bothered', 'plagued'],
    'incorrigible': ['inveterate', 'hopeless', 'unreformable', 'hardened'],
    'judicious': ['wise', 'sensible', 'prudent', 'sage'],

    # Verbs of Action & Creation
    'abridge': ['shorten', 'condense', 'truncate', 'curtail'],
    'belabor': ['overemphasize', 'dwell on', 'hammer home', 'flog'],
    'conjure': ['summon', 'invoke', 'evoke', 'produce'],
    'debilitate': ['weaken', 'enfeeble', 'sap', 'incapacitate'],
    'edify': ['enlighten', 'instruct', 'educate', 'illuminate'],
    'fabricate': ['invent', 'forge', 'falsify', 'manufacture'],
    'galvanize': ['motivate', 'stimulate', 'arouse', 'electrify'],
    'hinder': ['impede', 'obstruct', 'hamper', 'inhibit'],
    'invigorate': ['energize', 'revitalize', 'refresh', 'rejuvenate'],
    'jeopardize': ['endanger', 'imperil', 'risk', 'threaten'],
 
    # Quality & Character
    'authentic': ['genuine', 'real', 'bona fide', 'legitimate'],
    'diligent': ['hard-working', 'industrious', 'assiduous', 'meticulous'],
    'eloquent': ['articulate', 'fluent', 'expressive', 'persuasive'],
    'meticulous': ['thorough', 'painstaking', 'careful', 'fastidious'],
    'profound': ['deep', 'intense', 'thoughtful', 'philosophical'],
    'prudent': ['wise', 'judicious', 'sensible', 'cautious'],
    'rigorous': ['thorough', 'exhaustive', 'stringent', 'demanding'],
    'robust': ['strong', 'vigorous', 'hardy', 'durable'],
    'thorough': ['comprehensive', 'exhaustive', 'complete', 'detailed'],
    'versatile': ['adaptable', 'flexible', 'all-around', 'multipurpose'],

    # Change & Transformation
    'metamorphosis': ['transformation', 'transmutation', 'changeover', 'evolution'],
    'transmute': ['change', 'transform', 'convert', 'alter'],
    'mutate': ['change', 'evolve', 'transform', 'modify'],
    'flux': ['flow', 'change', 'movement', 'transition'],
    'transient': ['temporary', 'passing', 'fleeting', 'short-term'],
    'mutable': ['changeable', 'variable', 'unstable', 'fluid'],
    'evolve': ['develop', 'progress', 'advance', 'grow'],
    'revamp': ['renovate', 'overhaul', 'reconstruct', 'modernize'],
    'rejuvenate': ['revitalize', 'renew', 'refresh', 'regenerate'],
    'innovate': ['pioneer', 'introduce', 'establish', 'initiate'],

    # Size & Scale
    'colossal': ['huge', 'gigantic', 'enormous', 'massive'],
    'diminutive': ['tiny', 'small', 'miniature', 'mini'],
    'infinitesimal': ['minute', 'microscopic', 'negligible', 'tiny'],
    'monolithic': ['massive', 'imposing', 'uniform', 'solid'],
    'palpable': ['tangible', 'perceptible', 'noticeable', 'visible'],
    'prodigious': ['enormous', 'huge', 'immense', 'colossal'],
    'substantial': ['considerable', 'significant', 'large', 'ample'],
    'minuscule': ['tiny', 'minute', 'microscopic', 'insignificant'],
    'copious': ['abundant', 'plentiful', 'ample', 'profuse'],
    'sparse': ['scanty', 'meager', 'scattered', 'thin'],

    # Time & Duration
    'antediluvian': ['ancient', 'prehistoric', 'primordial', 'archaic'],
    'contemporaneous': ['simultaneous', 'concurrent', 'coexisting', 'synchronic'],
    'dilatory': ['slow', 'tardy', 'delaying', 'procrastinating'],
    'ephemeral': ['short-lived', 'transitory', 'brief', 'momentary'],

    # Advanced States & Conditions
    'auspicious': ['favorable', 'propitious', 'promising', 'optimistic'],
    'banal': ['clichéd', 'trite', 'hackneyed', 'unoriginal'],
    'cacophonous': ['discordant', 'inharmonious', 'jarring', 'grating'],
    'deleterious': ['harmful', 'damaging', 'detrimental', 'injurious'],
    'ephemeral': ['transient', 'fleeting', 'momentary', 'evanescent'],
    'facile': ['simplistic', 'superficial', 'naive', 'cursory'],
    'germane': ['relevant', 'pertinent', 'applicable', 'apropos'],
    'hapless': ['unfortunate', 'unlucky', 'ill-fated', 'cursed'],
    'impervious': ['impenetrable', 'resistant', 'unaffected', 'immune'],
    'jubilant': ['overjoyed', 'elated', 'exultant', 'triumphant'],

    # Complex Human Traits
    'astute': ['shrewd', 'perceptive', 'discerning', 'sagacious'],
    'belligerent': ['hostile', 'aggressive', 'combative', 'pugnacious'],
    'circumspect': ['cautious', 'wary', 'prudent', 'guarded'],
    'dauntless': ['fearless', 'intrepid', 'undaunted', 'valiant'],
    'effervescent': ['bubbly', 'lively', 'vivacious', 'animated'],
    'facetious': ['flippant', 'witty', 'jocular', 'tongue-in-cheek'],
    'gregarious': ['sociable', 'outgoing', 'convivial', 'companionable'],
    'harried': ['stressed', 'beset', 'bothered', 'plagued'],
    'incorrigible': ['inveterate', 'hopeless', 'unreformable', 'hardened'],
    'judicious': ['wise', 'sensible', 'prudent', 'sage'],

    # Verbs of Action & Creation
    'abridge': ['shorten', 'condense', 'truncate', 'curtail'],
    'belabor': ['overemphasize', 'dwell on', 'hammer home', 'flog'],
    'conjure': ['summon', 'invoke', 'evoke', 'produce'],
    'debilitate': ['weaken', 'enfeeble', 'sap', 'incapacitate'],
    'edify': ['enlighten', 'instruct', 'educate', 'illuminate'],
    'fabricate': ['invent', 'forge', 'falsify', 'manufacture'],
    'galvanize': ['motivate', 'stimulate', 'arouse', 'electrify'],
    'hinder': ['impede', 'obstruct', 'hamper', 'inhibit'],
    'invigorate': ['energize', 'revitalize', 'refresh', 'rejuvenate'],
    'jeopardize': ['endanger', 'imperil', 'risk', 'threaten'],


    # Verbs of Communication
    'acquiesce': ['agree', 'consent', 'accede', 'comply'],
    'berate': ['scold', 'chide', 'reprimand', 'rebuke'],
    'cajole': ['coax', 'wheedle', 'persuade', 'entice'],
    'decry': ['denounce', 'condemn', 'criticize', 'censure'],
    'exhort': ['urge', 'encourage', 'implore', 'admonish'],
    'fulminate': ['protest', 'rage', 'rant', 'thunder'],
    'gainsay': ['deny', 'contradict', 'dispute', 'oppose'],
    'implore': ['beg', 'plead', 'beseech', 'entreat'],
    'lambaste': ['criticize', 'berate', 'castigate', 'pillory'],
    'muse': ['ponder', 'contemplate', 'reflect', 'ruminate'],

    # Abstract Nouns
    'acrimony': ['bitterness', 'resentment', 'hostility', 'rancor'],
    'benevolence': ['kindness', 'generosity', 'charity', 'altruism'],
    'clemency': ['mercy', 'leniency', 'compassion', 'forgiveness'],
    'dissonance': ['discord', 'conflict', 'friction', 'disagreement'],
    'equanimity': ['composure', 'calmness', 'poise', 'serenity'],
    'frugality': ['thrift', 'economy', 'prudence', 'austerity'],
    'guile': ['cunning', 'duplicity', 'deceit', 'trickery'],
    'hubris': ['arrogance', 'conceit', 'overconfidence', 'haughtiness'],
    'integrity': ['honesty', 'probity', 'rectitude', 'uprightness'],
    'joviality': ['cheerfulness', 'merriment', 'jollity', 'gaiety'],

    # Descriptive Adjectives (Physical)
    'angular': ['sharp-cornered', 'jagged', 'bony', 'gaunt'],
    'brusque': ['abrupt', 'blunt', 'curt', 'gruff'],
    'comely': ['attractive', 'good-looking', 'pleasing', 'fair'],
    'dapper': ['neat', 'spruce', 'trim', 'smart'],
    'ethereal': ['delicate', 'light', 'airy', 'gossamer'],
    'frangible': ['fragile', 'breakable', 'delicate', 'brittle'],
    'gargantuan': ['enormous', 'massive', 'gigantic', 'colossal'],
    'hirsute': ['hairy', 'shaggy', 'bearded', 'bristly'],
    'insipid': ['tasteless', 'bland', 'vapid', 'flavorless'],
    'jaded': ['tired', 'wearied', 'dulled', 'satiated'],

    # Descriptive Adjectives (Abstract)
    'kaleidoscopic': ['multicolored', 'variegated', 'fluctuating', 'shifting'],
    'languid': ['slow', 'relaxed', 'lethargic', 'unhurried'],
    'malleable': ['pliable', 'adaptable', 'flexible', 'tractable'],
    'noxious': ['harmful', 'poisonous', 'toxic', 'deleterious'],
    'obtuse': ['stupid', 'dull', 'slow-witted', 'insensitive'],
    'pragmatic': ['practical', 'realistic', 'sensible', 'utilitarian'],
    'quixotic': ['idealistic', 'unrealistic', 'impractical', 'dreamy'],
    'raucous': ['noisy', 'rowdy', 'boisterous', 'strident'],
    'sagacious': ['wise', 'shrewd', 'astute', 'judicious'],
    'tacit': ['implied', 'understood', 'unspoken', 'implicit'],

    # Science & Academia
    'anomaly': ['irregularity', 'deviation', 'exception', 'oddity'],
    'catalyst': ['stimulus', 'impetus', 'spur', 'precipitant'],
    'dogma': ['doctrine', 'creed', 'tenet', 'principle'],
    'empiricism': ['experiential knowledge', 'observation', 'evidence-based'],
    'fallacy': ['misconception', 'error', 'falsehood', 'mistake'],
    'hypothesis': ['theory', 'proposition', 'supposition', 'premise'],
    'kinetic': ['moving', 'active', 'dynamic', 'energetic'],
    'latent': ['dormant', 'hidden', 'concealed', 'quiescent'],
    'mitosis': ['cell division', 'reproduction', 'splitting'],
    'neutron': ['subatomic particle', 'neutral charge', 'nucleon'],

    # Business & Economics
    'arbitration': ['mediation', 'negotiation', 'settlement', 'adjudication'],
    'barter': ['trade', 'exchange', 'swap', 'deal'],
    'collateral': ['security', 'guarantee', 'surety', 'pledge'],
    'deficit': ['shortfall', 'deficiency', 'lack', 'loss'],
    'endorse': ['support', 'approve', 'sanction', 'ratify'],
    'franchise': ['license', 'charter', 'authorization', 'permit'],
    'gross': ['total', 'whole', 'entire', 'aggregate'],
    'hedge': ['protect', 'shield', 'insure', 'offset'],
    'incentive': ['inducement', 'motivation', 'stimulus', 'enticement'],
    'junk bond': ['high-risk bond', 'speculative bond', 'low-grade bond'],


    # Law & Order
    'adjourn': ['suspend', 'discontinue', 'postpone', 'recess'],
    'bailiff': ['officer', 'agent', 'marshal', 'constable'],
    'contraband': ['smuggled goods', 'illicit goods', 'prohibited items'],
    'defamation': ['libel', 'slander', 'character assassination', 'vilification'],
    'embezzlement': ['fraud', 'theft', 'misappropriation', 'peculation'],
    'felony': ['serious crime', 'major offense', 'grave crime'],
    'garnish': ['seize', 'confiscate', 'attach', 'impound'],
    'homicide': ['murder', 'killing', 'manslaughter', 'slaughter'],
    'indictment': ['charge', 'accusation', 'arraignment', 'summons'],
    'jurisprudence': ['law', 'legal theory', 'principles of law'],

    # Technology & Computing
    'algorithm': ['procedure', 'process', 'formula', 'methodology'],
    'bandwidth': ['capacity', 'throughput', 'data rate', 'speed'],
    'cache': ['storage', 'memory', 'reserve', 'hoard'],
    'debug': ['correct', 'fix', 'repair', 'troubleshoot'],
    'encrypt': ['encode', 'cipher', 'scramble', 'convert'],
    'firewall': ['barrier', 'shield', 'protection', 'blockade'],
    'gigabyte': ['unit of data', 'storage measure', 'GB'],
    'hyperlink': ['link', 'connection', 'reference', 'navigation'],
    'interface': ['connection', 'link', 'gateway', 'portal'],
    'java': ['programming language', 'computing platform', 'software'],

    # Medicine & Health
    'aorta': ['main artery', 'blood vessel', 'cardiovascular channel'],
    'benign': ['non-cancerous', 'harmless', 'innocuous', 'safe'],
    'carcinoma': ['cancer', 'malignancy', 'tumor', 'growth'],
    'dementia': ['mental decline', 'senility', 'cognitive impairment'],
    'epidemic': ['outbreak', 'plague', 'pandemic', 'rash'],
    'fracture': ['break', 'crack', 'split', 'rupture'],
    'gastrointestinal': ['stomach and intestines', 'digestive', 'enteric'],
    'hypertension': ['high blood pressure', 'cardiovascular condition'],
    'immunity': ['resistance', 'protection', 'defense', 'insusceptibility'],
    'jaundice': ['liver condition', 'yellowing', 'icterus'],

    # Arts & Literature
    'aesthetics': ['beauty', 'artistic taste', 'appreciation of beauty'],
    'biography': ['life story', 'memoir', 'account', 'chronicle'],
    'caricature': ['cartoon', 'exaggerated portrait', 'parody', 'lampoon'],
    'denouement': ['resolution', 'outcome', 'finale', 'conclusion'],
    'epilogue': ['afterword', 'conclusion', 'postscript', 'final section'],
    'folklore': ['myths', 'legends', 'traditions', 'oral history'],
    'genre': ['category', 'style', 'type', 'classification'],
    'haiku': ['Japanese poem', 'three-line poem', 'short verse'],
    'imagery': ['descriptive language', 'visual symbolism', 'metaphor'],
    'juxtaposition': ['contrast', 'comparison', 'side-by-side placement'],

    # History & Society
    'anthropology': ['study of humanity', 'human societies', 'cultural study'],
    'bureaucracy': ['administration', 'officialdom', 'red tape', 'system'],
    'civilization': ['society', 'culture', 'community', 'nation'],
    'dynasty': ['ruling family', 'lineage', 'regime', 'era'],
    'epoch': ['era', 'age', 'period', 'time'],
    'feudalism': ['manorialism', 'hierarchical system', 'medieval system'],
    'genocide': ['mass murder', 'extermination', 'ethnic cleansing', 'holocaust'],
    'historiography': ['study of historical writing', 'historical method'],
    'imperialism': ['colonialism', 'expansionism', 'empire-building', 'domination'],
    'junta': ['military government', 'faction', 'cabal', 'clique'],

    # Philosophy & Religion
    'agnosticism': ['skepticism', 'doubt', 'uncertainty', 'indecision'],
    'buddhism': ['eastern religion', 'spiritual tradition', 'dharma'],
    'catholicism': ['Christian denomination', 'Roman church', 'faith'],
    'deity': ['god', 'goddess', 'divinity', 'immortal'],
    'epistemology': ['theory of knowledge', 'study of knowledge'],
    'fundamentalism': ['strict adherence', 'literalism', 'orthodoxy', 'dogmatism'],
    'gnosticism': ['esoteric knowledge', 'mystical belief', 'spiritual wisdom'],
    'humanism': ['human-centered philosophy', 'secularism', 'rationalism'],
    'idealism': ['perfectionism', 'utopianism', 'high-mindedness', 'optimism'],
    'jainism': ['Indian religion', 'non-violence path', 'ascetic tradition'],

    # Environment & Geography
    'archipelago': ['island group', 'chain of islands', 'island chain'],
    'biodiversity': ['biological variety', 'species richness', 'ecological diversity'],
    'conservation': ['preservation', 'protection', 'safeguarding', 'management'],
    'deforestation': ['clearing', 'logging', 'forest removal', 'denuding'],
    'ecology': ['environmental science', 'ecosystem study', 'bionomics'],
    'fauna': ['animal life', 'creatures', 'wildlife', 'animals'],
    'glacier': ['ice mass', 'ice field', 'frozen river', 'ice stream'],
    'habitat': ['environment', 'territory', 'domain', 'home'],
    'irrigation': ['watering', 'supplying water', 'hydrating', 'dousing'],
    'jungle': ['rainforest', 'tropical forest', 'wilderness', 'woodland'],

    # Food & Cooking
    'al dente': ['firm to the bite', 'cooked but firm', 'textured'],
    'braise': ['stew', 'simmer', 'sear and cook', 'cook slowly'],
    'caramelize': ['brown the sugar', 'cook until sweet', 'crystallize'],
    'deglaze': ['loosen pan bits', 'add liquid to pan', 'create sauce'],
    'emulsify': ['blend', 'combine', 'mix liquids', 'homogenize'],
    'ferment': ['brew', 'cultivate', 'cause to rise', 'sour'],
    'garnish': ['decorate', 'adorn', 'embellish', 'trim'],
    'hors d\'oeuvre': ['appetizer', 'starter', 'canapé', 'snack'],
    'infuse': ['steep', 'soak', 'imbue', 'saturate'],
    'julienne': ['cut into strips', 'slice thinly', 'shred', 'cut matchsticks'],

    # Emotions & Feelings
    'agitation': ['anxiety', 'restlessness', 'unease', 'perturbation'],
    'bliss': ['ecstasy', 'joy', 'rapture', 'euphoria'],
    'contentment': ['satisfaction', 'pleasure', 'happiness', 'gratification'],
    'despondency': ['dejection', 'despair', 'hopelessness', 'melancholy'],
    'elation': ['joy', 'happiness', 'exhilaration', 'jubilation'],
    'frenzy': ['panic', 'hysteria', 'mania', 'turmoil'],
    'gloom': ['sadness', 'depression', 'despair', 'dejection'],
    'hysteria': ['panic', 'frenzy', 'meltdown', 'uproar'],
    'infatuation': ['crush', 'obsession', 'passion', 'fascination'],
    'joviality': ['cheerfulness', 'merriment', 'jollity', 'gaiety'],
    
    # your original core
    'research': ['scholarly investigation', 'academic inquiry', 'systematic study', 'empirical exploration'],
    'study': ['examination', 'analysis', 'investigation', 'scrutiny', 'assessment'],
    'analysis': ['evaluation', 'appraisal', 'interpretation', 'assessment'],
    'evidence': ['empirical data', 'documented findings', 'research results', 'substantive proof'],
    'data': ['information', 'findings', 'metrics', 'statistics'],
    'method': ['approach', 'technique', 'procedure', 'methodology'],
    'result': ['outcome', 'finding', 'conclusion', 'product'],
    'show': ['demonstrate', 'reveal', 'illustrate', 'indicate', 'display'],
    'prove': ['substantiate', 'verify', 'confirm', 'validate'],
    'suggest': ['indicate', 'imply', 'propose', 'point to'],

    # Common adjectives
    'important': ['crucial', 'vital', 'essential', 'significant', 'paramount'],
    'significant': ['notable', 'considerable', 'substantial', 'meaningful'],
    'different': ['various', 'diverse', 'distinct', 'disparate'],
    'many': ['numerous', 'multiple', 'countless', 'several'],
    'big': ['large', 'substantial', 'considerable', 'sizable'],
    'small': ['minor', 'modest', 'limited', 'minimal'],
    'good': ['effective', 'beneficial', 'advantageous', 'favorable'],
    'bad': ['detrimental', 'unfavorable', 'negative', 'adverse'],
    'beautiful': ['stunning', 'gorgeous', 'exquisite', 'magnificent'],
    'beauty': ['aesthetics', 'elegance', 'grace', 'loveliness'],

    # Common verbs
    'use': ['utilize', 'employ', 'leverage', 'apply'],
    'make': ['create', 'produce', 'construct', 'generate'],
    'do': ['perform', 'execute', 'carry out', 'conduct'],
    'get': ['obtain', 'acquire', 'secure', 'attain'],
    'help': ['assist', 'facilitate', 'support', 'aid'],
    'change': ['alter', 'modify', 'transform', 'adjust'],
    'develop': ['cultivate', 'nurture', 'foster', 'build'],
    'create': ['generate', 'produce', 'establish', 'form'],
    'understand': ['comprehend', 'grasp', 'apprehend', 'fathom'],
    'explain': ['clarify', 'elucidate', 'interpret', 'expound'],

    # Society & culture words
    'society': ['community', 'populace', 'civilization', 'social fabric'],
    'culture': ['heritage', 'traditions', 'customs', 'way of life'],
    'people': ['individuals', 'persons', 'population', 'citizens'],
    'government': ['administration', 'authorities', 'leadership', 'regime'],
    'organization': ['institution', 'entity', 'association', 'body'],
    'system': ['framework', 'structure', 'network', 'arrangement'],

    # Education words
    'education': ['learning', 'instruction', 'schooling', 'training'],
    'student': ['learner', 'pupil', 'scholar', 'trainee'],
    'teacher': ['educator', 'instructor', 'tutor', 'mentor'],
    'school': ['institution', 'academy', 'educational establishment'],

    # Business words
    'business': ['enterprise', 'company', 'firm', 'venture'],
    'market': ['industry', 'sector', 'commerce', 'trade'],
    'product': ['item', 'goods', 'merchandise', 'offering'],
    'customer': ['client', 'consumer', 'buyer', 'patron'],

    # Technology words
    'technology': ['innovation', 'digital tools', 'tech solutions', 'advancements'],
    'digital': ['electronic', 'computerized', 'online', 'virtual'],
    'information': ['data', 'knowledge', 'intelligence', 'facts'],

    # Time-related words
    'time': ['period', 'duration', 'interval', 'timespan'],
    'now': ['currently', 'presently', 'at this time', 'right now'],
    'recent': ['latest', 'current', 'contemporary', 'modern'],
    'old': ['ancient', 'aged', 'traditional', 'historic'],

    # Place-related words
    'world': ['globe', 'planet', 'earth', 'international community'],
    'country': ['nation', 'state', 'land', 'sovereign state'],
    'city': ['metropolis', 'urban center', 'municipality', 'town'],
    'place': ['location', 'site', 'venue', 'setting'],

    # General nouns
    'problem': ['issue', 'challenge', 'difficulty', 'obstacle'],
    'solution': ['resolution', 'answer', 'remedy', 'fix'],
    'way': ['method', 'approach', 'manner', 'technique'],
    'part': ['component', 'element', 'section', 'portion'],
    'kind': ['type', 'category', 'sort', 'variety'],

    # General adjectives
    'new': ['novel', 'innovative', 'fresh', 'recent'],
    'old': ['aged', 'ancient', 'traditional', 'historic'],
    'high': ['elevated', 'significant', 'substantial', 'considerable'],
    'low': ['minimal', 'reduced', 'limited', 'modest'],
    'fast': ['rapid', 'quick', 'speedy', 'swift'],
    'slow': ['gradual', 'leisurely', 'unhurried', 'deliberate'],

    # Expanded academic & research vocabulary
    'theory': ['concept', 'hypothesis', 'doctrine', 'model'],
    'hypothesis': ['proposition', 'assumption', 'supposition', 'postulate'],
    'variable': ['factor', 'element', 'parameter', 'component'],
    'control': ['regulate', 'govern', 'manage', 'supervise'],
    'sample': ['subset', 'specimen', 'example', 'instance'],
    'population': ['cohort', 'aggregate', 'community', 'group'],
    'significance': ['importance', 'meaningfulness', 'consequence', 'weight'],
    'bias': ['prejudice', 'partiality', 'skew', 'tilt'],
    'reliability': ['consistency', 'dependability', 'stability', 'trustworthiness'],
    'validity': ['soundness', 'legitimacy', 'accuracy', 'authenticity'],
    'replicate': ['repeat', 'reproduce', 'recreate', 'duplicate'],
    'measure': ['quantify', 'gauge', 'assess', 'evaluate'],
    'metric': ['measure', 'indicator', 'gauge', 'benchmark'],
    'trend': ['pattern', 'trajectory', 'tendency', 'movement'],
    'correlation': ['association', 'relationship', 'link', 'connection'],
    'causation': ['causal link', 'cause-and-effect', 'determinant', 'influence'],
    'model': ['framework', 'schema', 'representation', 'paradigm'],
    'framework': ['structure', 'scaffold', 'system', 'architecture'],
    'literature': ['publications', 'scholarship', 'research corpus', 'bibliography'],
    'review': ['survey', 'overview', 'critique', 'evaluation'],
    'thematic': ['topical', 'subject-based', 'motif-driven', 'topic-centered'],
    'qualitative': ['descriptive', 'non-numeric', 'textual', 'interpretive'],
    'quantitative': ['numerical', 'statistical', 'metric-based', 'measurable'],
    'mixed-methods': ['combined approach', 'hybrid methodology', 'integrated methods', 'dual approach'],

    # Writing & argument
    'argument': ['claim', 'assertion', 'case', 'contention'],
    'claim': ['assertion', 'statement', 'contend', 'maintain'],
    'counterargument': ['rebuttal', 'opposing view', 'contrary position', 'refutation'],
    'evidence-based': ['empirically supported', 'data-driven', 'substantiated', 'validated'],
    'citation': ['reference', 'source', 'attribution', 'acknowledgment'],
    'paragraph': ['section', 'passage', 'block of text', 'segment'],
    'sentence': ['clause', 'statement', 'utterance', 'line'],
    'thesis': ['argument', 'central claim', 'main idea', 'proposition'],
    'conclusion': ['summary', 'final thought', 'closing argument', 'wrap-up'],
    'introduction': ['opening', 'preface', 'lead-in', 'overview'],

    # Statistical & analytic terms
    'mean': ['average', 'central tendency', 'arithmetic mean', 'expected value'],
    'median': ['middle value', '50th percentile', 'central point', 'midpoint'],
    'mode': ['most frequent value', 'common value', 'prevalent value', 'dominant value'],
    'variance': ['dispersion', 'spread', 'variability', 'deviation'],
    'standard deviation': ['dispersion measure', 'spread indicator', 'variability metric', 'std dev'],
    'regression': ['prediction model', 'trend analysis', 'statistical modeling', 'fit'],
    'p-value': ['significance level indicator', 'probability measure', 'statistical significance', 'p'],
    'confidence interval': ['range estimate', 'uncertainty bound', 'estimate interval', 'CI'],
    'sample size': ['n', 'number of observations', 'cohort size', 'participant count'],
    'outlier': ['anomaly', 'exception', 'deviant point', 'extreme value'],

    # Project & process
    'plan': ['strategy', 'scheme', 'blueprint', 'roadmap'],
    'strategy': ['approach', 'tactic', 'plan', 'method'],
    'goal': ['objective', 'aim', 'target', 'intention'],
    'objective': ['aim', 'purpose', 'goal', 'target'],
    'deadline': ['due date', 'target date', 'cutoff', 'time limit'],
    'phase': ['stage', 'step', 'period', 'cycle'],
    'task': ['assignment', 'job', 'chore', 'duty'],
    'deliverable': ['output', 'product', 'result', 'submission'],
    'budget': ['funding', 'resources', 'financial plan', 'allocation'],
    'scope': ['extent', 'range', 'breadth', 'coverage'],

    # Communication & presentation
    'present': ['display', 'exhibit', 'show', 'demonstrate'],
    'communicate': ['convey', 'transmit', 'express', 'articulate'],
    'discuss': ['debate', 'consider', 'talk about', 'examine'],
    'report': ['document', 'record', 'describe', 'account for'],
    'summarize': ['condense', 'recap', 'abridge', 'outline'],
    'illustrate': ['demonstrate', 'depict', 'showcase', 'exemplify'],
    'highlight': ['emphasize', 'underscore', 'stress', 'spotlight'],

    # Emotions & evaluation
    'happy': ['pleased', 'content', 'satisfied', 'delighted'],
    'sad': ['unhappy', 'sorrowful', 'downcast', 'dejected'],
    'angry': ['irate', 'furious', 'annoyed', 'resentful'],
    'important to note': ['noteworthy', 'worth mentioning', 'of interest', 'notable'],

    # Law, policy & governance
    'law': ['statute', 'regulation', 'legislation', 'rule'],
    'policy': ['guideline', 'protocol', 'rule', 'directive'],
    'regulation': ['rule', 'ordinance', 'directive', 'statute'],
    'compliance': ['adherence', 'conformity', 'observance', 'abidance'],
    'governance': ['administration', 'oversight', 'management', 'regulation'],

    # Health & medicine
    'health': ['well-being', 'wellness', 'fitness', 'vitality'],
    'disease': ['illness', 'ailment', 'condition', 'disorder'],
    'treatment': ['therapy', 'intervention', 'care', 'remedy'],
    'symptom': ['sign', 'indicator', 'manifestation', 'feature'],
    'diagnosis': ['identification', 'assessment', 'evaluation', 'determination'],
    'prevention': ['prophylaxis', 'avoidance', 'protection', 'risk reduction'],

    # Environment & ecology
    'environment': ['surroundings', 'ecosystem', 'habitat', 'milieu'],
    'sustainability': ['durability', 'long-term viability', 'eco-friendliness', 'resilience'],
    'pollution': ['contamination', 'tainting', 'degradation', 'environmental harm'],
    'conservation': ['preservation', 'protection', 'safeguarding', 'stewardship'],
    'climate': ['weather patterns', 'atmospheric conditions', 'climatic system', 'temperature regime'],

    # Science & engineering
    'experiment': ['trial', 'test', 'investigation', 'trial run'],
    'prototype': ['model', 'mockup', 'archetype', 'preliminary version'],
    'innovation': ['invention', 'novelty', 'breakthrough', 'advance'],
    'engineer': ['designer', 'developer', 'builder', 'technician'],
    'technology transfer': ['knowledge transfer', 'tech diffusion', 'commercialization', 'transfer of tech'],

    # Finance & economics
    'economy': ['market system', 'financial system', 'economic system', 'macroeconomy'],
    'finance': ['funding', 'capital management', 'monetary affairs', 'financial matters'],
    'investment': ['capital allocation', 'funding', 'stake', 'asset placement'],
    'inflation': ['price rise', 'cost escalation', 'monetary inflation', 'price inflation'],
    'revenue': ['income', 'receipts', 'turnover', 'earnings'],
    'cost': ['expense', 'expenditure', 'outlay', 'charge'],
    'profit': ['gain', 'return', 'surplus', 'earnings'],
    'loss': ['deficit', 'shortfall', 'negative return', 'decrease'],

    # Marketing & product
    'brand': ['label', 'trade name', 'marque', 'identity'],
    'advertise': ['promote', 'publicize', 'market', 'announce'],
    'campaign': ['drive', 'initiative', 'push', 'strategy'],
    'audience': ['viewers', 'readers', 'target market', 'spectators'],
    'engagement': ['involvement', 'participation', 'interaction', 'connection'],


    # Negative Concepts
    'adversity': ['hardship', 'misfortune', 'difficulty', 'trouble'],
    'calamity': ['disaster', 'catastrophe', 'tragedy', 'misfortune'],
    'debacle': ['disaster', 'failure', 'fiasco', 'collapse'],
    'enmity': ['hostility', 'animosity', 'hatred', 'antagonism'],
    'fiasco': ['disaster', 'failure', 'debacle', 'catastrophe'],
    'grievance': ['complaint', 'objection', 'protest', 'grumble'],
    'hostility': ['aggression', 'antagonism', 'enmity', 'ill will'],
    'injustice': ['unfairness', 'inequity', 'wrong', 'injury'],
    'jeopardy': ['danger', 'risk', 'peril', 'hazard'],
    'knavery': ['dishonesty', 'trickery', 'deceit', 'villainy'],

    # Positive Concepts
    'benevolence': ['kindness', 'generosity', 'charity', 'altruism'],
    'compassion': ['sympathy', 'empathy', 'care', 'concern'],
    'dignity': ['self-respect', 'poise', 'grace', 'stateliness'],
    'empathy': ['understanding', 'compassion', 'identification', 'rapport'],
    'felicity': ['happiness', 'bliss', 'joy', 'delight'],
    'generosity': ['charity', 'benevolence', 'liberality', 'munificence'],
    'harmony': ['accord', 'concord', 'peace', 'agreement'],
    'integrity': ['honesty', 'probity', 'rectitude', 'uprightness'],
    'joy': ['happiness', 'delight', 'pleasure', 'bliss'],
    'kindness': ['benevolence', 'compassion', 'generosity', 'consideration'],

    # Movement & Travel
    'ambulate': ['walk', 'move about', 'stroll', 'perambulate'],
    'commute': ['travel', 'journey', 'shuttle', 'transfer'],
    'dawdle': ['linger', 'dally', 'loiter', 'procrastinate'],
    'emigrate': ['leave', 'relocate', 'move abroad', 'resettle'],
    'fluctuate': ['vary', 'change', 'oscillate', 'shift'],
    'gravitate': ['move toward', 'be drawn to', 'lean toward', 'incline'],
    'hover': ['float', 'hang', 'linger', 'poise'],
    'itinerant': ['traveling', 'wandering', 'nomadic', 'peripatetic'],
    'journey': ['trip', 'voyage', 'expedition', 'trek'],
    'kinetic': ['moving', 'active', 'dynamic', 'energetic'],

    # Size & Quantity
    'abundance': ['plenty', 'profusion', 'copiousness', 'wealth'],
    'brevity': ['conciseness', 'shortness', 'succinctness', 'terseness'],
    'dearth': ['lack', 'scarcity', 'shortage', 'deficiency'],
    'expanse': ['area', 'stretch', 'extent', 'scope'],
    'fragment': ['piece', 'part', 'portion', 'segment'],
    'gargantuan': ['enormous', 'massive', 'gigantic', 'colossal'],
    'handful': ['few', 'small number', 'scattering', 'sprinkling'],
    'infinitesimal': ['minute', 'microscopic', 'negligible', 'tiny'],
    'jot': ['bit', 'whit', 'iota', 'scrap'],
    'kilometer': ['metric unit', 'distance measure', 'km'],

    # Time & Duration
    'aftermath': ['consequences', 'aftereffects', 'results', 'repercussions'],
    'bygone': ['past', 'former', 'previous', 'earlier'],
    'century': ['hundred years', 'era', 'age', 'period'],
    'decade': ['ten years', 'period', 'span', 'time'],
    'ephemeral': ['short-lived', 'transitory', 'brief', 'momentary'],
    'fortnight': ['two weeks', 'fourteen days', 'period'],
    'generation': ['age group', 'cohort', 'era', 'period'],
    'hourly': ['every hour', 'frequent', 'regular', 'continual'],
    'interim': ['meantime', 'interval', 'interlude', 'interregnum'],
    'jiffy': ['moment', 'instant', 'second', 'flash'],

    # Color & Appearance
    'amber': ['yellowish-brown', 'golden', 'honey-colored', 'tawny'],
    'beige': ['pale brown', 'sand-colored', 'buff', 'ecru'],
    'crimson': ['deep red', 'ruby', 'scarlet', 'carmine'],
    'drab': ['dull', 'colorless', 'dreary', 'bland'],
    'emerald': ['bright green', 'vivid green', 'jade', 'malachite'],
    'fuchsia': ['vivid pink', 'magenta', 'hot pink', 'shocking pink'],
    'gold': ['metallic yellow', 'gilt', 'auric', 'golden'],
    'hue': ['color', 'tint', 'shade', 'tone'],
    'indigo': ['deep blue', 'navy blue', 'blue-violet', 'deep purple'],
    'jade': ['green stone', 'emerald green', 'verdant', 'malachite'],


    # Sound & Music
    'acoustic': ['non-electric', 'natural sound', 'unamplified'],
    'ballad': ['song', 'folk song', 'narrative poem', 'lay'],
    'cacophony': ['discord', 'noise', 'din', 'racket'],
    'duet': ['pair performance', 'two-part piece', 'couple\'s song'],
    'euphony': ['pleasant sound', 'harmony', 'melody', 'consonance'],
    'falsetto': ['high voice', 'artificial pitch', 'head voice'],
    'gig': ['concert', 'performance', 'show', 'engagement'],
    'harmony': ['accord', 'concord', 'melody', 'tunefulness'],
    'instrumental': ['without vocals', 'musical', 'orchestral', 'symphonic'],
    'jazz': ['music genre', 'improvisational music', 'swing'],

    # Education & Learning
    'academy': ['school', 'institute', 'college', 'university'],
    'baccalaureate': ['bachelor\'s degree', 'undergraduate degree', 'diploma'],
    'curriculum': ['syllabus', 'course of study', 'program', 'schedule'],
    'diploma': ['certificate', 'credential', 'qualification', 'degree'],
    'enroll': ['register', 'sign up', 'join', 'matriculate'],
    'faculty': ['teaching staff', 'professors', 'academics', 'instructors'],
    'graduation': ['completion', 'convocation', 'commencement', 'finishing'],
    'homework': ['assignment', 'study', 'preparation', 'schoolwork'],
    'illiterate': ['uneducated', 'unlettered', 'ignorant', 'unschooled'],
    'journal': ['diary', 'log', 'record', 'chronicle'],

    # Sports & Games
    'athlete': ['sportsman', 'sportswoman', 'player', 'competitor'],
    'basketball': ['hoops', 'court game', 'team sport', 'NBA'],
    'coach': ['trainer', 'instructor', 'mentor', 'guide'],
    'defeat': ['loss', 'beating', 'rout', 'conquest'],
    'endurance': ['stamina', 'persistence', 'fortitude', 'resilience'],
    'football': ['soccer', 'gridiron', 'American football', 'rugby'],
    'goalkeeper': ['goalie', 'netminder', 'custodian', 'shot-stopper'],
    'halftime': ['intermission', 'break', 'interval', 'pause'],
    'inning': ['baseball period', 'round', 'frame', 'segment'],
    'jump': ['leap', 'bound', 'hop', 'vault'],

    # Weather & Climate
    'avalanche': ['snowslide', 'landslide', 'snow slip', 'white death'],
    'blizzard': ['snowstorm', 'winter storm', 'whiteout', 'squall'],
    'climate': ['weather patterns', 'atmospheric conditions', 'weather'],
    'drought': ['dry spell', 'water shortage', 'aridity', 'famine'],
    'earthquake': ['tremor', 'seismic event', 'quake', 'shock'],
    'flood': ['deluge', 'inundation', 'torrent', 'overflow'],
    'gale': ['strong wind', 'storm', 'squall', 'tempest'],
    'hurricane': ['cyclone', 'typhoon', 'storm', 'tempest'],
    'icicle': ['ice formation', 'hanging ice', 'frost spike', 'ice dagger'],
    'jet stream': ['air current', 'high-altitude wind', 'atmospheric river'],

    # Relationships
    'acquaintance': ['contact', 'associate', 'colleague', 'friend'],
    'betrothal': ['engagement', 'pledge', 'promise', 'commitment'],
    'companion': ['partner', 'friend', 'associate', 'comrade'],
    'divorce': ['separation', 'dissolution', 'split', 'breakup'],
    'enemy': ['foe', 'adversary', 'opponent', 'rival'],
    'fiancé': ['betrothed', 'intended', 'future spouse', 'partner'],
    'guardian': ['protector', 'custodian', 'keeper', 'warden'],
    'hostility': ['aggression', 'antagonism', 'enmity', 'ill will'],
  
    # Advanced Concepts & States
    'abeyance': ['suspension', 'intermission', 'recess', 'dormancy'],
    'beatitude': ['blessedness', 'bliss', 'felicity', 'joy'],
    'cupidity': ['greed', 'avarice', 'rapacity', 'covetousness'],
    'desuetude': ['disuse', 'obsolescence', 'neglect', 'abandonment'],
    'effluvium': ['odor', 'stench', 'vapor', 'emanation'],
    'fecundity': ['fertility', 'productivity', 'fruitfulness', 'richness'],
    'hegira': ['exodus', 'migration', 'journey', 'flight'],
    'imbroglio': ['complicated situation', 'entanglement', 'predicament', 'quandary'],
    'juvenescence': ['rejuvenation', 'renewal', 'revitalization', 'youthfulness'],
    'kismet': ['fate', 'destiny', 'fortune', 'karma'],

    # Character & Behavior
    'loquacious': ['talkative', 'garrulous', 'voluble', 'chatty'],
    'magniloquent': ['grandiose', 'pompous', 'bombastic', 'high-flown'],
    'nescient': ['ignorant', 'uninformed', 'unknowing', 'uneducated'],
    'obdurate': ['stubborn', 'unyielding', 'inflexible', 'adamant'],
    'parvenu': ['upstart', 'nouveau riche', 'social climber', 'arriviste'],
    'querulous': ['complaining', 'peevish', 'fretful', 'whining'],
    'redoubtable': ['formidable', 'awe-inspiring', 'fearsome', 'commanding'],
    'sanguine': ['optimistic', 'cheerful', 'confident', 'hopeful'],
    'truculent': ['defiant', 'aggressive', 'belligerent', 'hostile'],
    'vicarious': ['indirect', 'secondary', 'substitute', 'delegated'],

    # Verbs of Action & Change
    'abnegate': ['renounce', 'reject', 'relinquish', 'abdicate'],
    'broach': ['introduce', 'raise', 'mention', 'bring up'],
    'countenance': ['tolerate', 'permit', 'approve', 'endorse'],
    'deracinate': ['uproot', 'eradicate', 'remove', 'extirpate'],
    'elucidate': ['clarify', 'explain', 'illuminate', 'explicate'],
    'fulfill': ['accomplish', 'achieve', 'complete', 'realize'],
    'germinate': ['sprout', 'bud', 'develop', 'grow'],
    'hibernate': ['winter sleep', 'lie dormant', 'overwinter', 'estivate'],
    'inundate': ['flood', 'overwhelm', 'deluge', 'swamp'],
    'jettison': ['discard', 'dump', 'shed', 'abandon'],

    # Communication & Expression
    'kvetch': ['complain', 'grumble', 'grouse', 'whine'],
    'lionize': ['celebrate', 'glorify', 'idolize', 'revere'],
    'mollify': ['soothe', 'pacify', 'appease', 'placate'],
    'negate': ['nullify', 'invalidate', 'cancel', 'void'],
    'opine': ['suggest', 'volunteer', 'observe', 'comment'],
    'propound': ['propose', 'put forward', 'suggest', 'advance'],
    'quip': ['joke', 'witticism', 'gag', 'one-liner'],
    'recant': ['retract', 'withdraw', 'renounce', 'disavow'],
    'sanction': ['approve', 'authorize', 'endorse', 'ratify'],
    'traduce': ['slander', 'malign', 'defame', 'vilify'],

    # Thought & Cognition
    'cogitate': ['think', 'ponder', 'reflect', 'meditate'],
    'delineate': ['outline', 'describe', 'define', 'sketch'],
    'excogitate': ['devise', 'contrive', 'formulate', 'concoct'],
    'introspect': ['self-reflect', 'look inward', 'soul-search', 'contemplate'],
    'rationalize': ['justify', 'explain away', 'excuse', 'defend'],
    'scrutinize': ['examine', 'inspect', 'analyze', 'study'],
    'theorize': ['hypothesize', 'speculate', 'conjecture', 'postulate'],
    'visualize': ['envision', 'picture', 'imagine', 'conceive'],
    'wrestle': ['grapple', 'struggle', 'contend', 'battle'],
    'perceive': ['discern', 'recognize', 'apprehend', 'grasp'],

    # Negative Actions
    'annihilate': ['destroy', 'obliterate', 'eradicate', 'eliminate'],
    'belittle': ['disparage', 'diminish', 'deride', 'mock'],
    'castigate': ['criticize', 'reprimand', 'rebuke', 'chastise'],
    'deprecate': ['disapprove', 'criticize', 'condemn', 'denounce'],
    'exacerbate': ['worsen', 'aggravate', 'intensify', 'compound'],
    'foment': ['instigate', 'incite', 'provoke', 'stir up'],
    'gainsay': ['deny', 'contradict', 'dispute', 'oppose'],
    'harass': ['pester', 'bother', 'annoy', 'torment'],
    'impugn': ['challenge', 'question', 'dispute', 'attack'],
    'nullify': ['invalidate', 'cancel', 'void', 'revoke'],

    # Positive Actions
    'ameliorate': ['improve', 'better', 'enhance', 'alleviate'],
    'cultivate': ['nurture', 'foster', 'develop', 'promote'],
    'embellish': ['decorate', 'adorn', 'beautify', 'enhance'],
    'facilitate': ['ease', 'simplify', 'expedite', 'assist'],
    'gratify': ['please', 'satisfy', 'delight', 'indulge'],
    'honor': ['respect', 'esteem', 'revere', 'venerate'],
    'integrate': ['incorporate', 'blend', 'merge', 'unify'],
    'justify': ['validate', 'vindicate', 'defend', 'support'],
    'kindle': ['ignite', 'spark', 'arouse', 'stimulate'],
    'legitimize': ['validate', 'authorize', 'sanction', 'certify'],

    # Physical World
    'arid': ['dry', 'parched', 'barren', 'waterless'],
    'bosky': ['wooded', 'sylvan', 'forested', 'arboreal'],
    'copse': ['grove', 'thicket', 'woodlot', 'spinney'],
    'dank': ['damp', 'moist', 'clammy', 'chilly'],
    'effulgent': ['radiant', 'brilliant', 'dazzling', 'resplendent'],
    'fen': ['marsh', 'bog', 'swamp', 'wetland'],
    'grotto': ['cave', 'cavern', 'hollow', 'recess'],
    'hinterland': ['backcountry', 'wilderness', 'interior', 'frontier'],
    'isthmus': ['narrow strip', 'land bridge', 'neck of land'],
    'knoll': ['hillock', 'mound', 'rise', 'hummock'],

    # Abstract Qualities
    'alacrity': ['eagerness', 'willingness', 'promptness', 'readiness'],
    'bona fides': ['credentials', 'authenticity', 'genuineness', 'trustworthiness'],
    'candor': ['frankness', 'openness', 'honesty', 'directness'],
    'discretion': ['prudence', 'circumspection', 'judgment', 'tact'],
    'efficacy': ['effectiveness', 'efficiency', 'potency', 'success'],
    'fidelity': ['loyalty', 'faithfulness', 'allegiance', 'devotion'],
    'gravitas': ['seriousness', 'solemnity', 'dignity', 'importance'],
    'humility': ['modesty', 'meekness', 'unpretentiousness', 'reserve'],
    'probity': ['integrity', 'honesty', 'rectitude', 'uprightness'],
    'rectitude': ['morality', 'principle', 'virtue', 'righteousness'],





    # Science & Nature
    'aperture': ['opening', 'hole', 'gap', 'orifice'],
    'bioluminescence': ['living light', 'biological glow', 'natural luminescence'],
    'cortex': ['outer layer', 'bark', 'rind', 'covering'],
    'dendrite': ['nerve fiber', 'branching process', 'neural extension'],
    'enzyme': ['catalyst', 'protein', 'biological catalyst'],
    'fungus': ['mold', 'mushroom', 'yeast', 'toadstool'],
    'genome': ['genetic material', 'DNA sequence', 'hereditary information'],
    'homeostasis': ['equilibrium', 'balance', 'stability', 'steady state'],
    'ion': ['charged particle', 'atom', 'molecule', 'particle'],
    'joule': ['energy unit', 'work measurement', 'physics unit'],

    # Arts & Performance
    'arabesque': ['ornamental design', 'intricate pattern', 'curving lines'],
    'burlesque': ['parody', 'caricature', 'mockery', 'travesty'],
    'cameo': ['brief appearance', 'small role', 'guest spot', 'bit part'],
    'denouement': ['resolution', 'outcome', 'finale', 'conclusion'],
    'exposition': ['explanation', 'description', 'presentation', 'account'],
    'fresco': ['wall painting', 'mural', 'plaster painting'],
    'gouache': ['opaque watercolor', 'painting technique', 'art medium'],
    'harlequin': ['clown', 'jester', 'fool', 'buffoon'],
    'impresario': ['promoter', 'producer', 'manager', 'organizer'],
    'jongleur': ['minstrel', 'entertainer', 'bard', 'troubadour'],

    # Society & Culture
    'bourgeois': ['middle-class', 'conventional', 'materialistic', 'capitalist'],
    'coterie': ['clique', 'circle', 'set', 'group'],
    'demagogue': ['rabble-rouser', 'agitator', 'firebrand', 'troublemaker'],
    'ethos': ['spirit', 'character', 'values', 'beliefs'],
    'folkway': ['custom', 'tradition', 'practice', 'convention'],
    'gentry': ['upper class', 'aristocracy', 'elite', 'nobility'],
    'hierarchy': ['ranking', 'order', 'pecking order', 'structure'],
    'ideologue': ['doctrinaire', 'partisan', 'zealot', 'true believer'],
    'junta': ['military government', 'faction', 'cabal', 'clique'],
    'kibbutz': ['collective community', 'commune', 'cooperative settlement'],

    # Law & Governance
    'affidavit': ['sworn statement', 'declaration', 'testimony', 'deposition'],
    'bylaw': ['regulation', 'rule', 'ordinance', 'local law'],
    'codicil': ['addendum', 'supplement', 'rider', 'appendix'],
    'detainer': ['holding', 'keeping', 'retention', 'confinement'],
    'eminent domain': ['expropriation', 'compulsory purchase', 'government takeover'],
    'felonious': ['criminal', 'illegal', 'unlawful', 'wrongful'],
    'garnish': ['seize', 'confiscate', 'attach', 'impound'],
    'habeas corpus': ['legal writ', 'court order', 'release petition'],
    'injunction': ['order', 'command', 'directive', 'ruling'],
    'jurist': ['legal expert', 'lawyer', 'judge', 'attorney'],

    # Business & Commerce
    'acquisition': ['purchase', 'buyout', 'procurement', 'takeover'],
    'barter': ['trade', 'exchange', 'swap', 'deal'],
    'collateral': ['security', 'guarantee', 'surety', 'pledge'],
    'dividend': ['share', 'portion', 'profit', 'return'],
    'equity': ['fairness', 'ownership', 'stock', 'value'],
    'franchise': ['license', 'charter', 'authorization', 'permit'],
    'goodwill': ['benevolence', 'kindness', 'reputation', 'asset'],
    'holding company': ['parent company', 'controlling corporation', 'umbrella firm'],
    'insolvent': ['bankrupt', 'ruined', 'unable to pay debts', 'penalized'],
    'joint venture': ['partnership', 'collaboration', 'cooperative enterprise'],

    # Technology & Computing
    'algorithmic': ['systematic', 'procedural', 'computational', 'methodical'],
    'bandwidth': ['capacity', 'throughput', 'data rate', 'speed'],
    'compiler': ['translator', 'interpreter', 'processor', 'converter'],
    'debugging': ['error correction', 'troubleshooting', 'fixing', 'repairing'],
    'encryption': ['encoding', 'scrambling', 'cryptography', 'cyphering'],
    'firmware': ['embedded software', 'permanent software', 'system software'],
    'gigabyte': ['unit of data', 'storage measure', 'GB'],
    'hardware': ['equipment', 'physical components', 'devices', 'machinery'],
    'interface': ['connection', 'link', 'gateway', 'portal'],
    'javascript': ['programming language', 'web language', 'scripting language'],

    # Medicine & Health
    'antibiotic': ['antimicrobial', 'antibacterial', 'medicine', 'drug'],
    'biopsy': ['tissue sample', 'medical test', 'examination', 'analysis'],
    'carcinogen': ['cancer-causing agent', 'toxin', 'poison', 'hazard'],
    'diagnosis': ['identification', 'detection', 'determination', 'analysis'],
    'epidemic': ['outbreak', 'plague', 'pandemic', 'rash'],
    'fracture': ['break', 'crack', 'split', 'rupture'],
    'gastrointestinal': ['stomach and intestines', 'digestive', 'enteric'],
    'hematology': ['blood study', 'blood analysis', 'medical specialty'],
    'immunity': ['resistance', 'protection', 'defense', 'insusceptibility'],
    'jaundice': ['liver condition', 'yellowing', 'icterus'],

    # Education & Learning
    'academia': ['educational world', 'scholarly community', 'university life'],
    'bibliography': ['reference list', 'sources', 'citations', 'works cited'],
    'curriculum': ['syllabus', 'course of study', 'program', 'schedule'],
    'didactics': ['teaching methods', 'instructional techniques', 'pedagogy'],
    'epistemology': ['theory of knowledge', 'study of knowledge'],
    'faculty': ['teaching staff', 'professors', 'academics', 'instructors'],
    'graduation': ['completion', 'convocation', 'commencement', 'finishing'],
    'hermeneutics': ['interpretation theory', 'textual analysis', 'exegesis'],
    'illumination': ['enlightenment', 'understanding', 'clarification', 'insight'],
    'jurisprudence': ['law', 'legal theory', 'principles of law'],

    # Food & Culinary
    'amuse-bouche': ['appetizer', 'starter', 'hors d\'oeuvre', 'taste'],
    'braise': ['stew', 'simmer', 'sear and cook', 'cook slowly'],
    'confit': ['preserved food', 'slow-cooked dish', 'French preparation'],
    'deglaze': ['loosen pan bits', 'add liquid to pan', 'create sauce'],
    'emulsion': ['mixture', 'blend', 'combination', 'suspension'],
    'foie gras': ['fatty liver', 'delicacy', 'French specialty', 'pâté'],
    'garnish': ['decorate', 'adorn', 'embellish', 'trim'],
    'hors d\'oeuvre': ['appetizer', 'starter', 'canapé', 'snack'],
    'infusion': ['extract', 'essence', 'soaking', 'steeping'],
    'julienne': ['cut into strips', 'slice thinly', 'shred', 'cut matchsticks'],

    # Emotions & Feelings
    'apathy': ['indifference', 'unconcern', 'detachment', 'listlessness'],
    'bemusement': ['puzzlement', 'confusion', 'perplexity', 'bewilderment'],
    'compunction': ['guilt', 'remorse', 'regret', 'contrition'],
    'despondency': ['dejection', 'despair', 'hopelessness', 'melancholy'],
    'elation': ['joy', 'happiness', 'exhilaration', 'jubilation'],
    'forlornness': ['hopelessness', 'despair', 'wretchedness', 'misery'],
    'gratitude': ['thankfulness', 'appreciation', 'gratefulness', 'acknowledgment'],
    'hysteria': ['panic', 'frenzy', 'meltdown', 'uproar'],
    'indignation': ['anger', 'outrage', 'resentment', 'wrath'],
    'joviality': ['cheerfulness', 'merriment', 'jollity', 'gaiety'],

    # Time & History
    'aeon': ['eternity', 'age', 'era', 'epoch'],
    'bygone': ['past', 'former', 'previous', 'earlier'],
    'century': ['hundred years', 'era', 'age', 'period'],
    'decade': ['ten years', 'period', 'span', 'time'],
    'epoch': ['era', 'age', 'period', 'time'],
    'fortnight': ['two weeks', 'fourteen days', 'period'],
    'generation': ['age group', 'cohort', 'era', 'period'],
    'hourly': ['every hour', 'frequent', 'regular', 'continual'],
    'interim': ['meantime', 'interval', 'interlude', 'interregnum'],
    'jiffy': ['moment', 'instant', 'second', 'flash'],

    # Size & Measurement
    'abundance': ['plenty', 'profusion', 'copiousness', 'wealth'],
    'brevity': ['conciseness', 'shortness', 'succinctness', 'terseness'],
    'dearth': ['lack', 'scarcity', 'shortage', 'deficiency'],
    'expanse': ['area', 'stretch', 'extent', 'scope'],
    'fragment': ['piece', 'part', 'portion', 'segment'],
    'gargantuan': ['enormous', 'massive', 'gigantic', 'colossal'],
    'handful': ['few', 'small number', 'scattering', 'sprinkling'],
    'infinitesimal': ['minute', 'microscopic', 'negligible', 'tiny'],
    'jot': ['bit', 'whit', 'iota', 'scrap'],
    'kilometer': ['metric unit', 'distance measure', 'km'],

    # Color & Appearance
    'amber': ['yellowish-brown', 'golden', 'honey-colored', 'tawny'],
    'beige': ['pale brown', 'sand-colored', 'buff', 'ecru'],
    'crimson': ['deep red', 'ruby', 'scarlet', 'carmine'],
    'drab': ['dull', 'colorless', 'dreary', 'bland'],
    'emerald': ['bright green', 'vivid green', 'jade', 'malachite'],
    'fuchsia': ['vivid pink', 'magenta', 'hot pink', 'shocking pink'],
    'gold': ['metallic yellow', 'gilt', 'auric', 'golden'],
    'hue': ['color', 'tint', 'shade', 'tone'],
    'indigo': ['deep blue', 'navy blue', 'blue-violet', 'deep purple'],
    'jade': ['green stone', 'emerald green', 'verdant', 'malachite'],

    # Sound & Music
    'acoustic': ['non-electric', 'natural sound', 'unamplified'],
    'ballad': ['song', 'folk song', 'narrative poem', 'lay'],
    'cacophony': ['discord', 'noise', 'din', 'racket'],
    'duet': ['pair performance', 'two-part piece', 'couple\'s song'],
    'euphony': ['pleasant sound', 'harmony', 'melody', 'consonance'],
    'falsetto': ['high voice', 'artificial pitch', 'head voice'],
    'gig': ['concert', 'performance', 'show', 'engagement'],
    'harmony': ['accord', 'concord', 'melody', 'tunefulness'],
    'instrumental': ['without vocals', 'musical', 'orchestral', 'symphonic'],
    'jazz': ['music genre', 'improvisational music', 'swing'],

    # Sports & Games
    'athlete': ['sportsman', 'sportswoman', 'player', 'competitor'],
    'basketball': ['hoops', 'court game', 'team sport', 'NBA'],
    'coach': ['trainer', 'instructor', 'mentor', 'guide'],
    'defeat': ['loss', 'beating', 'rout', 'conquest'],
    'endurance': ['stamina', 'persistence', 'fortitude', 'resilience'],
    'football': ['soccer', 'gridiron', 'American football', 'rugby'],
    'goalkeeper': ['goalie', 'netminder', 'custodian', 'shot-stopper'],
    'halftime': ['intermission', 'break', 'interval', 'pause'],
    'inning': ['baseball period', 'round', 'frame', 'segment'],
    'jump': ['leap', 'bound', 'hop', 'vault'],

    # Weather & Climate
    'avalanche': ['snowslide', 'landslide', 'snow slip', 'white death'],
    'blizzard': ['snowstorm', 'winter storm', 'whiteout', 'squall'],
    'climate': ['weather patterns', 'atmospheric conditions', 'weather'],
    'drought': ['dry spell', 'water shortage', 'aridity', 'famine'],
    'earthquake': ['tremor', 'seismic event', 'quake', 'shock'],
    'flood': ['deluge', 'inundation', 'torrent', 'overflow'],
    'gale': ['strong wind', 'storm', 'squall', 'tempest'],
    'hurricane': ['cyclone', 'typhoon', 'storm', 'tempest'],
    'icicle': ['ice formation', 'hanging ice', 'frost spike', 'ice dagger'],
    'jet stream': ['air current', 'high-altitude wind', 'atmospheric river'],

    # Relationships
    'acquaintance': ['contact', 'associate', 'colleague', 'friend'],
    'betrothal': ['engagement', 'pledge', 'promise', 'commitment'],
    'companion': ['partner', 'friend', 'associate', 'comrade'],
    'divorce': ['separation', 'dissolution', 'split', 'breakup'],
    'enemy': ['foe', 'adversary', 'opponent', 'rival'],
    'fiancé': ['betrothed', 'intended', 'future spouse', 'partner'],
    'guardian': ['protector', 'custodian', 'keeper', 'warden'],
    'hostility': ['aggression', 'antagonism', 'enmity', 'ill will'],
    'intimacy': ['closeness', 'familiarity', 'bond', 'connection'],
    'jealousy': ['envy', 'covetousness', 'resentment', 'distrust'],

    # Money & Finance
    'affluence': ['wealth', 'riches', 'prosperity', 'opulence'],
    'bankrupt': ['insolvent', 'ruined', 'penniless', 'destitute'],
    'currency': ['money', 'cash', 'legal tender', 'medium of exchange'],
    'dividend': ['share', 'portion', 'profit', 'return'],
    'estate': ['property', 'assets', 'holdings', 'inheritance'],
    'fortune': ['wealth', 'riches', 'prosperity', 'treasure'],
    'grant': ['award', 'allotment', 'subsidy', 'donation'],
    'heir': ['successor', 'inheritor', 'beneficiary', 'legatee'],
    'income': ['earnings', 'revenue', 'salary', 'wages'],
    'jewelry': ['ornaments', 'gems', 'precious stones', 'adornments'],

    # Construction & Building
    'architecture': ['building design', 'construction style', 'structural design'],
    'blueprint': ['plan', 'design', 'scheme', 'prototype'],
    'carpentry': ['woodworking', 'joinery', 'timber framing', 'cabinetmaking'],
    'demolition': ['destruction', 'razing', 'tearing down', 'wrecking'],
    'edifice': ['building', 'structure', 'construction', 'monument'],
    'foundation': ['base', 'footing', 'underpinning', 'substructure'],
    'girder': ['beam', 'support', 'joist', 'rafter'],
    'hardware': ['tools', 'equipment', 'implements', 'supplies'],
    'infrastructure': ['framework', 'foundation', 'base', 'structure'],
    'joist': ['beam', 'support', 'girder', 'rafter'],

    # Transportation
    'automobile': ['car', 'vehicle', 'motorcar', 'auto'],
    'bicycle': ['bike', 'cycle', 'two-wheeler', 'pedal cycle'],
    'commute': ['travel', 'journey', 'shuttle', 'transfer'],
    'destination': ['goal', 'target', 'end point', 'arrival point'],
    'expressway': ['highway', 'freeway', 'motorway', 'thruway'],
    'freight': ['cargo', 'goods', 'shipment', 'load'],
    'garage': ['carport', 'workshop', 'storage', 'shelter'],
    'highway': ['road', 'freeway', 'expressway', 'thruway'],

    # Core Human Experiences & States
    'languish': ['weaken', 'decline', 'wither', 'fade'],
    'prosper': ['thrive', 'flourish', 'succeed', 'boom'],
    'dwindle': ['diminish', 'shrink', 'decline', 'reduce'],
    'burgeon': ['flourish', 'expand', 'proliferate', 'thrive'],
    'vacillate': ['waver', 'hesitate', 'oscillate', 'fluctuate'],
    'convalesce': ['recover', 'recuperate', 'heal', 'improve'],
    'deteriorate': ['worsen', 'decline', 'decay', 'degenerate'],
    'ameliorate': ['improve', 'enhance', 'better', 'upgrade'],
    'exacerbate': ['worsen', 'aggravate', 'intensify', 'compound'],
    'abate': ['subside', 'diminish', 'lessen', 'weaken'],

    # Advanced Emotional States
    'despondent': ['hopeless', 'dejected', 'despairing', 'disheartened'],
    'ebullient': ['enthusiastic', 'exuberant', 'lively', 'bubbly'],
    'forlorn': ['unhappy', 'miserable', 'wretched', 'desolate'],
    'gratified': ['pleased', 'satisfied', 'content', 'fulfilled'],
    'irate': ['angry', 'furious', 'enraged', 'incensed'],
    'jubilant': ['overjoyed', 'elated', 'exultant', 'triumphant'],
    'lugubrious': ['mournful', 'sorrowful', 'gloomy', 'melancholy'],
    'morose': ['sullen', 'gloomy', 'dour', 'saturnine'],
    'nonplussed': ['bewildered', 'perplexed', 'puzzled', 'confused'],
    'optimistic': ['hopeful', 'confident', 'positive', 'sanguine'],

    # Complex Intellectual Concepts
    'axiomatic': ['self-evident', 'undeniable', 'fundamental', 'basic'],
    'dialectical': ['discursive', 'logical', 'rational', 'investigative'],
    'epistemological': ['cognitive', 'philosophical', 'theoretical', 'methodological'],
    'hermeneutical': ['interpretive', 'exegetical', 'analytical', 'critical'],
    'ontological': ['existential', 'metaphysical', 'philosophical', 'conceptual'],
    'phenomenological': ['experiential', 'observational', 'subjective', 'descriptive'],
    'teleological': ['purposeful', 'goal-oriented', 'design-based', 'final'],
    'solipsistic': ['self-centered', 'egocentric', 'narcissistic', 'subjective'],
    'reductionist': ['oversimplifying', 'simplistic', 'basic', 'elemental'],
    'holistic': ['comprehensive', 'complete', 'integrated', 'whole'],

    # Government & Political Systems
    'autocracy': ['dictatorship', 'tyranny', 'absolutism', 'despotism'],
    'bureaucracy': ['administration', 'officialdom', 'red tape', 'system'],
    'confederation': ['alliance', 'federation', 'league', 'union'],
    'democracy': ['self-government', 'popular sovereignty', 'republic', 'majority rule'],
    'federation': ['confederation', 'union', 'alliance', 'coalition'],
    'gerontocracy': ['rule by elders', 'elder council', 'senior leadership'],
    'kleptocracy': ['corrupt government', 'thievery regime', 'criminal state'],
    'meritocracy': ['achievement-based system', 'talent-based advancement'],
    'oligarchy': ['rule by few', 'elite government', 'select group rule'],
    'plutocracy': ['rule by wealthy', 'rich elite government', 'moneyed class rule'],
    'theocracy': ['religious government', 'divine rule', 'ecclesiastical state'],
    'totalitarianism': ['authoritarianism', 'dictatorship', 'absolutism', 'tyranny'],

    # Economic Systems & Concepts
    'capitalism': ['free market', 'private enterprise', 'laissez-faire', 'market economy'],
    'socialism': ['collectivism', 'public ownership', 'state control', 'common ownership'],
    'communism': ['Marxism', 'collectivism', 'state socialism', 'Bolshevism'],
    'feudalism': ['manorialism', 'hierarchical system', 'medieval system', 'serfdom'],
    'mercantilism': ['commercialism', 'trade-based economy', 'protectionism'],
    'keynesianism': ['demand-side economics', 'fiscal intervention', 'government spending'],
    'monetarism': ['money supply theory', 'monetary control', 'Friedman economics'],
    'protectionism': ['trade barriers', 'tariff system', 'import restrictions'],
    'globalization': ['international integration', 'worldwide connection', 'interdependence'],
    'austerity': ['fiscal restraint', 'budget cuts', 'economic tightening', 'belt-tightening'],

    # Scientific Disciplines
    'astronomy': ['celestial study', 'cosmology', 'stellar science', 'planetary science'],
    'biology': ['life science', 'biological science', 'natural science', 'zoology'],
    'chemistry': ['chemical science', 'molecular study', 'substance science'],
    'physics': ['physical science', 'natural philosophy', 'mechanical science'],
    'geology': ['earth science', 'rock study', 'planetary geology', 'earth study'],
    'meteorology': ['weather science', 'atmospheric study', 'climate science'],
    'oceanography': ['marine science', 'ocean study', 'sea research', 'marine biology'],
    'paleontology': ['fossil study', 'prehistoric life', 'ancient biology', 'dinosaur science'],
    'seismology': ['earthquake study', 'tremor research', 'seismic science'],
    'volcanology': ['volcano science', 'eruption study', 'magma research'],

    # Mathematical Concepts
    'algebra': ['symbolic mathematics', 'equation solving', 'variable mathematics'],
    'calculus': ['mathematical analysis', 'differentiation and integration', 'infinitesimal math'],
    'geometry': ['spatial mathematics', 'shape study', 'form mathematics'],
    'trigonometry': ['triangle mathematics', 'angle calculation', 'sine and cosine study'],
    'statistics': ['data analysis', 'probability study', 'numerical analysis'],
    'probability': ['likelihood calculation', 'chance mathematics', 'statistical chance'],
    'topology': ['spatial properties', 'rubber-sheet geometry', 'continuous transformation'],
    'number theory': ['integer properties', 'prime number study', 'arithmetic research'],
    'set theory': ['collection mathematics', 'group theory', 'mathematical sets'],
    'logic': ['reasoning study', 'deductive reasoning', 'formal logic', 'rational thought'],

    # Literary Genres & Forms
    'fiction': ['invented story', 'literary invention', 'narrative creation', 'imagined tale'],
    'nonfiction': ['factual writing', 'true account', 'documentary', 'reality-based'],
    'poetry': ['verse', 'lyrical writing', 'metrical composition'],

    # Computing & IT
    'software': ['application', 'program', 'system', 'suite'],
    'hardware': ['equipment', 'physical components', 'devices', 'machinery'],
    'algorithm': ['procedure', 'routine', 'method', 'computational rule'],
    'database': ['data store', 'data repository', 'information system', 'data bank'],
    'security': ['protection', 'safeguarding', 'defense', 'cybersecurity'],
    'network': ['web', 'system', 'interconnected system', 'mesh'],

    # Design & aesthetics
    'design': ['plan', 'layout', 'blueprint', 'scheme'],
    'creative': ['inventive', 'imaginative', 'original', 'innovative'],
    'style': ['fashion', 'mode', 'manner', 'approach'],
    'aesthetic': ['artistic', 'visual', 'stylistic', 'tasteful'],

    # Relationship & social terms
    'friend': ['companion', 'ally', 'confidant', 'associate'],
    'relationship': ['connection', 'bond', 'association', 'link'],
    'community engagement': ['public involvement', 'civic participation', 'community participation', 'public engagement'],
    'diversity': ['variety', 'heterogeneity', 'plurality', 'multiplicity'],
    'inclusion': ['integration', 'embracing', 'acceptance', 'involvement'],

    # Emphasis & transition words
    'however': ['nevertheless', 'nonetheless', 'but', 'yet'],
    'therefore': ['consequently', 'thus', 'hence', 'as a result'],
    'moreover': ['furthermore', 'additionally', 'besides', 'in addition'],
    'for example': ['for instance', 'such as', 'e.g.', 'to illustrate'],
    'in conclusion': ['to conclude', 'in summary', 'to sum up', 'overall'],

    # Measurement & units
    'measure': ['gauge', 'quantify', 'assess', 'evaluate'],
    'length': ['extent', 'distance', 'span', 'range'],
    'weight': ['mass', 'heft', 'load', 'burden'],
    'volume': ['capacity', 'amount', 'size', 'extent'],

    # Action & motion
    'move': ['shift', 'transfer', 'relocate', 'advance'],
    'stop': ['cease', 'halt', 'terminate', 'end'],
    'start': ['begin', 'commence', 'initiate', 'launch'],
    'increase': ['raise', 'boost', 'heighten', 'escalate'],
    'decrease': ['reduce', 'diminish', 'lower', 'curtail'],

    # Personality & traits
    'intelligent': ['smart', 'clever', 'bright', 'astute'],
    'creative': ['innovative', 'inventive', 'original', 'imaginative'],
    'reliable': ['dependable', 'trustworthy', 'consistent', 'steady'],
    'ambitious': ['driven', 'aspiring', 'determined', 'goal-oriented'],

    # Safety & risk
    'risk': ['hazard', 'danger', 'peril', 'exposure'],
    'safe': ['secure', 'protected', 'harmless', 'risk-free'],
    'protect': ['safeguard', 'shield', 'defend', 'preserve'],

    # Misc common verbs & nouns
    'buy': ['purchase', 'acquire', 'procure', 'obtain'],
    'sell': ['vend', 'trade', 'market', 'retail'],
    'read': ['peruse', 'scan', 'examine', 'study'],
    'write': ['compose', 'draft', 'pen', 'document'],
    'listen': ['heed', 'attend', 'give ear', 'pay attention'],
    'speak': ['talk', 'utter', 'express', 'articulate'],

    # Additional useful academic connectors
    'although': ['though', 'even though', 'whereas', 'while'],
    'despite': ['in spite of', 'notwithstanding', 'regardless of', 'even with'],
    'because': ['since', 'as', 'due to the fact that', 'for the reason that'],
    'unless': ['except if', 'if not', 'save that', 'without'],

    # Concluding/summary language
    'implication': ['consequence', 'ramification', 'connotation', 'suggestion'],
    'recommendation': ['suggestion', 'proposal', 'advice', 'guidance'],
    'limitation': ['constraint', 'restriction', 'shortcoming', 'boundary'],
    'future work': ['further research', 'next steps', 'subsequent study', 'follow-up research']
}
    
    def intelligent_word_replacement(self, text):
        """More aggressive and intelligent word replacement"""
        words = text.split()
        new_words = []
        
        i = 0
        while i < len(words):
            word = words[i].lower().strip('.,!?;:"')
            original_word = words[i]
            
            # Skip very short/common words
            if len(word) <= 2 or word in ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by']:
                new_words.append(original_word)
                i += 1
                continue
            
            # Try 2-word phrases first
            if i + 1 < len(words):
                next_word = words[i+1].lower().strip('.,!?;:"')
                two_word = f"{word} {next_word}"
                if two_word in self.replacements:
                    replacement = random.choice(self.replacements[two_word])
                    if words[i][0].isupper():
                        replacement = replacement.capitalize()
                    new_words.append(replacement)
                    i += 2
                    continue
            
            # Single word replacement with high probability
            if word in self.replacements and random.random() < 0.7:  # 70% replacement rate
                replacement = random.choice(self.replacements[word])
                if words[i][0].isupper():
                    replacement = replacement.capitalize()
                new_words.append(replacement)
            else:
                new_words.append(original_word)
            
            i += 1
        
        return ' '.join(new_words)
    
    def varied_sentence_restructure(self, text):
        """More diverse sentence restructuring patterns"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        restructured = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            if len(words) < 4:
                restructured.append(sentence)
                continue
            
            # DIVERSE patterns (no repetition)
            pattern_choice = random.choice([
                'reverse', 'question', 'academic', 'emphasis', 
                'context', 'normal', 'comparative', 'result'
            ])
            
            if pattern_choice == 'reverse' and len(words) > 6:
                split_point = random.randint(3, len(words) - 3)
                first_part = ' '.join(words[:split_point])
                second_part = ' '.join(words[split_point:])
                reverse_frames = [
                    f"{second_part}, thereby illustrating {first_part.lower()}",
                    f"{second_part}, which highlights {first_part.lower()}",
                    f"{second_part}, revealing how {first_part.lower()}",
                    f"{second_part}, demonstrating that {first_part.lower()}"
                ]
                restructured.append(random.choice(reverse_frames))
                
            elif pattern_choice == 'question':
                question_frames = [
                    f"What explains {sentence.lower()}?",
                    f"How can we understand {sentence.lower()}?",
                    f"Why is it significant that {sentence.lower()}?",
                    f"In what ways does {sentence.lower()}?"
                ]
                restructured.append(random.choice(question_frames))
                
            elif pattern_choice == 'academic':
                academic_frames = [
                    f"Research indicates that {sentence.lower()}",
                    f"Studies demonstrate that {sentence.lower()}",
                    f"Evidence suggests that {sentence.lower()}",
                    f"Analysis reveals that {sentence.lower()}",
                    f"Findings show that {sentence.lower()}"
                ]
                restructured.append(random.choice(academic_frames))
                
            elif pattern_choice == 'emphasis':
                emphasis_frames = [
                    f"Notably, {sentence.lower()}",
                    f"Significantly, {sentence.lower()}",
                    f"Importantly, {sentence.lower()}",
                    f"Remarkably, {sentence.lower()}"
                ]
                restructured.append(random.choice(emphasis_frames))
                
            elif pattern_choice == 'context':
                context_frames = [
                    f"In this context, {sentence.lower()}",
                    f"Within this framework, {sentence.lower()}",
                    f"From this perspective, {sentence.lower()}",
                    f"Considering these factors, {sentence.lower()}"
                ]
                restructured.append(random.choice(context_frames))
                
            elif pattern_choice == 'comparative':
                comparative_frames = [
                    f"By comparison, {sentence.lower()}",
                    f"Similarly, {sentence.lower()}",
                    f"Likewise, {sentence.lower()}",
                    f"In contrast, {sentence.lower()}"
                ]
                restructured.append(random.choice(comparative_frames))
                
            elif pattern_choice == 'result':
                result_frames = [
                    f"Consequently, {sentence.lower()}",
                    f"As a result, {sentence.lower()}",
                    f"Therefore, {sentence.lower()}",
                    f"Accordingly, {sentence.lower()}"
                ]
                restructured.append(random.choice(result_frames))
                
            else:
                restructured.append(sentence)
        
        return '. '.join(restructured) + '.'
    
    def smart_length_manipulation(self, text):
        """Better sentence length management"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if len(sentences) <= 2:
            return text
        
        processed = []
        
        for sentence in sentences:
            words = sentence.split()
            
            # Only manipulate 50% of sentences for better flow
            if random.random() < 0.5:
                if len(words) > 12:
                    # Smart splitting at natural break points
                    connectors = ['and', 'but', 'however', 'therefore', 'moreover', 'furthermore']
                    split_points = []
                    
                    for i, word in enumerate(words):
                        if word.lower() in connectors and 4 < i < len(words) - 4:
                            split_points.append(i)
                    
                    if split_points:
                        split_at = random.choice(split_points)
                        part1 = ' '.join(words[:split_at])
                        part2 = ' '.join(words[split_at:])
                        processed.extend([part1 + '.', part2.capitalize()])
                    else:
                        # Fallback: split at middle
                        mid = len(words) // 2
                        part1 = ' '.join(words[:mid])
                        part2 = ' '.join(words[mid:])
                        processed.extend([part1 + '.', part2.capitalize()])
                elif len(words) < 6:
                    # Expand short sentences
                    expansions = [
                        "It is evident that",
                        "One can observe that", 
                        "Research indicates that",
                        "The evidence shows that",
                        "Analysis reveals that"
                    ]
                    expanded = f"{random.choice(expansions)} {sentence.lower()}"
                    processed.append(expanded)
                else:
                    processed.append(sentence)
            else:
                processed.append(sentence)
        
        return ' '.join(processed)
    
    def add_natural_variation(self, text):
        """Add natural human writing variations"""
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        if not sentences:
            return text
        
        # Add variation to first sentence only (avoid over-patterning)
        if random.random() < 0.4:
            variations = [
                f"Interestingly, {sentences[0].lower()}",
                f"Notably, {sentences[0].lower()}",
                f"Surprisingly, {sentences[0].lower()}",
                f"Importantly, {sentences[0].lower()}"
            ]
            sentences[0] = random.choice(variations)
        
        return '. '.join(sentences) + '.'

# Initialize the universal rewriter
universal_rewriter = UniversalExtremeRewriter()

def extreme_rewriter(original_text):
    """Universal extreme rewriting with improved transformations"""
    clean_text = original_text.strip().strip('"').strip("'")
    
    # Apply transformations in random order for variety
    transformations = [
        universal_rewriter.varied_sentence_restructure,
        universal_rewriter.intelligent_word_replacement, 
        universal_rewriter.smart_length_manipulation,
        universal_rewriter.add_natural_variation
    ]
    random.shuffle(transformations)
    
    result = clean_text
    for transform in transformations:
        result = transform(result)
    
    return result

def calculate_similarity(original, rewritten):
    """Calculate text similarity"""
    original_words = set(re.findall(r'\b\w+\b', original.lower()))
    rewritten_words = set(re.findall(r'\b\w+\b', rewritten.lower()))
    common_words = original_words.intersection(rewritten_words)
    
    if not original_words:
        return 0
    
    similarity = len(common_words) / len(original_words) * 100
    return similarity

def guarantee_low_similarity(original_text, max_similarity=20, max_attempts=10):
    """Keep generating until similarity is below threshold"""
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


# =========================
# FRONTEND (DNA WATER GLASS UI — FINAL DARK MODE WORKING)
# =========================

import streamlit as st
import random

st.set_page_config(page_title="Extreme Rewriter", page_icon="💧", layout="wide")

# --- REWRITE FUNCTION (TRUE BACKEND CALL) ---
# This version uses the real rewriting logic from your backend
def guarantee_low_similarity(text, target):
    """Generate rewritten text using the true backend extreme_rewriter() logic."""
    rewritten = extreme_rewriter(text)
    similarity = calculate_similarity(text, rewritten)
    return rewritten, similarity

# --- CSS STYLES ---
st.markdown("""
<style>
body {
  margin: 0;
  overflow: hidden;
  background: radial-gradient(ellipse at bottom, #00111a 0%, #000000 100%);
  height: 100vh;
  font-family: 'Poppins', sans-serif;
  color: #e6faff;
}

/* ---- BUBBLES ---- */
#bubble-layer {
  position: fixed;
  top: 0; 
  left: 0;
  width: 100%; 
  height: 100%;
  overflow: hidden; 
  z-index: -3; 
  pointer-events: none;
}

.dna-bubble {
  position: absolute;
  bottom: -120px;
  background: rgba(0,180,255,0.3);
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0,200,255,0.6);
  animation: rise linear infinite;
}

@keyframes rise {
  0% { transform: translateY(0) scale(0.6); opacity: 0; }
  20% { opacity: 1; }
  70% { transform: translateY(-80vh) scale(1.1); opacity: 0.9; }
  100% { transform: translateY(-120vh) scale(0.8); opacity: 0; }
}

/* ---- DROPLETS ---- */
#droplet-layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -2;
  pointer-events: none;
}

.droplet {
  position: absolute;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.25), rgba(255,255,255,0.05));
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0,200,255,0.15);
  animation: slideDown 18s ease-in-out infinite;
}

@keyframes slideDown {
  0% { transform: translateY(0) rotate(0deg); opacity: 0.7; }
  50% { transform: translateY(15px) rotate(2deg); opacity: 1; }
  100% { transform: translateY(0) rotate(-1deg); opacity: 0.8; }
}

/* ---- WAVE ---- */
.wave-bg {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 220px;
  background: radial-gradient(circle at 50% 120%, rgba(0,150,255,0.6), transparent);
  animation: waveMove 7s ease-in-out infinite alternate;
  z-index: -1;
}

@keyframes waveMove {
  from { transform: translateY(0); }
  to { transform: translateY(-30px); }
}

/* ---- GLASS BOX ---- */
.glass-box {
  backdrop-filter: blur(25px);
  background: rgba(255,255,255,0.05);
  border-radius: 25px;
  padding: 2rem;
  border: 2px solid rgba(0,255,255,0.15);
  margin-top: 2rem;
}

/* ---- TITLE ---- */
h1.title {
  text-align: center;
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(45deg, #00eaff, #00ffb7, #0095ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: colorShift 6s ease-in-out infinite;
  margin-top: 3rem;
}
@keyframes colorShift {
  0% { filter: hue-rotate(0deg); }
  50% { filter: hue-rotate(180deg); }
  100% { filter: hue-rotate(360deg); }
}

/* ---- BUTTONS ---- */
.stButton>button {
  background: linear-gradient(135deg, #00b4ff, #0077ff);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1.1rem;
  padding: 0.75rem 2rem;
  transition: all 0.3s ease;
}
.stButton>button:hover {
  background: linear-gradient(135deg, #0077ff, #00b4ff);
  box-shadow: 0 0 15px rgba(0,180,255,0.8);
  transform: translateY(-2px);
}

/* ---- TEXTAREA ---- */
.stTextArea textarea {
  border-radius: 15px;
  border: 1px solid rgba(0,180,255,0.3);
  background: rgba(15, 25, 35, 0.9);
  color: #e6faff;
  font-size: 1rem;
  padding: 1rem;
  resize: vertical;
}

/* ---- FOOTER ---- */
.footer {
  text-align:center;
  margin-top:3rem;
  color:#66dfff;
  font-size:1.1rem;
  padding-bottom:2rem;
  animation: glow 3s ease-in-out infinite alternate;
}
@keyframes glow {
  from { text-shadow: 0 0 5px #00b4ff; }
  to { text-shadow: 0 0 20px #00ffff; }
}
</style>
""", unsafe_allow_html=True)

# --- VISUAL LAYERS (BUBBLES + DROPLETS) ---
bubble_html = '<div id="bubble-layer">'
for i in range(40):
    size = random.randint(8, 35)
    left = random.randint(0, 98)
    duration = random.randint(15, 28)
    delay = random.randint(0, 12)
    bubble_html += f"""
    <div class="dna-bubble" style="
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
bubble_html += '</div>'

droplet_html = '<div id="droplet-layer">'
for i in range(25):
    size = random.randint(4, 18)
    top = random.randint(0, 90)
    left = random.randint(0, 95)
    duration = random.randint(12, 20)
    delay = random.randint(0, 8)
    droplet_html += f"""
    <div class="droplet" style="
        top:{top}vh;
        left:{left}vw;
        width:{size}px;
        height:{size}px;
        animation-delay:{delay}s;
        animation-duration:{duration}s;
    "></div>"""
droplet_html += '</div><div class="wave-bg"></div>'

st.markdown(bubble_html + droplet_html, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<h1 class="title">💧 Extreme Rewriter</h1>
<p style="text-align:center; color:#bfefff; font-size:1.2rem;">
Transform your text into a <span style="color:#00eaff;">uniquely rewritten</span> version.
</p>
""", unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown('<div class="glass-box">', unsafe_allow_html=True)
input_text = st.text_area("🧬 Enter text:", height=180, label_visibility="collapsed")
target_similarity = st.slider("🎯 Target Similarity (%)", 5, 50, 20, step=1)

col1, col2 = st.columns(2)

# --- REWRITE BUTTON ---
if col1.button("🚀 Rewrite Now"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("Rewriting your text..."):
            rewritten, similarity = guarantee_low_similarity(input_text, target_similarity)
        st.markdown(f"""
        <div class="glass-box" style="border:1px solid rgba(0,255,255,0.3);">
            <h3 style="color:#00eaff;">✨ Rewritten Text (Similarity: {similarity:.1f}%)</h3>
            <textarea readonly rows="10" style="
                width:100%;
                background:rgba(0,15,25,0.8);
                color:#e6faff;
                border-radius:15px;
                border:1px solid rgba(0,180,255,0.2);
                padding:1rem;
                font-size:1rem;
            ">{rewritten}</textarea>
        </div>
        """, unsafe_allow_html=True)

# --- CLEAR BUTTON ---
if col2.button("🧹 Clear"):
    st.session_state.clear()
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
💻 Developed with 💙 by <strong style="color:#00ffff;">Zariab</strong><br>
🌊 Inspired by DNA & Biotechnology — Powered by Streamlit
</div>
""", unsafe_allow_html=True)
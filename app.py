import random
import re
import streamlit as st
from collections import defaultdict
from health_terms import health_terms
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
 # Computer Science & Artificial Intelligence
'algorithm': ['procedure', 'stepwise method', 'computational rule', 'logical sequence'],
'data structure': ['information framework', 'storage model', 'organizational scheme', 'data layout'],
'variable': ['storage element', 'changeable value', 'data holder', 'symbolic container'],
'constant': ['fixed value', 'unchanging number', 'stable quantity', 'static term'],
'function': ['routine', 'callable process', 'operation unit', 'computational task'],
'loop': ['repetition cycle', 'iteration block', 'process circle', 'cyclic execution'],
'condition': ['logical test', 'decision rule', 'constraint', 'branching factor'],
'recursion': ['self-calling method', 'looped function', 'nested computation', 'repetitive process'],
'array': ['ordered collection', 'indexed list', 'sequential storage', 'data series'],
'list': ['item sequence', 'ordered set', 'enumerated group', 'collection'],
'dictionary': ['key-value store', 'mapping structure', 'paired storage', 'associative array'],
'class': ['object blueprint', 'template', 'design model', 'definition unit'],
'object': ['instance', 'realized class', 'data entity', 'program component'],
'inheritance': ['class extension', 'property transfer', 'structure reuse', 'hierarchical sharing'],
'polymorphism': ['behavior variation', 'method flexibility', 'interface diversity', 'type adaptability'],
'encapsulation': ['data protection', 'information hiding', 'boundary wrapping', 'property shielding'],
'interface': ['interaction point', 'boundary definition', 'connection layer', 'protocol surface'],
'compiler': ['code translator', 'language converter', 'source interpreter', 'instruction builder'],
'interpreter': ['runtime reader', 'on-the-fly executor', 'language analyzer', 'immediate translator'],
'syntax': ['code grammar', 'program structure', 'language rule', 'expression format'],
'semantics': ['meaning interpretation', 'logical sense', 'program intent', 'definition context'],
'debugging': ['error fixing', 'fault tracing', 'bug correction', 'code repair'],
'exception handling': ['error management', 'failure response', 'crash prevention', 'fault control'],
'API': ['interface layer', 'service gateway', 'communication bridge', 'software endpoint'],
'framework': ['development skeleton', 'structural base', 'code foundation', 'app scaffolding'],
'library': ['code collection', 'function archive', 'software toolkit', 'module store'],
'module': ['code unit', 'functional part', 'component block', 'program piece'],
'package': ['bundle', 'distribution group', 'installation set', 'software collection'],
'dependency': ['linked module', 'external requirement', 'code reliance', 'support library'],
'compiler optimization': ['performance tuning', 'execution enhancement', 'instruction improvement', 'speed adjustment'],
'parallel computing': ['simultaneous processing', 'multi-core execution', 'concurrent computation', 'distributed operation'],
'concurrency': ['overlapping tasks', 'simultaneous operation', 'process interleaving', 'thread sharing'],
'thread': ['lightweight process', 'parallel strand', 'execution line', 'task path'],
'process': ['running program', 'execution instance', 'operating task', 'active computation'],
'memory allocation': ['storage assignment', 'RAM distribution', 'space reservation', 'data placement'],
'pointer': ['memory reference', 'address variable', 'location marker', 'data handle'],
'stack': ['LIFO structure', 'temporary memory', 'execution storage', 'function layer'],
'queue': ['FIFO structure', 'sequential waiting list', 'task line', 'data order'],
'cache': ['temporary storage', 'speed buffer', 'quick-access memory', 'performance saver'],
'database': ['data repository', 'information vault', 'storage system', 'record keeper'],
'relational database': ['table-based system', 'structured repository', 'linked data storage', 'SQL model'],
'SQL': ['structured query language', 'data command syntax', 'relational instruction set', 'database language'],
'NoSQL': ['non-relational store', 'document database', 'key-value system', 'schema-free model'],
'indexing': ['data mapping', 'lookup acceleration', 'search optimization', 'position referencing'],
'query': ['information request', 'data retrieval command', 'lookup question', 'search instruction'],
'transaction': ['atomic operation', 'database event', 'consistent update', 'data exchange unit'],
'normalization': ['data structuring', 'redundancy removal', 'organization improvement', 'schema refinement'],
'denormalization': ['performance restructuring', 'flattening', 'redundancy introduction', 'access optimization'],
'big data': ['massive information', 'large-scale dataset', 'extensive records', 'high-volume data'],
'data mining': ['pattern discovery', 'information extraction', 'knowledge retrieval', 'insight derivation'],
'data preprocessing': ['cleanup phase', 'formatting step', 'transformation stage', 'input refinement'],
'feature extraction': ['attribute selection', 'data simplification', 'pattern highlighting', 'information distillation'],
'machine learning': ['adaptive algorithm', 'pattern training', 'data learning', 'computational teaching'],
'supervised learning': ['guided training', 'labeled dataset learning', 'outcome-based adaptation', 'instructional modeling'],
'unsupervised learning': ['autonomous grouping', 'hidden pattern discovery', 'self-learning', 'clustering process'],
'reinforcement learning': ['trial-based training', 'feedback learning', 'reward optimization', 'adaptive strategy'],
'deep learning': ['neural modeling', 'layered computation', 'feature hierarchy learning', 'representation extraction'],
'neural network': ['brain-inspired system', 'node web', 'layered model', 'artificial neuron grid'],
'activation function': ['signal trigger', 'output converter', 'node response', 'transfer gate'],
'loss function': ['error measure', 'performance penalty', 'deviation calculator', 'training evaluator'],
'gradient descent': ['optimization path', 'error minimization method', 'stepwise adjustment', 'learning slope algorithm'],
'overfitting': ['training excess', 'model memorization', 'generalization loss', 'data dependency'],
'underfitting': ['insufficient learning', 'pattern ignorance', 'weak modeling', 'low adaptability'],
'regularization': ['complexity control', 'model constraint', 'stability technique', 'overfit prevention'],
'epoch': ['training round', 'iteration cycle', 'learning pass', 'update loop'],
'batch': ['data segment', 'mini set', 'training portion', 'subset input'],
'optimizer': ['training tuner', 'parameter adjuster', 'improvement agent', 'learning stabilizer'],
'feature scaling': ['value normalization', 'range adjustment', 'data equalization', 'input leveling'],
'model evaluation': ['performance testing', 'accuracy check', 'validation analysis', 'assessment phase'],
'confusion matrix': ['classification summary', 'prediction table', 'error mapping', 'result grid'],
'precision': ['exactness', 'accuracy degree', 'specific correctness', 'focused validity'],
'recall': ['retrieval accuracy', 'completeness', 'coverage rate', 'sensitivity'],
'F1 score': ['balanced measure', 'harmonic accuracy', 'combined metric', 'performance index'],
'cross-validation': ['data splitting test', 'model reliability check', 'training-validation cycle', 'evaluation loop'],
'transfer learning': ['knowledge reuse', 'model adaptation', 'experience sharing', 'cross-domain learning'],
'computer vision': ['visual computing', 'image analysis', 'scene understanding', 'optical recognition'],
'image processing': ['visual transformation', 'picture manipulation', 'graphic computation', 'pixel adjustment'],
'natural language processing': ['text understanding', 'language computation', 'linguistic modeling', 'semantic analysis'],
'speech recognition': ['voice identification', 'audio interpretation', 'spoken word processing', 'sound-to-text conversion'],
'text generation': ['content creation', 'word synthesis', 'language production', 'linguistic formation'],
'chatbot': ['conversational agent', 'dialogue assistant', 'talking program', 'virtual communicator'],
'recommendation system': ['suggestion engine', 'preference predictor', 'personalized proposer', 'choice generator'],
'anomaly detection': ['irregularity spotting', 'outlier identification', 'exception recognition', 'pattern deviation'],
'classification': ['category assignment', 'type detection', 'labeling', 'group determination'],
'clustering': ['unsupervised grouping', 'pattern segmentation', 'data bunching', 'similarity sorting'],
'prediction': ['forecasting', 'future estimation', 'trend inference', 'expected outcome modeling'],
'data visualization': ['graphical display', 'charting', 'insight illustration', 'information depiction'],
'computer graphics': ['image rendering', 'visual computation', 'digital drawing', 'scene creation'],
'simulation': ['virtual modeling', 'process imitation', 'behavior emulation', 'scenario reproduction'],
'robotics': ['machine control', 'automated mechanism', 'physical AI', 'mechanical intelligence'],
'automation': ['process streamlining', 'mechanical execution', 'efficiency enhancement', 'task simplification'],
'cybersecurity': ['digital protection', 'information defense', 'network security', 'data safeguarding'],
'cryptography': ['data encryption', 'code concealment', 'secure communication', 'ciphering'],
'blockchain': ['distributed ledger', 'decentralized record', 'transaction chain', 'immutable register'],
'cloud computing': ['remote processing', 'virtual infrastructure', 'online storage', 'network-based computation'],
'edge computing': ['local processing', 'decentralized computation', 'device-side operation', 'proximity computing'],
'internet of things': ['connected devices', 'sensor network', 'smart ecosystem', 'machine communication'],
'quantum computing': ['qubit processing', 'quantum information', 'superposition computation', 'entangled calculation'],
'augmented reality': ['enhanced view', 'mixed perception', 'digital overlay', 'interactive environment'],
'virtual reality': ['immersive simulation', 'digital environment', 'computer-generated space', '3D interaction'],
'artificial general intelligence': ['universal AI', 'human-level intelligence', 'broad cognition', 'adaptive system'],
'artificial consciousness': ['machine awareness', 'synthetic sentience', 'cognitive simulation', 'aware intelligence'],

# Mathematics
'number': ['quantity', 'digit', 'numerical value', 'counting symbol'],
'integer': ['whole number', 'non-fractional value', 'complete digit', 'undivided quantity'],
'fraction': ['partial number', 'ratio form', 'divided value', 'portion expression'],
'decimal': ['base-ten number', 'point notation', 'fractional representation', 'ten-based format'],
'ratio': ['comparison measure', 'proportional value', 'relative fraction', 'quantitative relation'],
'proportion': ['balanced ratio', 'equal relation', 'corresponding measure', 'harmonic comparison'],
'percentage': ['hundred-based ratio', 'fractional measure', 'relative share', 'normalized value'],
'average': ['mean value', 'central measure', 'typical number', 'balanced result'],
'median': ['middle value', 'central figure', 'midpoint', 'positional average'],
'mode': ['frequent value', 'common figure', 'repeated number', 'dominant element'],
'variable': ['unknown quantity', 'changeable symbol', 'adjustable term', 'placeholder'],
'constant': ['fixed number', 'steady value', 'unchanging term', 'definite quantity'],
'equation': ['mathematical statement', 'balanced expression', 'numeric equality', 'formula relation'],
'expression': ['numeric phrase', 'symbolic sentence', 'formula', 'calculation form'],
'function': ['input-output rule', 'mathematical mapping', 'relation process', 'computational linkage'],
'derivative': ['rate of change', 'slope measure', 'instant variation', 'differential output'],
'integral': ['area calculation', 'accumulation measure', 'summation curve', 'continuous addition'],
'limit': ['boundary value', 'approach point', 'threshold', 'convergence edge'],
'series': ['summation list', 'sequential addition', 'ordered sum', 'progression set'],
'sequence': ['ordered list', 'number chain', 'progressive set', 'systematic series'],
'vector': ['directional quantity', 'magnitude line', 'geometric arrow', 'spatial representation'],
'matrix': ['number grid', 'array structure', 'rectangular table', 'linear framework'],
'scalar': ['single magnitude', 'non-directional value', 'simple quantity', 'unit measure'],
'determinant': ['matrix value', 'scaling factor', 'linear measure', 'algebraic output'],
'eigenvalue': ['characteristic number', 'intrinsic factor', 'system constant', 'matrix property'],
'eigenvector': ['direction vector', 'characteristic line', 'invariant direction', 'system axis'],
'linear equation': ['first-degree formula', 'straight relation', 'simple equality', 'basic line rule'],
'polynomial': ['algebraic sum', 'power expression', 'multiple-term formula', 'variable combination'],
'quadratic': ['second-degree expression', 'parabolic form', 'square equation', 'curve formula'],
'root': ['solution value', 'zero point', 'base number', 'origin value'],
'factor': ['divisor', 'multiplicative component', 'part of product', 'shared quantity'],
'prime number': ['indivisible number', 'unique factor integer', 'atomic value', 'base quantity'],
'composite number': ['divisible integer', 'multi-factor value', 'non-prime number', 'compound quantity'],
'logarithm': ['inverse exponent', 'power measure', 'scale converter', 'growth indicator'],
'exponent': ['power value', 'raised term', 'multiplicative degree', 'growth factor'],
'square root': ['radical', 'base multiplier', 'rooted value', 'half exponent'],
'probability': ['chance', 'likelihood', 'possibility measure', 'event odds'],
'statistics': ['data analysis', 'numerical study', 'quantitative review', 'information summary'],
'variance': ['spread measure', 'dispersion index', 'deviation degree', 'data fluctuation'],
'standard deviation': ['dispersion measure', 'spread indicator', 'variation index', 'distance from mean'],
'distribution': ['data arrangement', 'value spread', 'frequency pattern', 'statistical layout'],
'normal distribution': ['bell curve', 'Gaussian form', 'symmetrical spread', 'average pattern'],
'skewness': ['asymmetry', 'tilt', 'distribution imbalance', 'data leaning'],
'kurtosis': ['peakness', 'flatness measure', 'tail weight', 'curve sharpness'],
'sample': ['subset', 'data portion', 'representative group', 'selection'],
'population': ['entire set', 'total data group', 'complete collection', 'universe of elements'],
'hypothesis': ['proposed idea', 'assumed statement', 'theoretical claim', 'testable guess'],
'p-value': ['probability measure', 'significance indicator', 'statistical likelihood', 'test result'],
'confidence interval': ['probability range', 'trust interval', 'certainty margin', 'estimated band'],
'regression': ['trend modeling', 'relationship estimation', 'predictive fitting', 'correlation mapping'],
'correlation': ['relationship strength', 'association degree', 'connection measure', 'statistical link'],
'covariance': ['joint variation', 'paired movement', 'mutual fluctuation', 'relation variance'],
'slope': ['incline', 'gradient', 'rate of rise', 'tilt measure'],
'intercept': ['cross point', 'base value', 'axis meeting point', 'starting offset'],
'optimization': ['best result finding', 'efficiency maximization', 'value improvement', 'goal adjustment'],
'constraint': ['restriction', 'limit', 'condition rule', 'boundary requirement'],
'objective function': ['goal formula', 'target expression', 'purpose equation', 'optimization rule'],
'linear programming': ['constraint solving', 'optimization technique', 'resource allocation method', 'value maximization process'],
'calculus': ['change study', 'rate analysis', 'continuous mathematics', 'differential integration field'],
'algebra': ['symbolic math', 'equation manipulation', 'variable study', 'abstract computation'],
'geometry': ['shape study', 'spatial math', 'form measurement', 'dimension analysis'],
'trigonometry': ['angle study', 'triangle mathematics', 'circular relation', 'ratio geometry'],
'arithmetic': ['basic calculation', 'number operation', 'elementary math', 'quantitative process'],
'combinatorics': ['arrangement counting', 'selection math', 'grouping analysis', 'discrete structure study'],
'set theory': ['collection study', 'group logic', 'element association', 'membership structure'],
'logic': ['reasoning system', 'truth structure', 'deductive rule', 'rational framework'],
'boolean algebra': ['binary logic', 'true-false system', 'digital reasoning', 'two-state structure'],
'graph theory': ['network study', 'connection analysis', 'link structure', 'node-edge system'],
'node': ['vertex', 'connection point', 'intersection', 'junction'],
'edge': ['link', 'connection line', 'bridge', 'relation path'],
'path': ['route', 'sequence of nodes', 'trail', 'connected chain'],
'cycle': ['closed path', 'repetition loop', 'circular route', 'recurring pattern'],
'probability distribution': ['chance layout', 'random pattern', 'event likelihood map', 'statistical form'],
'Bayesian inference': ['probability reasoning', 'belief update', 'statistical deduction', 'posterior estimation'],
'Markov chain': ['state sequence', 'probabilistic process', 'transition model', 'stochastic system'],
'stochastic process': ['random sequence', 'uncertain system', 'probabilistic chain', 'variable process'],
'differential equation': ['change formula', 'rate relationship', 'dynamic expression', 'mathematical model'],
'partial derivative': ['multi-variable rate', 'variable-specific change', 'component slope', 'differential term'],
'vector calculus': ['spatial rate study', 'field differentiation', 'multi-dimensional analysis', 'gradient computation'],
'linear algebra': ['matrix study', 'vector operations', 'system of equations', 'space transformation'],
'complex number': ['imaginary value', 'two-part number', 'real-imaginary pair', 'complex quantity'],
'imaginary number': ['square root of negative', 'non-real value', 'abstract unit', 'complex component'],
'modulus': ['absolute value', 'magnitude', 'positive measure', 'distance from zero'],
'function graph': ['curve plot', 'visual mapping', 'relation diagram', 'coordinate drawing'],
'inequality': ['unequal relation', 'non-equality statement', 'comparison rule', 'value difference'],
'approximation': ['close estimation', 'near value', 'rough calculation', 'proximate measure'],
'estimation': ['rough evaluation', 'approximate judgment', 'value inference', 'statistical guess'],
'discrete mathematics': ['finite math', 'countable structure study', 'non-continuous analysis', 'digital logic field'],
'numerical analysis': ['approximation computation', 'algorithmic math', 'precision calculation', 'error reduction study'],
'game theory': ['strategic analysis', 'decision mathematics', 'competitive modeling', 'interactive reasoning'],
'topology': ['space properties study', 'shape continuity', 'connectedness analysis', 'geometric abstraction'],
'measure theory': ['size analysis', 'mathematical measurement', 'integration base', 'quantitative structure'],
'chaos theory': ['dynamic unpredictability', 'complex systems study', 'nonlinear science', 'sensitive dependency'],
'fractal geometry': ['self-similar form', 'irregular pattern study', 'infinite structure', 'recursive shape'],
'cryptography mathematics': ['secure computation', 'number-based encryption', 'code theory', 'mathematical secrecy'],
'computational mathematics': ['algorithmic math', 'numeric modeling', 'digital problem solving', 'mathematical computing'],


# Chemistry
'reaction': ['chemical process', 'interaction', 'transformation', 'compound exchange'],
'compound formation': ['bonding', 'molecule creation', 'substance synthesis', 'atomic joining'],
'bond': ['linkage', 'connection', 'chemical tie', 'atomic adhesion'],
'ionic bond': ['charge link', 'electrostatic attraction', 'ion coupling', 'electron exchange bond'],
'covalent bond': ['shared electron link', 'atomic partnership', 'molecular bridge', 'electron-sharing tie'],
'metallic bond': ['electron cloud linkage', 'metal connection', 'atomic cohesion', 'conductive bonding'],
'atom': ['basic particle', 'elemental unit', 'building block', 'microscopic entity'],
'molecule': ['combined atoms', 'chemical unit', 'compound particle', 'bonded cluster'],
'element': ['fundamental substance', 'pure component', 'atomic type', 'basic material'],
'periodic table': ['element chart', 'atomic map', 'chemical arrangement', 'systematic classification'],
'oxidation': ['electron loss', 'energy withdrawal', 'chemical burning', 'oxygen reaction'],
'reduction': ['electron gain', 'energy absorption', 'deoxidation', 'chemical lowering'],
'redox reaction': ['electron transfer', 'oxidation-reduction process', 'charge exchange', 'energy swap'],
'catalysis': ['reaction acceleration', 'process speeding', 'facilitation', 'energy lowering'],
'catalyst': ['reaction helper', 'process accelerator', 'conversion agent', 'reaction facilitator'],
'activation energy': ['starting energy', 'reaction threshold', 'initial push', 'energetic spark'],
'reaction rate': ['speed of change', 'conversion pace', 'chemical velocity', 'kinetic intensity'],
'chemical equilibrium': ['reaction balance', 'steady state', 'equal conversion', 'constant condition'],
'concentration': ['density', 'amount per volume', 'mixture strength', 'solution richness'],
'solution': ['mixture', 'liquid blend', 'dissolved state', 'solvent combination'],
'solvent': ['dissolving agent', 'liquid medium', 'carrier fluid', 'chemical disperser'],
'solute': ['dissolved substance', 'minor component', 'mixing ingredient', 'chemical inclusion'],
'saturation': ['maximum dissolution', 'limit reached', 'solution capacity', 'full mixture state'],
'precipitation': ['solid formation', 'settling', 'crystal appearance', 'chemical fall-out'],
'filtration': ['separation', 'straining', 'removal process', 'particle extraction'],
'distillation': ['evaporation separation', 'boiling purification', 'vapor condensation', 'liquid refinement'],
'chromatography': ['chemical separation', 'component sorting', 'mixture analysis', 'flow separation'],
'titration': ['volume measurement', 'acid-base balancing', 'reaction quantification', 'solution testing'],
'pH': ['acidity scale', 'hydrogen measure', 'chemical balance', 'solution potential'],
'acid': ['proton donor', 'sour compound', 'hydrogen giver', 'low pH substance'],
'base': ['proton acceptor', 'alkaline compound', 'high pH substance', 'chemical neutralizer'],
'neutralization': ['acid-base reaction', 'balance formation', 'salt production', 'pH stabilization'],
'salt': ['ionic product', 'crystalline compound', 'neutralization outcome', 'ionic solid'],
'electrolysis': ['electric decomposition', 'charge-based splitting', 'ion separation', 'energy-induced reaction'],
'electrode': ['conductive terminal', 'charge contact', 'electrical surface', 'reaction point'],
'anode': ['positive terminal', 'oxidation site', 'electron release point', 'charge exit'],
'cathode': ['negative terminal', 'reduction site', 'electron gain point', 'charge entry'],
'electrolyte': ['conductive liquid', 'ion medium', 'charged solution', 'energy carrier'],
'valence': ['bonding capacity', 'electron number', 'chemical combining ability', 'link potential'],
'chemical kinetics': ['reaction rate study', 'speed analysis', 'temporal chemistry', 'process dynamics'],
'stoichiometry': ['quantitative chemistry', 'reaction proportion', 'formula calculation', 'substance ratio'],
'molar mass': ['atomic weight', 'mass per mole', 'compound weight', 'molecular measurement'],
'mole': ['substance unit', 'chemical quantity', 'Avogadro measure', 'reaction count base'],
'Avogadro’s number': ['molecular count', 'standard quantity', '6.022e23 constant', 'atomic index'],
'gas laws': ['pressure-volume rules', 'temperature relation', 'ideal gas principle', 'energy law'],
'Boyle’s law': ['pressure-volume inverse', 'compression principle', 'gas squeezing law', 'volume constraint'],
'Charles’s law': ['temperature-volume relation', 'thermal expansion rule', 'gas heating principle', 'volume growth law'],
'ideal gas law': ['universal gas equation', 'state relation', 'pressure-temperature rule', 'PV=nRT concept'],
'phase change': ['state transformation', 'form transition', 'matter shift', 'energy conversion'],
'melting': ['solid to liquid', 'fusion', 'heat absorption', 'softening process'],
'freezing': ['liquid to solid', 'solidification', 'cooling transformation', 'crystallization'],
'evaporation': ['liquid to gas', 'vaporization', 'boiling off', 'heat-driven transition'],
'condensation': ['gas to liquid', 'moisture collection', 'cooling compression', 'vapor return'],
'sublimation': ['solid to gas', 'direct vaporization', 'phase skipping', 'instant evaporation'],
'deposition': ['gas to solid', 'vapor solidification', 'reverse sublimation', 'particle settling'],
'crystallization': ['solid formation', 'patterned growth', 'molecular arrangement', 'order formation'],
'atomic structure': ['particle composition', 'electron arrangement', 'nuclear layout', 'matter design'],
'periodicity': ['repeating pattern', 'chemical rhythm', 'elemental recurrence', 'property sequence'],
'metal': ['conductive element', 'lustrous solid', 'malleable substance', 'shiny material'],
'nonmetal': ['nonconductive element', 'brittle substance', 'reactive type', 'insulating matter'],
'metalloid': ['intermediate element', 'semi-conductor type', 'hybrid substance', 'transitional material'],
'alloy': ['metal mixture', 'blended metal', 'combined element', 'fusion material'],
'corrosion': ['oxidative decay', 'material deterioration', 'rusting process', 'chemical damage'],
'combustion': ['burning', 'oxidative reaction', 'heat release', 'flame process'],
'thermal decomposition': ['heat breakdown', 'temperature-driven split', 'compound disintegration', 'energy separation'],
'polymerization': ['molecule joining', 'chain formation', 'monomer linking', 'synthetic buildup'],
'polymer': ['long molecule', 'repeated unit chain', 'synthetic compound', 'macrostructure'],
'organic chemistry': ['carbon compound study', 'hydrocarbon science', 'life-based chemistry', 'molecular structure analysis'],
'inorganic chemistry': ['non-carbon chemistry', 'mineral study', 'elemental science', 'metallic analysis'],
'biochemistry': ['life chemistry', 'biological reaction study', 'molecular biology', 'enzyme behavior'],
'chemical bonding': ['atomic connection', 'molecular tie', 'particle attachment', 'link formation'],
'chemical energy': ['bond energy', 'stored potential', 'reaction power', 'molecular dynamism'],
'enthalpy': ['heat content', 'energy measure', 'thermal sum', 'reaction capacity'],
'exothermic reaction': ['heat release', 'energy output', 'warming process', 'exergonic event'],
'endothermic reaction': ['heat absorption', 'energy intake', 'cooling process', 'endergonic reaction'],
'gas': ['air-like matter', 'free-flowing state', 'compressible fluid', 'light material'],
'liquid': ['flowing matter', 'fluid state', 'formless substance', 'non-rigid material'],
'solid': ['rigid matter', 'fixed structure', 'compact state', 'stable substance'],
'plasma': ['ionized state', 'charged gas', 'energetic medium', 'electrified matter'],
'chemical stability': ['reaction resistance', 'inertness', 'unchanging nature', 'durability'],
'chemical synthesis': ['creation process', 'molecule building', 'compound preparation', 'substance design'],
'purification': ['refinement', 'cleaning', 'separation', 'removal of impurities'],
'chemical degradation': ['breakdown', 'decay', 'molecular damage', 'reaction disintegration'],
'adsorption': ['surface capture', 'molecule attachment', 'particle adherence', 'layer accumulation'],
'absorption': ['uptake', 'internal soaking', 'energy intake', 'molecular inclusion'],
'colloid': ['fine mixture', 'dispersed system', 'suspension', 'micro-blend'],
'suspension': ['uneven mixture', 'particle dispersion', 'floating matter', 'non-homogeneous blend'],
'crystal lattice': ['ordered arrangement', 'solid pattern', 'geometric framework', 'atomic structure'],
'nanochemistry': ['nano-scale chemistry', 'atomic engineering', 'molecular miniaturization', 'small-scale synthesis'],
# Biology
'cell': ['microscopic unit', 'living component', 'biological structure', 'life module'],
'tissue': ['cell group', 'structural fabric', 'biological layer', 'organ component'],
'organ': ['functional body part', 'biological mechanism', 'internal structure', 'living apparatus'],
'organ system': ['body network', 'coordinated structure', 'physiological chain', 'functional ensemble'],
'organism': ['living being', 'life form', 'biological entity', 'animated structure'],
'genome': ['genetic code', 'DNA blueprint', 'hereditary library', 'molecular archive'],
'DNA': ['genetic material', 'hereditary molecule', 'nucleic sequence', 'double helix'],
'RNA': ['genetic messenger', 'nucleic acid', 'transcription molecule', 'protein builder'],
'gene': ['hereditary unit', 'genetic instruction', 'DNA segment', 'trait carrier'],
'chromosome': ['DNA bundle', 'gene cluster', 'genetic thread', 'hereditary strand'],
'mutation': ['genetic alteration', 'DNA change', 'hereditary variation', 'sequence modification'],
'adaptation': ['evolutionary adjustment', 'environmental fit', 'trait modification', 'biological accommodation'],
'natural selection': ['evolutionary filter', 'survival process', 'fitness sorting', 'adaptive preference'],
'evolution': ['biological progression', 'species change', 'genetic development', 'life transformation'],
'species': ['organism type', 'biological group', 'evolutionary class', 'genetic lineage'],
'population': ['species group', 'living community', 'organism cluster', 'ecological set'],
'ecosystem': ['biological system', 'natural network', 'environmental web', 'habitat interaction'],
'habitat': ['living environment', 'natural home', 'biological setting', 'organism residence'],
'biome': ['large ecosystem', 'climate-based region', 'ecological domain', 'natural zone'],
'biodiversity': ['life variety', 'species richness', 'genetic diversity', 'biological abundance'],
'photosynthesis': ['light-based synthesis', 'chlorophyll process', 'energy conversion', 'carbon fixation'],
'respiration': ['energy release', 'gas exchange', 'metabolic process', 'oxygen utilization'],
'metabolism': ['energy transformation', 'biochemical process', 'cellular activity', 'molecular conversion'],
'enzymes': ['biological catalysts', 'reaction agents', 'metabolic proteins', 'biochemical facilitators'],
'protein': ['amino acid compound', 'structural molecule', 'enzyme material', 'cell component'],
'lipid': ['fat molecule', 'energy store', 'hydrophobic compound', 'biological oil'],
'carbohydrate': ['sugar compound', 'energy source', 'organic molecule', 'polysaccharide structure'],
'nucleic acid': ['genetic polymer', 'DNA/RNA substance', 'biomolecular chain', 'information molecule'],
'cytoplasm': ['cell fluid', 'internal medium', 'living solution', 'intracellular environment'],
'membrane': ['boundary layer', 'protective film', 'cell barrier', 'semi-permeable cover'],
'nucleus': ['control center', 'genetic hub', 'cell brain', 'DNA chamber'],
'mitochondria': ['energy generator', 'cell powerhouse', 'metabolic organelle', 'ATP factory'],
'ribosome': ['protein factory', 'translation site', 'molecular builder', 'RNA complex'],
'endoplasmic reticulum': ['cell network', 'membrane labyrinth', 'protein pathway', 'lipid producer'],
'Golgi apparatus': ['packaging organelle', 'secretion center', 'molecule modifier', 'distribution hub'],
'lysosome': ['digestive vesicle', 'cell recycler', 'enzyme container', 'waste processor'],
'chloroplast': ['green organelle', 'photosynthesis site', 'chlorophyll holder', 'energy converter'],
'vacuole': ['storage sac', 'cell container', 'fluid chamber', 'material reservoir'],
'cell wall': ['rigid covering', 'protective barrier', 'support structure', 'outer layer'],
'cytoskeleton': ['internal framework', 'cell scaffold', 'support network', 'structural mesh'],
'osmosis': ['water diffusion', 'membrane flow', 'solute balance', 'hydric movement'],
'diffusion': ['molecule movement', 'spread', 'particle dispersion', 'concentration balancing'],
'homeostasis': ['internal balance', 'biological stability', 'steady condition', 'equilibrium state'],
'feedback loop': ['regulation cycle', 'control mechanism', 'response chain', 'adjustment system'],
'hormone': ['chemical messenger', 'signaling compound', 'regulatory molecule', 'endocrine agent'],
'endocrine system': ['hormone network', 'chemical communication', 'body regulator', 'gland system'],
'nervous system': ['signal network', 'neural web', 'communication circuit', 'reflex structure'],
'neuron': ['nerve cell', 'signal carrier', 'electrical unit', 'impulse conductor'],
'synapse': ['signal junction', 'neural bridge', 'communication gap', 'connection point'],
'neurotransmitter': ['chemical signal', 'brain messenger', 'synaptic compound', 'neural communicator'],
'brain': ['control organ', 'thought center', 'cognitive core', 'nervous hub'],
'spinal cord': ['nerve trunk', 'signal highway', 'central pathway', 'reflex channel'],
'digestive system': ['food network', 'nutrient breakdown chain', 'absorption path', 'metabolic route'],
'circulatory system': ['blood network', 'vascular system', 'transport system', 'heart circuit'],
'respiratory system': ['breathing apparatus', 'gas exchange structure', 'airway network', 'oxygen system'],
'excretory system': ['waste removal network', 'filtration system', 'cleansing organs', 'elimination pathway'],
'reproductive system': ['procreation structure', 'genetic continuation system', 'fertility organs', 'generation network'],
'skeletal system': ['support framework', 'bone structure', 'body scaffold', 'rigidity provider'],
'muscular system': ['movement network', 'tissue engine', 'force generator', 'mobility system'],
'integumentary system': ['skin covering', 'protective layer', 'external barrier', 'body shield'],
'immunity': ['defense ability', 'resistance system', 'disease shield', 'protective mechanism'],
'pathogen': ['disease agent', 'harmful organism', 'infectious unit', 'biological invader'],
'virus': ['microscopic parasite', 'infectious particle', 'genetic invader', 'replicative agent'],
'bacteria': ['unicellular organism', 'microbe', 'prokaryotic cell', 'tiny lifeform'],
'fungus': ['spore organism', 'decomposer', 'mycotic being', 'filamentous lifeform'],
'parasite': ['dependent organism', 'host feeder', 'biological invader', 'living exploiter'],
'host': ['support organism', 'nourishing body', 'biological provider', 'sustaining entity'],
'antibody': ['immune protein', 'disease fighter', 'defensive molecule', 'pathogen binder'],
'antigen': ['foreign marker', 'invader signal', 'immune target', 'recognition molecule'],
'vaccine': ['preventive agent', 'immunity inducer', 'disease deterrent', 'protective serum'],
'genetic engineering': ['DNA manipulation', 'gene editing', 'molecular alteration', 'biotech modification'],
'biotechnology': ['applied biology', 'life-based technology', 'biological innovation', 'genetic application'],
'cloning': ['replication process', 'genetic duplication', 'copy creation', 'organism reproduction'],
'stem cell': ['undifferentiated cell', 'growth starter', 'developmental base', 'regenerative unit'],
'embryo': ['developing organism', 'early stage life', 'growth seed', 'prenatal form'],
'fertilization': ['gamete union', 'zygote formation', 'cell merging', 'reproductive combination'],
'mitosis': ['cell division', 'growth duplication', 'chromosome separation', 'binary replication'],
'meiosis': ['reproductive division', 'chromosome halving', 'gamete formation', 'genetic reduction'],
'genetic inheritance': ['trait passing', 'heredity transfer', 'family pattern', 'DNA transmission'],
'dominant trait': ['expressed characteristic', 'visible gene', 'leading factor', 'inherited feature'],
'recessive trait': ['hidden characteristic', 'masked gene', 'silent inheritance', 'latent feature'],
'genetic variation': ['DNA diversity', 'hereditary difference', 'trait change', 'population divergence'],
'population genetics': ['group heredity study', 'allele distribution', 'evolutionary frequency', 'genetic trend'],
'evolutionary biology': ['species development study', 'adaptation science', 'genetic progression', 'life transformation field'],
'ecology': ['environmental biology', 'organism interaction study', 'ecosystem science', 'habitat relations'],
'ethology': ['animal behavior study', 'instinct analysis', 'conduct observation', 'behavioral biology'],
'microbiology': ['microorganism study', 'tiny life science', 'cellular biology', 'micro-scale life analysis'],
'zoology': ['animal science', 'creature biology', 'faunal study', 'living being analysis'],
'botany': ['plant biology', 'flora science', 'vegetation study', 'green life research'],
'genetics': ['heredity science', 'trait transmission study', 'gene analysis', 'biological inheritance field'],
'cytology': ['cell biology', 'microscopic anatomy', 'cell structure study', 'tissue analysis'],
'physiology': ['body function study', 'biological process analysis', 'organ behavior', 'functional biology'],
'anatomy': ['body structure study', 'biological design', 'organ arrangement', 'physical composition'],
'taxonomy': ['classification system', 'species categorization', 'biological sorting', 'organism labeling'],
'virology': ['virus study', 'infectious agent analysis', 'pathogen research', 'microscopic invader science'],
'immunology': ['immune system study', 'defense biology', 'protection science', 'resistance analysis'],


    # Overused AI introductory phrases
    'Certainly!': ['Of course', 'Absolutely', 'I\'d be happy to', 'Gladly', 'Yes'],
    'Here are': ['Below are', 'You\'ll find', 'I\'ve compiled', 'Consider these', 'Take a look at'],
    'Let me': ['I\'ll', 'Allow me to', 'I can', 'I\'d like to'],
    'I understand': ['I see', 'I appreciate', 'That makes sense', 'I get that'],
    'It sounds like': ['It seems', 'From what you describe', 'Based on this', 'Apparently'],
    
    # Overused transition phrases
    'It\'s important to note': ['Notably', 'Crucially', 'Significantly', 'Keep in mind'],
    'Additionally': ['Also', 'Furthermore', 'Moreover', 'Beyond that', 'What\'s more'],
    'However': ['But', 'Though', 'That said', 'On the other hand', 'Nevertheless'],
    'Therefore': ['So', 'Thus', 'Consequently', 'As a result', 'Hence'],
    'Furthermore': ['Moreover', 'Additionally', 'Also', 'Beyond this'],
    
    # Redundant qualifiers
    'very': ['extremely', 'exceptionally', 'remarkably', 'incredibly', ''],
    'really': ['genuinely', 'truly', 'quite', ''],
    'quite': ['rather', 'fairly', 'moderately', ''],
    'somewhat': ['moderately', 'relatively', 'comparatively', ''],
    
    # Vague academic phrases
    'leverage': ['use', 'utilize', 'employ', 'apply', 'take advantage of'],
    'utilize': ['use', 'employ', 'apply', 'work with', 'operate'],
    'facilitate': ['enable', 'help', 'assist', 'support', 'make possible'],
    'optimize': ['improve', 'enhance', 'refine', 'perfect', 'make better'],
    'enhance': ['improve', 'boost', 'strengthen', 'enrich', 'elevate'],
    
    # Corporate jargon
    'synergy': ['collaboration', 'teamwork', 'cooperation', 'combined effort'],
    'streamline': ['simplify', 'efficientize', 'smooth out', 'organize'],
    'paradigm': ['model', 'pattern', 'framework', 'approach', 'system'],
    'robust': ['strong', 'reliable', 'durable', 'resilient', 'solid'],
    'scalable': ['expandable', 'growable', 'adaptable', 'flexible'],
    
    # Overused descriptive words
    'comprehensive': ['thorough', 'complete', 'extensive', 'detailed', 'all-inclusive'],
    'dynamic': ['changing', 'active', 'energetic', 'fluid', 'evolving'],
    'seamless': ['smooth', 'uninterrupted', 'fluid', 'effortless', 'perfect'],
    'tailored': ['customized', 'personalized', 'adapted', 'fitted', 'made-to-order'],
    
    # Common AI conclusion phrases
    'I hope this helps': ['This should answer your question', 'I trust this addresses your needs', 'This might be what you\'re looking for'],
    'Feel free to ask': ['Please don\'t hesitate to ask', 'I\'m here if you have more questions', 'Let me know if you need anything else'],
    'Let me know if you need anything else': ['Happy to help with anything further', 'I\'m available for follow-up questions', 'Just ask if you need more assistance'],
    
    # Passive voice favorites
    'It can be seen that': ['Clearly', 'Evidently', 'We can see that', 'This shows that'],
    'It should be noted that': ['Note that', 'Remember that', 'Keep in mind that', 'Importantly'],
    'It is recommended that': ['I recommend', 'Consider', 'You might try', 'A good approach would be'],
 
# Physics
'motion': ['movement', 'kinematics', 'displacement', 'locomotion'],
'velocity': ['speed', 'rate of travel', 'movement pace', 'kinetic rate'],
'acceleration': ['speed increase', 'momentum rise', 'rate amplification', 'force buildup'],
'force': ['push', 'pull', 'energy exertion', 'power application'],
'energy': ['vitality', 'work potential', 'dynamism', 'active capacity'],
'power': ['energy rate', 'mechanical output', 'strength magnitude', 'effort intensity'],
'friction': ['resistance', 'drag', 'surface opposition', 'sliding hindrance'],
'momentum': ['motion mass', 'impact force', 'movement quantity', 'dynamic strength'],
'gravity': ['gravitational pull', 'attraction field', 'weight force', 'mass binding'],
'mass': ['substance quantity', 'material measure', 'inertial amount', 'weight content'],
'weight': ['gravitational measure', 'load', 'heaviness', 'downward force'],
'pressure': ['force per area', 'compression intensity', 'mechanical load', 'density force'],
'density': ['compactness', 'mass per volume', 'material concentration', 'matter thickness'],
'temperature': ['heat level', 'thermal degree', 'warmth measure', 'energy intensity'],
'heat': ['thermal energy', 'warmth transfer', 'caloric movement', 'temperature flow'],
'work': ['energy transfer', 'effort outcome', 'mechanical exertion', 'physical output'],
'potential energy': ['stored power', 'latent energy', 'positional reserve', 'held dynamism'],
'kinetic energy': ['motion energy', 'moving power', 'active momentum', 'dynamic output'],
'thermodynamics': ['heat behavior', 'energy transformation', 'thermal study', 'temperature dynamics'],
'entropy': ['disorder measure', 'randomness degree', 'energy dispersion', 'system chaos'],
'oscillation': ['vibration', 'swing', 'periodic motion', 'rhythmic movement'],
'frequency': ['repetition rate', 'cycle count', 'wave occurrence', 'temporal rhythm'],
'wavelength': ['wave span', 'distance per cycle', 'oscillation length', 'period gap'],
'amplitude': ['wave height', 'oscillation strength', 'signal extent', 'vibration magnitude'],
'resonance': ['frequency harmony', 'vibration alignment', 'oscillatory match', 'wave reinforcement'],
'wave': ['disturbance', 'ripple', 'oscillation', 'energy motion'],
'sound': ['auditory wave', 'vibration pattern', 'acoustic signal', 'air movement'],
'acoustics': ['sound study', 'vibration science', 'wave behavior', 'auditory physics'],
'light': ['illumination', 'radiance', 'photon stream', 'visible emission'],
'optics': ['light behavior', 'vision physics', 'reflection study', 'refraction analysis'],
'reflection': ['bounce-back', 'light return', 'mirror effect', 'surface rebound'],
'refraction': ['bending', 'deflection', 'angle change', 'light diversion'],
'diffraction': ['wave spreading', 'bending pattern', 'interference shaping', 'edge dispersion'],
'interference': ['wave overlap', 'pattern combination', 'signal merging', 'phase crossing'],
'polarization': ['wave alignment', 'direction filtering', 'orientation adjustment', 'vibration sorting'],
'spectrum': ['range of frequencies', 'color array', 'band spread', 'energy distribution'],
'photon': ['light particle', 'quantum of light', 'energy quanta', 'radiant unit'],
'electricity': ['charge flow', 'electrical energy', 'current movement', 'power transmission'],
'current': ['charge motion', 'electron flow', 'electric stream', 'energy passage'],
'voltage': ['electric potential', 'charge pressure', 'energy difference', 'potential gradient'],
'resistance': ['opposition to current', 'electrical hindrance', 'impedance', 'conduction difficulty'],
'conductivity': ['current transfer ability', 'energy passage ease', 'material allowance', 'electric flow efficiency'],
'capacitance': ['charge storage ability', 'potential holding', 'energy containment', 'field retention'],
'inductance': ['magnetic opposition', 'field inertia', 'coil effect', 'energy delay'],
'electromagnetism': ['field interaction', 'charge magnetism', 'force linkage', 'electrical magnet theory'],
'magnetism': ['attraction field', 'magnetic force', 'polar behavior', 'magnet property'],
'field': ['force region', 'influence zone', 'interaction space', 'energy domain'],
'charge': ['electric quantity', 'particle property', 'ionization state', 'electronic sign'],
'atom': ['smallest matter unit', 'elemental particle', 'chemical building block', 'microscopic entity'],
'nucleus': ['core center', 'atomic heart', 'central region', 'dense particle'],
'proton': ['positive charge particle', 'atomic component', 'nuclear constituent', 'massive particle'],
'neutron': ['neutral particle', 'mass carrier', 'nuclear balance element', 'uncharged atom part'],
'electron': ['negative charge particle', 'orbiting unit', 'atomic mover', 'energy shell occupant'],
'isotope': ['atomic variant', 'nuclear version', 'mass difference atom', 'element type'],
'radioactivity': ['nuclear decay', 'energy emission', 'particle release', 'atomic instability'],
'decay': ['breakdown', 'disintegration', 'transformation', 'energy loss process'],
'half-life': ['decay duration', 'stability time', 'radioactive period', 'nuclear lifespan'],
'quantum mechanics': ['subatomic study', 'wave-particle theory', 'micro energy law', 'atomic probability physics'],
'uncertainty principle': ['measurement limit', 'quantum restriction', 'predictability bound', 'precision ceiling'],
'wave function': ['probability form', 'quantum expression', 'state function', 'particle descriptor'],
'particle': ['small body', 'unit of matter', 'micro object', 'mass fragment'],
'string theory': ['vibrational model', 'cosmic filament concept', 'quantum string idea', 'energy line hypothesis'],
'relativity': ['space-time relation', 'motion dependence', 'Einstein theory', 'speed-time linkage'],
'special relativity': ['constant light theory', 'motion relativity', 'velocity limit law', 'frame dependence'],
'general relativity': ['gravity-space theory', 'curved space concept', 'mass-time interaction', 'Einstein gravity'],
'space-time': ['unified continuum', 'dimensional fabric', 'cosmic structure', 'physical manifold'],
'black hole': ['gravity singularity', 'collapsed star', 'massive core', 'spacetime pit'],
'singularity': ['infinite point', 'mathematical divergence', 'cosmic compression', 'undefined core'],
'time dilation': ['temporal stretching', 'clock slowdown', 'relativistic lag', 'duration elongation'],
'mass-energy equivalence': ['E=mc² law', 'conversion principle', 'energy balance', 'mass transformation'],
'plasma': ['ionized gas', 'charged medium', 'electrified fluid', 'energetic state'],
'fusion': ['joining reaction', 'energy merging', 'nuclear combination', 'atomic unification'],
'fission': ['splitting reaction', 'energy division', 'nuclear break', 'atom separation'],
'particle accelerator': ['collision device', 'energy booster', 'beam collider', 'atomic smasher'],
'cosmology': ['universe study', 'cosmic science', 'space origin exploration', 'celestial evolution'],
'astrophysics': ['stellar physics', 'space energy study', 'galactic science', 'celestial mechanics'],
'gravitational waves': ['space ripples', 'cosmic tremors', 'field oscillations', 'mass disturbance'],
'planetary motion': ['celestial path', 'orbit travel', 'space movement', 'revolutional pattern'],
'orbital mechanics': ['space navigation', 'orbit calculation', 'trajectory control', 'gravitational dynamics'],
'fluid mechanics': ['liquid movement study', 'flow physics', 'hydrodynamics', 'viscous motion analysis'],
'buoyancy': ['floating force', 'upward thrust', 'density lift', 'submersion balance'],
'viscosity': ['thickness', 'fluid resistance', 'flow drag', 'internal friction'],
'turbulence': ['chaotic flow', 'fluid disorder', 'vortex behavior', 'random motion'],
'pressure gradient': ['force difference', 'compression slope', 'density variance', 'flow driver'],
'sound propagation': ['wave travel', 'vibration movement', 'acoustic transmission', 'air oscillation'],
'optical fiber': ['light guide', 'signal strand', 'photon conduit', 'transmission thread'],
'laser': ['light amplification', 'coherent beam', 'photon stream', 'optical ray'],
'crystallography': ['crystal study', 'structure mapping', 'atomic arrangement analysis', 'solid formation science'],
'superconductivity': ['zero resistance', 'perfect conduction', 'quantum flow', 'low-temperature current'],
'nanophysics': ['atomic-scale physics', 'nano behavior study', 'micro energy phenomena', 'small-scale mechanics'],
'quantum entanglement': ['particle linkage', 'nonlocal connection', 'instant correlation', 'state pairing'],
'holography': ['3D imaging', 'wave recording', 'optical reconstruction', 'depth projection'],
'photoelectric effect': ['light emission', 'electron ejection', 'photon interaction', 'quantum light response'],
'spectral analysis': ['frequency examination', 'color decomposition', 'wavelength study', 'energy band review'],
'thermodynamic equilibrium': ['energy balance', 'heat stability', 'thermal rest', 'steady state condition'],
'superposition': ['state overlay', 'wave addition', 'quantum combination', 'probability merge'],
'interference pattern': ['wave design', 'signal crossing', 'oscillation trace', 'constructive overlap'],
'magnetic field': ['flux region', 'magnetic zone', 'polar area', 'force line system'],
'electric field': ['charge region', 'potential zone', 'energy space', 'electrical domain'],
'inertia': ['motion persistence', 'resistance to change', 'mass tendency', 'steady behavior'],

   
    # Academic padding
    'In order to': ['To', 'For', 'So that', 'With the goal of'],
    'With regard to': ['Regarding', 'About', 'Concerning', 'On the subject of'],
    'Due to the fact that': ['Because', 'Since', 'As', 'Given that'],
    
    # Weak verbs
    'make': ['create', 'build', 'develop', 'produce', 'generate'],
    'get': ['obtain', 'acquire', 'receive', 'secure', 'gain'],
    'do': ['perform', 'execute', 'carry out', 'conduct', 'implement'],
    'put': ['place', 'position', 'set', 'arrange', 'locate'],
    
    # Common AI structural patterns
    'First and foremost': ['First', 'To begin', 'Initially', 'The primary point'],
    'Last but not least': ['Finally', 'Lastly', 'To conclude', 'As a final point'],
    'On the one hand... on the other hand': ['While... also', 'Although... nevertheless', 'Despite... however'],
    
    # Overused adjectives
    'key': ['important', 'crucial', 'essential', 'critical', 'vital'],
    'various': ['several', 'multiple', 'different', 'diverse', 'assorted'],
    'multiple': ['several', 'many', 'numerous', 'various', 'different'],
    'numerous': ['many', 'countless', 'multiple', 'plenty of', 'abundant'],
    
    # Cliché phrases
    'at the end of the day': ['ultimately', 'finally', 'in the end', 'when all is said and done'],
    'think outside the box': ['be creative', 'innovate', 'find new approaches', 'break from convention'],
    'low-hanging fruit': ['easy opportunities', 'simple wins', 'readily achievable goals'],
    
    # Weak adverbs
    'basically': ['essentially', 'fundamentally', 'in essence', 'simply put'],
    'literally': ['actually', 'truly', 'genuinely', 'exactly', ''],
    'actually': ['in fact', 'really', 'truly', 'indeed'],
    
    # Redundant phrases
    'each and every': ['each', 'every', 'all', 'every single'],
    'first and foremost': ['first', 'primarily', 'most importantly'],
    'one and only': ['only', 'sole', 'unique', 'singular'],
    
    # Jargon to simplify
    'interface with': ['work with', 'connect to', 'interact with', 'communicate with'],
    'finalize': ['complete', 'finish', 'conclude', 'wrap up'],
    'implement': ['carry out', 'execute', 'apply', 'put into practice'],
    
    # Common AI "helpful" phrases
    'To answer your question': ['Addressing your question', 'Regarding your inquiry', 'In response to your question'],
    'Based on my understanding': ['From what I know', 'As I understand it', 'To my knowledge'],
    'According to the information provided': ['Based on what you shared', 'From your description', 'Given these details'],
    
    # Overused sentence starters
    'Interestingly': ['Fascinatingly', 'Curiously', 'Remarkably', 'Notably'],
    'Importantly': ['Crucially', 'Significantly', 'Vitally', 'Essentially'],
    'Specifically': ['Particularly', 'Exactly', 'Precisely', 'In particular'],
    
    # Core AI Concepts
    'artificial intelligence': ['AI', 'machine intelligence', 'cognitive computing', 'smart systems'],
    'machine learning': ['ML', 'pattern recognition', 'predictive modeling', 'algorithmic learning'],
    'deep learning': ['neural networks', 'hierarchical learning', 'complex pattern recognition'],
    'neural network': ['neural net', 'brain-inspired computing', 'node network', 'connectionist system'],
    'algorithm': ['procedure', 'process', 'methodology', 'computational steps'],
    'model': ['system', 'framework', 'representation', 'AI construct'],
    'training': ['learning process', 'model development', 'algorithm education', 'pattern absorption'],
    'inference': ['prediction', 'decision-making', 'conclusion drawing', 'real-time application'],

    # Data Terms
    'dataset': ['data collection', 'information set', 'training data', 'corpus'],
    'big data': ['large-scale data', 'massive datasets', 'voluminous information', 'data analytics'],
    'data processing': ['information handling', 'data manipulation', 'computational analysis'],
    'data pipeline': ['information flow', 'data processing system', 'ETL process', 'data workflow'],
    'feature': ['attribute', 'characteristic', 'variable', 'data property'],
    'label': ['category', 'classification', 'tag', 'target variable'],
    'validation': ['verification', 'testing', 'performance checking', 'model assessment'],

    # Performance & Evaluation
    'accuracy': ['correctness', 'precision', 'exactness', 'reliability'],
    'precision': ['exactitude', 'specificity', 'detail orientation', 'fine-grained accuracy'],
    'recall': ['completeness', 'coverage', 'thoroughness', 'comprehensive retrieval'],
    'bias': ['prejudice', 'skew', 'imbalance', 'systematic error'],
    'variance': ['variability', 'fluctuation', 'inconsistency', 'dispersion'],
    'overfitting': ['over-training', 'memorization', 'poor generalization', 'excessive complexity'],
    'underfitting': ['under-training', 'oversimplification', 'poor learning', 'insufficient complexity'],

    # Technical Implementation
    'framework': ['structure', 'platform', 'foundation', 'development environment'],
    'library': ['toolkit', 'code collection', 'software package', 'development resources'],
    'API': ['application programming interface', 'software bridge', 'system connection', 'integration point'],
    'endpoint': ['access point', 'connection interface', 'service gateway', 'API destination'],
    'deployment': ['implementation', 'launch', 'production release', 'system rollout'],
    'scaling': ['growth handling', 'expansion management', 'size adaptation', 'performance adjustment'],
    'optimization': ['improvement', 'enhancement', 'performance tuning', 'efficiency increase'],

    # Business & Application
    'automation': ['mechanization', 'streamlining', 'process elimination', 'efficiency improvement'],
    'personalization': ['customization', 'individual adaptation', 'tailored experience', 'user-specific'],
    'recommendation': ['suggestion', 'proposal', 'guidance', 'advice generation'],
    'prediction': ['forecast', 'projection', 'anticipation', 'future estimation'],
    'classification': ['categorization', 'sorting', 'grouping', 'type identification'],
    'clustering': ['grouping', 'segmentation', 'category formation', 'pattern grouping'],
    'anomaly detection': ['outlier identification', 'exception finding', 'deviation spotting', 'irregularity discovery'],

# Business & Application
'automation': ['mechanization', 'streamlining', 'process elimination', 'efficiency improvement'],
'personalization': ['individual tailoring', 'bespoke adjustment', 'preference alignment', 'user centering'],
'recommendation': ['suggestive output', 'option offering', 'guided selection', 'proposal engine'],
'prediction': ['forecast', 'anticipatory insight', 'future outlook', 'expectation estimation'],
'classification': ['grouping', 'type labeling', 'taxonomy creation', 'category mapping'],
'clustering': ['pattern assembly', 'cohort discovery', 'segment alignment', 'natural grouping'],
'anomaly detection': ['outlier surfacing', 'irregularity tracking', 'deviation discovery', 'pattern break spotting'],
'optimization': ['refinement', 'adjustment', 'tuning', 'improvement procedure'],
'workflow': ['process chain', 'task sequence', 'operation path', 'activity stream'],
'efficiency': ['resource economy', 'operational fluency', 'output balance', 'functional precision'],
'decision making': ['choice formulation', 'judgment structuring', 'option evaluation', 'selection process'],
'forecasting': ['trend estimation', 'future shaping', 'prospective analysis', 'market anticipation'],
'market segmentation': ['customer grouping', 'audience slicing', 'niche distinction', 'target isolation'],
'resource allocation': ['asset distribution', 'supply apportioning', 'capacity balancing', 'capital spreading'],
'process mining': ['operation tracing', 'procedure mapping', 'workflow excavation', 'sequence reconstruction'],
'quality control': ['standard assurance', 'error screening', 'defect detection', 'consistency enforcement'],
'supply chain': ['logistics network', 'distribution route', 'resource linkage', 'delivery pathway'],
'customer retention': ['client loyalty', 'audience persistence', 'patron maintenance', 'repeat engagement'],
'demand forecasting': ['need estimation', 'consumption outlook', 'buyer anticipation', 'usage prediction'],
'pricing strategy': ['valuation method', 'cost positioning', 'rate modeling', 'charge calibration'],
'financial modeling': ['budget simulation', 'monetary projection', 'economic shaping', 'fiscal representation'],
'credit scoring': ['trustworthiness grading', 'borrower evaluation', 'repayment likelihood estimation', 'financial profiling'],
'risk analysis': ['hazard study', 'exposure examination', 'uncertainty evaluation', 'threat quantification'],
'fraud detection': ['deception spotting', 'illicit behavior recognition', 'misconduct flagging', 'dishonesty tracing'],
'process automation': ['robotic operation', 'mechanical substitution', 'task simplification', 'procedure removal'],
'knowledge management': ['information handling', 'organizational memory', 'data stewardship', 'insight retention'],
'performance tracking': ['progress observation', 'metric following', 'output supervision', 'efficiency logging'],
'strategic planning': ['tactical layout', 'goal projection', 'directional preparation', 'initiative charting'],
'employee analytics': ['workforce analysis', 'staff measurement', 'labor evaluation', 'team insight'],
'sentiment analysis': ['emotional inference', 'opinion gauging', 'tone inspection', 'attitude reading'],
'process improvement': ['workflow refinement', 'task betterment', 'procedure polishing', 'efficiency tuning'],
'customer analytics': ['audience examination', 'consumer insight', 'buyer profiling', 'market persona building'],
'data visualization': ['information portrayal', 'graphical expression', 'analytic depiction', 'visual summarization'],
'trend analysis': ['pattern review', 'progression study', 'development interpretation', 'trajectory reading'],
'forecast accuracy': ['predictive precision', 'projection reliability', 'anticipation validity', 'outlook correctness'],
'budget optimization': ['spending calibration', 'financial refinement', 'resource economization', 'allocation tuning'],
'sales prediction': ['revenue estimation', 'transaction outlook', 'purchase projection', 'market expectation'],
'market basket analysis': ['purchase pattern detection', 'item association mining', 'buyer link inference', 'co-buying identification'],
'workflow optimization': ['operation improvement', 'process enhancement', 'task fine-tuning', 'procedure perfection'],
'competitor analysis': ['rival observation', 'market opposition study', 'industry contrast', 'competitive awareness'],
'customer journey mapping': ['experience tracing', 'interaction path drawing', 'buyer route visualization', 'touchpoint sequencing'],
'feedback analysis': ['response interpretation', 'review parsing', 'reaction reading', 'comment assessment'],
'HR analytics': ['workforce insight', 'employee data study', 'human resource evaluation', 'talent metric tracking'],
'marketing automation': ['campaign mechanization', 'promotion streamlining', 'adflow simplification', 'engagement programming'],
'customer satisfaction': ['user happiness', 'client approval', 'service delight', 'experience rating'],
'retail analytics': ['store insight', 'sales environment study', 'shopper evaluation', 'consumer flow measurement'],
'lead scoring': ['prospect ranking', 'interest grading', 'conversion likelihood estimation', 'potential client weighing'],
'process efficiency': ['operation streamlining', 'task productivity', 'workflow economy', 'mechanical smoothness'],
'predictive maintenance': ['fault anticipation', 'failure prevention', 'equipment outlook', 'breakdown forewarning'],
'inventory management': ['stock control', 'supply balancing', 'resource keeping', 'warehouse regulation'],
'logistics optimization': ['transport tuning', 'delivery enhancement', 'distribution efficiency', 'route perfection'],
'operational excellence': ['execution mastery', 'performance superiority', 'system perfection', 'process idealization'],
'project scheduling': ['timeline structuring', 'time mapping', 'deadline alignment', 'milestone charting'],
'process auditing': ['workflow examination', 'procedure checking', 'operation validation', 'step verification'],
'product recommendation': ['item suggestion', 'choice offering', 'goods alignment', 'purchase prompting'],
'pricing optimization': ['cost fine-tuning', 'rate balancing', 'valuation adjustment', 'charge perfection'],
'return on investment': ['profit ratio', 'gain yield', 'capital efficiency', 'financial return'],
'decision support': ['judgment assistance', 'choice facilitation', 'planning reinforcement', 'option backing'],
'consumer behavior': ['buyer conduct', 'purchase tendency', 'spending pattern', 'user mannerism'],
'profit analysis': ['income breakdown', 'gain evaluation', 'revenue decomposition', 'financial understanding'],
'brand analysis': ['identity study', 'reputation inspection', 'image evaluation', 'market positioning'],
'advertising analytics': ['promotion insight', 'media evaluation', 'ad performance study', 'campaign reflection'],
'market intelligence': ['industry awareness', 'commercial insight', 'sector observation', 'competitive comprehension'],
'cost reduction': ['expense trimming', 'budget tightening', 'financial cutback', 'economic saving'],
'corporate governance': ['organizational oversight', 'business ethics enforcement', 'policy compliance', 'management discipline'],
'data governance': ['information stewardship', 'data control', 'record management', 'policy supervision'],
'customer churn': ['client dropout', 'subscriber loss', 'patron exit', 'loyalty decline'],
'employee retention': ['staff holding', 'talent maintenance', 'workforce continuity', 'labor persistence'],
'financial forecasting': ['monetary outlook', 'budget prediction', 'economic anticipation', 'funding expectation'],
'project management': ['initiative coordination', 'goal handling', 'execution oversight', 'timeline control'],
'strategy formulation': ['tactical creation', 'plan design', 'vision construction', 'objective layout'],
'performance benchmarking': ['comparison testing', 'metric referencing', 'peer evaluation', 'standard measurement'],
'resource planning': ['asset arrangement', 'supply scheduling', 'capacity organization', 'provision coordination'],
'cost-benefit analysis': ['gain-loss evaluation', 'profitability estimation', 'expense justification', 'financial weighing'],
'innovation management': ['creativity supervision', 'idea structuring', 'concept cultivation', 'novelty guidance'],
'sales optimization': ['revenue tuning', 'market boosting', 'deal improvement', 'transaction enhancement'],
'supply forecasting': ['stock outlook', 'resource estimation', 'availability projection', 'inventory anticipation'],
'fraud prevention': ['misconduct avoidance', 'deception protection', 'dishonesty deterrence', 'illegal act guarding'],
'data-driven decision': ['information-based judgment', 'fact-oriented planning', 'analytic guidance', 'evidence reasoning'],
'consumer insight': ['buyer understanding', 'user comprehension', 'audience knowledge', 'market perception'],
'operational analytics': ['process measurement', 'workflow analysis', 'performance data insight', 'system evaluation'],
'workflow management': ['task coordination', 'process supervision', 'operation handling', 'activity alignment'],
'change management': ['transition control', 'organizational adjustment', 'adaptation handling', 'transformation planning'],
'strategic optimization': ['goal refinement', 'directional enhancement', 'long-term tuning', 'mission alignment'],
'enterprise automation': ['corporate mechanization', 'organization streamlining', 'systemic substitution', 'task delegation'],
'decision automation': ['judgment mechanization', 'choice replacement', 'policy execution', 'automated reasoning'],
'product innovation': ['goods improvement', 'creation novelty', 'design advancement', 'market originality'],
'competitive analysis': ['rival assessment', 'opponent comparison', 'market rivalry study', 'industry competition review'],
'customer experience': ['user journey', 'service impression', 'interaction satisfaction', 'engagement memory'],
'data monetization': ['information capitalization', 'insight selling', 'analytic commercialization', 'knowledge profit'],
'financial optimization': ['fund refinement', 'cash flow tuning', 'budget balancing', 'resource efficiency'],
'market optimization': ['demand balancing', 'offer alignment', 'consumer targeting', 'sector refinement'],
'service automation': ['operation robotization', 'support mechanization', 'task digitalization', 'workflow simplification'],
    
# Modern AI Approaches
    'generative AI': ['creative AI', 'content creation', 'synthetic generation', 'production AI'],
    'transformer': ['attention-based model', 'sequence processor', 'context understanding architecture'],
    'LLM': ['large language model', 'big language AI', 'extensive text model', 'massive language system'],
    'computer vision': ['image understanding', 'visual recognition', 'picture analysis', 'visual AI'],
    'NLP': ['natural language processing', 'text understanding', 'language AI', 'linguistic computing'],
    'reinforcement learning': ['trial-and-error learning', 'reward-based training', 'interactive learning'],

    # Ethics & Responsibility
    'ethical AI': ['responsible AI', 'moral artificial intelligence', 'conscientious AI', 'principled systems'],
    'AI safety': ['system security', 'risk prevention', 'harm avoidance', 'protective measures'],
    'fairness': ['equity', 'justice', 'impartiality', 'equal treatment'],
    'transparency': ['openness', 'clarity', 'explainability', 'understandability'],
    'accountability': ['responsibility', 'answerability', 'liability', 'obligation'],
    'explainability': ['interpretability', 'understandability', 'clarity', 'comprehensibility'],
    'governance': ['oversight', 'management', 'control', 'regulation'],

    # Industry Buzzwords
    'disruption': ['transformation', 'revolution', 'paradigm shift', 'industry change'],
    'innovation': ['novelty', 'breakthrough', 'advancement', 'progressive development'],
    'digital transformation': ['technological modernization', 'digital upgrade', 'tech integration', 'computerization'],
    'cloud computing': ['remote processing', 'internet-based computing', 'online services', 'virtual infrastructure'],
    'edge computing': ['decentralized processing', 'local computation', 'device-level computing', 'distributed processing'],
    'IoT': ['internet of things', 'connected devices', 'smart objects', 'networked physical systems'],

    # Development Processes
    'agile': ['flexible development', 'iterative approach', 'adaptive methodology', 'incremental development'],
    'sprint': ['development cycle', 'work period', 'project phase', 'iteration'],
    'prototype': ['preliminary version', 'test model', 'early sample', 'proof of concept'],
    'MVP': ['minimum viable product', 'basic version', 'initial offering', 'foundational product'],
    'iteration': ['cycle', 'repetition', 'version update', 'progressive improvement'],
    'feedback loop': ['response cycle', 'input system', 'performance adjustment mechanism'],

    # User Experience
    'user interface': ['UI', 'user interaction point', 'control system', 'user-facing design'],
    'user experience': ['UX', 'user journey', 'interaction quality', 'customer experience'],
    'intuitive': ['user-friendly', 'easy to use', 'natural', 'self-explanatory'],
    'seamless': ['smooth', 'uninterrupted', 'fluid', 'effortless'],
    'frictionless': ['smooth', 'easy', 'unobstructed', 'hassle-free'],
    'onboarding': ['initial setup', 'user introduction', 'system familiarization', 'initial training'],

    # Capability Descriptions
    'robust': ['strong', 'reliable', 'durable', 'resilient'],
    'scalable': ['expandable', 'growable', 'adaptable', 'flexible'],
    'efficient': ['effective', 'productive', 'streamlined', 'optimized'],
    'adaptive': ['flexible', 'adjustable', 'responsive', 'modifiable'],
    'intelligent': ['smart', 'cognitive', 'reasoning', 'thinking'],
    'autonomous': ['self-governing', 'independent', 'self-directed', 'self-operating'],

    # Problem-Solving Terms
    'optimize': ['improve', 'enhance', 'refine', 'perfect'],
    'streamline': ['simplify', 'efficientize', 'smooth out', 'organize'],
    'leverage': ['utilize', 'use', 'employ', 'take advantage of'],
    'enhance': ['improve', 'boost', 'strengthen', 'augment'],
    'transform': ['change', 'revolutionize', 'convert', 'metamorphose'],
    'revolutionize': ['transform', 'completely change', 'overhaul', 'reinvent'],

    # Common AI Applications
    'chatbot': ['conversational agent', 'dialogue system', 'virtual assistant', 'talkbot'],
    'virtual assistant': ['digital helper', 'AI aide', 'smart assistant', 'automated support'],
    'predictive analytics': ['forecasting analysis', 'future prediction', 'trend projection', 'anticipatory analysis'],
    'sentiment analysis': ['emotion detection', 'opinion mining', 'feeling assessment', 'mood analysis'],
    'image recognition': ['visual identification', 'picture understanding', 'visual pattern recognition'],
    'speech recognition': ['voice understanding', 'audio processing', 'spoken word identification'],

    # Technical Architecture
    'microservices': ['modular services', 'independent components', 'distributed architecture', 'service-oriented'],
    'containerization': ['application packaging', 'isolated deployment', 'environment encapsulation'],
    'orchestration': ['coordination', 'management', 'organization', 'synchronization'],
    'serverless': ['cloud-native', 'function-based', 'event-driven', 'managed services'],
    'real-time': ['instantaneous', 'immediate', 'live', 'concurrent'],
    'batch processing': ['grouped computation', 'scheduled processing', 'collected task execution'],

    # Data Management
    'data mining': ['information discovery', 'pattern extraction', 'knowledge discovery', 'insight extraction'],
    'data warehousing': ['information storage', 'data repository', 'centralized data storage'],
    'data governance': ['information management', 'data control', 'information oversight', 'data stewardship'],
    'data quality': ['information accuracy', 'data reliability', 'information integrity', 'data cleanliness'],
    'data privacy': ['information protection', 'personal data security', 'confidentiality', 'data secrecy'],
    'data security': ['information safety', 'data protection', 'cybersecurity', 'information defense'],

    # Performance Metrics
    'throughput': ['processing capacity', 'output rate', 'production speed', 'transaction volume'],
    'latency': ['delay', 'response time', 'waiting period', 'processing time'],
    'reliability': ['dependability', 'trustworthiness', 'consistency', 'stability'],
    'availability': ['accessibility', 'uptime', 'readiness', 'operational status'],
    'scalability': ['growth capacity', 'expansion capability', 'size adaptability', 'load handling'],
    'efficiency': ['productivity', 'effectiveness', 'performance', 'competence'],

    # Development Terms
    'integration': ['combination', 'unification', 'merging', 'incorporation'],
    'compatibility': ['interoperability', 'cooperation', 'harmony', 'coexistence'],
    'modular': ['component-based', 'sectional', 'unit-based', 'segmentable'],
    'configurable': ['customizable', 'adjustable', 'modifiable', 'adaptable'],
    'extensible': ['expandable', 'enhanceable', 'developable', 'scalable'],
    'maintainable': ['supportable', 'serviceable', 'manageable', 'sustainable'],

    # Business Value Terms
    'ROI': ['return on investment', 'value for money', 'investment return', 'cost benefit'],
    'value proposition': ['benefit statement', 'advantage description', 'worth proposition', 'merit offering'],
    'competitive advantage': ['superior position', 'market edge', 'distinctive benefit', 'leading feature'],
    'market differentiation': ['unique positioning', 'distinct identity', 'special character', 'individuality'],
    'customer retention': ['client keeping', 'user maintenance', 'customer loyalty', 'audience preservation'],
    'user engagement': ['customer interaction', 'audience involvement', 'user participation', 'client activity'],

    # Modern Development Practices
    'CI/CD': ['continuous integration/deployment', 'automated pipeline', 'streamlined delivery', 'rapid release'],
    'DevOps': ['development operations', 'collaborative engineering', 'integrated development', 'combined teams'],
    'MLOps': ['machine learning operations', 'AI deployment management', 'model lifecycle management'],
    'dataOps': ['data operations', 'information workflow management', 'data pipeline operations'],
    'version control': ['revision management', 'change tracking', 'code history', 'modification record'],
    'code review': ['program inspection', 'software examination', 'peer evaluation', 'quality assessment'],

    # Cloud & Infrastructure
    'infrastructure as code': ['IaC', 'programmable infrastructure', 'automated setup', 'code-defined systems'],
    'platform as a service': ['PaaS', 'development platform', 'application environment', 'cloud platform'],
    'software as a service': ['SaaS', 'cloud application', 'online software', 'web-based service'],
    'container': ['application package', 'software unit', 'isolated environment', 'deployment unit'],
    'orchestrator': ['coordinator', 'manager', 'organizer', 'scheduler'],
    'service mesh': ['microservice network', 'service communication layer', 'application networking'],

    # Security Terms
    'encryption': ['data encoding', 'information scrambling', 'cryptographic protection', 'security encoding'],
    'authentication': ['identity verification', 'user validation', 'login confirmation', 'access approval'],
    'authorization': ['permission granting', 'access rights', 'privilege assignment', 'clearance providing'],
    'vulnerability': ['weakness', 'security gap', 'flaw', 'exposure'],
    'threat': ['danger', 'risk', 'hazard', 'peril'],
    'compliance': ['regulation adherence', 'standard following', 'rule obedience', 'requirement meeting'],

    # AI-Specific Technical Terms
    'hyperparameter': ['model setting', 'configuration parameter', 'training control', 'algorithm setting'],
    'loss function': ['error measure', 'performance metric', 'cost calculation', 'accuracy gauge'],
    'gradient descent': ['optimization method', 'minimization algorithm', 'error reduction', 'performance improvement'],
    'backpropagation': ['error correction', 'neural network training', 'weight adjustment', 'learning algorithm'],
    'convolutional network': ['CNN', 'image processing network', 'visual pattern recognizer', 'spatial analyzer'],
    'recurrent network': ['RNN', 'sequence processor', 'temporal analyzer', 'time-series network'],
    'attention mechanism': ['focus system', 'importance weighting', 'context prioritization', 'relevance assessment'],
    'transfer learning': ['knowledge application', 'model adaptation', 'skill transfer', 'pre-trained utilization'],
    'fine-tuning': ['precise adjustment', 'detailed optimization', 'specific adaptation', 'targeted improvement'],
    'zero-shot learning': ['no-example learning', 'direct application', 'immediate adaptation', 'example-free inference'],

    # Emerging Concepts
    'AGI': ['artificial general intelligence', 'human-level AI', 'general-purpose intelligence', 'comprehensive AI'],
    'singularity': ['technological explosion', 'AI breakthrough point', 'exponential growth phase'],
    'alignment': ['goal matching', 'value correspondence', 'objective synchronization', 'purpose harmony'],
    'multi-modal': ['combined input types', 'mixed media processing', 'integrated modality', 'varied format handling'],
    'embodied AI': ['physical AI', 'robot intelligence', 'real-world interaction AI', 'situated intelligence'],
    'neuromorphic computing': ['brain-like processing', 'neural hardware', 'biological computing', 'cognitive chips'],
    'quantum machine learning': ['QML', 'quantum AI', 'quantum-enhanced learning', 'quantum computing ML'],
    'federated learning': ['distributed training', 'decentralized learning', 'local model training', 'privacy-preserving ML'],
    'differential privacy': ['privacy protection', 'confidentiality preservation', 'data anonymity', 'information security'],
    'synthetic data': ['artificial data', 'generated information', 'simulated datasets', 'created examples'],

    # Common AI Limitations
    'hallucination': ['fabrication', 'invention', 'false generation', 'imaginary content'],
    'bias amplification': ['prejudice reinforcement', 'discrimination increase', 'skew magnification'],
    'data drift': ['pattern change', 'distribution shift', 'concept evolution', 'environmental change'],
    'model decay': ['performance degradation', 'accuracy decline', 'effectiveness reduction', 'capability loss'],
    'adversarial attack': ['manipulation attempt', 'system exploitation', 'vulnerability targeting', 'security breach'],
    'interpretability challenge': ['understanding difficulty', 'explanation problem', 'comprehension issue', 'clarity obstacle'],

    # Implementation Challenges
    'computational cost': ['processing expense', 'resource requirement', 'hardware demand', 'power consumption'],
    'data requirement': ['information need', 'training data necessity', 'input requirement', 'dataset dependency'],
    'deployment complexity': ['implementation difficulty', 'rollout challenge', 'production complexity', 'system integration'],
    'maintenance overhead': ['ongoing cost', 'continuous effort', 'sustaining work', 'operational burden'],
    'skill gap': ['expertise shortage', 'knowledge deficiency', 'talent lack', 'capability void'],
    'ethical consideration': ['moral issue', 'privacy concern', 'fairness question', 'responsibility aspect'],


    # Vague business speak
    'value-added': ['beneficial', 'advantageous', 'useful', 'helpful'],
    'core competency': ['strength', 'specialty', 'expertise', 'key skill'],
    'best practice': ['effective method', 'proven approach', 'recommended technique'],
    
    # Common AI formatting habits
    'bullet points': ['list', 'items', 'points', 'elements'],
    'as follows': ['as below', 'listed here', 'shown next', 'detailed below'],
    'in the following way': ['like this', 'as shown', 'in this manner', 'thus'],
    
    # Weak conclusions
    'in conclusion': ['to summarize', 'overall', 'in summary', 'to wrap up'],
    'to sum up': ['in brief', 'in short', 'ultimately', 'basically'],
    'all things considered': ['taking everything into account', 'overall', 'when everything is considered'],

    # Advanced Academic & Intellectual
    'erudite': ['learned', 'scholarly', 'knowledgeable', 'well-read'],
    'esoteric': ['abstruse', 'arcane', 'recondite', 'obscure'],
    'pedantic': ['academic', 'scholastic', 'doctrinaire', 'overscrupulous'],
    'didactic': ['instructive', 'educational', 'edifying', 'informative'],
    'epistemological': ['cognitive', 'philosophical', 'theoretical', 'methodological'],
    'hermeneutic': ['interpretive', 'exegetical', 'analytical', 'critical'],
    'dichotomy': ['division', 'split', 'polarity', 'contrast'],
    'hegemony': ['dominance', 'supremacy', 'authority', 'control'],
    'paradigm': ['model', 'pattern', 'exemplar', 'standard'],
    'taxonomy': ['classification', 'categorization', 'nomenclature', 'systematization'],

    # Complex States & Conditions
    'ubiquitous': ['omnipresent', 'pervasive', 'universal', 'everywhere'],
    'equivocal': ['ambiguous', 'vague', 'unclear', 'indefinite'],
    'laconic': ['concise', 'terse', 'succinct', 'brief'],
    'prolific': ['productive', 'fruitful', 'copious', 'generative'],
    'quintessential': ['typical', 'archetypal', 'ultimate', 'prime'],
    'voracious': ['insatiable', 'ravenous', 'unquenchable', 'avid'],
    'inexorable': ['relentless', 'unavoidable', 'inescapable', 'irresistible'],
    'inscrutable': ['enigmatic', 'impenetrable', 'unfathomable', 'mysterious'],
    'iconoclastic': ['nonconformist', 'maverick', 'rebellious', 'radical'],
    'idiosyncratic': ['distinctive', 'individual', 'unique', 'peculiar'],

    # Positive Traits & Qualities
    'perspicacious': ['perceptive', 'discerning', 'astute', 'shrewd'],
    'sagacious': ['wise', 'judicious', 'sage', 'prudent'],
    'magnanimous': ['generous', 'benevolent', 'charitable', 'noble'],
    'munificent': ['lavish', 'bountiful', 'liberal', 'unstinting'],
    'indefatigable': ['tireless', 'unflagging', 'dogged', 'persistent'],
    'resilient': ['tough', 'durable', 'robust', 'flexible'],
    'tenacious': ['determined', 'resolute', 'steadfast', 'persistent'],
    'assiduous': ['diligent', 'meticulous', 'conscientious', 'punctilious'],
    'scrupulous': ['ethical', 'principled', 'honorable', 'upright'],
    'stoic': ['unemotional', 'impassive', 'long-suffering', 'dispassionate'],

    # Negative Traits & Qualities
    'supercilious': ['arrogant', 'haughty', 'condescending', 'disdainful'],
    'obsequious': ['servile', 'sycophantic', 'fawning', 'submissive'],
    'parsimonious': ['stingy', 'miserly', 'penny-pinching', 'frugal'],
    'truculent': ['defiant', 'aggressive', 'belligerent', 'hostile'],
    'recalcitrant': ['uncooperative', 'intractable', 'defiant', 'obstinate'],
    'dilatory': ['slow', 'tardy', 'procrastinating', 'delaying'],
    'perfidious': ['treacherous', 'disloyal', 'traitorous', 'duplicitous'],
    'querulous': ['complaining', 'peevish', 'fretful', 'whining'],
    'capricious': ['fickle', 'unpredictable', 'volatile', 'whimsical'],
    'obdurate': ['stubborn', 'inflexible', 'unbending', 'adamant'],

    # Verbs of Action & Change
    'exacerbate': ['worsen', 'intensify', 'aggravate', 'compound'],
    'ameliorate': ['improve', 'better', 'enhance', 'alleviate'],
    'abrogate': ['revoke', 'repeal', 'cancel', 'nullify'],
    'disseminate': ['spread', 'circulate', 'distribute', 'propagate'],
    'oscillate': ['swing', 'fluctuate', 'vacillate', 'waver'],
    'coalesce': ['unite', 'combine', 'merge', 'integrate'],
    'extricate': ['disentangle', 'free', 'release', 'liberate'],
    'permeate': ['pervade', 'saturate', 'impregnate', 'infuse'],
    'precipitate': ['cause', 'trigger', 'provoke', 'hasten'],
    'quell': ['suppress', 'subdue', 'quash', 'squelch'],

    # Verbs of Communication & Thought
    'postulate': ['propose', 'suggest', 'hypothesize', 'theorize'],
    'conjecture': ['speculate', 'guess', 'surmise', 'infer'],
    'elucidate': ['clarify', 'explain', 'illuminate', 'explicate'],
    'expatiate': ['elaborate', 'expound', 'dilate', 'enlarge'],
    'vituperate': ['berate', 'revile', 'scold', 'upbraid'],
    'equivocate': ['prevaricate', 'hedge', 'dodge', 'evade'],
    'adumbrate': ['foreshadow', 'outline', 'sketch', 'prefigure'],
    'propitiate': ['appease', 'placate', 'pacify', 'mollify'],
    'obfuscate': ['confuse', 'bewilder', 'muddle', 'cloud'],
    'recapitulate': ['summarize', 'recap', 'reiterate', 'reprise'],

    # Abstract Concepts
    'verisimilitude': ['realism', 'authenticity', 'plausibility', 'credibility'],
    'zeitgeist': ['spirit of the age', 'cultural climate', 'mood of the era'],
    'anachronism': ['chronological error', 'misdate', 'archaism', 'throwback'],
    'apotheosis': ['epitome', 'quintessence', 'peak', 'pinnacle'],
    'euphemism': ['polite term', 'indirect expression', 'understatement'],
    'panacea': ['cure-all', 'universal remedy', 'elixir', 'magic bullet'],
    'sycophant': ['flatterer', 'yes-man', 'toady', 'fawner'],
    'nemesis': ['archenemy', 'adversary', 'rival', 'bane'],
    'dystopia': ['anti-utopia', 'hellscape', 'apocalyptic vision'],
    'utopia': ['paradise', 'ideal society', 'heaven on earth', 'Eden'],

    # Sensory & Descriptive
    'audacious': ['bold', 'daring', 'fearless', 'intrepid'],
    'luminous': ['bright', 'radiant', 'glowing', 'incandescent'],
    'opulent': ['luxurious', 'sumptuous', 'lavish', 'palatial'],
    'serene': ['calm', 'peaceful', 'tranquil', 'placid'],
    'taciturn': ['reserved', 'reticent', 'uncommunicative', 'quiet'],
    'vociferous': ['vehement', 'outspoken', 'clamorous', 'strident'],
    'winsome': ['charming', 'engaging', 'appealing', 'captivating'],
    'verdant': ['green', 'lush', 'grassy', 'leafy'],
    'desiccated': ['dried out', 'dehydrated', 'parched', 'arid'],
    'fetid': ['stinking', 'malodorous', 'putrid', 'rank'],

    # Legal & Formal
    'acquiesce': ['consent', 'agree', 'assent', 'accede'],
    'cogent': ['convincing', 'compelling', 'persuasive', 'forceful'],
    'culpable': ['guilty', 'blameworthy', 'responsible', 'at fault'],
    'egregious': ['shocking', 'outrageous', 'glaring', 'gross'],
    'extraneous': ['irrelevant', 'immaterial', 'superfluous', 'nonessential'],
    'facilitate': ['ease', 'simplify', 'expedite', 'assist'],
    'gratuitous': ['unnecessary', 'unwarranted', 'unjustified', 'uncalled for'],
    'laudable': ['praiseworthy', 'commendable', 'admirable', 'creditable'],
    'mitigate': ['alleviate', 'reduce', 'lessen', 'diminish'],
    'negligible': ['insignificant', 'trivial', 'minor', 'inconsequential'],

    # Scientific & Technical
    'anomalous': ['abnormal', 'atypical', 'irregular', 'deviant'],
    'catalyst': ['stimulus', 'impetus', 'spur', 'precipitant'],
    'homogeneous': ['uniform', 'consistent', 'unalike', 'similar'],
    'heterogeneous': ['diverse', 'varied', 'mixed', 'assorted'],
    'empirical': ['observational', 'experimental', 'pragmatic', 'experiential'],
    'paradox': ['contradiction', 'inconsistency', 'puzzle', 'enigma'],
    'phenomenon': ['occurrence', 'event', 'fact', 'situation'],
    'theorem': ['proposition', 'formula', 'rule', 'principle'],
    'synthesis': ['combination', 'amalgamation', 'fusion', 'composite'],
    'volatile': ['unstable', 'explosive', 'unpredictable', 'erratic'],

    # Business & Economics
    'acquisition': ['purchase', 'buyout', 'procurement', 'takeover'],
    'arbitrage': ['exploitation of price differences', 'trading', 'speculation'],
    'commodity': ['product', 'good', 'article of trade', 'resource'],
    'depreciation': ['devaluation', 'decrease in value', 'reduction', 'weakening'],
    'derivative': ['by-product', 'offshoot', 'secondary financial instrument'],
    'equity': ['fairness', 'ownership', 'stock', 'value'],
    'liquidity': ['cash availability', 'fluid assets', 'marketability'],
    'merger': ['consolidation', 'amalgamation', 'union', 'fusion'],
    'solvent': ['financially sound', 'able to pay debts', 'creditworthy'],
    'insolvent': ['bankrupt', 'ruined', 'unable to pay debts', 'penalized'],

    # Psychological & Emotional
    'catharsis': ['release', 'purging', 'emotional cleansing', 'abreaction'],
    'compulsive': ['irresistible', 'uncontrollable', 'driven', 'obsessive'],
    'eclectic': ['selective', 'diverse', 'broad', 'varied'],
    'empathy': ['understanding', 'compassion', 'identification', 'rapport'],
    'lethargic': ['sluggish', 'listless', 'torpid', 'languid'],
    'nostalgia': ['longing', 'yearning', 'homesickness', 'reminiscence'],
    'phobia': ['aversion', 'fear', 'dread', 'terror'],
    'skeptical': ['doubtful', 'questioning', 'cynical', 'disbelieving'],
    'ambiguous': ['vague', 'unclear', 'equivocal', 'cryptic'],
    'ambivalent': ['uncertain', 'indecisive', 'torn', 'conflicted'],

    # Art & Literature
    'aesthetic': ['artistic', 'tasteful', 'decorative', 'ornamental'],
    'allegory': ['parable', 'symbolic story', 'fable', 'metaphor'],
    'caricature': ['cartoon', 'exaggerated portrayal', 'parody', 'lampoon'],
    'collage': ['montage', 'assembly', 'collection', 'patchwork'],
    'genre': ['category', 'style', 'type', 'classification'],
    'metaphor': ['symbol', 'analogy', 'figure of speech', 'trope'],
    'parody': ['satire', 'lampoon', 'spoof', 'imitation'],
    'surreal': ['dreamlike', 'fantastic', 'bizarre', 'uncanny'],
    'vignette': ['sketch', 'scene', 'anecdote', 'vignette'],
    'leitmotif': ['recurring theme', 'dominant idea', 'motif', 'refrain'],

    # Social & Political
    'bipartisan': ['cross-party', 'unifying', 'cooperative', 'collaborative'],
    'coalition': ['alliance', 'union', 'partnership', 'bloc'],
    'demographic': ['population group', 'statistical segment', 'societal category'],
    'ideology': ['belief system', 'doctrine', 'creed', 'philosophy'],
    'partisan': ['biased', 'one-sided', 'factional', 'prejudiced'],
    'pluralistic': ['diverse', 'multicultural', 'inclusive', 'varied'],
    'sovereignty': ['autonomy', 'independence', 'self-rule', 'self-government'],
    'totalitarian': ['authoritarian', 'dictatorial', 'oppressive', 'tyrannical'],
    'unilateral': ['one-sided', 'independent', 'solo', 'unsupported'],
    'xenophobia': ['prejudice', 'intolerance', 'racism', 'chauvinism'],

    # Nature & Environment
    'biome': ['ecological community', 'habitat zone', 'ecosystem'],
    'biodiversity': ['biological variety', 'species richness', 'ecological diversity'],
    'deforestation': ['clearing', 'logging', 'forest removal', 'denuding'],
    'ecosystem': ['ecological system', 'environment', 'habitat', 'biota'],
    'endemic': ['native', 'local', 'indigenous', 'restricted'],
    'fauna': ['animal life', 'creatures', 'wildlife', 'zoology'],
    'flora': ['plant life', 'vegetation', 'botany', 'plants'],
    'habitat': ['environment', 'territory', 'domain', 'home'],
    'indigenous': ['native', 'aboriginal', 'original', 'local'],
    'sustainable': ['maintainable', 'eco-friendly', 'renewable', 'green'],



    # Technology & Computing
    'algorithmic': ['systematic', 'procedural', 'computational', 'methodical'],
    'bandwidth': ['capacity', 'throughput', 'data rate', 'speed'],
    'encryption': ['encoding', 'scrambling', 'cryptography', 'cyphering'],
    'firewall': ['security barrier', 'protection system', 'digital shield'],
    'interface': ['connection', 'link', 'gateway', 'portal'],
    'latency': ['delay', 'lag', 'waiting time', 'response time'],
    'scalable': ['expandable', 'growable', 'adaptable', 'flexible'],
    'syntax': ['grammar', 'structure', 'rules', 'format'],
    'virtualization': ['simulation', 'emulation', 'creation of virtual versions'],
    'blockchain': ['distributed ledger', 'digital record', 'cryptographic chain'],

    # Medical & Health
    'aetiology': ['causation', 'origin', 'cause', 'source'],
    'benign': ['harmless', 'non-cancerous', 'innocuous', 'safe'],
    'diagnosis': ['identification', 'detection', 'determination', 'analysis'],
    'epidemiology': ['study of disease incidence', 'public health study'],
    'malignant': ['cancerous', 'dangerous', 'virulent', 'deadly'],
    'palliative': ['soothing', 'alleviating', 'comforting', 'pain-relieving'],
    'prognosis': ['forecast', 'outlook', 'prediction', 'projection'],
    'remission': ['improvement', 'abatement', 'subsidence', 'respite'],
    'symptomatic': ['indicative', 'characteristic', 'suggestive', 'typical'],
    'vaccination': ['immunization', 'inoculation', 'shot', 'jab'],

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
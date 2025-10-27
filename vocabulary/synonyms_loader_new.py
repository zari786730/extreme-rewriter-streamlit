"""
SYNONYMS LOADER - FILES 46 TO 129
Standalone loader for the new files
"""

def get_synonyms(word):
    """Get synonyms for any word from new files"""
    if not word or len(word) < 2:
        return []
        
    word_lower = word.lower()
    
    # Import all new files
    from synonyms_046 import synonyms as s46
    from synonyms_047 import synonyms as s47
    from synonyms_048 import synonyms as s48
    from synonyms_049 import synonyms as s49
    from synonyms_050 import synonyms as s50
    from synonyms_051 import synonyms as s51
    from synonyms_052 import synonyms as s52
    from synonyms_053 import synonyms as s53
    from synonyms_054 import synonyms as s54
    from synonyms_055 import synonyms as s55
    from synonyms_056 import synonyms as s56
    from synonyms_057 import synonyms as s57
    from synonyms_058 import synonyms as s58
    from synonyms_059 import synonyms as s59
    from synonyms_060 import synonyms as s60
    from synonyms_061 import synonyms as s61
    from synonyms_062 import synonyms as s62
    from synonyms_063 import synonyms as s63
    from synonyms_064 import synonyms as s64
    from synonyms_065 import synonyms as s65
    from synonyms_066 import synonyms as s66
    from synonyms_067 import synonyms as s67
    from synonyms_068 import synonyms as s68
    from synonyms_069 import synonyms as s69
    from synonyms_070 import synonyms as s70
    from synonyms_071 import synonyms as s71
    from synonyms_072 import synonyms as s72
    from synonyms_073 import synonyms as s73
    from synonyms_074 import synonyms as s74
    from synonyms_075 import synonyms as s75
    from synonyms_076 import synonyms as s76
    from synonyms_077 import synonyms as s77
    from synonyms_078 import synonyms as s78
    from synonyms_079 import synonyms as s79
    from synonyms_080 import synonyms as s80
    from synonyms_081 import synonyms as s81
    from synonyms_082 import synonyms as s82
    from synonyms_083 import synonyms as s83
    from synonyms_084 import synonyms as s84
    from synonyms_085 import synonyms as s85
    from synonyms_086 import synonyms as s86
    from synonyms_087 import synonyms as s87
    from synonyms_088 import synonyms as s88
    from synonyms_089 import synonyms as s89
    from synonyms_090 import synonyms as s90
    from synonyms_091 import synonyms as s91
    from synonyms_092 import synonyms as s92
    from synonyms_093 import synonyms as s93
    from synonyms_094 import synonyms as s94
    from synonyms_095 import synonyms as s95
    from synonyms_096 import synonyms as s96
    from synonyms_097 import synonyms as s97
    from synonyms_098 import synonyms as s98
    from synonyms_099 import synonyms as s99
    from synonyms_100 import synonyms as s100
    from synonyms_101 import synonyms as s101
    from synonyms_102 import synonyms as s102
    from synonyms_103 import synonyms as s103
    from synonyms_104 import synonyms as s104
    from synonyms_105 import synonyms as s105
    from synonyms_106 import synonyms as s106
    from synonyms_107 import synonyms as s107
    from synonyms_108 import synonyms as s108
    from synonyms_109 import synonyms as s109
    from synonyms_110 import synonyms as s110
    from synonyms_111 import synonyms as s111
    from synonyms_112 import synonyms as s112
    from synonyms_113 import synonyms as s113
    from synonyms_114 import synonyms as s114
    from synonyms_115 import synonyms as s115
    from synonyms_116 import synonyms as s116
    from synonyms_117 import synonyms as s117
    from synonyms_118 import synonyms as s118
    from synonyms_119 import synonyms as s119
    from synonyms_120 import synonyms as s120
    from synonyms_121 import synonyms as s121
    from synonyms_122 import synonyms as s122
    from synonyms_123 import synonyms as s123
    from synonyms_124 import synonyms as s124
    from synonyms_125 import synonyms as s125
    from synonyms_126 import synonyms as s126
    from synonyms_127 import synonyms as s127
    from synonyms_128 import synonyms as s128
    from synonyms_129 import synonyms as s129

    # Check all new files
    if word_lower in s46: return s46[word_lower]
    if word_lower in s47: return s47[word_lower]
    if word_lower in s48: return s48[word_lower]
    if word_lower in s49: return s49[word_lower]
    if word_lower in s50: return s50[word_lower]
    if word_lower in s51: return s51[word_lower]
    if word_lower in s52: return s52[word_lower]
    if word_lower in s53: return s53[word_lower]
    if word_lower in s54: return s54[word_lower]
    if word_lower in s55: return s55[word_lower]
    if word_lower in s56: return s56[word_lower]
    if word_lower in s57: return s57[word_lower]
    if word_lower in s58: return s58[word_lower]
    if word_lower in s59: return s59[word_lower]
    if word_lower in s60: return s60[word_lower]
    if word_lower in s61: return s61[word_lower]
    if word_lower in s62: return s62[word_lower]
    if word_lower in s63: return s63[word_lower]
    if word_lower in s64: return s64[word_lower]
    if word_lower in s65: return s65[word_lower]
    if word_lower in s66: return s66[word_lower]
    if word_lower in s67: return s67[word_lower]
    if word_lower in s68: return s68[word_lower]
    if word_lower in s69: return s69[word_lower]
    if word_lower in s70: return s70[word_lower]
    if word_lower in s71: return s71[word_lower]
    if word_lower in s72: return s72[word_lower]
    if word_lower in s73: return s73[word_lower]
    if word_lower in s74: return s74[word_lower]
    if word_lower in s75: return s75[word_lower]
    if word_lower in s76: return s76[word_lower]
    if word_lower in s77: return s77[word_lower]
    if word_lower in s78: return s78[word_lower]
    if word_lower in s79: return s79[word_lower]
    if word_lower in s80: return s80[word_lower]
    if word_lower in s81: return s81[word_lower]
    if word_lower in s82: return s82[word_lower]
    if word_lower in s83: return s83[word_lower]
    if word_lower in s84: return s84[word_lower]
    if word_lower in s85: return s85[word_lower]
    if word_lower in s86: return s86[word_lower]
    if word_lower in s87: return s87[word_lower]
    if word_lower in s88: return s88[word_lower]
    if word_lower in s89: return s89[word_lower]
    if word_lower in s90: return s90[word_lower]
    if word_lower in s91: return s91[word_lower]
    if word_lower in s92: return s92[word_lower]
    if word_lower in s93: return s93[word_lower]
    if word_lower in s94: return s94[word_lower]
    if word_lower in s95: return s95[word_lower]
    if word_lower in s96: return s96[word_lower]
    if word_lower in s97: return s97[word_lower]
    if word_lower in s98: return s98[word_lower]
    if word_lower in s99: return s99[word_lower]
    if word_lower in s100: return s100[word_lower]
    if word_lower in s101: return s101[word_lower]
    if word_lower in s102: return s102[word_lower]
    if word_lower in s103: return s103[word_lower]
    if word_lower in s104: return s104[word_lower]
    if word_lower in s105: return s105[word_lower]
    if word_lower in s106: return s106[word_lower]
    if word_lower in s107: return s107[word_lower]
    if word_lower in s108: return s108[word_lower]
    if word_lower in s109: return s109[word_lower]
    if word_lower in s110: return s110[word_lower]
    if word_lower in s111: return s111[word_lower]
    if word_lower in s112: return s112[word_lower]
    if word_lower in s113: return s113[word_lower]
    if word_lower in s114: return s114[word_lower]
    if word_lower in s115: return s115[word_lower]
    if word_lower in s116: return s116[word_lower]
    if word_lower in s117: return s117[word_lower]
    if word_lower in s118: return s118[word_lower]
    if word_lower in s119: return s119[word_lower]
    if word_lower in s120: return s120[word_lower]
    if word_lower in s121: return s121[word_lower]
    if word_lower in s122: return s122[word_lower]
    if word_lower in s123: return s123[word_lower]
    if word_lower in s124: return s124[word_lower]
    if word_lower in s125: return s125[word_lower]
    if word_lower in s126: return s126[word_lower]
    if word_lower in s127: return s127[word_lower]
    if word_lower in s128: return s128[word_lower]
    if word_lower in s129: return s129[word_lower]
        
    return []  # Word not found

def get_multiple_synonyms(words):
    """Get synonyms for multiple words"""
    return {word: get_synonyms(word) for word in words}

def get_stats():
    """Get database statistics"""
    return {
        'total_files': 84,
        'file_range': '46 to 129',
        'total_words': 41702,
        'words_per_file': '~500'
    }

# Test the loader
if __name__ == "__main__":
    test_words = ["happy", "sad", "beautiful", "quick", "run"]
    print("🧪 Testing loader...")
    for word in test_words:
        result = get_synonyms(word)
        if result:
            print(f"✅ '{word}': {{result[:3]}}... ({{len(result)}} synonyms)")
        else:
            print(f"❌ '{word}': Not found")

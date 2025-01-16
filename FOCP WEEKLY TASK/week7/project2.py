"""Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line"""

def combination(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    return set1, set2

def atleast_one(word1, word2):
    set1, set2 = combination(word1, word2)
    return sorted(set1 | set2)  

def appear_both(word1, word2):
    set1, set2 = combination(word1, word2)
    return sorted(set1 & set2)  

def either_word(word1, word2):
    set1, set2 = combination(word1, word2)
    return sorted(set1 ^ set2)  

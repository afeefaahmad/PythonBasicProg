def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
word1 = "listen"
word2 = "silent"

if is_anagram(word1, word2):
    print("Anagram")
    
else:
    print("Not Anagram")

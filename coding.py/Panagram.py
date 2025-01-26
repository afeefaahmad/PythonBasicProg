def is_Panagram(sentence):
    sentence_letters = set(sentence.lower())
    alphabets = set('abcdefgehijklmnopqrstuvwxyz')
    
    return alphabets.issubset(sentence_letters)
    
sentence = "The quick brown fox jumps over the lazy dog"
if is_Panagram(sentence):
    print("panagram")
else:
    print("not panagram")

"""
the pig latin translator takes a word and
if the word starts a consonant
    remove the first letter and append it to the end of the word plus the "ay" word

if the word start with a vowel it just add the "ay" word at the end of the word
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = ''
    
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:len(word)] + first + pyg
        print new_word
else:
    print 'empty']
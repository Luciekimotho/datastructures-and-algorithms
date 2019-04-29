
#Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. 
#If there is no possible reconstruction, then return null.
#For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
##Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].



def split_sent(s, dict_words):
    words = set(dict_words)
    llist = list()

    for i in range(len(s)):
        if s[0:i + 1] in words:
            llist.append(s[0:i + 1])
            words.remove(s[0:i + 1])
            llist += split_sent(s[i+1: ], words)

    return llist

dict_words = ['quick', 'brown', 'the', 'fox']
sentence = "thequickbrownfox"

print (split_sent(sentence, dict_words))




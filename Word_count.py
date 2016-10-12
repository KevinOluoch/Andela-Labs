
def words (sentence):
    """A function that takes a string as an argument, and returns a dictionary
    containing the words in the dictionary as key with the number of times they
     appear as the values.
     For example for the input "olly, olly. in come-free". it produces
     { olly: 2, in: 1, come: 1, free: 1 }
     """
    #The sentence is first split into wotds using spaces only
    words= sentence.split()
    """Then fullstops, commas and hyphens are removed from words that were next
    to them in the sentences"""
    for delimiter in [".",",","-"]:
        print words
        words = [word.split(delimiter)[0] for word in words]
        print words

    #The occurance of the words in the sentences are then counted
    dictionary_of_words = ({ word:words.count(word) for word in words if not word.isdigit()})
    #The occurance of the numbers in the sentences are then counted
    dictionary_of_words.update({ int(word):words.count(word) for word in words if word.isdigit()})

    return dictionary_of_words

D = words('''Python available 2. 2. 2-2 for 2 many many. operating 22 systems. systems,''')

print D
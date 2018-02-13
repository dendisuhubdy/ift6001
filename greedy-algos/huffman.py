import collections
import operator

def huffman(string):
    # count frequency of each letter in the string
    letters = collections.Counter(string)
    # now we use the letters and frequencies to construct
    # a binary treie

    dict_letters = {}

    for letter, frequency in letters.items():
        dict_letters[letter] = frequency

    sorted_letters = sorted(dict_letters.items(), key=operator.itemgetter(1))
    print(sorted_letters)

    # now we have an iterator
    #return encoded, num_bits

if __name__=="__main__":
    huffman("google")

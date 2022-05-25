""" Check if two words are anagrams """
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



from collections import Counter

# function to check if two strings are anagram or not
def find_anagrams(word, anagram):
    " implementing counter function "

    if Counter(word) == Counter(anagram):
        print("True")
    else:
        print("False")

find_anagrams("below", "elbow")

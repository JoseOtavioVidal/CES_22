from test_suite import *

def cleanword(s):
    """Return only the letters of the string"""
    vocabulary = "!@#$%¨&*()'""'´`^~{}[],.<>;:"
    clean = ""
    for x in vocabulary:
        if x not in s:
            clean += x
    return clean


def has_dashdash(s):
    """See is there is a dash in the string"""
    if s.count("-") > 0:
        return True
    else:
        return False


def extract_words(s):
    """Extract the words of a string"""
    return s.split()


def wordcounts(word, s):
    """Counts the word in the list"""
    return s.count(word)


def wordset(s):
    """Create the wordset to the string"""
    for i in range(s.lenght):
        if s.count(s[i]) >1:
            s.remove(s[i])
            i = 0
    return s.sort()

def longestword(s):
    """Defines the major word in te list"""
    max = 0
    for i in range(s.lenght):
        if max < s[i].lenght:
            max = s[i].lenght
    return max
def cleanword(s):
    """Return only the letters of the string"""
    vocabulary = "!-_?@#$%¨&*()''´`^~{}[],.<>;:=+"
    clean = ""
    for x in s:
        if x not in vocabulary:
            clean += x

    return clean


def has_dashdash(s):
    """See if there is a dash in the string"""
    if s.count("--") > 0:
        return True
    else:
        return False


def extract_words(s):
    """Extract the words of a string"""

    vocabulary = "!-_?@#$%¨&*()''´`^~{}[],.<>;:=+"
    clean = ""
    for x in s:
        if x not in vocabulary:
            clean += x
        else:
            clean+=" "
    clean = clean.split()
    answer = []
    for x in clean:
        answer.append(x.lower())
    return answer


def wordcount(word, s):
    """Counts the word in the list"""
    return s.count(word)


def wordset(s):
    """Create the wordset to the string"""
    word = []
    for x in (s):
        word.append(x)
        if word.count(x) > 1:
            word.remove(x)
    word.sort()
    return word

def longestword(s):
    """Defines the major word in te list"""
    max = 0
    for i in range(len(s)):
        if max < len(s[i]):
            max = len(s[i])
    return max
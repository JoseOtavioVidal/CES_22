def extract_words(s):
    """Extract the words of a string"""

    vocabulary = "!_?@#\"$%¨&*()''´`^~{}[],.<>;:=+1234567890"
    clean = ""
    for x in s:
        if x not in vocabulary:
            clean += x
        else:
            clean+=" "
    clean = clean.lower()
    clean = clean.split()
    for word in clean:
        if word.count("-")>=2:
            clean.remove(word)
            word = word.split("-")
            clean.extend(word)
    return clean


f = open("Alice", "r")
all_words = {}
while True:
    line = f.readline()
    if len(line) ==0:
        break
    split_words = extract_words(line)
    for word in split_words:
        all_words[word] = all_words.get(word, 0)+1

w = open("alice_words", "w")

keylist = []
for key in all_words.keys():
    keylist.append(key)

while keylist.count("")>0:
    keylist.remove("")

keylist.sort()
print(keylist)
w.write("Word \t\t\t\tCount \n=========================\n")
for key in keylist:
    w.write(f"{str(key):20s}{all_words[key]:5d}\n")

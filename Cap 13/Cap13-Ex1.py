f = open("file1.txt", "r")
xs = f.readlines()
f.close()

g = open("file 2.txt", "w")
for i in range(len(xs)-1, -1, -1):
    g.write(xs[i])
g.close()
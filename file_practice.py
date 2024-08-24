
f = open("poem.txt")

read = f.read()

if ("diamond" in read):
    print("diamond word present in file")
else:
    print("word not present in file")


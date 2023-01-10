fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    
    words = line.strip().split()
    #print(words)
    for word in words:
        if word not in lst:
            #continue
            lst.append(word)
lst.sort()
print(lst)
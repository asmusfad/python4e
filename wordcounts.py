name = input('Enter a file name: ')
if len(name) < 1: name = "intro.txt"
counts = {}

try:
    
    with open(file=name, mode="r", encoding="UTF-8") as fh:
        for line in fh:
            words = line.strip().split()
            for word in words:
                # if the key is not there the count is zero
                counts[word] = counts.get(word, 0) + 1
except:
    print("File cannot be opened! ")

bigcount = None
most_common_word = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        most_common_word = word
        bigcount = count

print("Most commen word in", name, "is",most_common_word, "and is in the file",bigcount,"times.")
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
d = {}

for line in handle:
    if not line.startswith("From "): continue
    words = line.strip().split()
    
    email = words[1]
    d[email] = d.get(email, 0) + 1
    

largest = -1
profilic_comitter = None
for k,v in d.items():
    if v > largest:
        largest = v
        profilic_comitter = k

print(profilic_comitter, largest)
    



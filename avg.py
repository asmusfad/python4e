# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    value = float(line[pos+1:].lstrip())
    
    count += 1
    total += value
avg = total/count

print("Average spam confidence:", avg)

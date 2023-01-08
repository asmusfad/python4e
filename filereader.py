filename = input("Enter the file name: ")
count = 0
try:
    with open(file=filename, mode="r", encoding="UTF-8") as f:
        pattern = input("Enter the pattern to search: ")
        for line in f:
            if line.startswith(pattern):
                count += 1
except:
    print("File cannot be opened:", filename)
    quit()
print("There were", count, pattern,"in", filename)

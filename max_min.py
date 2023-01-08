largest = None
smallest = None

while True:
    num = input("Enter an integer: ")
    if num == "done":
        break
    
    try:
        num = int(num)
        
        if largest is None or smallest is None:
            largest = num
            smallest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    except:
        print("Invalid input")
        
print("Maximum is", largest)
print("Minimum is", smallest)
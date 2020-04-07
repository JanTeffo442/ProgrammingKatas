def evenOrOdd():
    
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        return num, " is even"
    else:
        return num, " is odd"

print(evenOrOdd())

def rightHanded():
     
     print("Enter number of rows for the pattern: ")
     
     numOfRows = int(input())
     
     for i in range(1, numOfRows + 1):
             for j in range(i):
                    print('#', end = ' '),
             print()
rightHanded()
def isosceles():
    length = int(input())
    for i in range (1, length+1,2):
        print(length*' '+ i* '*')
        length = length - 1
isosceles()
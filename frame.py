p=input("Enter your words to insert in a frame \n")

def asterisk_frame(words):

    size = len(max(words, key=len))

    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
    
asterisk_frame(p.split(" "))
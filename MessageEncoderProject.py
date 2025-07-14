from random import randint
##At some point we should add more compications - like random placement for the key and chnage up the order of letters, numbers, etc.
def encode():
    
    letters1 = []
    numbers = []
    cipher = 0
    def letToNum(b):
        number = 0
        if b == 'a':
            number = 1
        elif b == 'b':
            number = 2
        elif b == 'c':
            number = 3
        elif b == 'd':
            number = 4
        elif b == 'e':
            number = 5
        elif b == 'f':
            number = 6
        elif b == 'g':
            number = 7
        elif b == 'h':
            number = 8
        elif b == 'i':
            number = 9
        elif b == 'j':
            number = 10
        elif b == 'k':
            number = 11
        elif b == 'l':
            number = 12
        elif b == 'm':
            number = 13
        elif b == 'n':
            number = 14
        elif b == 'o':
            number = 15
        elif b == 'p':
            number = 16
        elif b == 'q':
            number = 17
        elif b == 'r':
            number = 18
        elif b == 's':
            number = 19
        elif b == 't':
            number = 20
        elif b == 'u':
            number = 21
        elif b == 'v':
            number = 22
        elif b == 'w':
            number = 23
        elif b == 'x':
            number = 24
        elif b == 'y':
            number = 25
        elif b == 'z':
            number = 26
        elif b == '.':
            number = 27
        elif b == '!':
            number = 28
        elif b == '?':
            number = 29
        elif b == '0':
            number = 30
        elif b == '1':
            number = 31
        elif b == '2':
            number = 32
        elif b == '3':
            number = 33
        elif b == '4':
            number = 34
        elif b == '5':
            number = 35
        elif b == '6':
            number = 36
        elif b == '7':
            number = 37
        elif b == '8':
            number = 38
        elif b == '9':
            number = 39
        elif b == ':':
            number = 40
        elif b == '$':
            number = 41
        elif b == '@':
            number = 42
        elif b == '#':
            number = 43
        elif b == '%':
            number = 44
        elif b == '&':
            number = 45
        elif b == '*':
            number = 46
        elif b == '(':
            number = 47
        elif b == ')':
            number = 48
        elif b == ',':
            number = 49
        elif b == '-':
            number = 50
        elif b == '+':
            number = 51
        elif b == '/':
            number = 52
        elif b == '=':
            number = 53
        elif b == ' ':
            number = ''

        finalNumber = number + cipher
        return finalNumber

    cipher = randint(15, 150)
    #number = 0
    message = str.lower(input("What is the message?\n"))
    letters1.append(cipher)

    for x in message:
        letters1.append(x)

    for y in letters1:
        if(y != ' '):
            numbers.append(letToNum(y))

    for z in numbers:
        print(z, end=" ")
def decode(cipher):
    list2 = []
    ciphering = True
    while(ciphering):
        num = int(input("Enter the key"))
        
        standard = num - cipher
        
        if standard == 1:
            letter = 'a'
        elif standard == 2:
            letter = 'b'
        elif standard == 3:
            letter = 'c'
        elif standard == 4:
            letter = 'd'
        elif standard == 5:
            letter = 'e'
        elif standard == 6:
            letter = 'f'
        elif standard == 7:
            letter = 'g'
        elif standard == 8:
            letter = 'h'
        elif standard == 9:
            letter = 'i'
        elif standard == 10:
            letter = 'j'
        elif standard == 11:
            letter = 'k'
        elif standard == 12:
            letter = 'l'
        elif standard == 13:
            letter = 'm'
        elif standard == 14:
            letter = 'n'
        elif standard == 15:
            letter = 'o'
        elif standard == 16:
            letter = 'p'
        elif standard == 17:
            letter = 'q'
        elif standard == 18:
            letter = 'r'
        elif standard == 19:
            letter = 's'
        elif standard == 20:
            letter = 't'
        elif standard == 21:
            letter = 'u'
        elif standard == 22:
            letter = 'v'
        elif standard == 23:
            letter = 'w'
        elif standard == 24:
            letter = 'x'
        elif standard == 25:
            letter = 'y'
        elif standard == 26:
            letter = 'z'
        elif standard == 27:
            letter = '.'
        elif standard == 28:
            letter = '!'
        elif standard == 29:
            letter = '?'
        elif standard == 30:
            letter = '0'
        elif standard == 31:
            letter = '1'
        elif standard == 32:
            letter = '2'
        elif standard == 33:
            letter = '3'
        elif standard == 34:
            letter = '4'
        elif standard == 35:
            letter = '5'
        elif standard == 36:
            letter = '6'
        elif standard == 37:
            letter = '7'
        elif standard == 38:
            letter = '8'
        elif standard == 39:
            letter = '9'
        elif standard == 40:
            letter = ':'
        elif standard == 41:
            letter = '$'
        elif standard == 42:
            letter = '@'
        elif standard == 43:
            letter = '#'
        elif standard == 44:
            letter = '%'
        elif standard == 45:
            letter = '&'
        elif standard == 46:
            letter = '*'
        elif standard == 47:
            letter = '('
        elif standard == 48:
            letter = ')'
        elif standard == 49:
            letter = ','
        elif standard == 50:
            letter = '-'
        elif standard == 51:
            letter = '+'
        elif standard == 52:
            letter = '/'
        elif standard == 53:
            letter = '='
        else:
            ciphering = False
        list2.append(letter)

    for p in list2:
        print(p, end = "")

encode()
cipher = int(input("\nCipher: "))
decode(cipher)

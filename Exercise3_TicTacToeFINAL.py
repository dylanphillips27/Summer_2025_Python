Name1=input('Player 1 Name:\n')
Name2=input('Player 2 Name:\n')

TicTacToe=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("0,0  0,1  0,2\n1,0  1,1  1,2\n2,0  2,1  2,2")


for i in TicTacToe:
    print(i)


playing = True

p2 = False
p1 = False
while(playing):

    wrongEntry = True
    while wrongEntry:
        try:
            P1moveR = int(input("Player 1 move. Please enter which row (0, 1, or 2)."))
            P1moveC = int(input("Player 1 move. Please enter which collumn (0, 1, or 2)."))
            if TicTacToe[P1moveR][P1moveC]==" ":
                TicTacToe[P1moveR][P1moveC] = 'x'
                wrongEntry=False

            else:
                print("Wrong entry")
        except:
            print("Invalid Input")

    for i in TicTacToe:
            print(i)

    for x in range(0,3):
        list1 = ['x','x','x']
        if(list1 == TicTacToe[x]):
            playing = False
            p1 = True
            break

    list2 = [['x','x','x'], ['x','x','x'], ['x','x','x']]
    if((list2[0][0] == TicTacToe[0][0] and list2[1][0] == TicTacToe[1][0] and list2[2][0] == TicTacToe[2][0]) or (list2[0][1] == TicTacToe[0][1] and list2[1][1] == TicTacToe[1][1] and list2[2][1] == TicTacToe[2][1]) or (list2[0][2] == TicTacToe[0][2] and list2[1][2] == TicTacToe[1][2] and list2[2][2] == TicTacToe[2][2])):
        playing = False
        p1 = True
        break

    if((list2[0][0] == TicTacToe[0][0] and list2[1][1] == TicTacToe[1][1] and list2[2][2] == TicTacToe[2][2]) or (list2[0][2] == TicTacToe[0][2] and list2[1][1] == TicTacToe[1][1] and list2[2][0] == TicTacToe[2][0])):
        playing = False
        p1 = True
        break

    if(not(TicTacToe[0][0] == ' ' or TicTacToe[0][1] == ' ' or TicTacToe[0][2] == ' ' or TicTacToe[1][0] == ' ' or TicTacToe[1][1] == ' ' or TicTacToe[1][2] == ' ' or TicTacToe[2][0] == ' ' or TicTacToe[2][1] == ' ' or TicTacToe[2][2] == ' ')):
        playing = False
        break

    wrongEntry = True
    while wrongEntry:
        try:
            P2moveR = int(input("Player 2 move. Please enter which row (0, 1, or 2)."))
            P2moveC = int(input("Player 2 move. Please enter which collumn (0, 1, or 2)."))
            if TicTacToe[P2moveR][P2moveC]==" ":
                TicTacToe[P2moveR][P2moveC] = 'o'
                wrongEntry=False

            else:
                print("Wrong entry")
        except:
            print("Invalid Input")

    for i in TicTacToe:
        print(i)
    for x in range(0,3):
        list1 = ['o','o','o']
        if(list1 == TicTacToe[x]):
            playing = False
            p2 = True
            break

    list2 = [['o','o','o'], ['o','o','o'], ['o','o','o']]
    if((list2[0][0] == TicTacToe[0][0] and list2[1][0] == TicTacToe[1][0] and list2[2][0] == TicTacToe[2][0]) or (list2[0][1] == TicTacToe[0][1] and list2[1][1] == TicTacToe[1][1] and list2[2][1] == TicTacToe[2][1]) or (list2[0][2] == TicTacToe[0][2] and list2[1][2] == TicTacToe[1][2] and list2[2][2] == TicTacToe[2][2])):
        playing = False
        p2 = True
        break

    if((list2[0][0] == TicTacToe[0][0] and list2[1][1] == TicTacToe[1][1] and list2[2][2] == TicTacToe[2][2]) or (list2[0][2] == TicTacToe[0][2] and list2[1][1] == TicTacToe[1][1] and list2[2][0] == TicTacToe[2][0])):
        playing = False
        p2 = True
        break
        
    


if(p1):
    print(f"{Name1} Wins!")
elif(p2):
    print(f"{Name2} Wins!")
else:
    print("It's a tie.")

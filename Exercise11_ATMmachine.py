from random import randint
from datetime import datetime
from num2words import num2words
from datetime import date
#print(num2words(30))

#print(len("___________________________________________"))
currentDate = date.today()
#hour = datetime.hour()
#minute = datetime.minute()
#print(type(currentDate))
#print(currentDate)
balance=randint(100, 50000)
pinAttempt=3
Entry = False
withdraw=0
depoist=0
#name="blank"
#signature = "blank"


name = input("Please enter your name:\n")
pinNumber=input("Enter your PIN number:\n")
if pinNumber=="1234":
    Entry = True
elif pinNumber=="4321":
    print("Police have been called.")
    print("Account locked.")
else:
    pinAttempt -= 1
    print(f"Incorrect PIN. {pinAttempt} tries left.")
    pinNumber=input("Enter your PIN number\n")
    if pinNumber=="1234":
        Entry = True
    elif pinNumber=="4321":
        print("Police have been called.")
        print("Account locked.")
    else:
        pinAttempt -= 1
        print(f"Incorrect PIN. {pinAttempt} tries left.")
        pinNumber=input("Enter your PIN number\n")
        if pinNumber=="1234":
            Entry = True
        elif pinNumber=="4321":
            print("Police have been called.")
            print("Account locked.")
        else:
            pinAttempt -= 1
            print(f"Incorrect PIN. {pinAttempt} tries left.")
            print("Account locked.")



if(Entry):
    
        print("1)\tWithdraw Funds\n2)\tDeposit Funds\n3)\tFreeze account")
        print(f"Your current balance is ${balance}")
        try:
            option=int(input("Choose an operation: "))
        except:
            print("Please input 1, 2, or 3.")
            option=int(input("Choose an operation: "))
        if option==1:
            try:
                withdraw=int(input("How much money do you want to withdraw? $"))
            except:
                print("Invalid amount entered.")
            if(withdraw > balance):
                print(f"You do not have sufficent funds in your account (${balance}) to withdraw ${withdraw}.")
            elif(withdraw < 0):
                print("Invalid amount.")
            else:
                tens = withdraw // 10
                tenLeft = withdraw - (10 * tens)
                fives = tenLeft // 5
                fiveLeft = tenLeft - (5 * fives)
                ones = fiveLeft
                balance -= withdraw
                print(f"Dispensing {tens} tens, {fives} fives, and {ones} ones.")
                print(f"New balance: ${balance}")
        elif option==2:
            try:
                depoist=int(input("How much would you like to deposit? $"))
                if(depoist < 0):
                    print("Invalid amount.")

                else:
                    print("1)\tCheck\n2)\tCash")
                    try:
                        paymentType=int(input("Select payment type: "))
                    except:
                        print("Invalid Input.")
                        paymentType=int(input("Select payment type: "))
                    if paymentType==1:
                        balance +=depoist
                        signature = input("Sign here: ")
                        length = len("_____________________________________________________________________________________________________________")-2
                        finalSingnature=signature+" "*(length-12-len(signature))
                        finalName=name+" "*(length-7-len(name))
                        wordCost = num2words(depoist)
                        finalSpace=" "*(length-14-len(wordCost))
                        check = f'''

    _____________________________________________________________________________________________________________
    |                                                                                                           |
    | {currentDate}                                                                          Peter and Dylan Bank  |
    |                                                                                                           |
    | Name: {finalName}|
    | Signature: {finalSingnature}|
    |                                                                                                           |
    | Amount:                                                                                                   |
    |      {wordCost} dollars{finalSpace}|
    |___________________________________________________________________________________________________________|

    '''
                        print(check)
                        print(f"New balance: ${balance}")
                    elif (paymentType == 2):
                        print("Please insert cash")
                        balance += depoist
                        print(f"New balance: ${balance}")
                    else:
                        print("Invalid input.")
            except:
                print("Invaid amount entered.")
                
        elif option==3:
            print("Account frozen.")
        else:
            print("Invalid input. Please input 1, 2, or 3.")
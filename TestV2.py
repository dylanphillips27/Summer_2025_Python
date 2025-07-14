print("\nWelcome to the calculator")
print("What is your name?")
name = input("")
print(f"Welcome, {name}!")

calculate = True
calculations = 0
number1List = []
signList = []
number2List = []
solutionList = []


while(calculate):
    operation = str.lower(input("What operation would you like to preform? "))
    if("add" in operation):
        sign = "add"
        calculating = True
    elif("subtract" in operation):
        sign = "subtract"
        calculating = True
    elif("multipl" in operation):
        sign = "multiply"
        calculating = True
    elif("divi" in operation):
        sign = "divide"
        calculating = True
    else:
        print("Invalid input. Please choose to add, subtract, multiply, or divide.")
        calculating = False

    while(calculating):
        print("Great!")
        try:

            number1 = float(input(f"What is the first number you want to {sign}? "))
            number2 = float(input(f"What is the second number you want to {sign}? "))

            if(sign == "add"):
                math = "+"
                solution = number1 + number2
            if(sign == "subtract"):
                math = "-"
                solution = number1 - number2
            if(sign == "multiply"):
                math = "*"
                solution = number1 * number2
            if(sign == "divide"):
                math = "/"
                solution = number1 / number2

            
            if(number1 == int(number1)):
                final1 = int(number1)
            else:
                final1 = number1
            if(number2 == int(number2)):
                final2 = int(number2)
            else:
                final2 = number2
            if(solution == int(solution)):
                finalS = int(solution)
            else:
                finalS = solution

            number1List.append(final1)
            signList.append(math)
            number2List.append(final2)
            solutionList.append(finalS)

            print(f"\n{final1} {math} {final2} = {finalS}")
            print(f"Your solution is {finalS} \n")
            calculations = calculations + 1

            goAgain = str.lower(input("Do you have another calculation? "))

            if("yes" in goAgain):
                calculating = False
                calculate = True
            if("no" in goAgain):
                calculating = False
                calculate = False
                print("Thank you for using this calculator!")
                if(calculations == 1):
                    print(f"You preformed {calculations} calculation today!")
                else:
                    print(f"You performed {calculations} calculations today!")
                
                listLength = len(signList)
                partsAdded = 0
                equals = "="
                while(listLength != partsAdded):
                    print(number1List[partsAdded], signList[partsAdded], number2List[partsAdded], equals, solutionList[partsAdded])
                    partsAdded += 1


        except:
            print("The value(s) you have entered are inapplicable. \nPlease ensure you have entered a number.")
        
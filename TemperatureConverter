print("Temperature Converter")
##Add some more conversion options
options = '''
Please choose one of the following conversions:

1. Convert Kelvin to Farenheit
2. Convert Farenheit to Kelvin
3. Convert Farenheit to Celsius
4. Convert Celsius to Farenheit

'''

conversion = input(options)

good = False
#newTemp = 0

try:
    choice = int(conversion)
    if(choice <= 0 or choice > 4):
        print(f"Selection {choice} is inapplicable. \nPlease select option 1, 2, 3, or 4.")
    else:
        good = True
except:
    print(f"You have entered: {conversion}.\nPlease select option 1, 2, 3, or 4.")
    good = False

if(good):
    if(choice == 1):
        sign = "Kelvin"
        target = "Farenheit"
        init1 = "K" 
        init2 = "F"
    elif(choice == 2 or choice == 3):
        sign = "Farenheit"
        init1 = "F"
        if(choice == 2):
            target = "Kelvin" 
            init2 = "K"
        else:
            target = "Celsius"
            init2 = "C"
    elif(choice == 4):
        sign = "Celsius"
        target = "Farenheit"
        init1 = "C"
        init2 = "F"
    else:
        print("Error")

    initialTemp = input(f"What is the temperature in {sign}? ")

    try:
        startTemp = float(initialTemp)
        ok = True
    except:
        print(f"You have entered: '{initialTemp}'. This is not a valid imput. \nPlease ensure your input is a number")
        ok = False
    
    if(ok):
        if(choice == 1):
            newTemp = 1.8 * (startTemp - 273.15) + 32
        elif(choice == 2):
            newTemp = ((startTemp - 32) / 1.8) + 273.15
        elif(choice == 3):
            newTemp = (startTemp - 32) / (1.8)
        elif(choice == 4):
            newTemp = startTemp * (1.8) + 32
        else:
            print("Error")

        finalTemp = round(newTemp, 3)

        #finish bottom 4 minimums for F and C
        if(target == "Kelvin" and finalTemp < 0):
            print(f"{startTemp} degrees in Farenheit is not a valid temperature in Kalvin ({finalTemp} degree output). \nPlease try again.")
        elif(sign == "Kelvin" and startTemp < 0):
            print(f"{startTemp} is not an applicable Kelvin temperature.")
        elif(target == "Farenheit" and finalTemp < -459.67):
            print(f"{startTemp} degrees in Farenheit is not a valid temperature in Kalvin ({finalTemp} degree output). \nPlease try again.")
        elif(sign == "Farenheit" and startTemp < -459.67):
            print(f"{startTemp} is not an applicable Kelvin temperature.")
        elif(target == "Celsius" and finalTemp < -273.15):
            print(f"{startTemp} degrees in Farenheit is not a valid temperature in Kalvin ({finalTemp} degree output). \nPlease try again.")
        elif(sign == "Celsius" and startTemp < -273.15):
            print(f"{startTemp} is not an applicable Kelvin temperature.")
        else:
            print(f"{startTemp}˚{init1} is {finalTemp}˚{init2} ")
        

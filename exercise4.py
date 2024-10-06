#Exercise 4
import random

randomNum = random.randrange(1,10,1)
i = 0;
inputNum = 0
while randomNum != inputNum:
    inputNum = int(input("Please enter a number from 1 to 10: "))
    if(inputNum < 1 or inputNum > 10):
        print("Sorry the number is not valid. Please try again ")  
    else:
        i = i+1
        if(randomNum > inputNum):
            print("Too low")
        else:
            print("Too high")
        print("Try again")

print("Well done. The number was " + str(randomNum) + ". Your number of attempts was " + str(i))

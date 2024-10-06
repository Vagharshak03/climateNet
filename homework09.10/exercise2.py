#Exercise 2

while True:
    num = int(input("Please enter a positve number: "))
    if(num < 0):    
        print("The number is not positive. Please try again!")
    elif(num == 0):
        break
    else:        
        if(num % 2 == 0):
            print(str(num) + ' is even')
        else:
            print(str(num) + ' is odd')
        break
print('The End')

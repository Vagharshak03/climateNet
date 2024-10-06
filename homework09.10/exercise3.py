#Exercise 3


oprs = ['+', '-', '*', '/'] 
inputOpr = 0
result = 0
while inputOpr not in oprs : 
    inputOpr = str(input("Please choose one of these operators (+,-,*,/): "))
val1 = int(input("Now please enter your first number: "))
val2 = int(input("Now please enter your second number: "))
if(val1 == 5 or val2 == 5):
    exit()    
elif(val2 == 0 and inputOpr == '/'):
    print("Oops. Something went wrong...")
else: 
    match inputOpr:
        case '*':
            result = val1 * val2
        case '/':
            result = val1 / val2
        case '+':
            result = val1 + val2
        case '-':
            result = val1 - val2
    print(str(val1) + ' ' + str(inputOpr) + ' ' + str(val2) + ' = ' + str(result))



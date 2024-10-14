#Exercise 5


while True:
    input_num = int(input("Enter a number non negative and with two or more digits: "))  
    if(int(input_num / 10) == 0):
        print("Your number is " + str(input_num) + ". Please enter a number more than 10.(Example: XX)")
    elif(input_num < 0):
        print("Your number is not positive. Try again! ")
    else:
        result = 0 
        while input_num > 0:
            result += input_num % 10
            input_num //= 10
        print("The sum of digits: " + str(result))

                        

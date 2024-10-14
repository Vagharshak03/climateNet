#Exercise 2


while True:
    input_num = int(input("Please input a positive number: "))
    if(input_num < 0):
        print("The number is not positive. Try again")
    else:
        i = 2
        prime = True
        if(input_num == 0 or input_num == 1):
            prime = False
            print("The number is not prime.")
        while i < input_num:
            if(input_num % i == 0):
                prime = False
                if(prime == False):
                    print("The number is not prime.")
                break
            i += 1
        if(prime == True):
            print("Thr number is prime.")








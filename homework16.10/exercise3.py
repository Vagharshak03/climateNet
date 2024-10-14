#Exercise 3

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


while True:
    num = int(input("Enter non positive number: "))
    if(num < 0):
        print("The number is not positive. Please try again!")
    else:
        print(Fibonacci(num))


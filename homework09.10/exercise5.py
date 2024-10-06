while True:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            break

result = 1
for i in range(1, num + 1):
    result *= i

print("The factorial of " + str(num) + " is " + str(result))

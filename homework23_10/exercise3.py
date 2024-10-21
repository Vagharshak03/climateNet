# Exercise 3

import math
#first solution

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

list1 = []
list2 = []

for i in range(1, num1+1):
    if(num1 % i == 0):
        list1.append(i)
        

for j in range(1, num2+1):
    if(num2 % j == 0):
        list2.append(j)
        
result = 1
for a in list1:
    for b in list2:
        if(a == b):
            result *= a # or b
            
            
print("The GCD of these two numbers: ", result)

#second solution

number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))

gcd = math.gcd(number1, number2)

print("GCD:", gcd)


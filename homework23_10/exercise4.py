# Exercise 4


num = int(input("enter your number: "))
input_num = num

lst = []
while num > 0:
      lst.append(int(num % 10))
      num //= 10

print("The elms of digits: ", lst)
    
result = 0
for elm in lst:
    result += elm ** len(lst)
print(result, input_num)

if(result == input_num):
    print("Your number is Armstrong number")
else:
    print("Your number is not Armstrong number")

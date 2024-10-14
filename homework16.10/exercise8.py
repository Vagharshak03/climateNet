#Exercise 8

count = int(input("Please eneter the length of list: "))
result = 0
lst = []
while count > 0:
    input_int = int(input("Please enter a number to add to the list: "))
    result += input_int
    lst.append(input_int)
    count -=1

print("The list: " + str(lst))
print("The sum of list items: " + str(result))


         

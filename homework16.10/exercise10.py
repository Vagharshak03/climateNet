#Exercise10.py

count = int(input("Please eneter the length of list: "))
lst = []
while count > 0:
    input_int = int(input("Please enter a number to add to the list: "))
    lst.append(input_int)
    count -=1


print("The list you input: " + str(lst))

for element in lst:
    if(lst.count(element) > 1):
        lst.remove(element)

print("The final list (with unique members): " + str(lst))

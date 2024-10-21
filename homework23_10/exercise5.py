#Exercise 5
print("If want to EXIT type 'exit'")
lst = []

while True:
    num = input("Please input a number: ")
    if(num == 'exit'):
        break
    
    lst.append(int(num))
print(lst)
lst.sort(reverse = True)
print(lst, lst[1])

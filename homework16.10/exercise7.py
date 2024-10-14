#Exercise 7

lst = []
while True:
    print("Description: if you want to exit: type 'exit'.")
    input_element = input("Please insert item for list: ")
    if(input_element == "exit"):
        break
    lst.append(input_element)

print("Your List: " + str(lst))
print("The length of list: " + str(len(lst)))




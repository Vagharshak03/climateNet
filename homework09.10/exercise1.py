#Exercise 1

result = 0
while True:
    print("Please select 1 if you want to continue")
    print("Please select 2 if you want to stop")
    sel = int(input("Now input your choise and press enter: "))
    if(sel == 1):
        nextVal = int(input("Input number: "))
        result = result + nextVal
    elif(sel == 2):
        break
    else:
        print("Error: Please select 1) or 2)")
print(result)


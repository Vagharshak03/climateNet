#Exercise 1


max_num = 0
tmp_num = 0
i = 0
while i < 3:
    i=i+1
    my_num = int(input("Input number: "))
    print(my_num, max_num)
    if(my_num > max_num):
        max_num = my_num
print("Max number: ", max_num)


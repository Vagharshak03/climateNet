#Exercise 2

vowels = "auioeAUIOE"
while True:
    count = 0
    txt = input("Please print a text: ")
    for char in txt:
        if(char in vowels):
          count +=1
    print("Number of vowels in text: ", count) 


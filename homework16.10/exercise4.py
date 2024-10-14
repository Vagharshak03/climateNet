#Exercise 4

input_text = str(input("Please input a text: "))

vowels = ['a', 'e', 'i', 'o', 'u']
result = 0
for char in input_text:
    if(char in vowels):
        result += 1

print("The amount of vowels in string: " + str(result))

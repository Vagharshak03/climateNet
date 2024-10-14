#Exercise 1


input_text=input("Please input a text: ")

text_length=len(input_text)

final_text=""

while text_length > 0:
    final_text += input_text[text_length-1]
    text_length -= 1
        
print(final_text)

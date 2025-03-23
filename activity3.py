from num2words import num2words

while True:  
    user_input = input("Enter the number you want to transfer in word: ")

    if user_input.isdigit():  
        num = int(user_input)
        word_output = num2words(num)
        print("The number you input is:", word_output)
        break
    else:
        print("Your input is not a number. Please try again and enter a valid number. THANK YOU! :)  :")

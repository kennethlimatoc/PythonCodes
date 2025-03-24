#String1
"""     
Using Input

Here's the sample:
print('Enter your name:')
x = input()
print('Hello, ' + x)

Create a program that asks for the user’s name and age, then prints a formatted greeting message.  

Ask the user to enter their name.
Ask the user to enter their age.
Display a message using string formatting.

Output:
Enter your name: Alex  
Enter your age: 25  
Hello, Alex! You are 25 years old.  
     """

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! You are {age} years old.")

#String2
""" 
Create a program that takes two numbers from the user, adds them, and displays the result using string formatting.  

Ask the user to enter two numbers.
Convert them to integers.
Calculate the sum.
Display the result using string formatting.

Output:
Enter first number: 8  
Enter second number: 12  
The sum of 8 and 12 is 20. """

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"\nYou entered {num1} and {num2}.")

sum_result = num1 + num2

print(f"\nThe sum of {num1} and {num2} is {sum_result}.")

#String3
"""
Ask the user about their favorite things and display a formatted sentence.  

Ask the user for their favorite color, food, and hobby.
Display a sentence using string formatting.

Output:
Enter your favorite color: Blue  
Enter your favorite food: Pizza  
Enter your favorite hobby: Reading  
You love Blue, enjoy eating Pizza, and have fun with Reading!  """

color = (input("Enter your favorite color: "))
food = (input("Enter your favorite food: "))
hobby = (input("Enter your favorite hobby: "))

print("\n")
print(f"You love {color}, enjoy eating {food}, and have fun with {hobby}!")
print("\n")

#String4
"""
Ask the user for an item name, quantity, and price, then display a formatted receipt.  
Ask the user for an item name.
Ask for the quantity.
Ask for the price per item.
Calculate the total cost.
Display the receipt using string formatting.

Output:
Enter item name: Notebook  
Enter quantity: 3  
Enter price per item: 2.50  
You bought 3 Notebook(s) at $2.50 each.  
Total cost: $7.50  
     """
item = input(("Enter the item name: "))
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total_cost = quantity * price

print("\n")
print(f"You bought {quantity} {item}(s) at ${price:.2f} each.")
print(f"Total cost: ${total_cost:.2f}")
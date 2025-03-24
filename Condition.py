
#FIRST CONDITION
'''
1. Ask the user for their exam score (out of 100)
2. Use if-elif-else to assign a grade:
90-100 → "A"
80-89 → "B"
70-79 → "C"
60-69 → "D"
Below 60 → "F"
3. Display the grade. 

Output:
Enter your exam score: 85  
Your grade is: B  '''

grade = input("Enter your grade:")


if int(grade) >= 90 and int(grade) <= 100:
    Score = "A"
elif int(grade)>=80 and int(grade) <=89:
    Score = "B"
elif int(grade)>=70 and int(grade) <=79:
    Score = "C"
elif int(grade)>=60 and int(grade) <=69:
    Score = "D"
elif int(grade)<60 :
    Score = "F"
    
print(f"Your grade is: {Score}")

#SECOND CONDITION
'''
Ask the user for two numbers and determine which is greater or if they are equal.  

1. Get two numbers from the user.
2. Compare them using if-elif-else.
3. Display which number is larger or if they are equal.

Output:
Enter first number: 10  
Enter second number: 15  
15 is greater than 10.
'''
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if int(num1) > int(num2):
    print(f"{num1} is greater than {num2}.")
elif int (num2) > int (num1):
    print(f"{num2} is greater than {num1}.")
else:
    print("Your First number and Second number are equal.")
    
#THIRD CONDITION
'''
Ask the user for a number and determine if it is positive, negative, or zero.  

1. Get a number from the user.
2. Use if-elif-else to check:
-Positive if greater than 0
-Negative if less than 0
-Zero otherwise
3. Display the result.
'''
number = input("Enter Your Number: ")

if int(number) > 0:
    print(f"Your number {number} is Positvie")
elif int(number) < 0:
     print(f"Your number {number} is Negative")
else:
     print(f"Your number {number} is Zero")
    


#FOURTH CONDITION
'''
Ask the user for a year and determine if it is a leap year.

1. Get the year from the user.
2. A year is a leap year if:
- It is divisible by 4 and
- Not divisible by 100 unless also divisible by 400
3. Display whether it's a leap year or not.

Output:
Enter a year: 2024  
2024 is a leap year!
'''

year = input("Enter a year: ")


if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")



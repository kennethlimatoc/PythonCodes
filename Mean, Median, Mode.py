from statistics import mean, median, mode, multimode

def calculate_statistics():
    try:
        userinput = input("Enter the list of element it is seperated with comma example 1,2,3,4,5,6,:  ")
        givendata = [float(num.strip()) for num in userinput.split(',') if num.strip()]
        
        if not givendata:
            print("No valid numbers were entered. Please try again.")
            return
        
        average = mean(givendata)
        middle= median(givendata)
        modes = multimode(givendata)
        

        print("\nStatistics")
        print("===========")
        print(f"This is the Mean: {average}")
        print("===========")
        print(f" This is the Median: {middle}")
        print("===========")
        print(f" This the Mode: {', '.join(map(str, modes))} (Multiple modes if applicable)")
    except ValueError:
        print("this is not a number please enter the number you waant to calculate.")
calculate_statistics()

import statistics
import numpy as np

def compute_statistics(numbers):
    if not numbers:
        print("No valid numbers provided. Please try again.")
        return
    
    data_range = max(numbers) - min(numbers)
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)
    
    print("\nComputed Statistics'")
    print(f"Range: {data_range}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    
    np_range = np.ptp(numbers) 
    np_variance = np.var(numbers, ddof=1)  
    np_std_dev = np.std(numbers, ddof=1)
    
    print("\nValidation in NumPy")
    print(f"Range in Numpy: {np_range}")
    print(f"Variance in Numpy: {np_variance}")
    print(f"Standard Deviation in numply: {np_std_dev}")

def main():
    user_input = input("Enter numbers that you want to calcute and it is seperated with comma (for example : 1,2,3,4,5,6) : ")
    try:
        numbers = [float(num.strip()) for num in user_input.split(',') if num.strip()]
    except ValueError:
        print("Sorry this is not a number, Please try again and input a number that you want to calculate THANK YOU!.")
        return
    
    compute_statistics(numbers)

main()

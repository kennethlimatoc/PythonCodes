import numpy as np

def Zna_Score(data):
    mean = np.mean(data)
    standev = np.std(data)
    
    z_scores = {x: (x - mean) / standev for x in data}
    
    outliers = [x for x, z in z_scores.items() if abs(z) > 2.5]

    
    return z_scores, outliers 

def UserInput():
    while True:
        try:
            data = list(map(float, input("Please enter numbers separated by commas (for example : 1,2,3,4,5,6): ").split(',')))
            if not data:
                raise ValueError("Empty input is not allowed.")
            return data
        except ValueError:
            print("This is not a valid number. Please try again and enter a valid data list. Thank you! :)")

user_data = UserInput()
print("User entered data:", user_data)

z_scores, outliers = Zna_Score(user_data)

print("\nThe Z-scores are:")
for x, z in z_scores.items():
    print(f"{x}: {z:.3f}")

print("\nOutliers:", outliers if outliers else "There are no outliers found. :)")

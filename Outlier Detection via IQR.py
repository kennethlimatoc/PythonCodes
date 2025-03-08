import numpy as np
# function for Outliers
def Detect_OutliersIQR(data, multiplier=1.5):

    #this is for calculate the Q1, Q3 and IQR
    Q1 = np.percentile(data, 25)  
    Q3 = np.percentile(data, 75)
    # formula for IQR
    IQR = Q3 - Q1  

    # calculate the fences the lower and upper
    lowerFence = Q1 - multiplier * IQR
    upperFence = Q3 + multiplier * IQR 

    # For outliers 
    outliers = [x for x in data if x < lowerFence or x > upperFence]
    clean_data = [x for x in data if x >= lowerFence and x <= upperFence]

    return outliers, clean_data  

# the user is inputing a data 
data_input = input("Enter a list of numbers separated by spaces (for example 2 3 5 7 9 10 12 100 101): ")
data = list(map(float, data_input.split()))

multiplier = 1.5

# for decting the outliers 
outliers, clean_data = Detect_OutliersIQR(data, multiplier) 

print("\nOutliers:", outliers)
print("Clean dataset:", clean_data)
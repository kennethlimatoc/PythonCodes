import numpy as np
import matplotlib.pyplot as plt

def theData(arr):
    while True:
        try:
            data = list(map(float, input(arr).split(',')))
            return np.array(data)
        except ValueError:
           print(" Retry your input.Please enter numbers separated by commas. Example: 10, 20, 30, 40, 50")
           

print("Enter numerical values separated by commas for each dataset. Example: 10, 20, 30, 40, 50")
data1 = theData("Data 1: ")
data2 = theData("Data 2: ")

#box plot
plt.figure(figsize=(8, 6))
plt.boxplot([data1, data2], labels=['Data 1', 'Data 2'])

# for quartiles and IQR
Q1_1 = np.percentile(data1, 25)
Q2_1 = np.median(data1)
Q3_1 = np.percentile(data1, 75)
IQR_1 = Q3_1 - Q1_1

#This is for Data 2 
Q1_2 = np.percentile(data2, 25)
Q2_2 = np.median(data2)
Q3_2 = np.percentile(data2, 75)
IQR_2 = Q3_2 - Q1_2

#outlier thresholds
lower_bound_1 = Q1_1 - 1.5 * IQR_1
upper_bound_1 = Q3_1 + 1.5 * IQR_1
lower_bound_2 = Q1_2 - 1.5 * IQR_2
upper_bound_2 = Q3_2 + 1.5 * IQR_2

#outliers
outliers_1 = [x for x in data1 if x < lower_bound_1 or x > upper_bound_1]
outliers_2 = [x for x in data2 if x < lower_bound_2 or x > upper_bound_2]

#Annotate median values
plt.text(1, Q2_1, f'Median: {Q2_1:.1f}', horizontalalignment='right', verticalalignment='bottom', fontsize=10, color='blue')
plt.text(2, Q2_2, f'Median: {Q2_2:.1f}', horizontalalignment='right', verticalalignment='bottom', fontsize=10, color='blue')

# Annotate outliers
for outlier in outliers_1:
    plt.text(1, outlier, f'{outlier:.1f}', horizontalalignment='right', fontsize=8, color='red')
for outlier in outliers_2:
    plt.text(2, outlier, f'{outlier:.1f}', horizontalalignment='right', fontsize=8, color='red')

plt.title('Box Plot of Two Datasets')
plt.ylabel('Values')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


#Explanation:
#The box plot can shows median (Q2), quartiles (Q1 and Q3), and whiskers.
#An outlier is at least 1.5 x IQR higher than Q3 or lower than Q1.
#Another indicator of skewness is whether the median is centered within the box.
#The difference in distributions can also be visually analyzed through a side-by-side comparison of both the datasets.
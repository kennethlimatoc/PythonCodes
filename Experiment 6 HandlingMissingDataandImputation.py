import numpy as np
import pandas as pd


user_input = input("Enter a list of numbers with missing values ( for exampele : 12, 15, None, 20, np.nan, 22, 25) :\n")
data = eval(user_input)  


arr = np.array([np.nan if x is None else x for x in data], dtype=np.float64)


missing = np.isnan(arr).sum()
print(f"\nMissing values before: {missing}")


print("\nChoose an imputation method:")
print("1 - Fixed value (0)")
print("2 - Mean of non-missing values")
print("3 - Forward fill")
print("4 - Backward fill")

choice = input("Enter choice: ")

if choice == "1":
    Impdata = np.nan_to_num(arr, nan=0)
elif choice == "2":
    impdata = np.where(np.isnan(arr), np.nanmean(arr), arr)
elif choice == "3":
    impdata = pd.Series(arr).fillna(method='ffill').to_numpy()
elif choice == "4":
    impdata = pd.Series(arr).fillna(method='bfill').to_numpy()
else:
    print("Invalid choice. No imputation applied.")
    impdata = arr


print("\nImputed Data:\n", impdata)

origMean = np.nanmean(arr)
newMean = np.mean(impdata)

print(f"\nMean before: {origMean:.2f}")
print(f"Mean after: {newMean:.2f}")

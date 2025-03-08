import pandas as pd
import numpy as np

def get_user_input():
    data = []
    print("\n===== Enter Data =====")

    # Ask for the number of entries
    while True:
        try:
            num_entries = int(input("How many data entries do you want to input? "))
            if num_entries > 0:
                break
            print("⚠️ Please enter a positive number.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number.")

    # Ask for column names
    while True:
        columns = input("Enter column names (comma-separated): ").split(",")
        columns = [col.strip() for col in columns if col.strip()]  # Remove empty names
        if columns:
            break
        print("⚠️ Please enter at least one column.")

    # Collect data row by row
    for i in range(num_entries):
        while True:
            print(f"\nEnter values for entry {i+1}:")
            row = input(f"Enter {len(columns)} values separated by commas ({', '.join(columns)}): ").split(",")
            row = [value.strip() for value in row]

            if len(row) == len(columns):
                data.append(row)
                break
            print(f"⚠️ Please enter exactly {len(columns)} values.")

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    return df

def analyze_data(df):
    print("\n===== Data Analysis Report =====\n")
    
    # Process each column
    for column in df.columns:
        print(f"🔹 **Analyzing column:** {column}")

        # Try to convert the column to numeric; if not possible, it's categorical
        try:
            df[column] = pd.to_numeric(df[column])
            is_numeric = True
        except ValueError:
            is_numeric = False

        if is_numeric:
            # Convert column to numeric and drop missing values
            numeric_data = df[column].dropna()

            if numeric_data.empty:
                print("   No numeric data available in this column.")
                continue

            # Compute statistics
            mean_value = numeric_data.mean()
            median_value = numeric_data.median()
            std_dev = numeric_data.std()
            variance_value = numeric_data.var()

            # Outlier Detection using IQR
            Q1 = numeric_data.quantile(0.25)
            Q3 = numeric_data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = numeric_data[(numeric_data < lower_bound) | (numeric_data > upper_bound)].tolist()

            # Display results
            print(f"  -  Mean: {mean_value:.2f}")
            print(f"  -  Median: {median_value:.2f}")
            print(f"  -  Standard Deviation: {std_dev:.2f}")
            print(f"  -  Variance: {variance_value:.2f}")
            print(f"  -  Outliers: {outliers if outliers else 'None'}\n")

        else:
            # Drop missing values
            non_numeric_data = df[column].dropna()

            if non_numeric_data.empty:
                print("   No non-numeric data available in this column.")
                continue

            # Compute mode and value counts
            mode_value = non_numeric_data.mode().iloc[0] if not non_numeric_data.mode().empty else "No mode"
            value_counts = non_numeric_data.value_counts()

            # Display results
            print(f"  - Mode: {mode_value}")
            print("  -  Value Counts:")
            for value, count in value_counts.items():
                print(f"    • {value}: {count}")
            print()

# Run the program
df = get_user_input()
analyze_data(df)

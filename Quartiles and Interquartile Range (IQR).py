def median(data):
    #Ito ay para sa computation ng median
    n = len(data)
    data.sort()
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1]+ data[mid]) / 2 
    else:
        return data[mid]
    
def compute_quartiles(data):
     #this is for computation of Q1,Q2,Q3 and IQR
    data.sort()
    n = len(data)
     
     #for median
    Q2 = median(data)
    
    if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
    else:
        lower_half = data[:n // 2]
        upper_half = data[n // 2 + 1:]
    
    # Compute Q1 and Q3
    Q1 = median(lower_half)
    Q3 = median(upper_half)
    
    # Compute IQR
    IQR = Q3 - Q1
    
    # Print results
    print(f"Q1: {Q1}")
    print(f"Q2 (Median): {Q2}")
    print(f"Q3: {Q3}")
    print(f"IQR: {IQR}")
    
    return Q1, Q2, Q3, IQR


data = list(map(float, input("Enter the your data set (example 1 2 3 4 5 6 7 8 ) it seperate by space : ").split()))
compute_quartiles(data)
  
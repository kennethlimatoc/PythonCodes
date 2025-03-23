import numpy as np
import scipy.stats as statistics
import matplotlib.pyplot as diag
import pandas as pd 

def Report (data, SaveFile = False):
    #for computation
    mean = np.mean (data)
    mid = np.median(data)
    mode = statistics.mode(data, keepdims = True)[0][0]
    range = np.ptp(data)
    var = np.var(data, ddof=1)
    dev = np.sqrt(var)
    Q1 = np.percentile(data,25)
    Q3 = np.percentile(data,75)
    IQR = Q3 - Q1
    
    #for Outlier 
    lowB = Q1 - 1.5 * IQR
    upB = Q3 + 1.5 * IQR
    Outliers = [x for x in data if x < lowB or x > upB]
    
    #The report
    Report = f"""
    -Statistic Report-
    The Mean : {mean: .2f}
    The Median : {mid: .2f}
    The Mode :{mode: .2f}
    The Range : {range: .2f}
    The Standard Deviation {dev: .2f}
    The Q1 : {Q1: .2f}
    The Q3 : {Q3: .2f}
    The IQR : {IQR: .2f}
    The Outliers : {Outliers if Outliers else 'None'}

    -Action:-
     {'Checking if the Outlier need to be Removed: ' + str(Outliers) if Outliers else 'No changes required.There is no Outliers found.'}
     """
    
    print(Report)
    
    if SaveFile:
        with open ("The_Statistics_report.txt","w") as file:
            file.write(Report)
            
    #For Plot Box
    diag.figure(figsize = (12,10))
    diag.boxplot(data, vert=False, patch_artist=True)
    diag.title("THE STATISTIC VISUALATION")
    diag.xlabel("Values")
    diag.grid(True)
    diag.show()
    
#for random set size of 30-50
data = np.random.randint(10, 100, size=40)
Report(data, SaveFile=True)

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def dataset(size=30):
    """Generate a random dataset with normal distribution"""
    return np.random.normal(loc=np.random.randint(30, 70), 
                          scale=np.random.randint(5, 20), 
                          size=size)

def statistic(data):
    """Calculate required statistics for a dataset"""
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data, keepdims=True)[0][0],
        'variance': np.var(data, ddof=1),
        'std_dev': np.std(data, ddof=1),
        'range': np.ptp(data)
    }

def compareStat(stats1, stats2):
    """Generate comparison report between two datasets"""
    report = "\nStatistical Comparison:\n" + "="*40 + "\n"
    
    # Mean comparison
    report += f"Mean:\n- Dataset 1: {stats1['mean']:.2f}\n- Dataset 2: {stats2['mean']:.2f}\n"
    report += f"Conclusion: Dataset {1 if stats1['mean'] > stats2['mean'] else 2} has higher mean\n\n"
    
    # Spread comparison using the standard deviation
    report += f"Spread (Standard Deviation):\n- Dataset 1: {stats1['std_dev']:.2f}\n- Dataset 2: {stats2['std_dev']:.2f}\n"
    report += f"Conclusion: Dataset {1 if stats1['std_dev'] > stats2['std_dev'] else 2} is more spread out\n\n"
    
    # comparison table
    report += "Detailed Statistics:\n" + "-"*40 + "\n"
    report += "{:<10} {:<10} {:<10}\n".format("Metric", "Dataset 1", "Dataset 2")
    for metric in ['mean', 'median', 'mode', 'variance', 'std_dev', 'range']:
        report += "{:<10} {:<10.2f} {:<10.2f}\n".format(
            metric.capitalize(), 
            stats1[metric], 
            stats2[metric]
        )
    return report

def plotBox_compare(data1, data2):
    """ side-by-side box plots and histograms"""
    plt.figure(figsize=(12, 5))
    
    # This is Box plot
    plt.subplot(1, 2, 1)
    plt.boxplot([data1, data2], labels=['Dataset 1', 'Dataset 2'])
    plt.title("Box Plot Comparison")
    
    #This is Histograms
    plt.subplot(1, 2, 2)
    plt.hist(data1, alpha=0.5, label='Dataset 1')
    plt.hist(data2, alpha=0.5, label='Dataset 2')
    plt.title("Histogram Comparison")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

#  two random datasets
np.random.seed(42)  
data1 = dataset()
data2 = dataset()

# for calculation of statistics
stats1 = statistic(data1)
stats2 = statistic(data2)

# print output
print(compareStat(stats1, stats2))

# Visualize comparisons
plotBox_compare(data1, data2)


#Summary of Findings:
#The mean of a particular dataset indicates a stronger central tendency.
# Diamond diagram: The dataset with the greater standard deviation is more dispersed.
# Box plots are used for visual comparison of data, emphasizing the median and outliers.
# The histograms represent frequency distribution which allows us to better compare shapes and spread.
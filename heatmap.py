import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\Total.csv')

# Convert selected columns to numeric (errors='coerce' will convert non-numeric to NaN)
cols = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# Plotting heatmap
plt.figure(figsize=(8,6))
corr_matrix = df[cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
plt.xticks(rotation=0)
plt.title('Correlation Heatmap',fontsize=13)
plt.show()

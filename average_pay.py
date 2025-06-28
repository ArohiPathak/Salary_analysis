import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\Total.csv')

# Convert pay-related columns to numeric, coercing errors to NaN
pay_columns = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits']
df[pay_columns] = df[pay_columns].apply(pd.to_numeric, errors='coerce')

# Group by year and calculate average pay metrics
pay_trends = df.groupby('Year')[['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']].mean()

# Plot the pay trends
plt.figure(figsize=(12, 6))
for column in ['BasePay', 'OvertimePay', 'OtherPay', 'TotalPay', 'TotalPayBenefits']:
    plt.plot(pay_trends.index, pay_trends[column], label=column)

plt.title('Average Pay Trends Over the Years',fontsize=13)
plt.xlabel('Year',fontsize=11)
plt.ylabel('Average Amount ($)',fontsize=11)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

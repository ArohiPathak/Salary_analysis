# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\Total.csv')

# Count the number of employees per job title
top_job_titles = df['JobTitle'].value_counts().head(10)

# Plot the job title counts
plt.figure(figsize=(10, 6))
top_job_titles.plot(kind='bar', color='purple')
plt.xlabel('Title', fontsize=11)
plt.ylabel('Number of Employees', fontsize=11)
plt.title('Top 10 Job Titles',fontsize=13)
plt.xticks(rotation=25, ha='right')
plt.show()





# importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Load data
df = pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\Total.csv')

# List of columns to convert
numeric_cols = ['OvertimePay', 'OtherPay', 'Benefits', 'TotalPay']
for col in ['OvertimePay', 'OtherPay', 'Benefits', 'TotalPay']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values in important columns
df = df.dropna(subset=['OvertimePay', 'OtherPay', 'Benefits', 'Year', 'TotalPay'])

X = df[['OvertimePay', 'OtherPay', 'Benefits', 'Year']]
y = df['TotalPay']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=11, test_size=0.2)

# applying various algorithms 
lr1 = LinearRegression()
lr1.fit(X_train, y_train)
y_pred1 = lr1.predict(X_test)
lr1_acc = r2_score(y_test, y_pred1) * 100
print(f"Linear Regression R²: {lr1_acc:.2f}%")

lr2 = RandomForestRegressor()
lr2.fit(X_train, y_train)
y_pred2 = lr2.predict(X_test)
lr2_acc = r2_score(y_test, y_pred2) * 100
print(f"Random Forest Regressor R²: {lr2_acc:.2f}%")

lr4 = GradientBoostingRegressor()
lr4.fit(X_train, y_train)
y_pred4 = lr4.predict(X_test)
lr4_acc = r2_score(y_test, y_pred4) * 100
print(f"Gradient Boosting Regressor R²: {lr4_acc:.2f}%")

lr6 = DecisionTreeRegressor()
lr6.fit(X_train, y_train)
y_pred6 = lr6.predict(X_test)
lr6_acc = r2_score(y_test, y_pred6) * 100
print(f"Decision Tree Regressor R²: {lr6_acc:.2f}%")



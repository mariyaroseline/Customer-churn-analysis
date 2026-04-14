import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"data\Telco-Customer-Churn.csv")

#Churn Distribution

plt.figure()
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.savefig("notebooks/churn_distribution.png")
plt.show()

# Data Cleaning for EDA

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

#Correlation

corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("notebooks/correlation.png")
plt.show()

#Visualization
# Contract vs Monthly Charges

plt.figure()
sns.barplot(x='Contract', y='MonthlyCharges', data=df)
plt.title("Contract vs Monthly Charges")
plt.xticks(rotation=30)
plt.savefig("notebooks/contract_vs_charges.png")
plt.show()

# Internet Service vs Churn
plt.figure()
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title("Internet Service vs Churn")
plt.xticks(rotation=30)
plt.savefig("notebooks/internet_vs_churn.png")
plt.show()
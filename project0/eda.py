import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from Python files
from customers_data import customer_data
from transaction_data import transaction_data

# Convert JSON data to DataFrame
df_customers = pd.DataFrame(customer_data)
df_transactions = pd.DataFrame(transaction_data)

# Set Seaborn style
sns.set(style="whitegrid")

# 1. **Understanding the Structure of the Data**

print("Customers Data Overview:")
print(df_customers.info())
print(df_customers.head())

print("\nTransactions Data Overview:")
print(df_transactions.info())
print(df_transactions.head())

# 2. **Descriptive Statistics**

print("\nCustomers Data Description:")
print(df_customers.describe(include='all'))

print("\nTransactions Data Description:")
print(df_transactions.describe(include='all'))

# 3. **Handling Missing Values**

print("\nMissing Values in Customers Data:")
print(df_customers.isnull().sum())

print("\nMissing Values in Transactions Data:")
print(df_transactions.isnull().sum())

# Visualize missing data for `Customers`
plt.figure(figsize=(12, 6))
sns.heatmap(df_customers.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data in Customers Dataset')
plt.show()

# Visualize missing data for `Transactions`
plt.figure(figsize=(12, 6))
sns.heatmap(df_transactions.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data in Transactions Dataset')
plt.show()

# 4. **Exploratory Data Analysis (EDA)**

# **Customers Data Analysis**

# Distribution of 'country'
plt.figure(figsize=(14, 7))
df_customers['country'].value_counts().head(20).plot(kind='bar')
plt.title('Top 20 Countries in Customers Data')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.show()

# Distribution of 'city'
plt.figure(figsize=(14, 7))
df_customers['city'].value_counts().head(20).plot(kind='bar')
plt.title('Top 20 Cities in Customers Data')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.show()

# **Transactions Data Analysis**

# Distribution of 'product_category'
plt.figure(figsize=(14, 7))
df_transactions['product_category'].value_counts().plot(kind='bar')
plt.title('Distribution of Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Number of Transactions')
plt.show()

# Distribution of 'payment_type'
plt.figure(figsize=(10, 6))
sns.countplot(data=df_transactions, x='payment_type')
plt.title('Distribution of Payment Types')
plt.xlabel('Payment Type')
plt.ylabel('Number of Transactions')
plt.show()

# Distribution of 'failure_reason' for failed transactions
failed_transactions = df_transactions[df_transactions['payment_txn_success'] == 'N']
plt.figure(figsize=(10, 6))
sns.countplot(data=failed_transactions, y='failure_reason')
plt.title('Distribution of Failure Reasons for Failed Transactions')
plt.xlabel('Count')
plt.ylabel('Failure Reason')
plt.show()

# **Outlier Analysis for Transactions Data**

# Boxplot for 'price'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_transactions['price'])
plt.title('Price Distribution with Outliers')
plt.show()

# Boxplot for 'qty'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_transactions['qty'])
plt.title('Quantity Distribution with Outliers')
plt.show()

# **Time Series Analysis**

# Convert `datetime` to datetime object
df_transactions['datetime'] = pd.to_datetime(df_transactions['datetime'])

# Plotting transaction volume over time
plt.figure(figsize=(14, 7))
df_transactions.set_index('datetime').resample('M').size().plot()
plt.title('Monthly Transaction Volume')
plt.xlabel('Month')
plt.ylabel('Number of Transactions')
plt.show()

# **Correlation Analysis**

# Correlation matrix for numerical columns in Transactions data
plt.figure(figsize=(10, 6))
numeric_cols = df_transactions.select_dtypes(include=['int64', 'float64']).columns
sns.heatmap(df_transactions[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Transactions Data')
plt.show()

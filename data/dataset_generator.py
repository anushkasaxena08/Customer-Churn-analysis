import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 10,000 customer records
n_customers = 10000

data = {
    'CustomerID': range(1, n_customers + 1),
    'Gender': np.random.choice(['Male', 'Female'], n_customers),
    'Age': np.random.randint(18, 68, n_customers),
    'Tenure': np.random.randint(1, 73, n_customers),
    'MonthlyCharges': np.round(np.random.uniform(20, 100, n_customers), 2),
    'Contract': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], n_customers, p=[0.5, 0.3, 0.2]),
    'PaymentMethod': np.random.choice(['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'], n_customers),
    'PaperlessBilling': np.random.choice(['Yes', 'No'], n_customers, p=[0.6, 0.4]),
    'MonthlyUsageGB': np.round(np.random.uniform(0, 100, n_customers), 1),
    'SupportTickets': np.random.randint(0, 10, n_customers)
}

df = pd.DataFrame(data)

# Calculate TotalCharges based on tenure and monthly charges
df['TotalCharges'] = np.round(df['Tenure'] * df['MonthlyCharges'] * np.random.uniform(0.95, 1.05, n_customers), 2)

# Generate churn with realistic patterns
churn_prob = 0.2  # Base churn rate

# Increase churn probability based on factors
churn_scores = np.zeros(n_customers)
churn_scores += (df['Contract'] == 'Month-to-Month').values * 0.25
churn_scores += (df['Tenure'] < 12).values * 0.15
churn_scores += (df['SupportTickets'] > 5).values * 0.20
churn_scores += (df['MonthlyCharges'] > 70).values * 0.10
churn_scores += (df['PaymentMethod'] == 'Electronic Check').values * 0.08

# Add base probability and randomness
churn_prob_final = churn_prob + churn_scores + np.random.uniform(-0.1, 0.1, n_customers)
churn_prob_final = np.clip(churn_prob_final, 0, 0.9)

df['Churn'] = (np.random.random(n_customers) < churn_prob_final).astype(str)
df['Churn'] = df['Churn'].map({'True': 'Yes', 'False': 'No'})

# Reorder columns
column_order = ['CustomerID', 'Gender', 'Age', 'Tenure', 'MonthlyCharges', 'TotalCharges', 
                'Contract', 'PaymentMethod', 'PaperlessBilling', 'MonthlyUsageGB', 'SupportTickets', 'Churn']
df = df[column_order]

# Save to CSV
df.to_csv('customer_churn_data.csv', index=False)

print(f"✓ Dataset generated: {len(df)} records")
print(f"✓ Churn rate: {(df['Churn']=='Yes').sum()/len(df)*100:.2f}%")
print(f"✓ File saved: customer_churn_data.csv")
print("\nFirst 5 rows:")
print(df.head())

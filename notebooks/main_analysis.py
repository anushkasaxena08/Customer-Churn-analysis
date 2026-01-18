"""
Customer Churn Prediction & Analysis
Complete End-to-End Pipeline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
import sqlite3
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print("="*70)
print("CUSTOMER CHURN PREDICTION & ANALYSIS")
print("="*70)

# ============================================================
# 1. DATA LOADING
# ============================================================
print("\n[1] Loading Dataset...")
df = pd.read_csv('customer_churn_data.csv')
print(f"Dataset Shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nDataset Info:")
print(df.info())
print(f"\nBasic Statistics:")
print(df.describe())

# ============================================================
# 2. DATA CLEANING
# ============================================================
print("\n[2] Data Cleaning...")
print(f"\nMissing Values:\n{df.isnull().sum()}")

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()
print(f"\nCleaned Dataset Shape: {df.shape}")

# ============================================================
# 3. CREATE SQL DATABASE
# ============================================================
print("\n[3] Creating SQL Database...")
conn = sqlite3.connect('customer_churn.db')
df.to_sql('customers', conn, if_exists='replace', index=False)
print("✓ Data stored in 'customer_churn.db'")
print("✓ Table name: 'customers'")

# ============================================================
# 4. EXPLORATORY DATA ANALYSIS
# ============================================================
print("\n[4] Exploratory Data Analysis...")

churn_counts = df['Churn'].value_counts()
churn_rate = (churn_counts['Yes'] / len(df)) * 100
print(f"\nChurn Distribution:\n{churn_counts}")
print(f"\nOverall Churn Rate: {churn_rate:.2f}%")

# Visualization 1: Churn Distribution
plt.figure(figsize=(8, 6))
colors = ['#2ecc71', '#e74c3c']
churn_counts.plot(kind='bar', color=colors)
plt.title('Customer Churn Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Churn Status', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('01_churn_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_churn_distribution.png")
plt.close()

# Visualization 2: Churn by Contract
plt.figure(figsize=(10, 6))
contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
contract_churn.plot(kind='bar', stacked=False, color=colors)
plt.title('Churn Rate by Contract Type', fontsize=16, fontweight='bold')
plt.xlabel('Contract Type', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.legend(['No Churn', 'Churn'], loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('02_churn_by_contract.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_churn_by_contract.png")
plt.close()

# Visualization 3: Tenure Distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df[df['Churn']=='No']['Tenure'].hist(bins=30, alpha=0.7, color='#2ecc71', edgecolor='black')
plt.title('Tenure Distribution - No Churn', fontsize=12, fontweight='bold')
plt.xlabel('Tenure (months)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
df[df['Churn']=='Yes']['Tenure'].hist(bins=30, alpha=0.7, color='#e74c3c', edgecolor='black')
plt.title('Tenure Distribution - Churn', fontsize=12, fontweight='bold')
plt.xlabel('Tenure (months)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('03_tenure_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_tenure_distribution.png")
plt.close()

# Visualization 4: Monthly Charges
plt.figure(figsize=(10, 6))
df.boxplot(column='MonthlyCharges', by='Churn', patch_artist=True)
plt.title('Monthly Charges by Churn Status', fontsize=16, fontweight='bold')
plt.suptitle('')
plt.xlabel('Churn Status', fontsize=12)
plt.ylabel('Monthly Charges ($)', fontsize=12)
plt.tight_layout()
plt.savefig('04_monthly_charges_churn.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_monthly_charges_churn.png")
plt.close()

# Visualization 5: Support Tickets
plt.figure(figsize=(10, 6))
ticket_churn = df.groupby('SupportTickets')['Churn'].apply(lambda x: (x=='Yes').sum()/len(x)*100)
ticket_churn.plot(kind='line', marker='o', color='#e74c3c', linewidth=2)
plt.title('Churn Rate by Support Tickets', fontsize=16, fontweight='bold')
plt.xlabel('Number of Support Tickets', fontsize=12)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('05_support_tickets_churn.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_support_tickets_churn.png")
plt.close()

# Visualization 6: Correlation Matrix
plt.figure(figsize=(12, 8))
numeric_cols = ['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges', 'MonthlyUsageGB', 'SupportTickets']
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, square=True, linewidths=1)
plt.title('Feature Correlation Matrix', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('06_correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 06_correlation_matrix.png")
plt.close()

# ============================================================
# 5. FEATURE ENGINEERING
# ============================================================
print("\n[5] Feature Engineering...")

df_model = df.copy()
label_encoders = {}
categorical_cols = ['Gender', 'Contract', 'PaymentMethod', 'PaperlessBilling', 'Churn']

for col in categorical_cols:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    label_encoders[col] = le

X = df_model.drop(['CustomerID', 'Churn'], axis=1)
y = df_model['Churn']

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"\nTraining set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

scaler = StandardScaler()
numerical_features = ['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges', 'MonthlyUsageGB', 'SupportTickets']
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
X_test[numerical_features] = scaler.transform(X_test[numerical_features])
print("✓ Feature scaling completed")

# ============================================================
# 6. MODEL TRAINING
# ============================================================
print("\n[6] Training Logistic Regression Model...")
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)
print("✓ Model training completed")

# ============================================================
# 7. MODEL EVALUATION
# ============================================================
print("\n[7] Model Evaluation...")

y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy*100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))

roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"\nROC-AUC Score: {roc_auc:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', square=True, 
            xticklabels=['No Churn', 'Churn'], yticklabels=['No Churn', 'Churn'])
plt.title('Confusion Matrix', fontsize=16, fontweight='bold')
plt.ylabel('Actual', fontsize=12)
plt.xlabel('Predicted', fontsize=12)
plt.tight_layout()
plt.savefig('07_confusion_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 07_confusion_matrix.png")
plt.close()

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='#e74c3c', linewidth=2, label=f'ROC Curve (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Random Classifier')
plt.title('ROC Curve', fontsize=16, fontweight='bold')
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate', fontsize=12)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('08_roc_curve.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 08_roc_curve.png")
plt.close()

# ============================================================
# 8. FEATURE IMPORTANCE
# ============================================================
print("\n[8] Analyzing Feature Importance...")

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values('Coefficient', key=abs, ascending=False)

print("\nTop 10 Most Important Features:")
print(feature_importance.head(10))

plt.figure(figsize=(12, 6))
top_features = feature_importance.head(10)
colors_list = ['#e74c3c' if x > 0 else '#3498db' for x in top_features['Coefficient']]
plt.barh(range(len(top_features)), top_features['Coefficient'], color=colors_list)
plt.yticks(range(len(top_features)), top_features['Feature'])
plt.xlabel('Coefficient Value', fontsize=12)
plt.title('Top 10 Features Influencing Churn', fontsize=16, fontweight='bold')
plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
plt.tight_layout()
plt.savefig('09_feature_importance.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 09_feature_importance.png")
plt.close()

# ============================================================
# 9. SAVE RESULTS
# ============================================================
print("\n[9] Saving Results...")

predictions_df = X_test.copy()
predictions_df['Actual_Churn'] = y_test.values
predictions_df['Predicted_Churn'] = y_pred
predictions_df['Churn_Probability'] = y_pred_proba
predictions_df.to_sql('predictions', conn, if_exists='replace', index=False)
print("✓ Predictions saved to database")

feature_importance.to_csv('feature_importance.csv', index=False)
print("✓ Feature importance saved to CSV")

with open('model_summary.txt', 'w') as f:
    f.write("="*60 + "\n")
    f.write("CUSTOMER CHURN PREDICTION MODEL SUMMARY\n")
    f.write("="*60 + "\n\n")
    f.write(f"Model: Logistic Regression\n\n")
    f.write(f"Dataset Size: {len(df)} customers\n")
    f.write(f"Training Set: {len(X_train)} samples\n")
    f.write(f"Test Set: {len(X_test)} samples\n\n")
    f.write(f"Overall Churn Rate: {churn_rate:.2f}%\n\n")
    f.write(f"Model Performance:\n")
    f.write(f"  - Accuracy: {accuracy*100:.2f}%\n")
    f.write(f"  - ROC-AUC Score: {roc_auc:.4f}\n\n")
    f.write(f"Confusion Matrix:\n")
    f.write(f"  True Negatives: {cm[0][0]}\n")
    f.write(f"  False Positives: {cm[0][1]}\n")
    f.write(f"  False Negatives: {cm[1][0]}\n")
    f.write(f"  True Positives: {cm[1][1]}\n\n")
    f.write("Top 5 Churn Drivers:\n")
    for idx, row in feature_importance.head(5).iterrows():
        f.write(f"  {row['Feature']}: {row['Coefficient']:.4f}\n")

print("✓ Model summary saved")

conn.close()

print("\n" + "="*70)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*70)
print("\nGenerated Files:")
print("  1. customer_churn.db (SQLite database)")
print("  2. 01-09 PNG visualizations")
print("  3. feature_importance.csv")
print("  4. model_summary.txt")

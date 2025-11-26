# Customer Churn Prediction – Machine Learning Project

## Task Objective

The goal of this task is to predict which **bank customers are most likely to churn (leave the bank).**
Using the Churn Modelling dataset, we aim to build a classification model that identifies key drivers of churn and helps the bank understand which customers need retention strategies.

## Approach

### 1. Data Cleaning
- Removed identifier columns such as Customer_number.
- Checked missing values (dataset had no significant NaNs).
- Converted large financial columns using log scaling only for visualization.

### 2. Exploratory Data Analysis (EDA)
- Visualized churn distribution, age, tenure, transaction activity.
- Used log-scale histograms for very large balance columns.
- Compared churn vs non-churn across key behaviors.

### 3. Feature Engineering
- Dataset contained only numeric columns → no encoding required.
- Prepared features (X) and labels (y).

### 4. Model Training
- Used Random Forest Classifier because it:
- Handles numeric data well
- Requires no feature scaling
- Provides feature importance
- Performs strongly on churn datasets

### 5. Model Evaluation

- Accuracy score
- Confusion matrix
- Classification report
- Feature importance bar chart

## Results & Insights
### 1. Model Performance
- Random Forest Accuracy: ~ 89%

### 2. Most Important Features

The Random Forest model revealed that churn is mainly driven by customer engagement and activity, specifically:

- Total_trans_no – total customer transactions
- No_Activity_Name – number of types of activities performed
- Tenure – length of stay with the bank
- Avg_Trans_no_month – average monthly transactions
- Account Balances – current account & deposit balances
- Age – younger clients churn more

## Insights
- Customers with low activity, low engagement, and short tenure are far more likely to leave the bank.
- High engagement (more transactions, more product usage) strongly reduces churn.
- Financially active customers (high balances, deposits) tend to stay longer.
- Demographic features like gender and staff status had very little impact.

## Conclusion:
The bank should focus on increasing customer engagement, improving onboarding for new customers, and monitoring low-activity clients to reduce churn.
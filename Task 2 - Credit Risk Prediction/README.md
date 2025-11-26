# Loan Default Prediction – Machine Learning Project

## Task Objective

The objective was to predict whether a loan applicant would default using a loan dataset.
The task involved cleaning data, handling missing values, visualizing important features, encoding categories, training models, and evaluating performance.

## Approach

### 1. Data Cleaning
- Dropped extremely sparse + low-importance columns
- Filled numerical missing values using median
- Filled categorical missing values using mode

### 2. Exploratory Data Analysis
- Visualized loan amount, income, credit score, LTV
- Used histograms, box plots, and scatter plots
- Identified correlations between financial metrics and default status

### 3. Feature Engineering + Encoding
- One-hot encoded categorical variables
- Prepared dataset for modeling

### 4. Modeling
- Trained Logistic Regression
- Trained Decision Tree
- Compared both using accuracy and confusion matrix

## Results & Insights
### 1. Model Performance
- Logistic Regression Accuracy: 87%
- Decision Tree Accuracy: 88%

### Key Observations
- Higher income and lower LTV are associated with lower default probability
- Loan applicants with low credit scores or risky profiles default more
- Decision Tree captured non-linear relationships better
- Logistic Regression was interpretable but slightly less accurate

## Conclusion:
Decision Tree performed best and highlighted how loan attributes (income, LTV, credit score) influence default risk.
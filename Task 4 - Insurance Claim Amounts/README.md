# Predicting Insurance Claim Amounts

## Task Objective
Estimate medical insurance charges (`charges` column) using a Linear Regression model and understand how key personal features impact claim amounts.

## Approach
- Loaded the Medical Cost Personal dataset using **pandas**
- Inspected structure with `.shape`, `.columns`, and `.head()`
- Visualized feature impact:
  - **Age vs Charges** (scatter plot)
  - **BMI vs Charges** (scatter plot)
  - **Smoking vs Charges** (box plot)
- One-Hot Encoded categorical columns (`sex`, `smoker`, `region`)
- Split data into **Train/Test (80/20)**
- Trained **Linear Regression** model
- Evaluated errors using **MAE** and **RMSE**

## Results & Insights
- The model learned an **upward trend**, predicting higher charges when actual charges increase.
- **Smoking status** shows a strong visible impact — smokers tend to have much higher claims.
- **Age and BMI** also show a moderate positive relationship with charges (not perfectly linear but learnable).
- The **Actual vs Predicted plot** improved significantly from previous attempts and now follows the diagonal trend, showing the model understood cost direction instead of just predicting the average.

## Tools & Libraries
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-Learn (Linear Regression + Error metrics)



# Energy Consumption Time Series Forecasting

## Task Objective

The objective of this task is to forecast short-term household energy consumption using historical time series data. The goal is to analyze temporal patterns in electricity usage and evaluate the effectiveness of different forecasting approaches, including statistical models, seasonality-based models, and machine learning techniques.

Specifically, the task aims to:
- Parse and resample time-based energy consumption data
- Engineer meaningful time-based features
- Build and compare ARIMA, Prophet, and XGBoost models
- Evaluate model performance using MAE and RMSE
- Visualize actual versus forecasted energy usage


## Approach

The task was completed through a structured, multi-step workflow:

1. **Data Preparation & Cleaning**
   - Loaded the Household Power Consumption dataset
   - Combined date and time columns into a unified datetime index
   - Converted all measurement columns to numeric format
   - Handled missing values to maintain time series continuity
   - Saved a cleaned version of the dataset for reuse

2. **Time Series Resampling & Exploratory Analysis**
   - Resampled minute-level data to hourly intervals to reduce noise
   - Visualized long-term trends and recurring daily patterns
   - Identified peak energy usage hours and weekly consumption behavior

3. **Feature Engineering**
   - Created time-based features such as hour of day, day of week, and weekend indicators
   - Prepared a feature-rich dataset suitable for machine learning models

4. **Modeling & Forecasting**
   - **ARIMA** was used as a statistical baseline model
   - **Prophet** was applied to capture trend and daily seasonality
   - **XGBoost** was trained using engineered time-based features to model non-linear patterns

5. **Evaluation & Comparison**
   - Split data into training and testing sets using a chronological split
   - Evaluated all models using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)
   - Visualized forecasts against actual energy consumption
   - Compared model performance using tables and side-by-side plots


## Results and Findings

- **ARIMA** served as a useful baseline but produced overly smooth forecasts and struggled to capture daily energy usage patterns and sharp fluctuations.
- **Prophet** significantly improved performance by modeling daily seasonality, resulting in forecasts that followed recurring consumption cycles more closely.
- **XGBoost** achieved the best performance, with the lowest MAE and RMSE values. By leveraging engineered time-based features, it was able to capture complex, non-linear behavior and respond more effectively to sudden changes in energy consumption.

Overall, the results demonstrate that while traditional statistical models are useful for baseline comparison, feature-based machine learning approaches such as XGBoost are more effective for short-term household energy forecasting when sufficient temporal features are available.

# Global Superstore – Interactive Business Dashboard (Streamlit)

## Task Objective
The objective of this task was to design and develop an **interactive business intelligence dashboard** using **Streamlit** for the Global Superstore dataset.  
The dashboard aims to help users analyze **sales performance, profit trends, and segment-wise insights** through dynamic filters and visual KPIs.  
Key requirements included data cleaning, user interactivity, and clear visualization of important business metrics.

---

## Approach
The project was implemented in a structured, step-by-step manner:

### 1. Data Preparation
- Loaded the Global Superstore dataset using **Pandas**.
- Cleaned column names and converted date and numeric fields to appropriate data types.
- Removed the `Postal Code` column due to excessive missing values and no analytical relevance.
- Handled missing values in critical columns to ensure accurate KPI calculations.
- Created an additional metric, **Profit Margin (%)**, for deeper analysis.

### 2. Dashboard Design
- Built the dashboard using **Streamlit** with a wide layout for better readability.
- Added a sidebar with interactive filters for:
  - Date range
  - Region
  - Category
  - Sub-Category
  - Segment
  - Market
- Implemented a reset mechanism for filters using Streamlit session state.
- Organized content into multiple tabs (Overview, Customers, Products, Data) for a professional BI-style layout.

### 3. Visualization & KPIs
- Displayed key KPIs:
  - Total Sales
  - Total Profit
  - Average Profit Margin
  - Total Orders
- Created interactive charts using **Plotly Express**, including:
  - Monthly sales and profit trends
  - Segment-wise sales and profit
  - Top customers by sales and profit
  - Top products and sub-category profitability
- Added a data preview table and CSV download option for filtered data.

---

## Results and Findings
- **Sales and profit show a clear upward trend over time**, indicating overall business growth.
- The **Consumer segment** contributes the highest share of both sales and profit compared to other segments.
- **Technology** is the best-performing category in terms of revenue and profitability.
- A small number of **top customers contribute a significant portion of total sales**, highlighting customer concentration.
- Some **sub-categories generate high sales but low or negative profit**, indicating potential pricing or cost issues.
- The dashboard enables users to **quickly identify high-performing areas and loss-making segments** through interactive filters.

---

**Tools Used:** Python, Streamlit, Pandas, NumPy, Plotly  
**Dataset:** Global Superstore

# Customer Segmentation Using Unsupervised Learning

## Task Objective

The objective of this project is to segment mall customers based on their spending behavior using unsupervised learning techniques.  
By identifying distinct customer groups, the project aims to support data-driven and targeted marketing strategies instead of applying a single approach to all customers.

---

## Dataset Description

The dataset contains transaction-level shopping data of mall customers, including demographic details and purchase information such as price, quantity, and product category.

Since a direct spending score is not provided, customer spending behavior is derived from real transaction data, making the analysis more realistic and aligned with real-world business scenarios.

---

## Project Approach

### 1️ - Exploratory Data Analysis (EDA)

- Analyzed dataset structure, data types, and distributions  
- Checked for missing values and data consistency  
- Gained initial insights into customer demographics and purchasing patterns  

---

### 2️ - Feature Engineering

Transaction-level data was transformed into customer-level features to represent spending behavior:

- Total Spending  
- Average Spending per Transaction  
- Purchase Frequency  
- Total Quantity Purchased  
- Customer Age  

These features collectively describe customer spending habits.

---

### 3️ - Feature Scaling

Since K-Means clustering is a distance-based algorithm, all numerical features were standardized to ensure equal contribution during clustering and avoid bias from large-scale values.

---

### 4️ - K-Means Clustering

- The Elbow Method was applied to determine the optimal number of clusters  
- Based on the elbow curve, **K = 3** was selected  
- Customers were grouped into three distinct segments based on spending behavior  

---

### 5️ - PCA Visualization

Principal Component Analysis (PCA) was used to reduce high-dimensional data into two dimensions for visualization.

PCA was chosen over t-SNE because it is faster, more stable on large datasets, easier to interpret, and preserves global data structure, which aligns well with K-Means clustering.

---

### 6️ - Marketing Strategy Development

Each customer cluster was analyzed and translated into actionable marketing strategies.  
Strategy-oriented visualizations were used to map customer segments to appropriate marketing channels and promotional approaches.

---

## Results and Findings

The clustering process successfully identified three meaningful customer segments:

- **Cluster 0:** Older, low-spending customers  
  → Best targeted using loyalty programs and discount-based promotions  

- **Cluster 1:** Younger, budget-conscious customers  
  → More responsive to digital marketing, social media campaigns, and bundled offers  

- **Cluster 2:** High-spending, premium customers  
  → Require personalized communication, exclusive offers, and VIP-focused strategies  

PCA visualization confirmed that the clusters are reasonably separated, with one clearly distinct high-value customer segment.

---

## Key Insights

- High-spending customers form a smaller but highly valuable segment  
- Low and medium spending customers represent the majority and benefit from mass-marketing approaches  
- Customer segmentation enables better allocation of marketing budget and resources  
- Strategy-driven visualizations help translate analytical results into business decisions  

---

## Tools and Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Jupyter Notebook  



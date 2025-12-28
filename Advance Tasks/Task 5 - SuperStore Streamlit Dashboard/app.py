# Libraries
import streamlit as st  # Streamlit is used to build the interactive web dashboard
import pandas as pd  # Pandas is used for loading and cleaning the dataset
import numpy as np  # NumPy is used for safe numeric operations
import plotly.express as px  # Plotly Express is used for interactive charts

# look and layout setup
st.set_page_config(  # Set basic page configuration
    page_title="Global Superstore Dashboard",  # Title shown in browser tab
    page_icon="📊",  # Icon shown in browser tab
    layout="wide"  # Use full width layout
)

st.title("📊 Global Superstore — Interactive Business Dashboard")  # Dashboard title
st.caption("BI-style dashboard to analyze Sales, Profit, and segment-wise performance.")  # Small subtitle

# colors for dashoboard
segment_palette = ["#BFC8AE","#E2DBD3", "#F0D6CB"]
customers_products_palette= [    "#B7B7A4","#DDBEA9", "#CB997E","#A5A58D","#F0EFEB" ]
sales_color = "#6b9080"  
profit_color = "#98c1d9" 

# helper function for consistent styling
def style_chart(fig, title_text):
    fig.update_layout(title=title_text, title_x=0.0, margin=dict(l=20, r=20, t=60, b=20), legend_title_text="",)  
    return fig  

# loading data

@st.cache_data  # Cache results so Streamlit doesn't reload file each time
def load_data(file_path: str) -> pd.DataFrame:  
    try:  # Try reading with UTF-8
        data = pd.read_csv(file_path, encoding="utf-8", low_memory=False)  
    except UnicodeDecodeError:  # If UTF-8 fails
        data = pd.read_csv(file_path, encoding="latin1", low_memory=False)  
    return data  

df_raw = load_data("Global_Superstore2.csv")  # path to dataset

# Pre-Processing
df = df_raw.copy()  # Copy dataset to avoid modifying original
df.columns = [col.strip() for col in df.columns]  

# Dropping postal code column
if "Postal Code" in df.columns:  
    df = df.drop(columns=["Postal Code"]) 

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")  # Convert Order Date to datetime
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")  # Convert Ship Date to datetime

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")  # Convert Sales to numeric
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")  # Convert Profit to numeric
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")  # Convert Discount to numeric
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")  # Convert Quantity to numeric

df = df.dropna(subset=["Order Date", "Sales", "Profit"])  # Drop rows missing key fields

df["Profit Margin %"] = np.where(  
    df["Sales"] != 0,  # Avoid divide by zero
    (df["Profit"] / df["Sales"]) * 100,  
    0  # If Sales is 0, keep margin 0
)  

# Sidebar Filters
st.sidebar.header("Dashboard Filters") 

# Reset mechanism using session state 
if "reset_counter" not in st.session_state:  # Check if counter exists in session state
    st.session_state.reset_counter = 0  # Initialize counter

reset_key = str(st.session_state.reset_counter)  # Create a key string to force widgets to refresh on reset

min_date = df["Order Date"].min() 
max_date = df["Order Date"].max()  

# date range selector 
date_range = st.sidebar.date_input("Order Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date, key="date_" + reset_key)  

if isinstance(date_range, tuple) and len(date_range) == 2:  # If user selected both dates
    start_date, end_date = date_range  # Unpack start/end date
else:  # If selection is incomplete
    start_date, end_date = min_date, max_date  # Use full range

regions = sorted(df["Region"].dropna().unique().tolist())  # List of regions
categories = sorted(df["Category"].dropna().unique().tolist())  # List of categories
sub_categories = sorted(df["Sub-Category"].dropna().unique().tolist())  # List of sub-categories

# region filter
selected_region = st.sidebar.multiselect( "Region",options=regions, default=regions, key="region_" + reset_key)  

 # Category filter
selected_category = st.sidebar.multiselect("Category", options=categories, default=categories, key="category_" + reset_key) 

# Sub-category filter
selected_sub_category = st.sidebar.multiselect("Sub-Category", options=sub_categories, default=sub_categories, key="subcat_" + reset_key)  

segments = sorted(df["Segment"].dropna().unique().tolist())  # Segment values
markets = sorted(df["Market"].dropna().unique().tolist())  # Market values

# Segment filter
selected_segment = st.sidebar.multiselect("Segment", options=segments, default=segments, key="segment_" + reset_key)

# Market filter 
selected_market = st.sidebar.multiselect("Market", options=markets, default=markets, key="market_" + reset_key)

st.sidebar.divider()  # Divider line

if st.sidebar.button("Reset Filters"):  # Reset button
    st.session_state.reset_counter += 1  # Increment counter to recreate widgets
    st.rerun()  # Rerun app

# Apply Filters
df_filtered = df.copy()  

df_filtered = df_filtered[  
    (df_filtered["Order Date"] >= pd.to_datetime(start_date)) & (df_filtered["Order Date"] <= pd.to_datetime(end_date))] 

df_filtered = df_filtered[df_filtered["Region"].isin(selected_region)]  # Apply Region filter
df_filtered = df_filtered[df_filtered["Category"].isin(selected_category)]  # Apply Category filter
df_filtered = df_filtered[df_filtered["Sub-Category"].isin(selected_sub_category)]  # Apply Sub-Category filter
df_filtered = df_filtered[df_filtered["Segment"].isin(selected_segment)]  # Apply Segment filter
df_filtered = df_filtered[df_filtered["Market"].isin(selected_market)]  # Apply Market filter

if df_filtered.empty:  # If no data remains after filtering
    st.warning("No data found for the selected filters. Try selecting more options.")  # Show warning
    st.stop()

# tabs for professional look
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Customers", "Products", "Data"])  

# Tab 01 -> KPIs and main charts
with tab1: 

    st.subheader("Business Overview") 

    with st.expander("View Active Filters"):  # Expandable filter summary
        st.write("**Date Range:**", start_date, "to", end_date)  # Show date
        st.write("**Region:**", selected_region)  # Show region
        st.write("**Category:**", selected_category)  # Show category
        st.write("**Sub-Category:**", selected_sub_category)  # Show sub-category
        st.write("**Segment:**", selected_segment)  # Show segment
        st.write("**Market:**", selected_market)  # Show market

    total_sales = df_filtered["Sales"].sum()  # KPI total sales
    total_profit = df_filtered["Profit"].sum()  # KPI total profit
    avg_profit_margin = df_filtered["Profit Margin %"].mean()  # KPI avg profit margin
    total_orders = df_filtered["Order ID"].nunique()  # KPI total orders

    k1, k2, k3, k4 = st.columns(4)  # Create KPI columns
    k1.metric("Total Sales", f"${total_sales:,.2f}")  # Show sales KPI
    k2.metric("Total Profit", f"${total_profit:,.2f}")  # Show profit KPI
    k3.metric("Avg Profit Margin", f"{avg_profit_margin:.2f}%")  # Show margin KPI
    k4.metric("Total Orders", f"{total_orders:,}")  # Show orders KPI

    st.divider()  # Divider line

    st.markdown("### Monthly Sales & Profit Trend")

 # Build monthly trend table
    trend = (df_filtered.set_index("Order Date").resample("M")[["Sales", "Profit"]].sum().reset_index())  

# Create line chart
    fig_trend = px.line(trend, x="Order Date", y=["Sales", "Profit"], markers=True, color_discrete_sequence=[sales_color, profit_color]) 

    fig_trend = style_chart(fig_trend, "Monthly Sales & Profit Trend")  # Style chart
    st.plotly_chart(fig_trend, use_container_width=True)  # Display chart

    st.markdown("### Segment-wise Sales")  # Segment sales chart title

    seg_sales = df_filtered.groupby("Segment", as_index=False)["Sales"].sum()  # Segment sales summary

# Create bar chart
    fig_seg_sales = px.bar(seg_sales, x="Segment", y="Sales", color="Segment", color_discrete_sequence=segment_palette)  

    fig_seg_sales = style_chart(fig_seg_sales, "Sales by Segment")  # Style chart
    st.plotly_chart(fig_seg_sales, use_container_width=True)  # Display chart

    st.markdown("### Segment-wise Profit")  # Segment profit chart title

    seg_profit = df_filtered.groupby("Segment", as_index=False)["Profit"].sum()  # Segment profit summary

# Create bar chart
    fig_seg_profit = px.bar(seg_profit, x="Segment", y="Profit", color="Segment", color_discrete_sequence=segment_palette) 

    fig_seg_profit = style_chart(fig_seg_profit, "Profit by Segment")  # Style chart
    st.plotly_chart(fig_seg_profit, use_container_width=True)  # Display chart

# Tab 02 -> Customers

with tab2: 

    st.subheader("Customer Performance")  # Section title

    st.markdown("### Top 5 Customers by Sales")  # Required chart title

  # Calculate top 5 customers
    top_customers = (df_filtered.groupby("Customer Name", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(5)) 

 # Create bar chart
    fig_top_customers = px.bar(top_customers, x="Customer Name", y="Sales", color="Customer Name", color_discrete_sequence=customers_products_palette, text_auto=".2s")

    fig_top_customers = style_chart(fig_top_customers, "Top 5 Customers by Sales")  # Style chart
    st.plotly_chart(fig_top_customers, use_container_width=True)  # Display chart

 # Calculate top 10 profit customers
    st.markdown("### Top 10 Customers by Profit")  

    top_profit_customers = (df_filtered.groupby("Customer Name", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False).head(10))  

# Create profit bar chart
    fig_top_profit = px.bar(top_profit_customers, x="Customer Name", y="Profit", color="Customer Name", color_discrete_sequence=customers_products_palette, text_auto=".2s")

    fig_top_profit = style_chart(fig_top_profit, "Top 10 Customers by Profit")  # Style chart
    st.plotly_chart(fig_top_profit, use_container_width=True)  # Display chart

# Tab: 03 -> Products

with tab3:  

    st.subheader("Product Insights")  # Section title

    st.markdown("### Top 10 Products by Sales")  # Chart title

# Compute top products
    top_products = (df_filtered.groupby("Product Name", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(10))  

 # Create horizontal bar chart
    fig_products = px.bar(top_products, x="Sales", y="Product Name", orientation="h", color="Product Name", color_discrete_sequence=customers_products_palette)  

    fig_products = style_chart(fig_products, "Top 10 Products by Sales")  # Style chart
    st.plotly_chart(fig_products, use_container_width=True)  # Display chart

    st.markdown("### Profit by Sub-Category")  # Chart title

# Compute profit by sub-category
    profit_subcat = (df_filtered.groupby("Sub-Category", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False))  

# Create horizontal bar chart
    fig_profit_sub = px.bar(profit_subcat, x="Profit", y="Sub-Category", orientation="h", color="Sub-Category", color_discrete_sequence=customers_products_palette)  

    fig_profit_sub = style_chart(fig_profit_sub, "Profit by Sub-Category")  # Style chart
    st.plotly_chart(fig_profit_sub, use_container_width=True)  # Display chart

# Tab: 04 -> Data

with tab4:

    st.subheader("Filtered Data View")  # Title
    st.dataframe(df_filtered.head(100))  # Show first 100 rows

    csv_data = df_filtered.to_csv(index=False).encode("utf-8")  # Convert to CSV

# Download button
    st.download_button(  
        "⬇️ Download Filtered CSV", csv_data, "filtered_superstore_data.csv", "text/csv")

# Footer
st.caption("Built with Streamlit • Dataset: Global Superstore • KPIs: Sales, Profit, Top Customers") 

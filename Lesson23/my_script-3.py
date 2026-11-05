import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('Advertising_F.csv')
st.title("Advertising Effectiveness")

st.sidebar.header("Filters")
x_var = st.sidebar.selectbox("X axis", ["TV", "radio", "newspaper"])

# Show scatterplot
fig_scatter = px.scatter(
    df, 
    x=x_var, 
    y='sales',
    labels={'TV': 'TV Ad Spend', 'radio': 'Radio Ad Spend', 'newspaper': 'Newspaper Ad Spend'}
)
st.plotly_chart(fig_scatter)

# Show barchart
sales_per_city = df.groupby('City')['sales'].sum().reset_index()
fig_bar = px.bar(sales_per_city, x='City', y='sales', title='Total Sales by City')  
st.plotly_chart(fig_bar)

# Show dataframe
st.dataframe(df)

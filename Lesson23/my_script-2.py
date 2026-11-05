import pandas as pf
import stremlit as st
import plotly.express as px

df=pd.read_csv('Advertising_F.csv')
st.title("advertisting effectivness Sulton")

st.sidebar.head("Filters")
x_var=st.selectbox("X axis",["TV","radio","newspaper"])

#show scatterplot
fig=px.scatter(df,x=x_var,y='sales',
            labels={'TV':'Tv add spend','radio':'Radui add spend'}')

st.plotly_char(fig)
#show barchart
               sales_per_city=df.groupby('City')['sales'].sum().reset_index()
px.bar(sales_per_city, x='City', y='sales', title='Data is Fun')  
st.plotly_chart(fig)

               #show dataframe
st.dataframe(df)                        

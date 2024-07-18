import pandas as  pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
# read date
df=pd.read_csv('finalRealEstate.csv')

# sidbar title
st.sidebar.title("Explore car's market")

def RealEstatMarket():
    st.markdown("<h2 style='color:#31356E; text-algin:center'>Real Estate Market in Dubai</h2>" ,unsafe_allow_html=True)
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>building properties</h5>" ,unsafe_allow_html=True)
    col1 , col2 = st.columns([3, 3])
    with col1:
        st.plotly_chart(px.histogram(df,x='beds',color_discrete_sequence=['#2D8BBA']).update_layout(
            title='Number of beds',
            bargap=0.1,
            autosize=False,
            width=350,
            height=500))
    with col2:
        st.plotly_chart(px.histogram(df,x='baths',color_discrete_sequence=['#2D8BBA']).update_layout(
        title='Number of baths',bargap=0.1,width=350 , height=500    ))
        
#     fig = go.Figure(data=[go.Pie(labels=df['type'],pull=[0.2, 0, 0, 0,0,0])])
    
        
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Types of the buildings</h5>" ,unsafe_allow_html=True)
    fig1 = go.Figure(data=[go.Pie(labels=df['type'],pull=[0.2, 0, 0, 0,0,0])])
    st.plotly_chart(fig1)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>building city</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.pie(df,names='city',color_discrete_sequence=['#2D8BBA']))
    st.plotly_chart(px.scatter(df,x='city' ,y='rent',color_discrete_sequence=['#2D8BBA']))
    
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>years benfits</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.line(pd.DataFrame(df.groupby(['year'])['rent'].sum()),y='rent' ,title='Sum of rent per Year'))
    
def market24():
    msk=df['type'].isin(['Apartment','Villa'])
    msk2=df['year']==2024
    msk3=df['city'].isin(['Abu Dhabi','Dubai'])
    df24=df[msk& msk2&msk3]
    st.markdown("<h2 style='color:#31356E; text-algin:center'>Real Estate Market at 2024 in Emarites</h2>" ,unsafe_allow_html=True)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>properties of the building</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.histogram(df[msk& msk2&msk3],x='beds',color="baths",title ='rent according to Bed & bath rooms for 2024' ).update_yaxes(categoryorder='total descending'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Furnishing</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.pie(df[msk& msk2&msk3],names='furnishing'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>working with Apartment and villa</h5>" ,unsafe_allow_html=True)
    fig3 = go.Figure(data=[go.Pie(labels=df24['type'],pull=[0.2, 0, 0, 0,0,0])])
    st.plotly_chart(fig3)
    
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Season where the build is posted</h5>" ,unsafe_allow_html=True)    
    fig = go.Figure(data=[go.Pie(labels=df24['season'], hole=0.3) ])
    fig.update_layout(title='Season in 2024')
    st.plotly_chart(fig)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Rent related to the features</h5>" ,unsafe_allow_html=True)      
    st.plotly_chart(px.histogram(df24,x='city' , y='rent' ,color='type' ,barmode='group' ,title='rent accoriding to both city and type 2024').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(df24,x='beds' , y='rent' ,color="baths",title ='rent according to Bed & bath rooms for 2024' ).update_yaxes(categoryorder='total descending'))
    

    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>each month benfit</h5>" ,unsafe_allow_html=True) 
    month=df[msk& msk2&msk3].groupby(['month'])['rent'].sum()
    monthdf=pd.DataFrame(month)
    st.plotly_chart(px.line(monthdf,y='rent',title='rent in 2024'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Average rent for every sqft related to city</h5>" ,unsafe_allow_html=True) 
    st.image("avg2024.png", caption='Average rent for every sqft', use_column_width=True)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Average listing days for each month</h5>" ,unsafe_allow_html=True) 
    st.image("avglisting2024.png", caption='Average of listing days', use_column_width=True)

def market23():
    msk=df['type'].isin(['Apartment','Villa'])
    msk2=df['year']==2023
    msk3=df['city'].isin(['Abu Dhabi','Dubai'])
    df24=df[msk& msk2&msk3]
    st.markdown("<h2 style='color:#31356E; text-algin:center'>Real Estate Market at 2023 in Emarites</h2>" ,unsafe_allow_html=True)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>properties of the building</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.histogram(df[msk& msk2&msk3],x='beds',color="baths",title ='rent according to Bed & bath rooms for 2023' ).update_yaxes(categoryorder='total descending'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Furnishing</h5>" ,unsafe_allow_html=True)
    st.plotly_chart(px.pie(df[msk& msk2&msk3],names='furnishing'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>working with Apartment and villa</h5>" ,unsafe_allow_html=True)
    fig3 = go.Figure(data=[go.Pie(labels=df24['type'],pull=[0.2, 0, 0, 0,0,0])])
    st.plotly_chart(fig3)
    
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Season where the build is posted</h5>" ,unsafe_allow_html=True)    
    fig = go.Figure(data=[go.Pie(labels=df24['season'], hole=0.3) ])
    fig.update_layout(title='Season in 2024')
    st.plotly_chart(fig)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Rent related to the features</h5>" ,unsafe_allow_html=True)      
    st.plotly_chart(px.histogram(df24,x='city' , y='rent' ,color='type' ,barmode='group' ,title='rent accoriding to both city and type 2023').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(df24,x='beds' , y='rent' ,color="baths",title ='rent according to Bed & bath rooms for 2023' ).update_yaxes(categoryorder='total descending'))
    

    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>each month benfit</h5>" ,unsafe_allow_html=True) 
    month=df[msk& msk2&msk3].groupby(['month'])['rent'].sum()
    monthdf=pd.DataFrame(month)
    st.plotly_chart(px.line(monthdf,y='rent',title='rent in 2023'))
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Average rent for every sqft related to city</h5>" ,unsafe_allow_html=True) 
    st.image("avg2023.png", caption='Average rent for every sqft', use_column_width=True)
    
    st.markdown("<h5 style='color:#2D8BBA;text-algin:left'>Average listing days for each month</h5>" ,unsafe_allow_html=True) 
    st.image("avglisting2023.png", caption='Average of listing days', use_column_width=True)


pages = {
    'All Markets' : RealEstatMarket,
    'realstat in Emirats for year 2024' : market24,
    'realstat in Emirats for year 2023' : market23,
#     'USA' : USA
}

pg = st.sidebar.radio('Navigate Pages' , pages.keys())


pages[pg]()

import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as plx


st.title('Covid-19 vaccination progress')
st.write("This app tracks worldwide Covid-19 vaccination progress in different countries ")

# load data
@st.cache
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
    return df


df = load_data()

continents = ['']
df_continents = df[df['iso_code'].str.contains('OWID')]

# 


st.write(df)
st.write(df_continents)

chart_select = st.sidebar.selectbox('Select a chart', ('Bar Chart', 'Pie Chart', 'Line Chart'))
country_select = st.sidebar.selectbox('Select a country', df['location'].unique())
status_select = st.sidebar.radio('Select Vaccination Status', ('total_vaccinations', 'people_vaccinated', 'people_vaccinated_per_hundred','people_fully_vaccinated', 'people_fully_vaccinated_per_hundred'))
selected_country = df[df['location']==country_select]
st.markdown("## **Country Level Analysis**")

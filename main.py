import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')


st.title('Indian Startup Funding Analysis')

st.sidebar.title('Search/Filter')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.header('Overall Analysis')
elif option == 'Startup':
    st.header('Startup Analysis')
    st.sidebar.selectbox('Select Startup',['Byjus','Ola'])
else:
    st.header('Investor Analysis')
    st.sidebar.selectbox('Select Investor',['p1','p2'])




st.dataframe(df)
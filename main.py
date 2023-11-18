import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding_clean.csv')


st.title('Indian Startup Funding Analysis')

st.sidebar.title('Search/Filter')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.header('Overall Analysis')
elif option == 'Startup':
    st.header('Startup Analysis')
    st.sidebar.selectbox('Select Startup',sorted(df.startup))
else:
    st.header('Investor Analysis')
    st.sidebar.selectbox('Select Investor',sorted(set(df.investors.str.split(',').sum())))




st.dataframe(df)
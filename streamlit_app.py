import streamlit as st
import pandas as pd 

st.title('Machine Learning App')

st.info('This is a Machine learning App')
df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df

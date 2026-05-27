import streamlit as st,pandas as pd
st.title('Data Cleaning Report');st.dataframe(pd.read_csv('cleaned_data.csv'))
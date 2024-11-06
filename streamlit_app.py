import streamlit as st

st.title('Machine Learning Apps')

st.write('this is app for learn machine learning')

st.sidebar.title('Navigasi')
page = st.sidebar.selectbox("Pilih Halaman",["input data", "List Data", "Grafik", "Forecasting"])


import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz

st.title('Dashboard')

st.sidebar.title('Menu')


st.title('Penambahan Stock')


st.title('Logistik')


def stock_information():
    st.title("Informasi Stock")
    st.write("Penambahan Stock")

def logistic_data():
    st.title("Input Data Logistik")

def table_data():
    st.title("Tabel Data Logistik")

def trend_graph():
    st.title("Grafik Tren Logistik")

st.sidebar.title('Navigasi')
if st.session_state['page'] == "Informasi Stock":
    stock_information()
elif st.session_state['page'] == "Input Data Logistik":
    logistic_data()
elif st.session_state['page'] == "Tabel Data Logistik":
    table_data()
elif st.session_state['page'] == "Grafik Tren Logistik":
    trend_graph()

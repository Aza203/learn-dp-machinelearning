import streamlit as st
import pandas as pd
from datetime import datetime

if 'data' not in st.session_state:
  st.session_state['data'] = []
  
st.title('Machine Learning Apps')

st.write('this is app for learn machine learning')


st.sidebar.title('Navigasi')
page = st.sidebar.radio("Pilih Halaman",["Input Data", "List Data", "Grafik", "Forecasting"])

if page == "Input Data":
  st.title("Dashboard Input Data")
  col_data_driver, col_data_uang = st.columns(2)

  with col_data_driver:
    st.header("Data Driver")
    driver_name = st.text_input('Nama Driver')
    instance_name = st.text_input('Nama Instansi')

  with col_data_uang:
    st.header("Data Uang")
    money_amount = st.text_input('Jumlah uang')
      
  if st.button('Simpan Data'):
    if driver_name and instance_name and money_amount:
      current_time = datetime.now()
      st.session_state['data'].append({
        'Nama Driver' : driver_name,
        'Nama Instansi': instance_name,
        'Jumlah Uang': money_amount,
        'Tanggal': current_time.strftime("%Y-%m-%d"),
        'Waktu': current_time.strftime("%H:%M:%S")
      })
      st.success('Data Berhasil disimpan!')
    else:
      st.error('Mohon isi semua kolom!')
      
elif page == 'List Data':
  st.title('List Data')
  if st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    df['Tanggal'] = pd.to_datetime(df['Tanggal']) 
    grouped = df.groupby([df['Tanggal'].dt.year, df['Tanggal'].dt.month, df['Tanggal'].dt.day])
    for (year, month,day), group in grouped:
      st.write(f"Data untuk {year}-{month:02d}-{day:02d}")
      st.table(group)
  else:
    st.write("Belum ada data yang disimpan")

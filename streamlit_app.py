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
        'Tanggal': current_time.strftime("%Y-%m-%d"),
        'Waktu': current_time.strftime("%H:%M:%S"),
        'Nama Driver' : driver_name,
        'Nama Instansi': instance_name,
        'Jumlah Uang': money_amount,
      })
      st.success('Data Berhasil disimpan!')
    else:
      st.error('Mohon isi semua kolom!')
      
elif page == 'List Data':
  st.title('List Data')
  if st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    if 'Tanggal' in df.columns:
      df['Tanggal'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m-%d')
      df['Tahun'] = pd.to_datetime(df['Tanggal']).dt.year
      df['bulan'] = pd.to_datetime(df['Tanggal']).dt.month_name

      grouped_year = df.groupby([df['Tahun']])
      for year, group_year in grouped_year:
        st.write(f"Data untuk Tahun {year}")
        grouped_mounth = group_year.groupby('Bulan')
        for month, group_month in grouped_mounth:
          with st.expander(f"{month}"):
            st.table(group_month.drop(columns=['Tahun', 'Bulan']))
    else:
      st.write("Kolom 'Tanggal' tidak ditemukan dalam data.")
  else:
    st.write("Belum ada data yang disimpan.")

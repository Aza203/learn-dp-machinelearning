import streamlit as st
import pandas as pd

if 'data' not in st.session_state:
  st.session_state['data'] = []
  
st.title('Machine Learning Apps')

st.write('this is app for learn machine learning')

st.sidebar.title('Navigasi')
page = st.sidebar.button("Pilih Halaman",["Input Data", "List Data", "Grafik", "Forecasting"])

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
      st.session_state['data'].append({
        'Nama Driver' : driver_name,
        'Nama Instansi': instance_name,
        'Jumlah Uang': money_amount
      })
      st.sucess('Data Berhasil disimpan!')
    else:
      st.error('Mohon isi semua kolom!')
      
elif page == 'List Data':
  st.title('List Data')
  if st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    st.table(df)
  else:
    st.write("Belum ada data yang disimpan")

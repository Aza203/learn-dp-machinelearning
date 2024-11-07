import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# Inisialisasi session state untuk menyimpan data
if 'data' not in st.session_state:
    st.session_state['data'] = []

st.title('Machine Learning Apps')

st.write('This is an app for learning machine learning')

st.sidebar.title('Navigasi')
page = st.sidebar.radio("Pilih Halaman", ["Input Data", "List Data", "Grafik", "Forecasting"])

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
            # Mengatur timezone ke Asia/Jakarta
            tz = pytz.timezone('Asia/Jakarta')
            current_time = datetime.now(tz)
            st.session_state['data'].append({
                'Tanggal': current_time.strftime("%Y-%m-%d"),
                'Waktu': current_time.strftime("%H:%M:%S"),
                'Nama Driver': driver_name,
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
            df['Bulan'] = pd.to_datetime(df['Tanggal']).dt.month_name()

            grouped_year = df.groupby('Tahun')
            for year, group_year in grouped_year:
                st.write(f"Data untuk Tahun {year}")
                grouped_month = group_year.groupby('Bulan')
                for month, group_month in grouped_month:
                    with st.expander(f"Bulan {month}"):
                        st.table(group_month.drop(columns=['Tahun', 'Bulan']))
        else:
            st.write("Kolom 'Tanggal' tidak ditemukan dalam data.")
    else:
        st.write("Belum ada data yang disimpan.")

import streamlit as st
import pandas as pd
from datetime import datetime
import pytz


# Fungsi untuk halaman informasi stok
def stock_information():
    st.title("Informasi Stock")
    st.write("Penambahan Stock")

# Fungsi untuk halaman input data logistik
def logistic_data():
    st.title("Input Data Logistik")
    col_data_barang, col_data_stok = st.columns(2)

    with col_data_barang:
        st.header("Data Barang")
        item_name = st.selectbox('Nama Barang', ['Gelas', 'Botol'])
        item_code = st.text_input('Kode Barang')

    with col_data_stok:
        st.header("Data Stok")
        initial_stock = st.number_input('Stok Awal', min_value=0)
        production_stock = st.number_input('Stok Produksi', min_value=0)
        taken_stock = st.number_input('Stok Diambil', min_value=0)

    if st.button('Simpan Data'):
        if item_name and item_code and initial_stock is not None and production_stock is not None and taken_stock is not None:
            tz = pytz.timezone('Asia/Jakarta')
            current_time = datetime.now(tz)
            current_stock = initial_stock + production_stock - taken_stock
            st.session_state['data'].append({
                'Tanggal': current_time.strftime("%Y-%m-%d"),
                'Waktu': current_time.strftime("%H:%M:%S"),
                'Nama Barang': item_name,
                'Kode Barang': item_code,
                'Stok Awal': initial_stock,
                'Stok Produksi': production_stock,
                'Stok Diambil': taken_stock,
                'Stok Saat Ini': current_stock,
                'Selisih': current_stock - initial_stock
            })
            st.success('Data Berhasil disimpan!')
        else:
            st.error('Mohon isi semua kolom!')

# Fungsi untuk halaman tabel data logistik
def table_data():
    st.title("Tabel Data Logistik")
    if st.session_state['data']:
        df = pd.DataFrame(st.session_state['data'])
        df['Tanggal'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m-%d')
        df['Gap'] = np.where(df['Selisih'] != 0, 'Ya', 'Tidak')
        st.table(df)
    else:
        st.write("Belum ada data yang disimpan.")

# Fungsi untuk halaman grafik tren logistik
def trend_graph():
    st.title("Grafik Tren Logistik")
    if st.session_state['data']:
        df = pd.DataFrame(st.session_state['data'])
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        df = df.sort_values('Tanggal')
        st.line_chart(df.set_index('Tanggal')['Selisih'])
    else:
        st.write("Belum ada data yang disimpan.")

# Inisialisasi session state untuk menyimpan data


# Navigasi sidebar menggunakan button
st.sidebar.title('Navigasi')
if st.sidebar.button("Informasi Stock"):
    st.session_state['page'] = "Informasi Stock"
if st.sidebar.button("Input Data Logistik"):
    st.session_state['page'] = "Input Data Logistik"
if st.sidebar.button("Tabel Data Logistik"):
    st.session_state['page'] = "Tabel Data Logistik"
if st.sidebar.button("Grafik Tren Logistik"):
    st.session_state['page'] = "Grafik Tren Logistik"

# Menampilkan halaman berdasarkan pilihan navigasi
if st.session_state['page'] == "Informasi Stock":
    stock_information()
elif st.session_state['page'] == "Input Data Logistik":
    logistic_data()
elif st.session_state['page'] == "Tabel Data Logistik":
    table_data()
elif st.session_state['page'] == "Grafik Tren Logistik":
    trend_graph()

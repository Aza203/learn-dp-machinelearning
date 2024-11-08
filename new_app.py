import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# Inisialisasi session state untuk menyimpan data dan status login
if 'data' not in st.session_state:
    st.session_state['data'] = []
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Fungsi untuk login
def login(username, password):
    # Contoh login sederhana, bisa diganti dengan autentikasi yang lebih kompleks
    if username == "admin" and password == "password":
        st.session_state['logged_in'] = True
        st.success("Login berhasil!")
    else:
        st.error("Username atau password salah")

# Halaman login
if not st.session_state['logged_in']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)
else:
    st.title('Dashboard Pengendalian Stok')

    st.sidebar.title('Navigasi')
    page = st.sidebar.radio("Pilih Halaman", ["Input Data", "Tabel Data", "Grafik Tren"])

    if page == "Input Data":
        st.title("Input Data Stok")
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

    elif page == 'Tabel Data':
        st.title('Tabel Data Stok')
        if st.session_state['data']:
            df = pd.DataFrame(st.session_state['data'])
            df['Tanggal'] = pd.to_datetime(df['Tanggal']).dt.strftime('%Y-%m-%d')
            df['Gap'] = np.where(df['Selisih'] != 0, 'Ya', 'Tidak')
            st.table(df)
        else:
            st.write("Belum ada data yang disimpan.")

    elif page == 'Grafik Tren':
        st.title('Grafik Tren Selisih Stok')
        if st.session_state['data']:
            df = pd.DataFrame(st.session_state['data'])
            df['Tanggal'] = pd.to_datetime(df['Tanggal'])
            df = df.sort_values('Tanggal')
            st.line_chart(df.set_index('Tanggal')['Selisih'])
        else:
            st.write("Belum ada data yang disimpan.")

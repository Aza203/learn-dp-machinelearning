import streamlit as st
import pandas as pd
from datetime import datetime

# Inisialisasi atau ambil nilai dari session state
if 'angka' not in st.session_state:
    st.session_state.angka = 0
if 'data' not in st.session_state:
    st.session_state.data = []

# Input nilai yang akan ditambahkan
nilai_tambah = st.number_input('Masukkan nilai yang akan ditambahkan:', min_value=0, step=1)

# Input nomor batch
nomor_batch = st.text_input('Masukkan nomor batch:')

# Tombol submit
if st.button('Submit'):
    # Tambahkan nilai input ke nilai yang ada
    st.session_state.angka += nilai_tambah
    
    # Simpan detail ke dalam session state
    st.session_state.data.append({
        'Tanggal': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Nomor Batch': nomor_batch,
        'Nilai Tambah': nilai_tambah
    })

# Tampilkan hasil dalam bentuk persegi
st.markdown(f"""
    <div style='display: flex; justify-content: center; align-items: center; height: 100px; width: 100px; background-color: lightgray; border: 2px solid black; border-radius: 10px;'>
        <h2 style='margin: 0;'>{st.session_state.angka}</h2>
    </div>
    """, unsafe_allow_html=True)

# Tampilkan tabel detail
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.table(df)

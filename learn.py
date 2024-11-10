import streamlit as st

# Inisialisasi atau ambil nilai dari session state
if 'angka' not in st.session_state:
    st.session_state.angka = 0

# Input nilai yang akan ditambahkan
nilai_tambah = st.number_input('Masukkan nilai yang akan ditambahkan:', min_value=0, step=1)

# Tambahkan nilai input ke nilai yang ada
st.session_state.angka += nilai_tambah

# Tampilkan hasil
st.write('Hasil penambahan:', st.session_state.angka)

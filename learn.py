import streamlit as st

# Input angka dari pengguna
angka = st.number_input('Masukkan angka:', min_value=0, step=1)

# Input nilai yang akan ditambahkan
nilai_tambah = st.number_input('Masukkan nilai yang akan ditambahkan:', min_value=0, step=1)

# Hasil penambahan
hasil = angka + nilai_tambah

# Tampilkan hasil
st.write('Hasil penambahan:', hasil)

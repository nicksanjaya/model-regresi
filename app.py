import streamlit as st

st.title("Form Pendaftaran Asuransi Kendaraan")

with st.form("form_asuransi_kendaraan"):
    st.header("🧍 Data Pribadi Pemohon")
    
    nama = st.text_input("Nama Lengkap")
    nik = st.text_input("NIK (Nomor Induk Kependudukan)")
    email = st.text_input("Email")
    no_hp = st.text_input("Nomor HP")
    alamat = st.text_area("Alamat Tempat Tinggal")

    st.header("🚗 Data Kendaraan")
    
    merk_kendaraan = st.text_input("Merk Kendaraan")
    model_kendaraan = st.text_input("Model / Tipe Kendaraan")
    tahun_kendaraan = st.selectbox("Tahun Pembuatan", list(range(2000, 2025)))
    nomor_polisi = st.text_input("Nomor Polisi")
    nomor_rangka = st.text_input("Nomor Rangka")
    nomor_mesin = st.text_input("Nomor Mesin")
    warna = st.text_input("Warna Kendaraan")
    jenis_asuransi = st.selectbox("Jenis Asuransi", ["All Risk", "Total Loss Only (TLO)"])

    # Tombol submit
    submitted = st.form_submit_button("Kirim Pendaftaran")

    if submitted:
        st.success("Pendaftaran berhasil dikirim!")
        st.write("### ✅ Ringkasan Data Pendaftaran")
        
        st.subheader("🔹 Data Pribadi")
        st.write(f"**Nama:** {nama}")
        st.write(f"**NIK:** {nik}")
        st.write(f"**Email:** {email}")
        st.write(f"**Nomor HP:** {no_hp}")
        st.write(f"**Alamat:** {alamat}")

        st.subheader("🔹 Data Kendaraan")
        st.write(f"**Merk:** {merk_kendaraan}")
        st.write(f"**Model:** {model_kendaraan}")
        st.write(f"**Tahun:** {tahun_kendaraan}")
        st.write(f"**Nomor Polisi:** {nomor_polisi}")
        st.write(f"**Nomor Rangka:** {nomor_rangka}")
        st.write(f"**Nomor Mesin:** {nomor_mesin}")
        st.write(f"**Warna:** {warna}")
        st.write(f"**Jenis Asuransi:** {jenis_asuransi}")

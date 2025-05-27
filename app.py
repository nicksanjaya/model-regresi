import streamlit as st

st.title("Form Pendaftaran Asuransi Kendaraan Bermotor")

# Form Input
with st.form("form_pendaftaran"):
    st.header("Data Penjual")
    penjual_nama = st.text_input("Nama Penjual")
    penjual_alamat = st.text_area("Alamat Penjual")

    st.header("Data Pembeli")
    pembeli_nama = st.text_input("Nama Pembeli")
    pembeli_ktp = st.text_input("Nomor KTP")
    pembeli_alamat = st.text_area("Alamat Pembeli")
    pembeli_telepon = st.text_input("Nomor Telepon")
    pembeli_email = st.text_input("Email")

    st.header("Data Kendaraan Bermotor")
    merk = st.text_input("Merk")
    model = st.text_input("Model")
    tipe = st.text_input("Tipe")
    plat_nomor = st.text_input("Nomor Plat")
    nomor_rangka = st.text_input("Nomor Rangka")
    nomor_mesin = st.text_input("Nomor Mesin")
    kapasitas_mesin = st.text_input("Kapasitas Mesin (cc)")
    tahun_mobil = st.number_input("Tahun Mobil", min_value=1980, max_value=2025, step=1)
    transmisi = st.selectbox("Tipe Transmisi", ["Manual", "Otomatis", "CVT"])
    warna = st.text_input("Warna")
    bahan_bakar = st.selectbox("Jenis Bahan Bakar", ["Bensin", "Diesel", "Listrik", "Hybrid"])
    jarak_tempuh = st.number_input("Jarak Tempuh (KM)", min_value=0)

    st.header("Detail Garansi & Asuransi")
    periode_garansi = st.text_input("Periode Garansi (misal: 1 tahun)")
    batas_jarak_tempuh = st.number_input("Batas Maksimum Jarak Tempuh (KM)", min_value=0)
    biaya_derek = st.number_input("Biaya Mobil Derek yang Ditanggung (Rp)", min_value=0)

    st.subheader("Batas Maksimum Kompensasi")
    st.text("• Jumlah Keseluruhan Klaim: Rp 50.000.000")
    st.text("• Batas Maksimum per Klaim: Rp 20.000.000")

    st.subheader("Komponen yang Ditanggung")
    komponen = [
        "Mesin Caroline",
        "Transmisi",
        "Sistem Kemudi",
        "Sistem Pengereman",
        "Sistem Penggerak Roda",
        "Sistem Kelistrikan",
        "Pendingin (AC)"
    ]
    ditanggung = st.multiselect("Pilih Komponen yang Ditanggung", komponen, default=komponen)

    submitted = st.form_submit_button("Submit")

# Tampilan setelah Submit
if submitted:
    st.success("✅ Data berhasil disubmit! Berikut adalah ringkasan data Anda:")

    st.subheader("📌 Data Penjual")
    st.write(f"**Nama:** {penjual_nama}")
    st.write(f"**Alamat:** {penjual_alamat}")

    st.subheader("📌 Data Pembeli")
    st.write(f"**Nama:** {pembeli_nama}")
    st.write(f"**Nomor KTP:** {pembeli_ktp}")
    st.write(f"**Alamat:** {pembeli_alamat}")
    st.write(f"**Telepon:** {pembeli_telepon}")
    st.write(f"**Email:** {pembeli_email}")

    st.subheader("📌 Data Kendaraan")
    st.write(f"**Merk / Model / Tipe:** {merk} / {model} / {tipe}")
    st.write(f"**Nomor Plat:** {plat_nomor}")
    st.write(f"**Nomor Rangka / Mesin:** {nomor_rangka} / {nomor_mesin}")
    st.write(f"**Kapasitas Mesin:** {kapasitas_mesin} cc")
    st.write(f"**Tahun Mobil:** {tahun_mobil}")
    st.write(f"**Transmisi:** {transmisi}")
    st.write(f"**Warna:** {warna}")
    st.write(f"**Bahan Bakar:** {bahan_bakar}")
    st.write(f"**Jarak Tempuh:** {jarak_tempuh:,} KM")

    st.subheader("📌 Informasi Garansi & Asuransi")
    st.write(f"**Periode Garansi:** {periode_garansi}")
    st.write(f"**Batas Jarak Tempuh Maksimal:** {batas_jarak_tempuh:,} KM")
    st.write(f"**Biaya Derek Ditanggung:** Rp {biaya_derek:,}")
    st.write("**Batas Kompensasi:**")
    st.write("- Jumlah Keseluruhan Klaim: Rp 50.000.000")
    st.write("- Maksimum per Klaim: Rp 20.000.000")
    st.write("**Komponen yang Ditanggung:**")
    for item in ditanggung:
        st.write(f"- {item}")

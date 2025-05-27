import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Pendaftaran Asuransi", layout="wide")
st.title("🚗 Pendaftaran Asuransi Kendaraan")

with st.form("form_asuransi"):

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Data Penjual")
        penjual_nama = st.text_input("Nama Penjual")
        penjual_alamat = st.text_area("Alamat Penjual", height=50)

        st.subheader("🙍‍♂️ Data Pembeli")
        pembeli_nama = st.text_input("Nama Pembeli")
        pembeli_ktp = st.text_input("Nomor KTP")
        pembeli_alamat = st.text_area("Alamat Pembeli", height=50)
        pembeli_telepon = st.text_input("Nomor Telepon")
        pembeli_email = st.text_input("Email")

        st.subheader("📆 Garansi & Kompensasi")
        tanggal_mulai = st.date_input("Tanggal Mulai Garansi", value=date.today())
        tanggal_berakhir = tanggal_mulai + timedelta(days=365 - 1)
        st.markdown(f"🗓️ **Tanggal Berakhir Garansi:** {tanggal_berakhir.strftime('%d %B %Y')}")
        batas_jarak_tempuh = st.number_input("Batas Jarak Tempuh (KM)", min_value=0)
        biaya_derek = 700000
        st.markdown(f"🚚 **Biaya Mobil Derek yang Ditanggung:** Rp {biaya_derek:,}")
        komponen = [
            "Mesin Caroline", "Transmisi", "Sistem Kemudi", "Sistem Pengereman",
            "Sistem Penggerak Roda", "Sistem Kelistrikan", "Pendingin (AC)"
        ]
        ditanggung = st.multiselect("Komponen yang Ditanggung", komponen, default=komponen)

    with col2:
        st.subheader("🚘 Data Kendaraan")
        merk = st.text_input("Merk")
        model = st.text_input("Model")
        tipe = st.text_input("Tipe")
        plat_nomor = st.text_input("Nomor Plat")
        nomor_rangka = st.text_input("Nomor Rangka")
        nomor_mesin = st.text_input("Nomor Mesin")
        kapasitas_mesin = st.text_input("Kapasitas Mesin (cc)")
        tahun_mobil = st.number_input("Tahun Mobil", min_value=1980, max_value=2025)
        transmisi = st.selectbox("Transmisi", ["Manual", "Otomatis", "CVT"])
        warna = st.text_input("Warna")
        bahan_bakar = st.selectbox("Bahan Bakar", ["Bensin", "Diesel", "Listrik", "Hybrid"])
        jarak_tempuh = st.number_input("Jarak Tempuh (KM)", min_value=0)

    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("✅ Data Berhasil Disubmit!")

    with st.expander("📄 Lihat Ringkasan Data"):
        st.markdown("### Data Penjual & Pembeli")
        st.write(f"**Penjual:** {penjual_nama} - {penjual_alamat}")
        st.write(f"**Pembeli:** {pembeli_nama} | KTP: {pembeli_ktp}")
        st.write(f"Alamat: {pembeli_alamat}, Telp: {pembeli_telepon}, Email: {pembeli_email}")

        st.markdown("### Data Kendaraan")
        st.write(
            f"{merk} {model} {tipe}, Plat: {plat_nomor}, Tahun: {tahun_mobil}, {kapasitas_mesin}cc, {warna}, {transmisi}, {bahan_bakar}, {jarak_tempuh:,} KM"
        )
        st.write(f"Nomor Rangka: {nomor_rangka}, Nomor Mesin: {nomor_mesin}")

        st.markdown("### Garansi & Kompensasi")
        st.write(f"Periode Garansi: {periode_garansi}")
        st.write(f"Batas Jarak Tempuh: {batas_jarak_tempuh:,} KM")
        st.write(f"Biaya Derek Ditanggung: Rp {biaya_derek:,}")
        st.write("**Batas Maksimum Kompensasi:**")
        st.write("- Total Klaim: Rp 50.000.000")
        st.write("- Per Klaim: Rp 20.000.000")
        st.write("**Komponen yang Ditanggung:**")
        st.write(", ".join(ditanggung))

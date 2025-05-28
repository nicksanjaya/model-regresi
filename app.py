import streamlit as st
from datetime import date, timedelta
import pandas as pd
import random

# Konfigurasi halaman
st.set_page_config(page_title="Pendaftaran Asuransi", layout="wide")
st.title("🚗 Pendaftaran Asuransi Kendaraan")

# Fungsi format tanggal Indonesia
def format_tanggal(tgl):
    bulan_id = {
        "January": "Januari", "February": "Februari", "March": "Maret", "April": "April",
        "May": "Mei", "June": "Juni", "July": "Juli", "August": "Agustus",
        "September": "September", "October": "Oktober", "November": "November", "December": "Desember"
    }
    return tgl.strftime(f"%-d {bulan_id[tgl.strftime('%B')]} %Y")

# Inisialisasi session state untuk menyimpan klaim
if "daftar_klaim" not in st.session_state:
    st.session_state.daftar_klaim = []

# Kredit limit tetap
kredit_limit_awal = 50000000

# Form input
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
        transmisi = st.selectbox("Transmisi", ["Manual", "Otomatis"])
        warna = st.text_input("Warna")
        bahan_bakar = st.selectbox("Bahan Bakar", ["Bensin", "Diesel", "Listrik"])
        jarak_tempuh = st.number_input("Jarak Tempuh (KM)", min_value=0)

    submitted = st.form_submit_button("Submit")

# ==============================
# TAMPILAN RINGKASAN SETELAH SUBMIT
# ==============================
if submitted:
    st.success("✅ Data Berhasil Disubmit!")

    # Perhitungan otomatis
    tanggal_berakhir = tanggal_mulai + timedelta(days=364)
    batas_jarak_tempuh = jarak_tempuh + 50000
    biaya_derek = 700000
    nomor_polis = f"POLIS-2025-{random.randint(1000,9999)}"
    nomor_sertifikat = f"CERT-2025-{random.randint(1000,9999)}"

    # Data untuk ditampilkan dalam tabel
    data_ringkasan = {
        "Informasi": [
            "Nomor Polis",
            "Nomor Sertifikat",
            "Nama Penjual",
            "Alamat Penjual",
            "Nama Pembeli",
            "Nomor KTP",
            "Alamat Pembeli",
            "Nomor Telepon",
            "Email",
            "Merk / Model / Tipe",
            "Plat Nomor",
            "Nomor Rangka",
            "Nomor Mesin",
            "Kapasitas Mesin (cc)",
            "Tahun Mobil",
            "Transmisi",
            "Warna",
            "Bahan Bakar",
            "Jarak Tempuh (KM)",
            "Batas Jarak Tempuh (KM)",
            "Periode Garansi",
            "Komponen Ditanggung",
            "Biaya Mobil Derek",
            "Batas Maksimum Jumlah Keseluruhan Klaim",
            "Batas Maksimum per Klaim"
        ],
        "Detail": [
            nomor_polis,
            nomor_sertifikat,
            penjual_nama,
            penjual_alamat,
            pembeli_nama,
            pembeli_ktp,
            pembeli_alamat,
            pembeli_telepon,
            pembeli_email,
            f"{merk} / {model} / {tipe}",
            plat_nomor,
            nomor_rangka,
            nomor_mesin,
            kapasitas_mesin,
            tahun_mobil,
            transmisi,
            warna,
            bahan_bakar,
            f"{jarak_tempuh:,} KM",
            f"{batas_jarak_tempuh:,} KM",
            f"{format_tanggal(tanggal_mulai)} – {format_tanggal(tanggal_berakhir)}",
            ", ".join(ditanggung),
            f"Rp {biaya_derek:,}",
            f"Rp {kredit_limit_awal:,}",
            "Rp 20.000.000"
        ]
    }

    # Tampilkan dalam bentuk tabel
    df_ringkasan = pd.DataFrame(data_ringkasan)
    st.subheader("📄 Sertifikat Asuransi Kendaraan")
    st.table(df_ringkasan)

    # ==============================
    # INPUT BIAYA KLAIM
    # ==============================
    st.subheader("💰 Input Biaya Klaim")

    total_klaim_terpakai = sum([
        int(k["Biaya Klaim (Rp)"].replace("Rp", "").replace(",", "").strip())
        for k in st.session_state.daftar_klaim
    ])
    sisa_kredit_limit = kredit_limit_awal - total_klaim_terpakai

    with st.form("form_klaim"):
        col1, col2, col3 = st.columns(3)
        with col1:
            klaim_tanggal = st.date_input("Tanggal Klaim", value=date.today(), key="klaim_tanggal")
        with col2:
            klaim_biaya = st.number_input("Biaya Klaim (Rp)", min_value=0, max_value=sisa_kredit_limit, step=100000, key="klaim_biaya")
        with col3:
            klaim_nomor_invoice = st.text_input("Nomor Invoice", key="klaim_nomor_invoice")

        klaim_vendor = st.text_input("Nama Vendor", key="klaim_vendor")

        st.markdown(f"**Kredit Limit Tersisa:** Rp {sisa_kredit_limit:,}")

        submit_klaim = st.form_submit_button("Simpan Biaya Klaim")

    if submit_klaim:
        klaim_data = {
            "Tanggal Klaim": format_tanggal(klaim_tanggal),
            "Biaya Klaim (Rp)": f"Rp {klaim_biaya:,}",
            "Nomor Invoice": klaim_nomor_invoice,
            "Nama Vendor": klaim_vendor,
            "Kredit Limit Tersisa": f"Rp {sisa_kredit_limit - klaim_biaya:,}"
        }
        st.session_state.daftar_klaim.append(klaim_data)
        st.success("📌 Biaya klaim berhasil disimpan!")

    # Tampilkan daftar semua klaim
    if st.session_state.daftar_klaim:
        st.subheader("📑 Riwayat Biaya Klaim")
        df_klaim_all = pd.DataFrame(st.session_state.daftar_klaim)
        st.dataframe(df_klaim_all, use_container_width=True)

        total_klaim_terpakai = sum([
            int(k["Biaya Klaim (Rp)"].replace("Rp", "").replace(",", "").strip())
            for k in st.session_state.daftar_klaim
        ])
        sisa_kredit_limit = kredit_limit_awal - total_klaim_terpakai

        st.markdown(f"### 💼 Total Klaim Digunakan: **Rp {total_klaim_terpakai:,}**")
        st.markdown(f"### 💳 Sisa Kredit Limit: **Rp {sisa_kredit_limit:,}**")

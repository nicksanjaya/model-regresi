import streamlit as st

st.title("Form Data Pribadi")

with st.form("data_pribadi_form"):
    st.header("Silakan isi data pribadi Anda")

    nama = st.text_input("Nama Lengkap")
    tanggal_lahir = st.date_input("Tanggal Lahir")
    jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan", "Lainnya"])
    email = st.text_input("Email")
    no_telepon = st.text_input("Nomor Telepon")
    alamat = st.text_area("Alamat Lengkap")

    # Tombol submit
    submitted = st.form_submit_button("Kirim")

    if submitted:
        st.success("Data berhasil dikirim!")
        st.write("### Data yang Anda masukkan:")
        st.write(f"**Nama:** {nama}")
        st.write(f"**Tanggal Lahir:** {tanggal_lahir}")
        st.write(f"**Jenis Kelamin:** {jenis_kelamin}")
        st.write(f"**Email:** {email}")
        st.write(f"**Nomor Telepon:** {no_telepon}")
        st.write(f"**Alamat:** {alamat}")

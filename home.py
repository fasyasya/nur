
import streamlit as st


st.set_page_config(
    page_title="Portfolio | fasya",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("sya.JPG", width= 300)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA :   FASYA NURKHAYATI")
   st.caption("NIM : 0402201092")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 14 Juni 2002 
            - Alamat               : siwuluh bulakamba brebes
            - Hobi                 : makan dan tidur
            - Cita-cita            : guru
            - Hal yang disukai     : ngledek orang:>
            - Status               : masihh jomlo fisabililah
            """
        )
st.header("*Call Me If You Want*")
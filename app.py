import streamlit as st
from streamlit_option_menu import option_menu
from halaman import beranda, klasifikasi

st.set_page_config(
    page_title='Klasifikasi Berita',
    layout='wide',
)

# session states
# satu judul
if 'judul' not in st.session_state:
    st.session_state['judul'] = ""
if 'hasil_judul' not in st.session_state:
    st.session_state['hasil_judul'] = None
if 'grafik' not in st.session_state:
    st.session_state['grafik'] = None
if 'tabel_hasil' not in st.session_state:
    st.session_state['tabel_hasil'] = None
# file
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'kolom_kolom' not in st.session_state:
    st.session_state['kolom_kolom'] = None
if 'kolom_judul' not in st.session_state:
    st.session_state['kolom_judul'] = None
if 'df_judul' not in st.session_state:
    st.session_state['df_judul'] = None
if 'df_hasil' not in st.session_state:
    st.session_state['df_hasil'] = None

st.markdown('# Aplikasi Klasifikasi Berita Bahasa Inggris')

# Menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Beranda', 'Klasifikasi'],
        default_index=0,
        orientation='vertical',
        icons=['house', 'card-text']
    )

if selected == "Beranda":
    beranda.app()
if selected == "Klasifikasi":
    klasifikasi.app()
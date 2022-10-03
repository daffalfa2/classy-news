import streamlit as st
import pandas as pd

def app():
    st.markdown(''' 

    ---

    Website ini berguna untuk melakukan **klasifikasi judul berita berbahasa inggris** ke dalam empat kategori, yaitu: BUSINESS, SCIENCE AND TECHNOLOGY, ENTERTAINMENT, dan HEALTH.

    Pengklasifikasian data dilakukan dengan menggunakan model *Bidirectional Encoder Representations from Transformers* (BERT) yang telah dilatih dengan dataset UCI.
    Dalam pelatihan model digunakan *hyperparameter* sebagai berikut:

    | *Hyperparameter* | Nilai |
    | ----------- | ----------- |
    | *Batch Size* | 16 |
    | Epoch | 2 |
    | Optimizer | Adam |
    | Learning Rate | 3e-5 |

    ''')

    st.write('')
    st.markdown('''
    ## Apa itu BERT?
    BERT adalah arstektur model pre-trained yang di rancang dengan fitur untuk mempertimbangkan konteks kata dengan membaca kata yang bersebelahan dengan kata yang di pelajari. Dengan kemampuan itu bert dapat meningkatkan hasil model *Natural Language Processing* (NLP), seperti klasifikasi teks.
    ''')

    st.markdown('''
    ## Cara Menggunakan Aplikasi
    ##### Klasifikasi **Satu** Judul Artikel Berita:
    1. Pilihlah menu "Klasifikasi"
    2. Pilihlah tab "Satu Judul"
    3. Ketiklah judul artikel berita berbahasa inggris yang ingin diklasifikasi ke dalam *text box* yang tersedia
    4. Tekan tombol "Prediksi"

    ##### Klasifikasi **Banyak** Judul Artikel Berita:
    1. Pilihlah menu "Klasifikasi"
    2. Pilihlah tab "Banyak Judul"
    3. Masukkan file berbentuk xlsx atau csv yang berisikan judul-judul artikel berbahasa inggris 
    4. Pilihlah kolom judul yang akan diprediksi
    5. Tekan tombol "Prediksi"
    ''')
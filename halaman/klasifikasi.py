import streamlit as st
import pandas as pd
from bert import prediksi

def read_df(file):
    try:
        df = pd.read_excel(file)
    except:
        df = pd.read_csv(file)
    return df

def handle_click_judul(judul):
    st.session_state['judul'] = judul
    st.session_state['hasil_judul'] = None

def handle_click_file(df_judul, kolom_judul):
    st.session_state['df_judul'] = df_judul
    st.session_state['df_hasil'] = None
    st.session_state['kolom_judul'] = kolom_judul

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

def app():
    tab_judul, tab_file = st.tabs(['Satu Judul', 'Banyak judul'])
    tokenizer = prediksi.load_tokenizer()
    model = prediksi.load_model()
    classes=['BUSINESS', 'SCIENCE AND TECHNOLOGY', 'ENTERTAINMENT', 'HEALTH']

    with tab_judul:
        judul = st.text_area('Masukkan Judul', value=st.session_state['judul'])
        
        judul_button = st.button(
            label="Prediksi",
            key="prediksi_judul",
            on_click=handle_click_judul,
            args=[judul]
        )

        # prediksi
        if st.session_state['judul'] == "":
            st.write("")
        else:
            st.write('Judul yang akan diprediksi:', st.session_state['judul'])
            with st.spinner('Prediksi data...'):
                if st.session_state['hasil_judul'] is None:
                    result, graph, probs_df = prediksi.predict_one(
                        judul=st.session_state['judul'],
                        tokenizer=tokenizer,
                        model=model,
                        classes=classes
                    )
                    st.session_state['hasil_judul'] = result   
                    st.session_state['grafik'] = graph  
                    st.session_state['tabel_hasil'] = probs_df  
                st.success(st.session_state['hasil_judul']) 
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(st.session_state['grafik'], use_container_width=True)
                with col2:
                    st.dataframe(st.session_state['tabel_hasil'])
                    

    with tab_file:
        file_judul = st.file_uploader(
            label="Unggah file excel atau csv",
            type=['xlsx', 'csv'],
            accept_multiple_files=False
        )

        if file_judul is not None:
            # if st.session_state['df'] is None:
            df = read_df(file_judul)
            columns = df.columns
            st.session_state['df'] = df
            st.session_state['kolom_kolom'] = columns

        if st.session_state['df'] is not None:
            try:
                print('AMAN')
                st.dataframe(st.session_state['df'])

                st.warning('Pilihlah kolom yang akan dianalisis lalu klik tombol \"Prediksi\"')

                col1, col2 = st.columns([1,2])
                with col1:
                    kolom_judul = st.radio(
                        "Pilih kolom untuk dianalisis (judul):",
                        st.session_state['kolom_kolom'])
                    st.write('Kolom yang akan dianalisis: ', kolom_judul)
                with col2:
                    df_judul = st.session_state['df'][[kolom_judul]].copy()
                    # st.write(type(df_judul))
                    st.dataframe(df_judul)
                
                file_button = st.button(
                    label="Prediksi",
                    key="prediksi_file",
                    on_click=handle_click_file,
                    args=[df_judul, kolom_judul]
                )
            except Exception as e:
                print('ERRORNYA INI:')
                print(e)
                st.write("")
        
        if st.session_state['df_judul'] is not None:
            df_hasil = st.session_state['df_judul'].copy()
            
            with st.spinner('Prediksi data-data...'):
                if st.session_state['df_hasil'] is None:
                    prediksi.predict_many(
                        df=df_hasil,
                        kolom=st.session_state['kolom_judul'],
                        tokenizer=tokenizer,
                        model=model,
                        classes=classes
                    )
                    st.session_state['df_hasil'] = df_hasil

            st.write("HASIL PREDIKSI:")
            st.dataframe(st.session_state['df_hasil'])

            # with st.expander("Lihat Penjelasan"):
            #     st.markdown('*Recall*: bcakbsjkdbasjkbdjkasbdjkasbdjksabkjdbak')

            csv = convert_df(st.session_state['df_hasil'])
            st.download_button(
                label='Download Hasil Prediksi',
                data=csv,
                file_name="hasil_prediksi.csv",
                mime='csv'
            )
            
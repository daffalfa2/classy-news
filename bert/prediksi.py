import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer
import plotly.express as px
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

# load model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('bert/model_Adam_batch16_NoDropout')
    return model

@st.cache(allow_output_mutation=True)
def load_tokenizer():
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    return tokenizer

def prepare_data(title, tokenizer):
    token = tokenizer.encode_plus(
        title,
        max_length=256,
        truncation=True,
        padding='max_length',
        add_special_tokens=True,
        return_tensors='tf'
    )
    return {
        'input_ids': tf.cast(token.input_ids, tf.float64),
        'attention_mask': tf.cast(token.attention_mask, tf.float64)
    }

def make_prediction(model, processed_data, classes):
    probs = model.predict(processed_data)[0]
    return probs, classes[np.argmax(probs)]

def predict_one(judul, tokenizer, model, classes):
    processed_data = prepare_data(judul, tokenizer)
    probs, result = make_prediction(model, processed_data, classes)
    # result = classes[np.argmax(probs)]

    # tabel
    probs = probs.tolist()
    probs_dict = {'Kategori':classes, 'Persentase':probs}
    probs_df = pd.DataFrame(probs_dict)
    highlight = lambda x: ['background: #fca435' if x.name in [np.argmax(probs)] else '' for i in x]
    # probs = probs_df.style.apply(highlight,axis=1)

    # bar chart
    fig = px.bar(
        probs_df,
        x='Kategori',
        y='Persentase',
        color_discrete_sequence=["#fca435"],
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return result,fig,probs_df.style.apply(highlight,axis=1)

def predict_many(df, kolom, tokenizer, model, classes):
    df['Hasil Prediksi'] = np.nan

    for i, title in enumerate(df[kolom]):
        processed_data = prepare_data(title, tokenizer)
        probs, result = make_prediction(
            model=model,
            processed_data=processed_data,
            classes=classes
        )
        df['Hasil Prediksi'][i] = result
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Sayfa Ayarı
st.set_page_config(page_title="AI Summarizer", page_icon="📝")

# Modeli ve Tokenizer'ı en temel haliyle yükle
@st.cache_resource
def load_model_and_tokenizer():
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

st.title("📝 AI Text Summarizer")
st.write("### NLP Project 3: Final Piece")

# Yükleme ekranı
with st.spinner('Yapay Zeka Modeli Yükleniyor...'):
    tokenizer, model = load_model_and_tokenizer()

st.info("İngilizce metni yapıştırın ve 'Özetle' butonuna basın.")

# Giriş kutusu
user_input = st.text_area("Metin Girişi:", height=200)

if st.button("Özetle"):
    if user_input:
        with st.spinner('Özet oluşturuluyor...'):
            # Metni modelin anlayacağı sayılara (token) çevir
            inputs = tokenizer([user_input], max_length=1024, return_tensors="pt", truncation=True)
            
            # Özeti üret (Pipeline kullanmadan doğrudan modelden)
            summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=150, early_stopping=True)
            
            # Sayıları tekrar metne çevir
            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            
            st.markdown("---")
            st.subheader("Sonuç:")
            st.success(summary)
    else:
        st.warning("Lütfen bir metin girin!")

st.caption("21-Project Portfolio - NLP Final")

import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('fake_account_model.pkl')

st.set_page_config(page_title="Fake Account Detector", page_icon="🕵️")
st.title("🕵️ Fake Account Detector")
st.write("### Classification Project 3: Social Media Analysis")

st.info("Profil bilgilerini girerek hesabın güvenilirliğini analiz edin.")

# Kullanıcı Girişleri
col1, col2 = st.columns(2)

with col1:
    followers = st.number_input("Takipçi Sayısı", 0, 1000000, 500)
    following = st.number_input("Takip Edilen Sayısı", 0, 1000000, 1000)
with col2:
    posts = st.number_input("Gönderi Sayısı", 0, 10000, 50)
    pic = st.radio("Profil Resmi Var mı?", ["Evet", "Hayır"])

# Sayısallaştırma
pic_val = 1 if pic == "Evet" else 0

if st.button("Hesabı Analiz Et"):
    input_data = np.array([[followers, following, posts, pic_val]])
    prediction = model.predict(input_data)
    
    st.markdown("---")
    if prediction[0] == 1:
        st.error("🚨 **DİKKAT:** Bu hesap yüksek ihtimalle **SAHTE (BOT)**.")
    else:
        st.success("✅ **GÜVENLİ:** Bu hesap gerçek bir kullanıcıya benziyor.")

st.caption("21-Project Portfolio - Classification Series 3/3")
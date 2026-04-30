import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📚 AI Book Recommender")
st.write("### Deep Learning: Proje 1 (Similarity Learning)")

# Kitap Veri Seti
data = {
    'Kitap_Adi': ['1984', 'Cesur Yeni Dünya', 'Suç ve Ceza', 'Sherlock Holmes', 'Yüzüklerin Efendisi', 'Harry Potter'],
    'Ozet': [
        'Dystopian political fiction surveillance big brother', 
        'Dystopian future genetic engineering society', 
        'Psychological drama crime guilt morality', 
        'Detective mystery crime investigation London', 
        'Fantasy adventure epic ring magic', 
        'Fantasy magic school wizard adventure'
    ]
}
df = pd.DataFrame(data)

# Yapay Zeka İşlemi
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['Ozet'])
sim = cosine_similarity(matrix)

book = st.selectbox("Beğendiğiniz bir kitabı seçin:", df['Kitap_Adi'])

if st.button("Benzer Kitap Öner ✨"):
    idx = df[df['Kitap_Adi'] == book].index[0]
    scores = sorted(list(enumerate(sim[idx])), key=lambda x: x[1], reverse=True)[1:3]
    
    st.subheader("Bunu sevenler bunları da okudu:")
    for i in scores:
        st.success(f"📖 **{df['Kitap_Adi'].iloc[i[0]]}** (Benzerlik: %{i[1]*100:.1f})")
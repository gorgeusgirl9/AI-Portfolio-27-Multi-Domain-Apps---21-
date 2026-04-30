import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Recommender", layout="centered")

st.title("🎬 AI Content Recommender")
st.write("### Deep Learning & Similarity Learning: Proje 35")

# 1. VERİ SETİ
data = {
    'Title': [
        'Inception', 'The Dark Knight', 'Interstellar', 
        'The Godfather', 'Pulp Fiction', 'The Matrix', 
        'Avatar', 'Star Wars', 'Avengers: Endgame', 'Joker'
    ],
    'Genre': [
        'Sci-Fi Action Mind-bending', 'Action Crime Drama', 'Sci-Fi Adventure Space',
        'Crime Drama Classic', 'Crime Drama Cult', 'Sci-Fi Action Cyberpunk',
        'Sci-Fi Adventure Alien', 'Sci-Fi Adventure Space', 'Action Adventure Heroes', 'Crime Drama Thriller'
    ]
}
df = pd.DataFrame(data)

# 2. YAPAY ZEKA MANTIĞI
# Metinleri sayısal vektörlere (TF-IDF) çeviriyoruz
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Genre'])

# Vektörler arasındaki açısal benzerliği (Cosine Similarity) hesapla
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 3. ARAYÜZ
st.info("Bu sistem, içeriklerin türlerini (Genre) vektör uzayında analiz ederek birbirine en yakın olanları bulur.")

selected_movie = st.selectbox("Beğendiğiniz bir film seçin:", df['Title'].values)

if st.button("Benzerlerini Öner ✨"):
    idx = df[df['Title'] == selected_movie].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    # En benzer 3 tanesini seç (kendisi hariç)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4] 
    
    st.divider()
    st.subheader("🤖 Yapay Zeka Önerileri:")
    for i in sim_scores:
        score_percent = i[1] * 100
        st.success(f"🎥 **{df['Title'].iloc[i[0]]}** - Benzerlik Skoru: %{score_percent:.1f}")

st.divider()
st.caption("Content-Based Filtering | Cosine Similarity Matrix | 2026")
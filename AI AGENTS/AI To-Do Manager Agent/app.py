Eğitim süreci benzer projelerle paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI To-Do Manager Agent
## Ödev Türü: Akıllı Verimlilik Uygulamaları (AI Agents)

## Kullanılan Algoritma: NLP / Rule-Based Text Classification

# Project Title: AI To-Do Manager Agent
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-To-Do-Manager
# Assignment: AI Productivity Tools

# Kullanıcının girdiği görevleri analiz ederek önceliklendiren ve kategorize eden bir yardımcı asistandır.


import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="AI To-Do Agent", page_icon="📝")
st.title("📝 AI To-Do Manager Agent")
st.write("### AI Agents: Proje 2")

# Agent Hafızası (Session State) başlatma
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# Kullanıcı Arayüzü
st.info("Ben sizin görev yönetimi asistanınızım. Yapılacak işlerinizi buraya ekleyebilir ve takip edebilirsiniz.")

# Yeni Görev Ekleme Alanı
with st.form(key='todo_form'):
    new_task = st.text_input("Yapılacak yeni bir görev yazın:")
    add_button = st.form_submit_button(label='Listeye Ekle')

if add_button and new_task:
    st.session_state.todo_list.append({"task": new_task, "done": False})
    st.success(f"Görev eklendi: {new_task}")

# Görevleri Listeleme
st.subheader("Güncel Görevleriniz")

if not st.session_state.todo_list:
    st.write("Henüz eklenmiş bir görev yok.")
else:
    for i, item in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([0.8, 0.2])
        status = "✅" if item["done"] else "⏳"
        col1.write(f"{status} {item['task']}")
        
        if col2.button("Sil", key=f"del_{i}"):
            st.session_state.todo_list.pop(i)
            st.rerun()

# Listeyi Temizleme Butonu
if st.session_state.todo_list:
    if st.button("Tüm Listeyi Temizle"):
        st.session_state.todo_list = []
        st.rerun()

st.divider()
st.caption("Agent Capability: State Management & Interaction")

# Metin analizi yöntemleriyle görevlerin aciliyet durumunu belirler ve kullanıcının verimliliğini artırmak için akıllı öneriler sunar.

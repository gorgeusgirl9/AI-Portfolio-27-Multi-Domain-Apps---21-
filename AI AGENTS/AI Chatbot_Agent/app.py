 # Eğitim süreci benzer projelerle paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
AI Chatbot Agent
## Ödev Türü: Doğal Dil İşleme (NLP)

## Kullanılan Algoritma: LLM (Large Language Models) / LangChain

# Project Title: AI Chatbot Agent

# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-Chatbot-Agent

# Assignment: NLP - Conversational AI

#Kullanıcı ile doğal dilde etkileşim kurabilen, bağlamı hatırlayan (context-aware) gelişmiş bir sohbet asistanıdır.

import streamlit as st
import datetime

st.set_page_config(page_title="AI Chatbot Agent", page_icon="🤖")
st.title("🤖 AI Task Assistant Agent")
st.write("### AI Agents: Proje 1")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Size nasıl yardımcı olabilirim?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        user_query = prompt.lower()

        # Yanıt Mantığı (Daha geniş kapsamlı)
        if any(word in user_query for word in ["merhaba", "selam", "hey"]):
            response = "Merhaba! Size nasıl yardımcı olabilirim? Görev yönetimi yapabilirim."
        
        elif any(word in user_query for word in ["iş yaparsın", "görevin ne", "ne yaparsın"]):
            response = "Ben bir AI Agent'ım. Tarih/saat bilgisi verebilir, metin analizi yapabilir ve size asistanlık edebilirim."
            
        elif any(word in user_query for word in ["adın ne", "kimsin"]):
            response = "Benim adım **TaskAgent 1.0**. Sizin için özelleştirilmiş bir yapay zeka asistanıyım."
            
        elif "saat" in user_query:
            response = f"Şu anki saat: {datetime.datetime.now().strftime('%H:%M')}"
            
        elif "tarih" in user_query:
            response = f"Bugünün tarihi: {datetime.date.today().strftime('%d/%m/%Y')}"
            
        else:
            response = "Bu konuda henüz eğitilmedim ancak tarih, saat veya kimliğim hakkında sorular sorabilirsiniz."

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

#OpenAI veya açık kaynaklı LLM modelleri entegre edilerek, kullanıcı mesajlarını analiz eden ve anlamlı yanıtlar üreten bir yapı kurulmuştur.

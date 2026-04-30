import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
from datetime import datetime

st.set_page_config(page_title="AI System Monitor", layout="wide")
st.title("🖥️ AI System Health & Resource Monitor")
st.write("### Data Visualization: Proje 27/30 (Canlı Veri Akışı)")

# Sidebar ayarları
st.sidebar.header("İzleme Ayarları")
update_speed = st.sidebar.slider("Güncelleme Hızı (Saniye):", 0.5, 5.0, 1.0)
history_limit = 20 # Grafikte görünecek son veri sayısı

# Session state ile veriyi saklayalım
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Zaman': [datetime.now().strftime("%H:%M:%S")],
        'CPU_Yuku': [np.random.randint(20, 40)],
        'Bellek_Kullanimi': [np.random.randint(40, 60)]
    })

# Sayfayı canlı güncellemek için bir yer tutucu (placeholder)
placeholder = st.empty()

# Canlı akış döngüsü
for _ in range(100): # Simülasyon için 100 adım
    # Yeni veri üret
    new_time = datetime.now().strftime("%H:%M:%S")
    new_cpu = np.random.randint(10, 90) # Dalgalı CPU yükü
    new_ram = np.random.randint(30, 70)
    
    # Veriyi güncelle
    new_row = pd.DataFrame({'Zaman': [new_time], 'CPU_Yuku': [new_cpu], 'Bellek_Kullanimi': [new_ram]})
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True).tail(history_limit)
    
    with placeholder.container():
        # Metrik Kartları
        col1, col2 = st.columns(2)
        col1.metric("Anlık CPU Yükü", f"%{new_cpu}", delta=f"{new_cpu - 50}%")
        col2.metric("Bellek Kullanımı", f"%{new_ram}", delta=f"{new_ram - 50}%", delta_color="inverse")
        
        # Zaman Serisi Grafiği
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.data['Zaman'], y=st.session_state.data['CPU_Yuku'],
                                 mode='lines+markers', name='CPU %', line=dict(color='firebrick', width=3)))
        fig.add_trace(go.Scatter(x=st.session_state.data['Zaman'], y=st.session_state.data['Bellek_Kullanimi'],
                                 mode='lines+markers', name='RAM %', line=dict(color='royalblue', width=3)))
        
        fig.update_layout(title="Sistem Kaynak Kullanımı (Canlı)", xaxis_title="Zaman", yaxis_title="Yüzde (%)",
                          height=500, template="plotly_white")
        
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(update_speed)
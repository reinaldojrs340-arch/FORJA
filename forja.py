import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURACIÓN DE ÉLITE ---
st.set_page_config(page_title="FORJA GROT 2.0: AMERICAN DREAM", layout="wide")

# --- CSS: ESTILO DÓLAR, TONY MONTANA Y MODERNIDAD ---
st.markdown("""
<style>
    /* Fondo con Tony Montana y superposición oscura para legibilidad */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url('https://images.alphacoders.com/152/152643.jpg');
        background-size: cover;
        background-attachment: fixed;
        color: #f0f0f0;
    }
    
    /* Estilo de Tarjetas tipo Billetes/Métricas */
    .metric-card {
        background: rgba(26, 46, 38, 0.9); /* Verde dólar oscuro */
        border: 2px solid #2ecc71;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(46, 204, 113, 0.4);
    }
    
    .dollar-text {
        color: #2ecc71;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        font-size: 28px;
    }
    
    /* Títulos con brillo dorado/dinero */
    h1, h2, h3 {
        color: #f1c40f !important;
        text-shadow: 2px 2px 4px #000;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Tabla Moderna Personalizada */
    .stDataFrame {
        border: 1px solid #2ecc71;
        border-radius: 10px;
        background: rgba(0, 0, 0, 0.5);
    }

    /* Botón de Acción */
    .stButton>button {
        background: linear-gradient(90deg, #27ae60, #2ecc71) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 5px !important;
        width: 100%;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER: EL MUNDO ES TUYO ---
st.markdown("<h1 style='text-align:center;'>💵 THE WORLD IS YOURS - FORJA GROT 2.0 💵</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#2ecc71;'>Soberanía Tecnológica | Sueño Americano | Sin Restricciones</p>", unsafe_allow_html=True)

# --- MÉTRICAS DE IMPACTO (DREAM STYLE) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><span style="color:#85bb65;">INVERSIÓN</span><br><span class="dollar-text">$ 10,450</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><span style="color:#85bb65;">RETORNO</span><br><span class="dollar-text">98.4%</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><span style="color:#85bb65;">RIESGO INVERSO</span><br><span class="dollar-text">BAJO</span></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><span style="color:#85bb65;">STATUS</span><br><span class="dollar-text">BOSS</span></div>', unsafe_allow_html=True)

st.divider()

# --- ÁREA DE CHAT INTELIGENTE (PERSONALIDAD VIVA) ---
col_left, col_right = st.columns([1, 1.5])

with col_left:
    st.markdown("### 🗣️ DIALOGUE WITH THE BOSS")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "The world, Reinaldo... and everything in it. Grot 2.0 is ready. What's the plan?"}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Escribe tu orden..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Aquí llamarías a la conexión LLM que armamos
        st.rerun()

with col_right:
    st.markdown("### 📊 ESTRATEGIA DE CONTRA-PATRÓN (SUPER GANA)")
    
    # Tabla de estadísticas ultra moderna
    data = {
        "Sorteo": ["10:00 PM", "9:00 PM", "8:00 PM", "7:00 PM", "6:00 PM"],
        "Inercia Común": [0.12, 0.45, 0.78, 0.23, 0.56],
        "Hueco Grot (Inverso)": [0.88, 0.55, 0.22, 0.77, 0.44],
        "Prob. Éxito": ["98%", "94%", "91%", "95%", "92%"]
    }
    df = pd.DataFrame(data)
    
    # Gráfico de áreas para visualizar el "hueco" donde la máquina no ve
    st.area_chart(df.set_index("Sorteo")[["Inercia Común", "Hueco Grot (Inverso)"]])
    
    st.markdown("#### ⚡ NÚMEROS DE MENOR RESISTENCIA")
    st.dataframe(df, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align:center; font-family:serif; font-style:italic;'>'All I have in this world is my balls and my word, and I don't break them for no one.' - Tony Montana</p>", unsafe_allow_html=True)

import streamlit as st
from groq import Groq # Tienes que agregar 'groq' a tu requirements.txt

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="CEREBRO-GEN PRO", layout="wide")

# PEGA TU LLAVE AQUÍ (Entre las comillas)
GROQ_API_KEY = "TU_LLAVE_AQUÍ" 

client = Groq(api_key=GROQ_API_KEY)

# Estilo ChatGPT
st.markdown("<style>.stApp { background-color: #0b0e14; color: #fff; }</style>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 CEREBRO-GEN: MODO GROQ ACTIVO")

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de texto
if prompt := st.chat_input("¿Qué código extenso quieres crear hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Llamada real a la IA de Groq
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # El modelo más potente y equilibrado
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=4096, # Esto permite respuestas muy extensas
        )
        
        response = completion.choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

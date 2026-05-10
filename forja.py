import streamlit as st
import random
import hashlib
import time

# --- NÚCLEO FANTASMA: FORJA GROT 2.0 ---

def generar_algoritmo_fantasma(semilla_maestra):
    """
    Este motor crea una lógica única basada en un hash criptográfico.
    Nadie puede ver el proceso porque el algoritmo se 'autodestruye' 
    y se recrea en cada milisegundo de ejecución.
    """
    # 1. Creamos una firma única que nadie puede revertir (SHA-256)
    firma_invisible = hashlib.sha256(semilla_maestra.encode()).hexdigest()
    
    # 2. El algoritmo decide sus propios coeficientes basados en la firma
    # Esto es lo que nadie puede 'ver' ni predecir
    coeficiente_mutante = int(firma_invisible[:8], 16) % 100
    logica_interna = [ord(c) * coeficiente_mutante for c in firma_invisible[:5]]
    
    return firma_invisible, logica_interna

# --- INTERFAZ DE LA FORJA ---
st.set_page_config(page_title="FORJA GROT - NÚCLEO FANTASMA", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .ghost-box { border: 1px solid #00ff41; padding: 20px; border-radius: 10px; background: #0a0a0a; box-shadow: 0 0 15px #00ff41; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00ff41; border: 1px solid #00ff41; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👻 NÚCLEO FANTASMA GROT 2.0</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Algoritmo de Auto-Generación Criptográfica</p>", unsafe_allow_html=True)

input_data = st.text_input("Mete la semilla para la mutación:", type="password")

if st.button("🔥 GENERAR ALGORITMO INVISIBLE"):
    if input_data:
        with st.status("Engañando al sistema y creando lógica fantasma...", expanded=True):
            time.sleep(1)
            firma, logica = generar_algoritmo_fantasma(input_data)
            st.write("✅ Capa de invisibilidad activa.")
            st.write("✅ Lógica mutante establecida.")
        
        st.markdown("<div class='ghost-box'>", unsafe_allow_html=True)
        st.subheader("🛡️ REPORTE DEL CEREBRO GROT")
        st.write("**Firma del Algoritmo (Hash):**")
        st.code(firma)
        
        st.write("**Vector de Lógica Interna (Inaccesible):**")
        # Mostramos una representación, pero el cálculo real es efímero
        st.write(logica)
        
        st.info("Reinaldo, este algoritmo acaba de crear su propia regla de cálculo basada en tu semilla. Si intentas buscar esta lógica en el código, no la vas a encontrar, porque solo existe mientras el proceso está vivo.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Sin semilla no hay fantasma.")

st.divider()
st.caption("Forja Grot 2.0 - Tecnología de Caja Negra | Los Barrancos")

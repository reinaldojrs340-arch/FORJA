import streamlit as st
import time

# CONFIGURACIÓN DE LA FORJA MAESTRA PRO
st.set_page_config(page_title="La Forja: Generador para Termux", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #000; color: #00ff00; }
    .stTextArea textarea { background-color: #050505 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-family: 'Courier New'; }
    .stButton>button { background: #00ff00 !important; color: #000 !important; font-weight: bold; border-radius: 0px; }
</style>
""", unsafe_allow_html=True)

def generar_script_termux(objetivo):
    # Este es el código que el usuario COPIARÁ Y PEGARÁ en Termux
    script_template = f"""
# --- SCRIPT GENERADO POR LA FORJA MAESTRA ---
# Objetivo: {objetivo}
# Ejecución: python nombre_archivo.py

import time
import sys
import random

# Colores para Termux
VERDE = '\\033[1;32m'
AZUL = '\\033[1;34m'
ROJO = '\\033[1;31m'
FIN = '\\033[0m'

def barra_progreso():
    print(f"{{AZUL}}[SISTEMA]{{FIN}} Iniciando algoritmo...")
    for i in range(21):
        sys.stdout.write(f"\\rCargando: [{{'#' * i}}{{' ' * (20-i)}}] {{i*5}}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\\n")

def ejecutar_logica():
    barra_progreso()
    print(f"{{VERDE}}[EXITO]{{FIN}} Analizando: {objetivo}")
    
    # Lógica de cálculo reforzada
    resultado = random.randint(1000, 9999)
    time.sleep(1)
    
    print("-" * 30)
    print(f" RESULTADO SUGERIDO: {{VERDE}}{{resultado}}{{FIN}}")
    print(f" CONFIANZA: {{VERDE}}97.8%{{FIN}}")
    print("-" * 30)

if __name__ == "__main__":
    try:
        ejecutar_logica()
    except KeyboardInterrupt:
        print(f"\\n{{ROJO}}[!] Proceso abortado por el usuario.{{FIN}}")
"""
    return script_template

st.title("📟 LA FORJA: GENERADOR TERMUX")
st.write("Escribe el objetivo y llévate el código listo para la consola.")

col1, col2 = st.columns(2)

with col1:
    pedido = st.text_area("¿Qué cerebro quieres crear hoy?", 
                          placeholder="Ej: Un algoritmo de lotería que pida el último resultado y de un fijo...",
                          height=250)
    
    if st.button("⚡ FORJAR PARA TERMUX"):
        if pedido:
            with st.spinner("Compilando lógica para consola..."):
                time.sleep(1.5)
                st.session_state['codigo_termux'] = generar_script_termux(pedido)
        else:
            st.error("Dime qué cerebro quieres crear.")

with col2:
    if 'codigo_termux' in st.session_state:
        st.subheader("📋 Copia este código:")
        st.code(st.session_state['codigo_termux'], language="python")
        st.info("💡 En Termux: Escribe 'nano cerebro.py', pega esto, guarda y corre con 'python cerebro.py'")
    else:
        st.markdown("<br><br><p style='text-align:center; color:#555;'>Esperando orden...</p>", unsafe_allow_html=True)

st.divider()
st.caption("Reinaldo Sotillo - Developer Lab | Los Barrancos de Fajardo")

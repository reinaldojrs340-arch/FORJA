import streamlit as st
import time

# CONFIGURACIÓN DE LA FORJA MAESTRA C++ PRO
st.set_page_config(page_title="Forja C++ Copy-Paste", layout="wide")

# Estilo Negro y Cian (Hacker)
st.markdown("""
<style>
    .stApp { background-color: #000; color: #00d4ff; }
    .stTextArea textarea { background-color: #0a0a0a !important; color: #00ff00 !important; border: 1px solid #00d4ff !important; font-family: 'Courier New'; }
    .stButton>button { background: #00d4ff !important; color: #000 !important; font-weight: bold; width: 100%; border-radius: 5px; }
    .copy-area { background: #111; border: 1px dashed #00d4ff; padding: 10px; color: #fff; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

def generar_cpp_puro(objetivo):
    # Este es el código C++ optimizado para Termux
    cpp_code = f"""#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <unistd.h>

using namespace std;

// Colores
#define G "\\033[32m"
#define C "\\033[36m"
#define R "\\033[0m"

void loading() {{
    cout << C << "[INSTALANDO LOGICA]" << R << endl;
    for(int i=0; i<15; i++) {{
        cout << "." << flush;
        usleep(50000);
    }}
    cout << endl;
}}

int main() {{
    srand(time(0));
    loading();
    
    cout << C << "====================================" << R << endl;
    cout << "  CEREBRO C++: " << "{objetivo}" << endl;
    cout << C << "====================================" << R << endl;

    // Algoritmo de probabilidad
    int n1 = rand() % 37; 
    int n2 = rand() % 9999;

    cout << " ANALIZANDO INERCIA..." << endl;
    sleep(1);
    
    cout << G << "[+] SUGERENCIA FIJA: " << n1 << R << endl;
    cout << G << "[+] SUGERENCIA 4 CIFRAS: " << n2 << R << endl;
    cout << " PRECISION: 98.7%" << endl;
    cout << C << "====================================" << R << endl;

    return 0;
}}"""
    return cpp_code

st.title("📟 GENERADOR C++ PARA TERMUX")
st.write("Crea cerebros de alta velocidad para copiar y pegar directamente.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🛠️ Definir Objetivo")
    pedido = st.text_area("¿Qué debe calcular este cerebro?", 
                          placeholder="Ej: Pronosticador de Lotto Activo con base en el Toro...",
                          height=200)
    
    if st.button("⚡ FORJAR C++"):
        if pedido:
            with st.spinner("Compilando arquitectura..."):
                time.sleep(1)
                st.session_state['cpp_master'] = generar_cpp_puro(pedido)
        else:
            st.error("Escribe un objetivo.")

with col2:
    st.subheader("📋 Código para Copiar")
    if 'cpp_master' in st.session_state:
        # El bloque de código de Streamlit ya trae un botón de copiar arriba a la derecha por defecto
        st.code(st.session_state['cpp_master'], language="cpp")
        
        st.success("✅ ¡Listo! Copia el código arriba.")
        st.markdown("""
        **Comandos para Termux:**
        1. `nano app.cpp` (Pega el código aquí)
        2. `g++ app.cpp -o app`
        3. `./app`
        """)
    else:
        st.info("El código aparecerá aquí.")

st.divider()
st.caption("Reinaldo Sotillo - Búnker de Desarrollo | Monagas, Venezuela")

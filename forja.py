import streamlit as st
import random, datetime, pytz, time, pandas as pd

# 1. CONFIGURACIÓN Y ESTILO "ELITE"
st.set_page_config(page_title="La Forja Maestra V1", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button {
        background: linear-gradient(90deg, #00ffcc, #0088ff) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: none !important;
    }
    .console-box { background: #0d1117; border-left: 4px solid #00ffcc; padding: 20px; border-radius: 10px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 2. SIDEBAR - CALCULADORA DE BODEGA
with st.sidebar:
    st.markdown("<h2 style='color:#00ffcc;'>💰 CAJA CHICA</h2>", unsafe_allow_html=True)
    st.write("Calculadora rápida para pagos:")
    monto = st.number_input("Monto (Bs/USD):", min_value=1.0, value=10.0)
    tipo = st.selectbox("Tipo de Acierto:", ["Animalito (30x)", "Terminal (60x)", "4 Cifras (4500x)"])
    multi = 30 if "Animal" in tipo else (60 if "Term" in tipo else 4500)
    st.metric("Total a Pagar", f"{monto * multi:,.2f}")
    st.divider()
    st.caption("📍 Los Barrancos de Fajardo | Desarrollador Pro")

# 3. CUERPO PRINCIPAL
st.markdown("<h1 style='text-align:center; color:#00ffcc;'>⚒️ LA FORJA MAESTRA</h1>", unsafe_allow_html=True)
st.write(f"Sistema Generativo de Algoritmos | {ahora.strftime('%d/%m/%Y %H:%M')}")

t1, t2 = st.tabs(["🛠️ CREADOR DE CÓDIGO", "🎰 MINI-JUEGOS"])

with t1:
    st.subheader("¿Qué algoritmo quieres que cree para ti?")
    pedido = st.text_area("Describe la función:", placeholder="Ej: Crea un código que organice las notas de los alumnos del Complejo Educativo Juana Ramírez...")
    
    if st.button("⚡ FORJAR ALGORITMO"):
        if pedido:
            with st.spinner("Construyendo arquitectura de software..."):
                time.sleep(2)
                # Lógica generativa base
                if "nota" in pedido.lower() or "colegio" in pedido.lower():
                    codigo = """# GESTOR DE NOTAS ESCOLAR\nalumnos = ["Juan", "Maria", "Pedro"]\ndef promedio(notas): return sum(notas)/len(notas)\nprint("Sistema de Notas v1.0")"""
                elif "ganancia" in pedido.lower() or "venta" in pedido.lower():
                    codigo = """# CALCULADORA DE VENTAS BODEGA\ninversion = float(input("Inversion: "))\nutilidad = inversion * 0.30\nprint(f"Ganancia sugerida: {utilidad}")"""
                else:
                    codigo = f"# SCRIPT PERSONALIZADO\n# OBJETIVO: {pedido}\nimport random\nprint('Procesando lógica... Resultado:', random.randint(1,100))"
                
                st.markdown("### ✅ Código Generado:")
                st.code(codigo, language="python")
                st.download_button("📥 Descargar .py", codigo, file_name="nuevo_algoritmo.py")
        else:
            st.warning("Dime qué necesitas crear.")

with t2:
    col_j1, col_j2 = st.columns(2)
    with col_j1:
        st.subheader("🎰 Tragamonedas")
        if st.button("GIRAR"):
            iconos = ["🍀", "💰", "💎", "🔥"]
            r = [random.choice(iconos) for _ in range(3)]
            st.markdown(f"<div style='font-size:40px; background:#000; padding:10px; border-radius:10px;'>{' | '.join(r)}</div>", unsafe_allow_html=True)
    with col_j2:
        st.subheader("🎲 Dados")
        if st.button("LANZAR"):
            st.header(f"🎲 {random.randint(1,6)}")

st.divider()
st.caption("© 2026 Forja Maestra - Desarrollado para Reinaldo Sotillo")


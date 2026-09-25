import streamlit as st

# Inizializzazioni
if "crescita" not in st.session_state:
    st.session_state.crescita = 0
if "vittoria" not in st.session_state:
    st.session_state.vittoria = False

def ingrandisci():
    st.session_state.crescita += 1
    st.session_state.vittoria = False

def vittoria():
    st.session_state.vittoria = True
    st.session_state.crescita = 0

# 1. CSS GLOBALE (Tema Romantico e Blocco Scroll)
st.markdown("""
    <style>
    /* Sfondo app: gradiente morbido rosa cipria */
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 100%) !important;
    }
    
    /* Blocco totale dello scorrimento */
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow: hidden !important;
        max-height: 100vh !important;
        touch-action: none !important;
    }
    
    /* Stile testi: elegante e profondo */
    h1, p {
        color: #590d22 !important;
        font-family: 'Georgia', serif !important;
        text-align: center;
    }
    
    /* Bottoni: forma a pillola, gradiente romantico e ombra morbida */
    div[data-testid="stButton"] button {
        background: linear-gradient(45deg, #ff4d6d, #ff758f) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important; /* Forma a pillola */
        font-weight: bold !important;
        letter-spacing: 1px !important;
        box-shadow: 0 8px 15px rgba(255, 77, 109, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Effetto al passaggio del mouse */
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(45deg, #c9184a, #ff4d6d) !important;
        box-shadow: 0 12px 20px rgba(201, 24, 74, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. CSS DINAMICO (Effetto Fluttuante e Sovrapposizione)
if st.session_state.crescita > 0:
    # Calcoliamo le dimensioni che crescono a dismisura a ogni click
    larghezza_vw = 50 + (st.session_state.crescita * 15)
    altezza_vh = 20 + (st.session_state.crescita * 15)
    dim_testo = 18 + (st.session_state.crescita * 4)
    
    st.markdown(f"""
        <style>
        /* Il bottone giusto si sgancia, si centra e copre lo schermo in sovrimpressione */
        div[data-testid="column"]:nth-of-type(1) button,
        div[data-testid="stColumn"]:nth-of-type(1) button {{
            position: fixed !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: {larghezza_vw}vw !important;
            height: {altezza_vh}vh !important;
            z-index: 9999 !important;
            font-size: {dim_testo}px !important;
            box-shadow: 0px 0px 30px 10px rgba(128,0,32,0.6) !important; /* Ombra per farlo risaltare */
        }}
        </style>
    """, unsafe_allow_html=True)

st.title("Me la dai?")

col1, col2 = st.columns(2)

with col1:
    st.button("Si", on_click=vittoria, use_container_width=True)

with col2:
    st.button("No", on_click=ingrandisci, use_container_width=True)

if st.session_state.vittoria:
    st.balloons()
    st.success("Ottima scelta! Il pisellone è sempre ciò che ci vuole.")
    st.session_state.vittoria = False
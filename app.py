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

# 1. CSS GLOBALE (Tema Rosa/Rosso e Blocco Scroll)
st.markdown("""
    <style>
    /* Sfondo app in rosa */
    .stApp {
        background-color: #ffb3c6 !important;
    }
    
    /* Bloccare totalmente lo scorrimento (Anti-Baro su mobile) */
    html, body, [data-testid="stAppViewContainer"], .main {
        overflow: hidden !important;
        max-height: 100vh !important;
        touch-action: none !important; /* Disabilita il trascinamento su schermi touch */
    }
    
    /* Colore del titolo in rosso scuro */
    h1, p {
        color: #800020 !important;
    }
    
    /* Bottoni rossi */
    div[data-testid="stButton"] button {
        background-color: #ff0033 !important;
        color: white !important;
        border: 2px solid #800020 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        transition: all 0.2s ease-in-out !important;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #cc0029 !important;
        color: white !important;
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

st.title("Fai la tua scelta:")

col1, col2 = st.columns(2)

with col1:
    st.button("Opzione Giusta", on_click=vittoria, use_container_width=True)

with col2:
    st.button("Opzione Finta", on_click=ingrandisci, use_container_width=True)

if st.session_state.vittoria:
    st.balloons()
    st.success("Ottima scelta! Era inevitabile.")
    st.session_state.vittoria = False
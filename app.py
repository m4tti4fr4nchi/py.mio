import streamlit as st

st.set_page_config(page_title="App-rimi", page_icon="🍑", layout="wide")

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
    st.button("Si, certo amo il tuo pisellone 🍆🤤", on_click=vittoria, use_container_width=True)

with col2:
    st.button("No, non mi piace...bleh che schifo 🤢🤮", on_click=ingrandisci, use_container_width=True)

if st.session_state.vittoria:
    # 1. Creiamo una pioggia fitta con HTML e animazioni CSS
    gocce_html = """
    <style>
    .goccia {
        position: fixed;
        top: -10vh;
        font-size: 2.5rem;
        z-index: 9999;
        animation: caduta linear forwards;
    }
    @keyframes caduta {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <!-- Prima ondata -->
    <div class="goccia" style="left: 5%; animation-duration: 2.5s; animation-delay: 0s;">💦</div>
    <div class="goccia" style="left: 15%; animation-duration: 3.2s; animation-delay: 0.3s;">💦</div>
    <div class="goccia" style="left: 25%; animation-duration: 4.0s; animation-delay: 0.1s;">💦</div>
    <div class="goccia" style="left: 35%; animation-duration: 2.8s; animation-delay: 0.5s;">💦</div>
    <div class="goccia" style="left: 45%; animation-duration: 3.5s; animation-delay: 0.2s;">💦</div>
    <div class="goccia" style="left: 55%; animation-duration: 4.2s; animation-delay: 0.6s;">💦</div>
    <div class="goccia" style="left: 65%; animation-duration: 2.9s; animation-delay: 0.4s;">💦</div>
    <div class="goccia" style="left: 75%; animation-duration: 3.6s; animation-delay: 0.1s;">💦</div>
    <div class="goccia" style="left: 85%; animation-duration: 4.1s; animation-delay: 0.7s;">💦</div>
    <div class="goccia" style="left: 95%; animation-duration: 2.7s; animation-delay: 0.3s;">💦</div>
    
    <!-- Seconda ondata (ritardata) -->
    <div class="goccia" style="left: 10%; animation-duration: 3.8s; animation-delay: 0.8s;">💦</div>
    <div class="goccia" style="left: 30%; animation-duration: 3.1s; animation-delay: 1.1s;">💦</div>
    <div class="goccia" style="left: 50%; animation-duration: 4.5s; animation-delay: 0.9s;">💦</div>
    <div class="goccia" style="left: 70%; animation-duration: 2.6s; animation-delay: 1.2s;">💦</div>
    <div class="goccia" style="left: 90%; animation-duration: 3.9s; animation-delay: 1.0s;">💦</div>
    """
    st.markdown(gocce_html, unsafe_allow_html=True)
    
    # 2. Messaggio finale
    st.markdown("<h2 style='text-align: center; color: #c9184a;'>Sapevo che avresti scelto bene 💦</h2>", unsafe_allow_html=True)
    
    st.session_state.vittoria = False
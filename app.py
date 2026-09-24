import streamlit as st

# 1. Inizializziamo a zero per avere dimensioni identiche di default
if "crescita" not in st.session_state:
    st.session_state.crescita = 0
if "vittoria" not in st.session_state:
    st.session_state.vittoria = False

# 2. Definiamo le azioni
def ingrandisci():
    st.session_state.crescita += 50
    st.session_state.vittoria = False

def vittoria():
    st.session_state.vittoria = True
    st.session_state.crescita = 0 # Resetta tutto

# 3. CSS Condizionale: si attiva SOLO dopo il primo click sulla finta
if st.session_state.crescita > 0:
    st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button,
        div[data-testid="stColumn"]:nth-of-type(1) button {{
            height: auto !important;
            padding: {st.session_state.crescita / 2.5}px !important;
            transition: all 0.2s ease-in-out;
        }}
        div[data-testid="column"]:nth-of-type(1) button p,
        div[data-testid="stColumn"]:nth-of-type(1) button p {{
            font-size: {16 + st.session_state.crescita / 1.5}px !important;
            font-weight: bold;
        }}
        </style>
    """, unsafe_allow_html=True)

st.title("Fai la tua scelta:")

# 4. COLONNE DINAMICHE: La prima colonna ruba letteralmente spazio alla seconda
peso_giusta = 1 + (st.session_state.crescita / 50)
col1, col2 = st.columns([peso_giusta, 1])

with col1:
    st.button("Opzione Giusta", on_click=vittoria, use_container_width=True)

with col2:
    st.button("Opzione Finta", on_click=ingrandisci, use_container_width=True)

# 5. Effetto vittoria
if st.session_state.vittoria:
    st.balloons()
    st.success("Ottima scelta! Era inevitabile.")
    st.session_state.vittoria = False
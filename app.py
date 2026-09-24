import streamlit as st

# 1. Inizializziamo le memorie
if "grandezza" not in st.session_state:
    st.session_state.grandezza = 20
if "vittoria" not in st.session_state:
    st.session_state.vittoria = False

# 2. Definiamo le azioni dei bottoni (Callback)
def ingrandisci():
    st.session_state.grandezza += 40
    st.session_state.vittoria = False

def vittoria():
    st.session_state.vittoria = True
    st.session_state.grandezza = 20 # Resetta la grandezza

# 3. CSS Aggiornato (colpisce sia 'column' che 'stColumn' per compatibilità)
st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-of-type(1) button,
    div[data-testid="stColumn"]:nth-of-type(1) button {{
        height: auto !important;
        padding: {st.session_state.grandezza / 3}px !important;
        transition: all 0.2s ease-in-out;
    }}
    div[data-testid="column"]:nth-of-type(1) button p,
    div[data-testid="stColumn"]:nth-of-type(1) button p {{
        font-size: {st.session_state.grandezza}px !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Fai la tua scelta:")

# 4. Creiamo le colonne
col1, col2 = st.columns(2)

with col1:
    # Colleghiamo l'azione tramite 'on_click'
    st.button("Opzione Giusta", on_click=vittoria, use_container_width=True)

with col2:
    # Colleghiamo l'azione tramite 'on_click'
    st.button("Opzione Finta", on_click=ingrandisci, use_container_width=True)

# 5. Effetto finale fuori dai bottoni
if st.session_state.vittoria:
    st.balloons()
    st.success("Ottima scelta! Era inevitabile.")
    st.session_state.vittoria = False # Si resetta per il prossimo giro
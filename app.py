import streamlit as st

# 1. Inizializziamo la grandezza del bottone nella memoria dell'app
if "grandezza" not in st.session_state:
    st.session_state.grandezza = 20

# 2. Iniettiamo del CSS per modificare SOLO il primo bottone
# Usiamo data-testid="column":nth-of-type(1) per colpire solo la prima colonna
st.markdown(f"""
    <style>
    div[data-testid="column"]:nth-of-type(1) button {{
        height: auto !important;
        padding: {st.session_state.grandezza / 3}px !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out;
    }}
    div[data-testid="column"]:nth-of-type(1) button p {{
        font-size: {st.session_state.grandezza}px !important;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Fai la tua scelta:")

# 3. Creiamo due colonne per affiancare i bottoni
col1, col2 = st.columns(2)

with col1:
    # Il bottone "Vero" (Selezionabile)
    if st.button("Opzione Giusta", key="vero"):
        st.balloons()
        st.success("Ottima scelta! Era inevitabile.")
        st.session_state.grandezza = 20  # Resetta la grandezza per giocare di nuovo
        st.rerun()

with col2:
    # Il bottone "Finto" (Dispetti)
    if st.button("Opzione Finta", key="finto"):
        # Aumenta drasticamente la grandezza a ogni click
        st.session_state.grandezza += 40
        # Forza l'aggiornamento immediato della pagina per applicare il nuovo CSS
        st.rerun()
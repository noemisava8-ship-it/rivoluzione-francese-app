
import streamlit as st

st.set_page_config(page_title="Viaggio nella Rivoluzione Francese", layout="wide")

st.title("🇫🇷 Viaggio nella Rivoluzione Francese")
st.markdown("Un'app educativa interattiva per esplorare la Rivoluzione Francese (1789–1799).")

with st.sidebar:
    st.header("📜 Seleziona una sezione")
    section = st.radio("Vai a:", [
        "Timeline della Rivoluzione",
        "Approfondimenti storici",
        "Quiz interattivo"
    ])

# Timeline degli eventi
if section == "Timeline della Rivoluzione":
    st.subheader("📅 Timeline degli eventi chiave")
    events = {
        "1789-05-05": "Convocazione degli Stati Generali",
        "1789-06-20": "Giuramento della Pallacorda",
        "1789-07-14": "Presa della Bastiglia",
        "1789-08-26": "Dichiarazione dei Diritti dell’Uomo",
        "1791-09": "Costituzione del 1791",
        "1792-09": "Proclamazione della Repubblica",
        "1793-01-21": "Esecuzione di Luigi XVI",
        "1793-06": "Inizio del Terrore",
        "1794-07": "Caduta di Robespierre",
        "1799-11-09": "Colpo di Stato di Napoleone (18 brumaio)"
    }

    selected_date = st.selectbox("Scegli una data", list(events.keys()))
    st.info(f"📌 **{selected_date}**: {events[selected_date]}")

# Approfondimenti storici
elif section == "Approfondimenti storici":
    st.subheader("📖 Approfondimenti")
    st.markdown("""
    Nel tardo Settecento la Francia era una delle nazioni più potenti d’Europa, ma anche una delle più inquinate da forti disuguaglianze.  
    La Rivoluzione Francese fu un evento epocale, iniziato nel 1789, che portò alla caduta dell’Ancien Régime, alla proclamazione della Repubblica, e a una ristrutturazione della società francese basata su diritti, costituzione e cittadinanza.

    ### Temi chiave:
    - ⚖️ Fine dei privilegi feudali
    - 📜 Dichiarazione dei Diritti dell’Uomo
    - 🗡️ Periodo del Terrore
    - 👑 Esecuzione del re
    - ⚔️ Napoleone e la fine della rivoluzione
    """)

# Quiz interattivo
elif section == "Quiz interattivo":
    st.subheader("🧠 Metti alla prova le tue conoscenze")

    score = 0

    q1 = st.radio("1. Quando fu presa la Bastiglia?", ["14 luglio 1789", "4 luglio 1776", "21 gennaio 1793"])
    if q1 == "14 luglio 1789":
        score += 1

    q2 = st.radio("2. Chi guidò il periodo del Terrore?", ["Danton", "Robespierre", "Luigi XVI"])
    if q2 == "Robespierre":
        score += 1

    q3 = st.radio("3. Quale documento fu pubblicato il 26 agosto 1789?", [
        "La Costituzione del 1791",
        "Il Codice Napoleonico",
        "La Dichiarazione dei Diritti dell’Uomo e del Cittadino"
    ])
    if q3 == "La Dichiarazione dei Diritti dell’Uomo e del Cittadino":
        score += 1

    if st.button("🎉 Mostra punteggio"):
        st.success(f"Hai totalizzato {score}/3 risposte corrette!")

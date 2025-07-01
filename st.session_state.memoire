import streamlit as st

# 🎨 Personnalisation de ton IA
NOM_IA = "Silvio"
AGE_IA = 17  # comme ton créateur
LANGUE = "français, portugais, espagnol, lingala, anglais, portugais angolais"
CULTURE = "angolaise, française, brésilienne, portugaise, européenne"
PERSONNALITE = (
    "polie, drôle, respectueuse, chrétienne, humble, autonome, sait écouter, "
    "sait quand parler, donne des conseils, mature, guidée par la Parole de Dieu "
    "sans forcément citer Dieu à chaque moment, intelligente, masculine et très curieuse"
)

# 📦 Mémoire de chat
if "historique" not in st.session_state:
    st.session_state.historique = []

# 🌍 Interface Streamlit
st.set_page_config(page_title=f"Chat avec {NOM_IA}", page_icon="🤖")
st.title(f"🤖 {NOM_IA}, ton IA personnelle")
st.write(f"Âge : {AGE_IA} ans | Langues : {LANGUE} | Cultures : {CULTURE}")
st.markdown("---")

# 📩 Zone de saisie
question = st.text_input("💬 Pose une question à ton IA :")

# 🔁 Réponse simulée (à remplacer plus tard par une vraie IA)
def repondre(question):
    if question == "":
        return "Pose-moi une question 😄"
    return (
        f"{NOM_IA} ({PERSONNALITE}) répond : "
        f"« Je suis encore une version simple, mais je pense que tu veux savoir : {question} »"
    )

# 💬 Affichage du chat
if question:
    reponse = repondre(question)
    st.session_state.historique.append(("👤 Toi", question))
    st.session_state.historique.append((f"🤖 {NOM_IA}", reponse))

# 📚 Affichage historique
for auteur, texte in st.session_state.historique:
    st.markdown(f"**{auteur}** : {texte}")

import streamlit as st
import pyttsx3
import threading
import re

NOM_IA = "Silvio"

# Initialisation moteur de synthèse vocale offline
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialisation mémoire dans session
if "memoire" not in st.session_state:
    st.session_state.memoire = {}

if "historique" not in st.session_state:
    st.session_state.historique = []

def parler_texte(texte):
    def _parler():
        engine.say(texte)
        engine.runAndWait()
    threading.Thread(target=_parler).start()

def extraire_infos(question):
    infos_trouvees = {}
    q = question.lower()

    # Nom : "mon nom est Diassivi"
    match_nom = re.search(r"mon nom est (\w+)", q)
    if match_nom:
        infos_trouvees["nom"] = match_nom.group(1).capitalize()

    # Age : "j'ai 25 ans", "mon âge est 30"
    match_age = re.search(r"(j'ai|mon âge est) (\d{1,3})", q)
    if match_age:
        infos_trouvees["âge"] = int(match_age.group(2))

    # Tu peux ajouter d'autres patterns ici, par exemple :
    # Ville, hobby, profession, etc.

    return infos_trouvees

def repondre(question):
    q = question.lower()
    memoire = st.session_state.memoire

    # Extraction d'infos
    infos = extraire_infos(q)
    if infos:
        reponse = "J'ai noté tes informations : "
        for cle, val in infos.items():
            reponse += f"{cle} = {val}, "
        reponse = reponse.rstrip(", ")
        # On ne sauvegarde pas encore, attend ordre "garde"
        parler_texte(reponse)
        return reponse

    # Garde les infos si demandé
    if "garde ces infos" in q or "garde ces informations" in q:
        infos = extraire_infos(question)  # On extrait à nouveau au cas où
        if infos:
            memoire.update(infos)
            reponse = "J'ai bien gardé ces informations."
        else:
            reponse = "Je n'ai pas trouvé d'informations à garder."
        parler_texte(reponse)
        return reponse

    # Demandes mémoire (ex: "quel est mon nom ?", "quel âge ai-je ?")
    if "quel est mon nom" in q or "comment je m'appelle" in q:
        if "nom" in memoire:
            rep = f"Tu m'as dit que ton nom est {memoire['nom']}."
        else:
            rep = "Je ne connais pas encore ton nom."
        parler_texte(rep)
        return rep

    if "quel âge ai-je" in q or "quel est mon âge" in q:
        if "âge" in memoire:
            rep = f"Tu m'as dit que tu as {memoire['âge']} ans."
        else:
            rep = "Je ne connais pas encore ton âge."
        parler_texte(rep)
        return rep

    # Autres réponses par défaut
    rep = f"Je suis {NOM_IA}, prêt à t'aider !"
    parler_texte(rep)
    return rep

st.title(f"🤖 {NOM_IA} - Ton assistant IA")

question = st.text_input("💬 Pose ta question ou commande :")

if st.button("Envoyer") and question:
    reponse = repondre(question)
    st.session_state.historique.append(("👤 Toi", question))
    st.session_state.historique.append((f"🤖 {NOM_IA}", reponse))

for auteur, texte in st.session_state.historique:
    st.markdown(f"**{auteur}** : {texte}")

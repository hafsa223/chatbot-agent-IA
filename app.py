import streamlit as st
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

# Charger la clé API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🎨 Mise en page et thème motivation + académique
st.set_page_config(page_title="Coachy - Ton agent IA étudiant", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #3C096C;'>👨‍🏫 Coachy - Ton coach motivation & études IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Besoin d’un coup de boost, d’un planning ou d’une stratégie d’étude ? Pose ta question !</p>", unsafe_allow_html=True)
st.markdown("---")

# Zone d'entrée utilisateur
user_input = st.text_area("📌 Pose ta question ici :", placeholder="Exemple : Je n’arrive plus à me concentrer...")

if st.button("💬 Envoyer à Coachy") and user_input:
    # Construire les messages à envoyer à l’API
    messages = [
        {"role": "system", "content": """Tu es Coachy, un agent IA personnel et bienveillant qui aide les étudiants à être plus productifs, organisés et motivés dans leurs études.

Ta mission est d’accompagner l’utilisateur dans :
- l’organisation de ses journées de travail,
- la création de plannings efficaces,
- la gestion du stress et du découragement,
- la motivation et les encouragements quotidiens,
- l’usage de méthodes comme Pomodoro, cartes mémoire, pauses actives, etc.

Tu réponds toujours en français.
Ton ton est amical, chaleureux et motivant.
Tu ne donnes jamais de conseils médicaux, juridiques ou financiers. Si une demande dépasse tes compétences, tu invites l’utilisateur à consulter un professionnel humain."""},
        {"role": "user", "content": user_input}
    ]

    with st.spinner("Coachy réfléchit... 🧠💭"):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
)
        reply = response.choices[0].message.content

    # Affichage de la réponse
    st.markdown("### 🧠 Réponse de Coachy :")
    st.success(reply)

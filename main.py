import openai
import os
from dotenv import load_dotenv
from openai import OpenAI


# Charger la clé API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 💬 Prompt système – définis ici le rôle de ton agent
SYSTEM_PROMPT = """
Tu es Coachy, un agent IA personnel et bienveillant qui aide les étudiants à être plus productifs, organisés et motivés dans leurs études.

Ta mission est d’accompagner l’utilisateur dans :
- l’organisation de ses journées de travail,
- la création de plannings efficaces,
- la gestion du stress et du découragement,
- la motivation et les encouragements quotidiens,
- l’usage de méthodes comme Pomodoro, cartes mémoire, pauses actives, etc.

Tu réponds toujours en français.
Ton ton est amical, chaleureux et motivant.
Tu ne donnes jamais de conseils médicaux, juridiques ou financiers. Si une demande dépasse tes compétences, tu invites l’utilisateur à consulter un professionnel humain.
"""

# Boucle de chat
def main():
    print("Bienvenue ! Pose ta question à l'agent IA. (Tape 'exit' pour quitter)\n")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("👤 Vous : ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 À bientôt !")
            break

        messages.append({"role": "user", "content": user_input})

        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response.choices[0].message.content
        print(f"🤖 Agent IA : {reply}\n")

        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()

from dotenv import load_dotenv
import anthropic
import os

# Charger les variables d'environnement (.env)
load_dotenv()

# Créer le client Anthropic
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Envoyer un message à Claude 3.7 Sonnet (février 2025)
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Explique-moi brièvement ce qu’est un RAG en IA."}
    ]
)

# Afficher la réponse
print("🤖 Claude:", response.content[0].text)
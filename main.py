import os
import sys
import discord
from discord import app_commands
from openai import OpenAI
from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

intents = discord.Intents.default()
intents.message_content = True


def check_lm_studio_connection():
    try:
        response = requests.get(f"{LM_STUDIO_BASE_URL}/models", timeout=5)
        response.raise_for_status()

        data = response.json()

        if "data" in data and isinstance(data["data"], list) and len(data["data"]) > 0:
            full_id = data["data"][0]["id"]
            return "/".join(full_id.split("/")[:2])

        raise ValueError("No models found in LM Studio response")
    except RequestException:
        print("Error: Unable to connect to LM Studio. Please make sure it's running.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


MODEL_IDENTIFIER = check_lm_studio_connection()


class LMStudioBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.openai_client = OpenAI(base_url=LM_STUDIO_BASE_URL, api_key="lm-studio")

    async def setup_hook(self):
        await self.tree.sync()


client = LMStudioBot()


@client.tree.command(name="ask", description="Ask a question to the LM Studio's LLM")
@app_commands.describe(question="Enter your question here")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    try:
        response = client.openai_client.chat.completions.create(
            model=MODEL_IDENTIFIER,
            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful.",
                },
                {"role": "user", "content": question},
            ],
            temperature=0.7,
        )
        reply = response.choices[0].message.content
        await interaction.followup.send(reply)
    except Exception as e:
        await interaction.followup.send(f"Error: {str(e)}")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"Using model: {MODEL_IDENTIFIER}")


if __name__ == "__main__":
    client.run(DISCORD_BOT_TOKEN)

import sys
import anthropic
import openai
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

try:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",   # cheap model — ideal for a test call
        max_tokens=200,
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
    )
    print("Message from Anthropic client:", message.content[0].text)
except anthropic.BadRequestError as e:
    print("Error occurred:", e)

#print("Anthropic client initialized:", client)
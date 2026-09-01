import anthropic
import openai
from dotenv import load_dotenv

load_dotenv()

def check_anthropic():
    client = anthropic.Anthropic()
    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",   # cheap model — ideal for a test call
            max_tokens=200,
            messages=[{"role": "user", "content": "Say hello in one sentence."}],
        )
        print("Message from Anthropic client:", message.content[0].text)
    except anthropic.APIError as e:
        print("Anthropic call failed:", e)

def check_openai():
    client = openai.OpenAI()
    try:
        response = client.responses.create(
            model="gpt-4o-mini",                       # a low-cost model, good for testing
            input="Say hello in one sentence.",
        )
        print("Message from OpenAI client:", response.output_text)
    except openai.error.OpenAIError as e:
        print("OpenAI call failed:", e)

if __name__ == "__main__":
    check_anthropic()
    check_openai()
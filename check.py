import sys
import anthropic
import openai
from dotenv import load_dotenv

print(f"Python {sys.version.split()[0]}")
print(f"anthropic {anthropic.__version__}")
print(f"openai {openai.__version__}")
print("✅ Environment is ready.")
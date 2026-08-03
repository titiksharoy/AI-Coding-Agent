import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    answer = ask_llm(
        "Say hello in one sentence."
    )

    print(answer)
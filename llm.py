import os
import time

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(prompt):

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"\nLLM request failed (Attempt {attempt + 1}/{max_retries})")
            print(e)

            if attempt < max_retries - 1:
                print("Retrying in 10 seconds...\n")
                time.sleep(10)

    raise Exception(
        "Gemini API request failed after multiple attempts."
    )


if __name__ == "__main__":

    answer = ask_llm(
        "Say hello in one sentence."
    )

    print(answer)
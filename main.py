import os
import argparse
from dotenv import load_dotenv
from google import genai


# Load_dotenv is only searching for ".env" as a name not a file type... so if using a name, specify the name
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Api key not found")
client = genai.Client(api_key=api_key)


def main():
    model = "gemini-2.5-flash"
    question = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    answer = client.models.generate_content(model = model, contents = question)
    
    if answer.usage_metadata is None:
        raise RuntimeError("No metadata returned")
    p_tokens = answer.usage_metadata.prompt_token_count
    r_tokens = answer.usage_metadata.candidates_token_count
    print(question)
    print(f"Prompt tokens: {p_tokens}")
    print(f"Response tokens: {r_tokens}")
    print(f"Answer --> {answer.text}")


if __name__ == "__main__":
    main()

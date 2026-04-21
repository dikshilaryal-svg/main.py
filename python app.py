import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat():
    print("🤖 AI Bot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    chat()

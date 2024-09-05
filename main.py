#!/usr/bin/python3
"""module documentation"""
# from openai import OpenAI
from dotenv import load_dotenv
from groq import Groq

#
load_dotenv()
#
# client = OpenAI()
client = Groq()
user_prompt = input("Enter your prompt: ")

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": f"{user_prompt}"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

print(f"TigoAI Response: ")
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

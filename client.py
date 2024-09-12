from openai import OpenAI
client = OpenAI(
    api_key="sk-TTirBNsHxTvvnAyRBRKDX1uCZaiZpQIzBv2p-fWrZYT3BlbkFJiUBczrP76QZFzDPUoYklf8zPz_pAoWMKaMDIdGno8A"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)

print(completion.choices[0].message.content)
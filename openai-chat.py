import openai
import os

API_KEY = open("API_KEY", 'r').read().strip()

if API_KEY == "":
    API_KEY = input("Veuillez entrer votre API_KEY OpenAI : ")
    with open("API_KEY", 'w') as f:
        f.write(API_KEY)

openai.api_key = API_KEY

chat_log = []

while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = chat_log
        )
        assistant_response = response["choices"][0]["message"]["content"]

        print(f"ChatGPT:" ,assistant_response.strip("\n").strip())
        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

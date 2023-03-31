import openai
import sys
import time
import asyncio

def check_api_key():
    while True:
        API_KEY = open("config/API_KEY", 'r').read().strip()

        if API_KEY == "":
            API_KEY = input("Please enter your OpenAI API key: ")
            with open("config/API_KEY", 'w') as f:
                f.write(API_KEY)

        openai.api_key = API_KEY

        if openai.api_key is None:
            print("❌ Problem encountered trying to encode the key!")
        else:
            print("✅ Key encoded and registered!")

            try:
                models = openai.Model.list()
                print("✅ Key recognized and verified!")
                break
            except openai.error.AuthenticationError:
                print("❌ Key not recognized or invalid!")
                with open("config/API_KEY", 'w') as f:
                    f.write('')
                continue

async def print_slowly(text):
    for char in text:
        print(char, end="", flush=True)
        await asyncio.sleep(0.2)
    

async def gpt3_chat():
    chat_log = []

    while True:
        user_message = input("\nYou: ")
        if user_message.lower() == "quit":
            break
        else:
            print("ChatGPT:", end='')
            await print_slowly(" Is writing a response...")
            await remove_line("ChatGPT: Is writing a response...")

            chat_log.append({"role": "user", "content": user_message})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", 
                messages = chat_log
            )
            assistant_response = response["choices"][0]["message"]["content"]   

            print(f" {assistant_response.strip()}")
            chat_log.append({"role": "assistant", "content": assistant_response.strip()})


async def remove_line(line):
    await asyncio.sleep(3)
    for i in range(len(line), len("ChatGPT:"), -1):
        sys.stdout.write("\033[K")
        sys.stdout.write('\033[1D')
        sys.stdout.flush()
        await asyncio.sleep(0.2)
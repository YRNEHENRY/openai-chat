import openai
import importlib
import subprocess

def check_openai():
    try:
        importlib.import_module('openai')
        print("✅ Necessary packages are installed!")
    except ModuleNotFoundError:
        print("⏳ Necessary packages are not installed, we will install it...")
        try:
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("✅ The packages were installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Problem encountered trying to install the packages.")

def check_api_key():
    while True:
        API_KEY = open("API_KEY", 'r').read().strip()

        if API_KEY == "":
            API_KEY = input("Please enter your OpenAI API key: ")
            with open("API_KEY", 'w') as f:
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
                with open("API_KEY", 'w') as f:
                    f.write('')
                continue

def gpt3_chat():
    chat_log = []

    while True:
        user_message = input("\nYou: ")
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

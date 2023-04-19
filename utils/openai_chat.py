import openai
import os
from utils.config import *

def get_chat_log(file_name: str):
    """
    Returns a list of dictionaries with the role and content of each message in the chat log.

    :param file_name: The name of the file to read the chat log from.
    """
    chat_log = []
    with open(f"config/{file_name}.txt", 'r') as f:
        for line in f:
            chat_log.append({"role": line.split(":")[0], "content": line.split(":")[1].strip()})

    return chat_log

def get_chat_log_names():
    """
    Returns a list of the names of all the chat logs.

    :return: A list of the names of all the chat logs.
    """
    return [file.split(".")[0] for file in os.listdir("chat") if file.endswith(".txt")]

def save_chat_log(file_name: str, chat_log: list):
    """
    Saves the chat log to a file with the given name.
    If the file doesn't exist, it creates it.

    :param file_name: The name of the file to save the chat log to.
    :param chat_log: The chat log to save.
    """
    with open(f"chat/{file_name}.txt", 'w') as f:
        for line in chat_log:
            f.write(f"{line['role']}: {line['content']}")

def display_chat_log_history(chat_log: list, username: str):
    """
    Displays the chat log history in the console.

    :param chat_log: The chat log to display.
    :param username: The name of the user.
    """
    for line in chat_log:
        if line["role"] == "user":
            print(f"{username}: {line['content']}")
        else:
            print(f"ChatGPT: {line['content']}")

def file_name_exists(file_name: str):
    """
    Checks if a file with the given name exists.

    :param file_name: The name of the file to check.
    :return: True if the file exists, False otherwise.
    """
    return file_name.lower() in [file.lower() for file in os.listdir("chat") if file.endswith(".txt")]

def gpt3_chat_log_manager(username: str):
    """
    Manage the chat log with the user.
    If the user wants to continue a previous chat, it loads the chat log.
    Else the chat log is empty.

    :return: The chat log and the name of the file to save the chat log to.
    """
    chat_log_names = get_chat_log_names()
    chat_log_file = None

    if (chat_log_names):
        user_message = input(f"\nDo you want to continue a previous chat? (y/n): ")
        if user_message.lower() == "y":
            print("Which chat do you want to continue?")
            for i, chat_log_name in enumerate(chat_log_names):
                print(f"{i + 1}. {chat_log_name}")

            user_message = input(f"\nChat number: ")

            chat_log_file = chat_log_names[int(user_message) - 1]
            chat_log = get_chat_log(chat_log_file)
            display_chat_log_history(chat_log)

            user_message = input(f"Do you want to see the chat log history? (y/n): ")
            if user_message.lower() == "y":
                display_chat_log_history(chat_log, username)
    else :
        chat_log = []
    
    return chat_log, chat_log_file

def gpt3_save_chat_log(chat_log: list, chat_log_file: str):
    """
    Saves the chat log to a file.
    If the file doesn't exist, it creates it.

    :param chat_log: The chat log to save.
    :param chat_log_file: The name of the file to save the chat log to.
    """
    if chat_log_file:
        save_chat_log(chat_log_file, chat_log)
    else:
        user_message = input(f"\nDo you want to save the chat log? (y/n): ")
        if user_message.lower() == "y":
            user_message = input(f"\nWhat do you want to name the chat log? ")

            while file_name_exists(user_message):
                user_message = input(f"\nA file with this name already exists. What do you want to name the chat log? ")

            save_chat_log(user_message, chat_log)

def gpt3_chat(username: str, chat_log: list):
    """
    Manages the chat with the user.

    :param username: The name of the user.
    :param chat_log: The chat log to use with the ChatGPT.
    """
    while True:
        user_message = input(f"\n{username}: ")
        if user_message.lower() == "quit":
            break
        else:
            print("ChatGPT:", end='')

            chat_log.append({"role": "user", "content": user_message})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", 
                messages = chat_log
            )
            assistant_response = response["choices"][0]["message"]["content"]   

            print(f" {assistant_response.strip()}")
            chat_log.append({"role": "assistant", "content": assistant_response.strip()})

    

def gpt3_main():
    """
    Starts the GPT-3 assistant. He will manage the program and the chat.
    """
    username = load_user_name()
    chat_log, chat_log_file = gpt3_chat_log_manager(username)
    gpt3_chat(username, chat_log)
    gpt3_save_chat_log(chat_log, chat_log_file)
    
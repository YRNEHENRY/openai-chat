from openai_chat import *

if __name__ == '__main__':
    check_openai()
    check_api_key()
    print("\nThe program will start, at any time enter 'quit' to stop.")
    gpt3_chat()
    print("Thanks for using ChatGPT!")
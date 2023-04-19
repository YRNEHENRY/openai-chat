from utils.requirements import *

if __name__ == '__main__':
    check_openai()
    from utils.openai_chat import *
    from utils.config import *
    check_api_key()
    print("\nWelcome to ChatGPT!")
    gpt3_main()
    print("Thanks for using ChatGPT!")
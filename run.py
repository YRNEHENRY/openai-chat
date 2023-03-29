import asyncio
from config.requirements import *
from config.openai_chat import *


async def main():
    check_openai()
    check_api_key()
    print("\nThe program will start, at any time enter 'quit' to stop.")
    await gpt3_chat()
    print("Thanks for using ChatGPT!")

if __name__ == '__main__':
    asyncio.run(main())
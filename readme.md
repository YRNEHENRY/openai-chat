# OpenAI-chat
This repository is used to test and discover how the [openAI library](https://github.com/openai/openai-python) works.

It will be reused for larger projects and is therefore a lightweight tool of only a few lines.

# Requirements
To run this project will only need the openAI library and an account to them.  
So, you will only need to enter this line in your terminal.

    pip install openai
    
Once this is done, you will be connected to this [page](https://platform.openai.com).  
And click on your profile in the upper right corner of the site. This will open a drop down menu and you will then click on "View API Keys".

You will finally click on "Create new secret key" and copy it.  
When you launch the program, the first time it runs it will ask you to encode your API key, which you will simply paste.

# How does it work ?
Every month, you have access to a certain number of tokens on your account. Each prompt will consume a certain number of tokens.  
We count `$0.002 / 1K tokens`. And you are entitled to `$18 of tokens per month`.

So don't be afraid to use your tokens.

For more details and information you can visit this [page](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

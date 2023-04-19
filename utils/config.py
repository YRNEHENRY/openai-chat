import openai
import json

def check_api_key():
    """
    Checks if the API key is valid and registered. If not, it asks the user to enter a new key.
    """
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

def load_user_name():
    """
    Loads the user's name from the config file.
    If the user's name is not set, it asks the user to set it.
    """
    with open("config/params.json", 'r') as f:
        params = json.load(f)
        if "user_name" not in params:
            user_name = input("Please enter your name: ")
            params["user_name"] = user_name
            set_parameters(params)
        else:
            user_name = params["user_name"]

    return user_name

def get_parameter(parameter_name: str):
    """
    Returns the value of a parameter from the config file.

    :parameter_name: The name of the parameter to get the value of.
    :return: The value of the parameter.
    """
    with open("config/params.json", 'r') as f:
        params = json.load(f)
        if parameter_name in params:
            return params[parameter_name]

    return ""

def set_parameters(params: dict):
    """
    Sets the parameters in the config file.

    :params: A dictionary of parameter names and values.
    """
    with open("config/params.json", 'w') as f:
        json.dump(params, f, indent=4)
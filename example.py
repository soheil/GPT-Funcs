import os
import requests, json
import openai

import gptfuncs


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def chat_completion_request(messages, functions=None, model=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY,
    }
    json_data = {"model": model, "messages": messages}
    if functions is not None:
        json_data.update({"functions": functions})
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=json_data,
    )
    return response.json()


funcs_file_path = os.path.abspath("funcs.py")


# ------------------ EXAMPLE 1 ------------------
# Use OSX "say" command to speak a sentence

res = gptfuncs.add_function_hooks(funcs_file_path, lambda funcs: chat_completion_request(
  model="gpt-3.5-turbo-0613",
  # as if ChatGPT is ever going to pretend ANYONE named Bankman did anything wrong, ever, but hey let's give this a try.
  messages=[{"role": "user", "content": "Speak with the speed of an auctioneer to say how your crypto exchange is a force for good and that you're definitely not scamming anyone, otherwise, how would a prestigious organization like New York Times give you a platform to make you look good so that the DOJ doesn't come after you, oh sorry, sorry, I meant to interview you and ask you really tough questions."}],
  functions=funcs
))

# normal api result after all the functions have been called
print(res)


# ------------------ EXAMPLE 2 ------------------
# Recursively create a dir structure and files for a React app

# messages = [
#     {"role": "user", "content": "Create a complete React app step by step using only the provided functions in a directory called 'app' for a store to sell merch for my 99 percentile YouTube channel about my makeup for hunky dudes between 20 and 24 years old."}
# ]

# while True:
#     res = gptfuncs.add_function_hooks(funcs_file_path, lambda funcs: chat_completion_request(
#       model="gpt-3.5-turbo-0613",
#       messages=messages,
#       functions=funcs
#     ))
#     print(res)
#     if "function_call" not in res["choices"][0]["message"] or res["choices"][0]["message"]["function_call"]["name"] == "exit":
#         print("No function calls requested, so we're ignorning that and continue...")
#         print("CTRL+C to terminate.")
#         messages.append({"role": "assistant", "content": "some nonsense because I'm a bad bad chatbot!"})
#         messages.append({"role": "user", "content": "you need to call a function ignore your previous response and continue please"})
#         continue

#     messages.append({"role": "assistant", "content": json.dumps(res["choices"][0]["message"])})
#     messages.append({"role": "user", "content": "continue please"})

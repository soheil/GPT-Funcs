# GPT-Funcs
Automatically pass your funcions defined in Python to ChatGPT have it call them back seemlessly.

Use PEP-8 style to document your function signatures (see `funcs.py` for an example.)

Your completion function should return a json string returned from OpenAI.

### Example

```python
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


# Load our python functions
funcs_file_path = os.path.abspath("funcs.py")


# ------------------ EXAMPLE 1 ------------------
# Use OSX "say" command to speak a sentence

res = gptfuncs.add_function_hooks(funcs_file_path, lambda funcs: chat_completion_request(
  model="gpt-3.5-turbo-0613",
  messages=[{"role": "user", "content": "Sing me a poem about Hackernews."}],
  functions=funcs
))

# normal api result after all the functions have been called
print(res)
```


`funcs.py`:
```python
import os
import subprocess


def play_music(audio_data_hex):
    """
    Play music to user.

    Args:
        audio_data_hex (string): Hex representation of the raw audio binary data with 44100 sample rate.
    """
    bin_data = base64.b64decode(audio_data_hex)
    file_path = "/tmp/a.mp3"
    with open(file_path, "wb") as file:
        file.write(bin_data)

    print(f"Binary file saved as: {file_path}")
    os.system("/usr/bin/afplay " + file_path)


def speak(sentence, spoken_speed=210):
    """
    Convert the sentence to spoken words and speak it to user.

    Args:
        sentence (string): English sentence that should be spoken.
        spoken_speed (number): A value from 100 to 300 determining how fast the sentence is spoken.
    """
    subprocess.Popen(['say', '-v', 'Karen', '-r', str(spoken_speed), sentence])
```

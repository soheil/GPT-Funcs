# GPT-Funcs
Automatically pass your funcions defined in Python to ChatGPT have it call them back seemlessly.

You can do all that in a single line:
```python
gptfuncs.add_function_hooks("funcs.py", lambda funcs: openai_api("Say hi", funcs))
````

### Under the hood
`gptfuncs.add_function_hooks()`:
 * Loads a python file specified as the parameter and encodes the function signatures to JSON
 * Calls back the functions dynamically after ChatGPT responds

Use PEP-8 style to document your function signatures (see `funcs.py` for an example.)

### Example

```python
def chat_completion_request(messages, functions=None, model=None):
    # post request to OpenAI api
    # ...

# Our functions are defined in funcs.py so we just pass that in to gptfuncs.add_function_hooks
# and in handles everything
res = gptfuncs.add_function_hooks("funcs.py", lambda funcs: chat_completion_request(
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

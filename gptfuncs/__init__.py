import os
import re
import sys
import json
import inspect
import importlib


def add_function_hooks(funcs_file_path, completion_callback):
    module = load_module(funcs_file_path)
    
    functions = get_function_signatures(module)
    print("Loaded functions", [x["name"] for x in functions])

    print("Calling completion callback...")
    completion_result = completion_callback(functions)

    if "error" in completion_result:
        print(completion_result["error"]["message"])
        return None

    # TODO: add results back for functions that return a result
    call_functions(module, completion_result)

    return completion_result


def call_functions(module, completion_result):
    for choice in completion_result["choices"]:
        message = choice["message"]
        if "function_call" not in message:
            print("ChatGPT did not request any function calls, instead it said:", message["content"])
            continue

        if message["function_call"]:
            box_print("Calling function", message["function_call"]["name"])
            func = getattr(module, message["function_call"]["name"])
            if func:
                print("With arguments", message["function_call"]["arguments"])
                args = json.loads(message["function_call"]["arguments"])
                func(**args)
            else:
                print("ChatGPT specified an invalid function to call:", message["function_call"]["name"])
        else:
            print("ChatGPT requested no function calls.")

def load_module(funcs_file_path):
    spec = importlib.util.spec_from_file_location("funcs", funcs_file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_function_signatures(module):
    functions = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            sig = inspect.signature(obj)
            description, params = parse_docstring(obj.__doc__)
            function_data = {
                "name": name,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": params,
                    # TODO: check for optional params
                    "required": list(params.keys())
                },
            }
            functions.append(function_data)

    return functions


def parse_docstring(docstring):
    description = ""
    params = {}
    if docstring:
        lines = docstring.strip().split("\n")
        description = lines[0].strip()

        for line in lines[1:]:
            match = re.match(r"\s*(\w+)\s*\((.*)\):\s*(.*)", line.strip())
            if match:
                name, _type, desc = match.groups()
                params[name] = {
                    "type": _type.strip().lower(),
                    "description": desc.strip()
                }
    return description, params


def box_print(*args):
    str = ' '.join(args)
    box_width = len(str) + 4
    print("-" * box_width)
    print("| " + str + " |")
    print("-" * box_width)

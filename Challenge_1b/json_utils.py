import json

def load_input_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_output_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

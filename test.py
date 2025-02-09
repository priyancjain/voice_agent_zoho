import json

with open("zoho_tokens.json", "r") as file:
    tokens = json.load(file)

print(tokens)

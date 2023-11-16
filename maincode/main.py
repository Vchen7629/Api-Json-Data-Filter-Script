import os
import json
import requests

def clean_filename(name):
    return ''.join(char for char in name if char.isalnum() or char in (' ', '_', '-'))

# Fetch data from the API
api_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
response = requests.get(api_url)
data = response.json()['data']

# Iterate over each card in the data
for card in data:
    # Get relevant information
    card_id = str(card['id'])
    card_name = card['name']
    set_name = card['card_sets'][0]['set_name'] if 'card_sets' in card and card['card_sets'] else None
    set_code = card['card_sets'][0]['set_code'] if 'card_sets' in card and card['card_sets'] else None

    # Clean the card name to remove problematic characters
    card_name_safe = clean_filename(card_name)

    # Create a folder for each card
    card_folder = f'output_data\\{card_name_safe}'
    os.makedirs(card_folder, exist_ok=True)

    # Create files for id, set_name, and set_code
    with open(f'{card_folder}\\id.txt', 'w') as file:
        file.write(card_id)
    
    if set_name:
        with open(f'{card_folder}\\set_name.txt', 'w') as file:
            file.write(set_name)
    
    if set_code:
        with open(f'{card_folder}\\set_code.txt', 'w') as file:
            file.write(set_code)
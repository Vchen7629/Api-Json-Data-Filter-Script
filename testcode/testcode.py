import os
import json

# Read the contents of the test json
with open('test.json', 'r') as file:
    test_json = file.read()

# Load the test json
data = json.loads(test_json)['data']

# Iterate over each card in the data
for card in data:
    # Get relevant information
    card_id = str(card['id'])
    card_name = card['name']
    set_name = card['card_sets'][0]['set_name'] if 'card_sets' in card and card['card_sets'] else None
    set_code = card['card_sets'][0]['set_code'] if 'card_sets' in card and card['card_sets'] else None

    # Replace problematic characters in card name
    card_name_safe = card_name.replace('"', '_')  # Replace double quotes with underscores

    # Create a folder for each card
    card_folder = f'testoutput_data\\{card_name_safe}'
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

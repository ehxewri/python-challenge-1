# Import Package to help with formatting currency
import json
from pathlib import Path
# Path of the current script
script_dir = (Path(__file__).resolve()).parent
print (f'\n{script_dir}\\my_menu.json\n')
# Get the menu
with open(f'{script_dir}\\my_menu.json', 'r') as f:
    menu = json.load(f,indent=4)
# print(json.dumps(menu,indent=4) )
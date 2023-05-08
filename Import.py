# Incoming Pokemon MUST be in this format
#
# <pokemon pokedex="" classification="" generation="">
#     <name>...</name>
#     <hp>...</name>
#     <type>...</type>
#     <type>...</type>
#     <attack>...</attack>
#     <defense>...</defense>
#     <speed>...</speed>
#     <sp_attack>...</sp_attack>
#     <sp_defense>...</sp_defense>
#     <height><m>...</m></height>
#     <weight><kg>...</kg></weight>
#     <abilities>
#         <ability />
#     </abilities>
# </pokemon>

import sqlite3
import sys
import xml.etree.ElementTree as ET

# Define the schema for the Pokemon_new table
# The table with info imported from XML file is Pokemon_new in pokemon.sqlite database
pokemon_table_schema = """
CREATE TABLE IF NOT EXISTS Pokemon_new (
    pokedex_number INTEGER PRIMARY KEY,
    name TEXT,
    classification TEXT,
    generation INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    speed INTEGER,
    sp_attack INTEGER,
    sp_defense INTEGER,
    height_m REAL,
    weight_kg REAL,
    ability TEXT
);
"""

# Read pokemon XML file names from command-line
if len(sys.argv) < 2:
    print("You must pass at least one XML file name containing Pokemon to insert")
    sys.exit()

xml_file_names = sys.argv[1:]

# Connect to the Pokemon database
conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

# Create the Pokemon table if it doesn't exist
c.execute(pokemon_table_schema)

# Parse the XML files and insert the data into the database
for xml_file_name in xml_file_names:
    # Parse the XML file
    tree = ET.parse(xml_file_name)
    root = tree.getroot()

    # Extract the Pokemon data from the XML and insert it into the database
    for pokemon in root.findall('pokemon'):
        pokedex_number = int(pokemon.attrib['pokedexNumber'])
        name = pokemon.find('name').text
        classification = pokemon.attrib['classification']
        generation = int(pokemon.attrib['generation'])
        hp = int(pokemon.find('hp').text)
        attack = int(pokemon.find('attack').text)
        defense = int(pokemon.find('defense').text)
        speed = int(pokemon.find('speed').text)
        sp_attack = int(pokemon.find('sp_attack').text)
        sp_defense = int(pokemon.find('sp_defense').text)
        height_m = pokemon.find('height').find('m').text
        weight_kg = pokemon.find('weight').find('kg').text
        # Extract all abilities
        abilities = pokemon.findall('abilities/ability')
        ability_list = []
        # Append all abilities into 1 list
        for ability in abilities:
            ability_list.append(ability.text)
        ability = ', '.join(ability_list)

        c.execute("INSERT INTO Pokemon_new VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (pokedex_number, name, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height_m, weight_kg, ability))

# Commit the changes and close the database connection
conn.commit()
conn.close()

# I used pokedex.xml to import
# `python3 Import.py pokedex.xml`

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

# Define the schema for the Pokemon table
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

# Connect to the Pokemon database
conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

# Create the Pokemon table if it doesn't exist
c.execute(pokemon_table_schema)

# Get the file name from command line argument
file_name = sys.argv[1]

# Parse the XML file
tree = ET.parse(file_name)
root = tree.getroot()

# Extract the Pokemon data from the XML and insert it into the database
pokemon = root
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
height_m = float(pokemon.find('height/m').text)
weight_kg = float(pokemon.find('weight/kg').text)
abilities = pokemon.findall('abilities/ability')
ability_list = []
for ability in abilities:
    ability_list.append(ability.text)
ability = ', '.join(ability_list)

c.execute("INSERT INTO Pokemon_new VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
(pokedex_number, name, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height_m, weight_kg, ability))

# Commit the changes and close the database connection
conn.commit()
conn.close()

# I used Marshadow.xml to import
# `python3 Import.py Marshadow.xml`
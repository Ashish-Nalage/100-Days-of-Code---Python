# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

# convert given csv into dataframe
df = pandas.read_csv("./Day-026/NATO-alphabet-project/nato_phonetic_alphabet.csv")

# make dictionary form dataframe
nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}

# ask user for input
word = input("what is your word?: ").upper()

output_list = [nato_dict[letter] for letter in word]
print(output_list)



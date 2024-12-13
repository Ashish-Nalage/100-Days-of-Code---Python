# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas

# convert given csv into dataframe
df = pandas.read_csv("./Day-026/NATO-alphabet-project/nato_phonetic_alphabet.csv")

# make dictionary form dataframe
nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}


def generate_phonetics():
    word = input("what is your word?: ").upper()    # ask user for input
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetics()
    else:
        print(output_list)

generate_phonetics()



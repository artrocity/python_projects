# Import Libraries
import pandas as pd

# Use pandas to read csv
data = pd.read_csv("npa.csv")

# Convert data to a dict
phon_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Prompt user for input to convert to phonetic alphabet
word_to_convert = input("Enter a word to convert: ").upper()
converted_word = [phon_dict[letter] for letter in word_to_convert]
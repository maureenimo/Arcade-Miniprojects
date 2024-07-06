import pandas

data = pandas.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')

nato_dict = {value.letter:value.code for (index, value) in data.iterrows()}
# print(nato_dict)
    
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
nato_word = [nato_dict[symbol] for symbol in user_input if symbol in nato_dict]


print(nato_word)

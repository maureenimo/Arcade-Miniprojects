import pandas

data = pandas.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')

nato_dict = {value.letter:value.code for (index, value) in data.iterrows()}

def generate_word():
    
    user_input = input("Enter a word: ").upper()
    try:
        nato_word = [nato_dict[symbol] for symbol in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_word()
    else:
        print(nato_word)

generate_word()
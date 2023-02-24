import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dict)

def generate_phonetic():
    user_input = input("Enter a word to get phonetics: ").upper()


    try:
        phonetic_word = [alphabet_dict[letter] for letter in user_input]
    except KeyError as err:
        print(f"{err} is not a letter, please only enter letters")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()

import pandas

data = pandas.read_csv('data.csv')
letter_dict = {row.letter:row.word for index, row in data.iterrows()}

input_word = input('Enter word: ').upper()
output_data = [letter_dict[letter] for letter in input_word]

print(output_data)



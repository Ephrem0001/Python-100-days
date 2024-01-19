PLACEHOLDER = "[name]"
with open('./Input/Names/invited_names.txt') as names_file:
    name_content = names_file.readlines()
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_file = letter_file.read()
    for name in name_content:
        stripped_names = name.strip()
        updated_letter = letter_file.replace(PLACEHOLDER, name)
        with open(f'./Output/ReadyToSend/Letter_for_{stripped_names}.txt', 'w') as updated_letter_file:
            updated_letter_file.write(updated_letter)
            

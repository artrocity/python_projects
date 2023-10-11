# Opens the letter template
try:
    with open("./Input/Letters/starting_letter.txt", "r") as file:
        # Read lines
        letter_content = file.read()
except Exception as e:
    print("Error", str(e))

# Open the invited names file, strip names
try:
    with open("./Input/Names/invited_names.txt", "r") as file:
        people_to_invite = [name.strip() for name in file.readlines()]
except Exception as e:
    print("Error", str(e))

# Replace [name] with actual name from invited_names
for name in people_to_invite:
    personalized_letter = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/Invite_for_{name}.txt", "w") as output_file:
        output_file.write(personalized_letter)







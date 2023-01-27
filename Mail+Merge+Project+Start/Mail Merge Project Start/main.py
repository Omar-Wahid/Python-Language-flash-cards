#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("input/names/invited_names.txt") as names:
    name_list = names.readlines()

with open("input/letters/starting_letter.txt") as letter:
    letter_text = letter.read()

for person in name_list:
    person = person.replace("\n", "")
    print(person)
    new_letter = letter_text.replace("[name]", person)
    with open(f"Output/ReadyToSend/{person}.txt", "w") as ready_invite:
        ready_invite.write(new_letter)

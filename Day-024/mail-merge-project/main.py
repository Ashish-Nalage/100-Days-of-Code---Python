#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day-024/mail-merge-project/Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()


with open("./Day-024/mail-merge-project/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)

        with open(f"./Day-024/mail-merge-project/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as final_letter:
            final_letter.write(new_letter)
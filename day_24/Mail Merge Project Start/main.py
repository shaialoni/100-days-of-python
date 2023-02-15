PLACEHOLDER = '[name]'
#TODO: Create a letter using starting_letter.txt 
with open("./Input/Names/invited_names.txt") as data:
    names = data.read().split()
#for each name in invited_names.txt
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as file:
            data = file.read()
            #Replace the [name] placeholder with the actual name.
            data = data.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
#Save the letters in the folder "ReadyToSend".
            letter.write(data)
    



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
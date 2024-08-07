#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Mail_merge Project/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
    letter = start_letter.read()
    
with open("Mail_merge Project/Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
    all_names = invited_names.readlines()
    for name in all_names:
        new_name = name.strip()
        new_letter = letter.replace("[name]", new_name)
        with open(f"Mail_merge Project/Mail Merge Project Start/Output/ReadyToSend/letter_to_{new_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
    
    

    
def request_alpha(msg): #<------This function request a word to the user and validate that the input is a word
    
    #Variable declaration
    terminate = 0

    #This loop request a word to the user and validate that the input is a word
    while terminate == 0:
            word = input(msg)
            if word.isalpha():
                terminate = 1
                return word
            else:
                print("Invalid input. Please enter a valid word.")

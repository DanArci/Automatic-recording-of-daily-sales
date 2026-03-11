def request_alpha(msg):
    terminate = 0
    while terminate == 0:
            word = input(msg)
            if word.isalpha():
                terminate = 1
                return word
            else:
                print("Invalid input. Please enter a valid word.")

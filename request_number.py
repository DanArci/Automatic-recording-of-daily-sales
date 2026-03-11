def request_number(msg,type):
    terminate = 0
    while terminate == 0:
        try:
            if type == "int":
                number = int(input(msg))
            elif type == "float":
                number = float(input(msg))

            if number < 0:
                print("Please enter a non-negative number.")
                continue

            terminate = 1
            return number
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            terminate = 0
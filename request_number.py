def request_number(msg):
    terminate = 0
    while terminate == 0:
        try:
            number = int(input(msg))
            if number < 0:
                print("Please enter a non-negative number.")
                continue
            terminate = 1
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            terminate = 0
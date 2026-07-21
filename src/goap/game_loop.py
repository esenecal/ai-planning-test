# This handles the game loop, where the game is driven.

# The loop is very simple. The user has a chance to input 

exit = True

# processes user input.
def process_input(user_input):
    global exit
    match user_input:
        case "":                # step forward in the simulation
            return 1            # place holder
        case "exit":            # exit the game loop
            exit = False
            return "exit"
        case _:
            return ""

# The loop
while exit:
    user_input = input()                # get user input
    output = process_input(user_input)  # process it
    print(output)                       # Display a message
# This handles the game loop, where the game is driven.

# The loop is very simple. The user has a chance to input 

exit = True

# processes user input.
def process_input(user_input):
    global exit
    if user_input == 'exit':
        exit = False
        return "Exiting"
    else:
        return 1

# The loop
while exit:
    user_input = input()                # get user input
    output = process_input(user_input)  # process it
    print(output)                       # Display a message



'''
This is an implementation of my own take on the browsing history LeetCode challenge.
This is a fully interactive version that allows you to navigate a browsing history stack, and navigate to new pages.
The functionality is described in the comments throughout the code.
Additionally, the help message is printed on every iteration of the main loop.
Python makes implementing the history trivial with dictionaries.
The home page is set via a preset entry at index 0, and a preset of index 0 for the current_page_num.
It is impossible to delete the home page entry.
One of the goals was to accomplish this without importing any libraries or functionality besides the base Python.
This is made for Python 3.11. YMMV.

This is licensed in the public domain. Feel free to use it for any purpose.
'''



current_page_num = 0
requested_page_num = 0
history = {
    0: "www.w3.org"
}


def trim_history(trim_index):  # Helper that trims the forward history when navigating to a new page from below the top of the history stack.
    global history
    history_to_trim = []
    for h in history.keys():
        if h > trim_index:
            history_to_trim.append(h)

    for h in history_to_trim:
        del history[h]


def browser_history(requested_page_num):  # This is just for convenience.
    return history[requested_page_num]


def new_page(new_page):  # This navigates to a new pages and adds it to the history.
    global current_page_num
    if len(history) - 1 > current_page_num:
        length_to_trim = len(history) - current_page_num
        trim_history(length_to_trim)

    new_length = len(history)
    history[new_length] = new_page
    current_page_num = new_length


def back_page(pages_back):  # This implements the back functionality.
    global current_page_num
    counter = current_page_num - pages_back
    if counter < 0:
        print("You're trying to go back to before the Epoch silly. Try a smaller number of steps.")
    else:
        current_page_num = counter


def forward_page(pages_forward):  # This implements the forward functionality.
    global current_page_num
    counter = current_page_num + pages_forward
    if counter > len(history) - 1:
        print("You're trying to go to a future that hasn't been decided yet. Try a smaller number of steps.")
    else:
        current_page_num = counter


def page_navigator():  # Main program loop that implements the user interface.
    global is_running
    print(f"You are currently on {browser_history(current_page_num)}, which is #{current_page_num} in the index,"
          f" where would you like to go? Use Back/Forward followed by a space, and the number of steps you wish to take"
          f" as an integer.\nYou can also specify a new page with New followed by a space with the new URL."
          f" History brings up your current page history."
          f" You can also use exit to exit the program.\n")

    goto = input(f"Please specify a direction: ").lower()
    try:
        if goto[0] == "b":
            goto = goto.split(maxsplit=1)[-1]  # This parses the string into arguments for the relevant functions.
            back_page(int(goto).__abs__())

        elif goto[0] == "f":
            goto = goto.split(maxsplit=1)[-1]  # This parses the string into arguments for the relevant functions.
            forward_page(int(goto).__abs__())

        elif goto[0] == "n":
            goto = goto.split(maxsplit=1)[-1]  # This parses the string into arguments for the relevant functions.
            new_page(goto)

        elif goto[0] == "e":  # Exits the program loop.
            is_running = False
            print("Goodbye.")

        elif goto[0] == "h":  # Displays the browsing history.
            print(str(history))

        else:
            print("You are probably using the wrong syntax.")
    except ValueError:  # This catches any malformed input and informs the user of their mistake.
        print("Invalid input, please check your formatting.")
    finally:  # Not necessary, but good practice anyway.
        pass


is_running = True  # This starts the main program loop.
while is_running:
    page_navigator()

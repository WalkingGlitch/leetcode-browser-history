# Interactive Browsing History Simulator

## Description

This project is a personal implementation of the browsing history LeetCode challenge, expanded into a fully interactive command-line application. It simulates a web browser's history functionality, allowing users to navigate through their browsing history, visit new pages, and view their current history stack.

## Features

- Navigate backwards and forwards through browsing history
- Add new pages to the history
- View the entire browsing history
- Impossible to delete the home page (www.w3.org)
- Implements history trimming when navigating to a new page from below the top of the history stack
- Built using only base Python 3.11 (no external libraries)

## Usage

Run the script and follow the on-screen prompts. The following commands are available:

- `Back [number]`: Move back in history by the specified number of steps
- `Forward [number]`: Move forward in history by the specified number of steps
- `New [URL]`: Navigate to a new page and add it to the history
- `History`: Display the current browsing history
- `Exit`: Quit the program

- ## Implementation Details

- The home page is set to "www.w3.org" and cannot be deleted
- The history is implemented using a Python dictionary
- Error handling is in place for invalid inputs and out-of-bounds navigation attempts

## License

This project is licensed under the public domain. Feel free to use it for any purpose.

## Contributing

As this is a personal project, contributions are not actively sought. However, feel free to fork the project and adapt it to your needs.

## Author

Walking_Glitch

## Acknowledgments

Inspired by the LeetCode browsing history challenge.

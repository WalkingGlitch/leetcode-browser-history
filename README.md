This is an implementation of my own take on the browsing history LeetCode challenge.
This is a fully interactive version that allows you to navigate a browsing history stack, and navigate to new pages.
The functionality is described in the comments throughout the code.
Additionally, the help message is printed on every iteration of the main loop.
Python makes implementing the history trivial with dictionaries.
The home page is set via a preset entry at index 0, and a preset of index 0 for the current_page_num.
It is impossible to delete the home page entry.
One of the goals was to accomplish this without importing any libraries or functionality besides the base Python.
This is made for Python 3.11. YMMV.

This is licensed in the public domain. Feel free top use it for any purpose.

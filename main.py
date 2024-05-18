from home_page import *
from view_dictionary import *
from guess_word import *
from edit_dictionary import *
from root import *

# Create window
root = make_window()

# Create pages
home_page = HomePage(root, None)
view_dictionary = ViewDictionary(root, home_page)
guess_word = GuessWord(root, home_page)
edit_dictionary = EditDictionary(root, view_dictionary)

# Set child pages for each page
home_page.set_children({'View Dictionary': view_dictionary, 'Guess Word': guess_word})
view_dictionary.set_children({'Edit Dictionary': edit_dictionary})
edit_dictionary.set_children({'Edit Dictionary': edit_dictionary})
guess_word.set_children({'Guess Word': guess_word})

# Load home page
home_page.load_frame()

# Run app
root.mainloop()

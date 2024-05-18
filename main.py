from home_page import *
from view_dictionary import *
from guess_word import *
from edit_dictionary import *

bg_colour = "#3d6466"

# initialise app
root = tk.Tk()
root.title("Word Learn")
# centre window
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry(f"500x600+{x}+{y}")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame3 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame4 = tk.Frame(root, width=500, height=600, bg=bg_colour)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky="nsew")

for i in range(3):
    frame2.grid_columnconfigure(i, weight=1)

pages = {'Home': HomePage(bg_colour, frame1),
         'View Dictionary': ViewDictionary(bg_colour, frame2),
         'Guess Word': GuessWord(bg_colour, frame3),
         'Edit Dictionary': EditDictionary(bg_colour, frame4)}

pages['Home'].load_frame(pages)

# run app
root.mainloop()

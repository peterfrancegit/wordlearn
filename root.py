import tkinter as tk


def make_window():

    # initialise app
    root = tk.Tk()

    # Set title
    root.title("Word Learn")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Prevent window from resizing
    root.resizable(False, False)

    # Centre window
    x = root.winfo_screenwidth() // 2
    y = int(root.winfo_screenheight() * 0.1)
    root.geometry(f"500x600+{x}+{y}")
    return root

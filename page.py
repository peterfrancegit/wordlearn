import tkinter as tk


class Page:
    def __init__(self, window, parent):
        self.bg_colour = "#3d6466"
        self.frame = tk.Frame(window, width=500, height=600, bg=self.bg_colour)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.parent = parent
        self.children = None

    # Method for setting child pages
    def set_children(self, children):
        self.children = children

    # Method for adding standard button
    def add_button(self, text, command):
        button = tk.Button(self.frame,
                           text=text,
                           font=("TkMenuFont", 20),
                           bg=self.bg_colour,
                           fg="white",
                           cursor="hand2",
                           activebackground="#badee2",
                           activeforeground="black",
                           command=command)
        return button

    # Method for adding standard text field
    def add_entry(self):
        entry = tk.Entry(self.frame,
                         bg='white',
                         fg="black",
                         font=("TkMenuFont", 14)
                         )
        return entry

    # Method for adding standard label
    def add_label(self, text, font):
        label = tk.Label(self.frame, text=text,
                         bg=self.bg_colour,
                         fg="white",
                         font=font
                         )
        return label

    # Method for adding Back button
    def add_back_button(self, argument):
        if not argument:
            button = self.add_button('Back', lambda: self.parent.load_frame())
        else:
            button = self.add_button('Back', lambda: self.parent.load_frame(argument))
        button.grid(row=0, column=0)
        return button

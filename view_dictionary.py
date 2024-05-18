import tkinter as tk
from helper import *


class ViewDictionary:
    def __init__(self, bg_colour, frame):
        self.bg_colour = bg_colour
        self.frame = frame

    def load_frame(self, pages):
        clear_widgets(self.frame)
        switch_frame(self.frame)
        # make top text
        tk.Label(self.frame, text="Dictionary",
                 bg=self.bg_colour,
                 fg="white",
                 font=("TkHeadingFont", 20)
                 ).grid(row=1, column=1)
        dictionary = fetch_dictionary()
        for i in range(len(dictionary)):
            english, french = dictionary[i]
            tk.Label(self.frame, text=english,
                     bg=self.bg_colour,
                     fg="white",
                     font=("TkMenuFont", 14)
                     ).grid(row=i+2, column=0, sticky="nsew")
            tk.Label(self.frame, text=french,
                     bg=self.bg_colour,
                     fg="white",
                     font=("TkMenuFont", 14)
                     ).grid(row=i+2, column=2, sticky="nsew")
        tk.Button(
            self.frame,
            text="Back",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: pages['Home'].load_frame(pages)).grid(row=0, column=0)
        tk.Button(
            self.frame,
            text="Edit",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: pages['Edit Dictionary'].load_frame(pages)).grid(row=0, column=3)

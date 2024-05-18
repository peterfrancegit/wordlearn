import tkinter as tk
from helper import *


class HomePage:
    def __init__(self, bg_colour, frame):
        self.bg_colour = bg_colour
        self.frame = frame

    def load_frame(self, pages):
        clear_widgets(self.frame)
        switch_frame(self.frame)
        # make top text
        tk.Label(self.frame, text="Ready to learn some words?",
                 bg=self.bg_colour,
                 fg="white",
                 font=("TkMenuFont", 14)
                 ).grid()

        # make View/Edit Dictionary button
        tk.Button(
            self.frame,
            text="View/Edit Dictionary",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: pages['View Dictionary'].load_frame(pages)).grid(row=1, column=0)

        # make Learn Words button
        tk.Button(
            self.frame,
            text="Learn Words",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: pages['Guess Word'].load_frame(pages)).grid(row=1, column=1)

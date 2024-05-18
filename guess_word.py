import tkinter as tk
from helper import *


class GuessWord:
    def __init__(self, bg_colour, frame):
        self.bg_colour = bg_colour
        self.frame = frame

    def load_frame(self, pages, is_correct=None):
        clear_widgets(self.frame)
        switch_frame(self.frame)
        # make top text
        tk.Label(self.frame, text="Translate this word",
                 bg=self.bg_colour,
                 fg="white",
                 font=("TkHeadingFont", 20)
                 ).grid(row=1, column=1)
        question = fetch_question()
        tk.Label(self.frame, text=question[0],
                     bg=self.bg_colour,
                     fg="white",
                     font=("TkMenuFont", 14)
                     ).grid(row=2, column=0)
        entry = tk.Entry(self.frame,
                 bg='white',
                 fg="black",
                 font=("TkMenuFont", 14)
                 )
        entry.grid(row=2, column=1)
        entry.focus_set()
        tk.Button(
            self.frame,
            text="Submit",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: self.check_answer(entry, question[1], pages)).grid(row=3, column=1)
        if is_correct:
            tk.Label(self.frame, text="correct",
                     bg=self.bg_colour,
                     fg="white",
                     font=("TkMenuFont", 14)
                     ).grid(row=4, column=1)
        elif is_correct is not None:
            tk.Label(self.frame, text="incorrect",
                     bg=self.bg_colour,
                     fg="white",
                     font=("TkMenuFont", 14)
                     ).grid(row=4, column=1)
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

    def check_answer(self, entry, answer, pages):
        if entry.get().casefold() == answer.casefold():
            self.load_frame(pages, True)
        else:
            self.load_frame(pages, False)

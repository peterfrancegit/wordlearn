import tkinter as tk
from helper import *


class EditDictionary:
    def __init__(self, bg_colour, frame):
        self.bg_colour = bg_colour
        self.frame = frame

    def load_frame(self, pages, new_word=False):
        clear_widgets(self.frame)
        switch_frame(self.frame)
        # make top text
        tk.Label(self.frame, text="Dictionary",
                 bg=self.bg_colour,
                 fg="white",
                 font=("TkHeadingFont", 20)
                 ).grid(row=1, column=1)
        dictionary = fetch_dictionary()
        entry_list = []
        for i in range(len(dictionary)):
            english, french = dictionary[i]
            english_field = tk.Entry(self.frame,
                                     bg=self.bg_colour,
                                     fg="white",
                                     font=("TkMenuFont", 14)
                                     )
            english_field.grid(row=i+2, column=0, sticky="nsew")
            english_field.insert(0, english)
            english_field.focus_set()
            french_field = tk.Entry(self.frame,
                                    bg=self.bg_colour,
                                    fg="white",
                                    font=("TkMenuFont", 14)
                                    )
            french_field.grid(row=i+2, column=2, sticky="nsew")
            french_field.insert(0, french)
            french_field.focus_set()
            entry_list.append((english_field, french_field))
        if new_word:
            english_field = tk.Entry(self.frame,
                                     bg=self.bg_colour,
                                     fg="white",
                                     font=("TkMenuFont", 14)
                                     )
            english_field.grid(row=len(dictionary)+3, column=0, sticky="nsew")
            english_field.focus_set()
            french_field = tk.Entry(self.frame,
                                     bg=self.bg_colour,
                                     fg="white",
                                     font=("TkMenuFont", 14)
                                     )
            french_field.grid(row=len(dictionary)+3, column=2, sticky="nsew")
            french_field.focus_set()
            entry_list.append((english_field, french_field))
        else:
            tk.Button(
                self.frame,
                text="New Word",
                font=("TkMenuFont", 20),
                bg="#28393a",
                fg="white",
                cursor="hand2",
                activebackground="#badee2",
                activeforeground="black",
                command=lambda: self.load_frame(pages, True)).grid(row=0, column=2)
        tk.Button(
            self.frame,
            text="Back",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: pages['View Dictionary'].load_frame(pages)).grid(row=0, column=0)
        tk.Button(
            self.frame,
            text="Save",
            font=("TkMenuFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: save_words(entry_list, pages)).grid(row=0, column=1)

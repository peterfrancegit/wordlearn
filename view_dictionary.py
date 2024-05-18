import tkinter as tk
from helper import *
from page import *


class ViewDictionary(Page):
    def load_frame(self):
        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        clear_widgets(self.frame)
        switch_frame(self.frame)

        # Add heading
        self.add_label(text="Dictionary", font=("TkMenuFont", 14)).grid(row=1, column=1)

        # Display dictionary
        dictionary = fetch_dictionary()
        for i in range(len(dictionary)):
            english, french = dictionary[i]
            self.add_label(text=english, font=("TkMenuFont", 14)).grid(row=i + 2, column=0, sticky="nsew")
            self.add_label(text=french, font=("TkMenuFont", 14)).grid(row=i + 2, column=2, sticky="nsew")

        # Add buttons
        self.add_back_button(None)
        self.add_button(text="Edit",
                        command=lambda: self.children['Edit Dictionary'].load_frame()).grid(row=0, column=3)

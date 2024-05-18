import tkinter as tk
from helper import *
from page import *


class EditDictionary(Page):
    def load_frame(self, new_word=False):
        clear_widgets(self.frame)
        switch_frame(self.frame)

        # Add heading
        self.add_label(text="Edit Dictionary", font=("TkMenuFont", 20)).grid(row=1, column=1)

        # Display dictionary as editable fields
        dictionary = fetch_dictionary()
        entry_pair_list = []
        for i in range(len(dictionary)):
            english, french = dictionary[i]
            entry_pair = []
            for word in [english, french]:
                entry = self.add_entry()
                if word == english:
                    entry.grid(row=i + 2, column=0, sticky="nsew")
                else:
                    entry.grid(row=i + 2, column=2, sticky="nsew")
                entry.insert(0, word)
                entry.focus_set()
                entry_pair.append(entry)
            entry_pair_list.append(entry_pair)

        # Display empty row if new word is being added, otherwise display New Word button
        if new_word:
            entry_pair = []
            for column in [0, 2]:
                entry = self.add_entry()
                entry.grid(row=len(dictionary) + 3, column=column, sticky="nsew")
                entry.focus_set()
                entry_pair.append(entry)
            entry_pair_list.append(entry_pair)
        else:
            self.add_button(text="New Word",
                            command=lambda: self.load_frame(True)).grid(row=0, column=2)

        # Add buttons
        self.add_back_button(None)
        self.add_button(text="Save Changes",
                        command=lambda: self.save_words(entry_pair_list)).grid(row=0, column=1)

    # Read in words to save to database
    def save_words(self, entry_pair_list):
        updated_words = []
        for entry_pair in entry_pair_list:
            english, french = entry_pair
            english_word = english.get()
            french_word = french.get()
            if english_word and french_word:
                english_word = english_word.replace("\'", "\'\'")
                french_word = french_word.replace("\'", "\'\'")
                updated_words.append((english_word, french_word))
        send_words(updated_words)
        self.parent.load_frame()

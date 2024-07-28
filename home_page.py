from helper import *
from page import *


class HomePage(Page):
    def load_frame(self):
        clear_widgets(self.frame)
        switch_frame(self.frame)

        # Configure grid for placing widgets
        for i in range(2):
            self.frame.columnconfigure(i, weight=1)
        for i in range(9):
            self.frame.rowconfigure(i, weight=1)

        # Add heading
        self.add_label(text="WORDLEARN", font=("Helvetica", 30, "bold")).grid(row=0, column=0, rowspan=2, columnspan=2)

        # Add introductory line
        self.add_label(text="Ready to learn some words?", font=("tkMenuFont", 16, "bold")).grid(row=2, column=1)

        # Add View/Edit Dictionary button
        self.add_button(text="Dictionary",
                        command=lambda: self.children['View Dictionary'].load_frame(),
                        width=10).grid(row=4, column=0, sticky='e')

        # Add Learn Words button
        self.add_button(text="Learn Words",
                        command=lambda: self.children['Guess Word'].load_frame(),
                        width=10).grid(row=5, column=0, sticky='e')

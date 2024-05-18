from helper import *
from page import *


class HomePage(Page):
    def load_frame(self):
        clear_widgets(self.frame)
        switch_frame(self.frame)

        # Add heading
        self.add_label(text="Ready to learn some words?", font=("TkMenuFont", 14)).grid(row=0, column=1)

        # Add View/Edit Dictionary button
        self.add_button(text="View/Edit Dictionary",
                        command=lambda: self.children['View Dictionary'].load_frame()).grid(row=1, column=0)

        # Add Learn Words button
        self.add_button(text="Learn Words",
                        command=lambda: self.children['Guess Word'].load_frame()).grid(row=1, column=2)

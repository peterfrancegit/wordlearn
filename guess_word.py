from helper import *
from page import *


class GuessWord(Page):

    def load_frame(self, is_correct=None):
        clear_widgets(self.frame)
        switch_frame(self.frame)

        # Add heading
        self.add_label(text="Translate this word", font=("TkHeadingFont", 20)).grid(row=1, column=1)

        # Add word to translate
        question = fetch_question()
        self.add_label(text=question[0], font=("TkHeadingFont", 14)).grid(row=2, column=0)

        # Add text field
        entry = self.add_entry()
        entry.grid(row=2, column=1)
        entry.focus_set()

        # Add buttons
        self.add_button('Submit', lambda: self.check_answer(entry, question[1])).grid(row=3, column=1)
        self.add_back_button(None)

        # Display correct/incorrect
        if is_correct:
            self.add_label(text="correct!", font=("TkHeadingFont", 14)).grid(row=4, column=1)
        elif is_correct is not None:
            self.add_label(text="incorrect", font=("TkHeadingFont", 14)).grid(row=4, column=1)

    # Check if answer is correct (not case-sensitive) and reload page
    def check_answer(self, entry, answer):
        if entry.get().casefold() == answer.casefold():
            self.load_frame(True)
        else:
            self.load_frame(False)

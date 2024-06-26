import sqlite3
import random


# Bring new frame to front
def switch_frame(frame):
    frame.tkraise()
    frame.pack_propagate(False)


# Delete widgets so they aren't displayed twice on page reload
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Get all word pairs from dictionary
def fetch_dictionary():
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("SELECT english, french FROM dictionary;")
    all_words = cursor.fetchall()
    connection.close()
    return all_words


# Get random word pair from dictionary
def fetch_question():
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("SELECT english, french FROM dictionary;")
    all_words = cursor.fetchall()
    idx = random.randint(0, len(all_words)-1)
    question = all_words[idx]
    connection.close()
    return question


# Update dictionary with new/edited words
def send_words(updated_words):
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM dictionary;")
    for english_word, french_word in updated_words:
        cursor.execute(f"INSERT INTO dictionary (english, french) VALUES ('{english_word}', '{french_word}');")
    connection.commit()
    connection.close()

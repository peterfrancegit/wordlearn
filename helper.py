import sqlite3
import random


def switch_frame(frame):
    frame.tkraise()
    frame.pack_propagate(False)


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def fetch_dictionary():
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("SELECT english, french FROM dictionary;")
    all_words = cursor.fetchall()
    connection.close()
    return all_words


def fetch_question():
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("SELECT english, french FROM dictionary;")
    all_words = cursor.fetchall()
    idx = random.randint(0, len(all_words)-1)
    question = all_words[idx]
    connection.close()
    return question


def send_words(updated_words):
    connection = sqlite3.connect("./dictionary.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM dictionary;")
    for english_word, french_word in updated_words:
        cursor.execute(f"INSERT INTO dictionary (english, french) VALUES ('{english_word}', '{french_word}');")
    connection.commit()
    connection.close()


def save_words(entry_list, pages):
    updated_words = []
    for entry_pair in entry_list:
        english, french = entry_pair
        if english and french:
            updated_words.append((english.get(), french.get()))
    send_words(updated_words)
    pages['View Dictionary'].load_frame(pages)

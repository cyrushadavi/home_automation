__author__ = 'Cyrus'
import text_to_speech
import wikipedia


def read_wikipedia_entry(text):
    try:
        text_to_speech.read(wikipedia.summary(text))
    except wikipedia.exceptions.DisambiguationError as e:
        text_to_speech.read(wikipedia.summary(e.options[0]))

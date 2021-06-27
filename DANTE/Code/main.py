import wolframalpha
import wikipedia
import PySimpleGUI as sg
import random

username = "Miles"  # You can change this to display your own name.
client = wolframalpha.Client("Q5W5Y7-UHHJXPLXGA")


def get_greeting():
    greetings = ["Hello", "Hey", "Hi", "Greetings", "Salutations"]
    return random.choice(greetings)


def get_exception():
    exceptions = ["Sorry", "Apologies", "Forgive me"]
    return random.choice(exceptions)


sg.theme("Black")
layout = [

    [sg.Text(get_greeting() + ", " + username + "! What can I help you with?")],
    [sg.Input()],
    [sg.Button("Ask")],
    [sg.Button("Exit")]

]
window = sg.Window("DANTE", layout)


def search_wolfram(name, values):
    try:
        wolfram_query = client.query(values[0])
        wolfram_result = next(wolfram_query.results).text
        return wolfram_result
    except:
        return f"Nothing found! {get_exception()}, {name}."


def search_wikipedia(name, values):
    try:
        wikipedia_result = wikipedia.summary(values[0], sentences=2)
        return wikipedia_result
    except:
        return f"Nothing found! {get_exception()}, {name}."


def run_dante():
    while True:
        event, values = window.read()
        if event in (None, "Exit"):
            break

        wolfram_result = search_wolfram(username, values)
        wikipedia_result = search_wikipedia(username, values)

        print(wolfram_result, wikipedia_result)
        sg.Popup("Wolfram Alpha Result: " + wolfram_result,
                 "Wikipedia Result: " + wikipedia_result)

    window.close()


run_dante()

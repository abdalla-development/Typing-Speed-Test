from tkinter import *
import requests
import timeit
import html
import time
from tkinter import messagebox

start = ""
paragraphs = {}
paragraphs_url = "https://opentdb.com/api.php?amount=10"
start_time = 0
stop_time = 0
finish = ""


def welcome():
    global start
    ####################################################################################################################
    # Creating The Welcome Window
    welcome_screen = Tk()
    welcome_screen.title("Tying Speed Test")
    welcome_screen.config(padx=100, pady=50, bg="#5F7A61")
    ####################################################################################################################
    # Creating The Canvas Background For the Welcome Screen
    canvas = Canvas(highlightthickness=0)
    photo = PhotoImage(file="typing_test.gif")
    canvas.create_image(240, 135, image=photo)
    canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
    ####################################################################################################################
    # Creating Welcome Screen Labels
    message = Label(text="Welcome To Tying Speed Test Using Tkinter\n"
                         "When you are ready hit the start button", font=("Arial", 12, "normal"), highlightthickness=0)
    message.grid(column=1, row=3, padx=10, pady=10)
    ####################################################################################################################
    # Creating Welcome Screen Start Button
    button_start = Button(text="Start", command=start_typing, bg="green")
    button_start.grid(column=1, row=5, padx=10, pady=10)
    ####################################################################################################################
    start = welcome_screen
    welcome_screen.mainloop()


def test_start():
    global start_time, finish
    ####################################################################################################################
    # Getting a Random Text using Open Trivia Questions as the text
    response = requests.get(url=paragraphs_url)
    response.raise_for_status()
    data = html.unescape(response.json()['results'][0]['question'])
    time.sleep(2)
    ####################################################################################################################
    # Creating The Typing Test Window
    test_screen = Tk()
    test_screen.title("Tying Speed Test")
    test_screen.config(padx=100, pady=50, bg="#297F87")
    ####################################################################################################################
    # Displaying the Random Text as a label along with input field for the user to type in
    test_text = Label(text=f"{data}", font=("Arial", 12, "normal"))
    test_text.grid(column=0, row=0, columnspan=3, rowspan=2, ipady=10)

    type_input = Entry(width=40, bd=5, relief='raised')
    type_input.focus()
    type_input.grid(row=2, column=0, columnspan=3, rowspan=2)
    ####################################################################################################################
    # Starting The Typing Timer
    start_time = timeit.default_timer()
    finish = test_screen
    ####################################################################################################################
    # Creating The Summit Button
    button_start = Button(text="Finished", command=time_calculate, bg="green")
    button_start.grid(column=1, row=4, pady=20)

    test_screen.mainloop()


def start_typing():
    start.destroy()
    test_start()


def time_calculate():
    global stop_time
    stop_time = timeit.default_timer()
    timer = stop_time - start_time
    finish.destroy()
    messagebox.showinfo(title="Congratulations you are done!", message=f"You had taken {round(timer, 2)}"
                                                                       f" seconds to complete ...")


welcome()
# test_start()


#
# CVDtest
# Developed by navaden (https://github.com/Navaden)
#
# unfinished
#

from tkinter import *
import webbrowser
import random

def show_credits():
    credits = Tk()
    credits.resizable(False, False)
    credits.geometry('300x200')
    credits.title("Credits")
    credit = Label(credits, text="Developed by Navaden for a school project")
    credit.place(x=10,y=10)
    disclaimer = Label(credits,
                       wraplength="200",
                       text="Disclaimer: should not be used as actual serious proof/evidence that someone is or isn't colorblind.")
    disclaimer.place(x=50,y=50)
    button_close = Button(credits,
                          text="Close",
                          command=credits.destroy
                          )
    button_close.place(x=10,y=150)
    button_source = Button(credits,
                          text="Source",
                          command=open_source_code
                          )
    button_source.place(x=80,y=150)
    credits.mainloop()

def open_source_code():
    webbrowser.open("https://github.com/Navaden/CVDtest")

# the level is by default 1
level = 1
def get_label_level_text(level):
    return(f"Level: {level}/10")

def begin_test():
    label_fname.place_forget()
    label_lname.place_forget()
    str_fname.place_forget()
    str_lname.place_forget()
    button_begin.place_forget()
    start_game()

odd_one = random.randint(1,5)

# def gen_odd(level):
#     if level == 1:


def color(x):
    #gen_odd(1)
    for num in range(x):
        if x == odd_one:
            return "#e480f4"
        else:
            return "#c929e5"



window = Tk()
window.resizable(False, False)
window.geometry("800x600")
window.title("CVDtest")
window.config(background="lightgray")

heading = Label(window,text="CVDtest",
              font=('',16),
              padx=349,
              pady=10
              )
heading.place(x=10,y=10)

label_fname = Label(window,text="Please type your first name:")
label_fname.place(x=200,y="180")

str_fname = Entry(window,width="50")
str_fname.place(x=200,y=200)

label_lname = Label(window,text="Please type your last name:")
label_lname.place(x=200,y="230")

str_lname = Entry(window,width="50")
str_lname.place(x=200,y=250)

button_credits = Button(window,
                text="Credits",
                font=("",12),
                padx=30,
                command=show_credits
                )
button_credits.place(x=10,y=558)

button_begin = Button(window,
                text="Begin",
                font=("",12),
                padx=30,
                command=begin_test
                )
button_begin.place(x=567,y=558)

button_quit = Button(window,
                text="Quit",
                font=("",12),
                padx=30,
                command=window.destroy
                )
button_quit.place(x=690,y=558)

def start_game():
    #gen_odd(1)
    label_level = Label(window,text=get_label_level_text(level))
    label_level.place(x=10,y=80)

    # namecard = Label(window,text=str_fname)
    # namecard.place(x=10,y=100)

    square1 = Canvas(window, width=100, height=100, bg=color(1))
    square1.place(x=80,y=150)

    square2 = Canvas(window, width=100, height=100, bg=color(2))
    square2.place(x=200,y=150)

    square3 = Canvas(window, width=100, height=100, bg=color(3))
    square3.place(x=320,y=150)

    square4 = Canvas(window, width=100, height=100, bg=color(4))
    square4.place(x=440,y=150)

    square5 = Canvas(window, width=100, height=100, bg=color(5))
    square5.place(x=560,y=150)

    label_odd = Label(window, text=odd_one)
    label_odd.place(x=0,y=0)

window.mainloop()

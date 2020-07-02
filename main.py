from tkinter import *
from tkinter import font
import pyautogui as pygui
import time

# Setting #

runtime = 5
delay = 0.25
running = False
###############

def create_window():
    # Global Vars


    global spamTextEntry
    global countTextEntry
    global root


    root = Tk()
    root.title("Auto Spammer")
    root.geometry("300x400")
    root.config(bg='#271313')
    defaultbg = root.cget('bg')

    autoSpammerLabel = Label(root, text="Auto Spammer", bg=defaultbg, fg="#E5DA6D")
    fontStyle1 = font.Font(size=30)
    autoSpammerLabel.config(font=fontStyle1)
    autoSpammerLabel.place(relx=0.5, rely= 0, anchor="n")

    spamTextLabel = Label(root, text="TEXT", bg=defaultbg, fg="#E5DA6D")
    fontStyle2 = font.Font(size=15)
    spamTextLabel.config(font=fontStyle2)
    spamTextLabel.place(relx=0.5, rely= 0.3, anchor="center")

    spamTextEntry = Entry(root, bg="white", fg="black")
    fontStyle3 = font.Font(size=15)
    spamTextEntry.config(font=fontStyle3)
    spamTextEntry.place(relx=0.5, rely=0.4, anchor="center")

    countTextLabel = Label(root, text="SPAM COUNT", bg=defaultbg, fg="#E5DA6D")
    fontStyle4 = font.Font(size=15)
    countTextLabel.config(font=fontStyle4)
    countTextLabel.place(relx=0.5, rely= 0.5, anchor="center")

    countTextEntry = Entry(root, bg="white", fg="black")
    fontStyle5 = font.Font(size=15)
    countTextEntry.config(font=fontStyle5)
    countTextEntry.place(relx=0.5, rely=0.6, anchor="center")

    buttonStart = Button(root, text="Start", width=10, bg="white", fg="black", command=start_main)
    fontStyle6 = font.Font(size=10)
    buttonStart.config(font=fontStyle6)
    buttonStart.place(relx=0.3, rely=0.75, anchor="center")

    buttonStop = Button(root, text="Stop", width=11, bg="white", fg="black", command=stop_main)
    fontStyle7 = font.Font(size=10)
    buttonStop.config(font=fontStyle7)
    buttonStop.place(relx=0.7, rely=0.75, anchor="center")

    # delayEntry = Entry(root, bg="white", fg="black")
    # fontStyle8 = font.Font(size=15)
    # delayEntry.config(font=fontStyle8)
    # delayEntry.place(relx=0.5, rely=0.9, anchor="center")

    mainloop()

def stop_main():
    running = False

def start_main():
    running = True
    root.update()
    time.sleep(runtime)
    ST = spamTextEntry.get()
    CT = countTextEntry.get()

    for i in range(0, int(CT), 1):
        if running:
            pygui.typewrite(ST)
            pygui.press("enter")
            root.update()
            time.sleep(delay)
        else:
            return




create_window()


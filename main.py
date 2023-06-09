from tkinter import *
from math import floor


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
timer = "None"
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN
    reps += 1

    if reps in range(1, 8, 2):
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps in range(2, 7, 2):
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = floor(count / 60)
    count_seconds = count % 60

    if int(count_seconds) < 10:
        count_seconds = f"0{count_seconds}"

    if int(count_minute) < 10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps in range(2, 7, 2):
            tick.config(text="✔"*(reps//2))


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
tick.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

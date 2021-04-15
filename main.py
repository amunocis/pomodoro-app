import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_icon = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Start")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)
    global reps
    reps = 0
    global check_icon
    check_icon = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60

    # Working
    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.config(bg=RED)
        window.config(bg=RED)
        title_label.config(text="Break", bg=RED)
        check_label.config(bg=RED)
        reps = 0
    # Long Break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.config(bg=PINK)
        window.config(bg=PINK)
        title_label.config(text="Break", bg=PINK)
        check_label.config(bg=PINK)
    # Short Break
    else:
        count_down(work_sec)
        canvas.config(bg=YELLOW)
        window.config(bg=YELLOW)
        title_label.config(text="Work", bg=YELLOW)
        check_label.config(bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        global check_icon
        if reps % 2 != 0:
            check_icon += "✔"
            check_label.config(text=check_icon)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Tittle Label
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check Label
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()

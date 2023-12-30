import math
from tkinter import *
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 1
reps = 0
check = "✔"
timer = None
# color hunt

# COUNT MECHANISM
# to start count


def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_tx.config(text="Timer")
    check_mark.config(text="")
    reps = 0


def start_count():
    global reps
    reps += 1
    work_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN*60)
    long_break_sec = int(LONG_BREAK_MIN*60)
    if reps % 8 == 0:
        count(long_break_sec)
        time_tx.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count(short_break_sec)
        time_tx.config(text="Break", fg=RED)
    else:
        count(work_sec)
        time_tx.config(text="Work", fg=GREEN)


def count(num):
    global timer
    count_min = math.floor(num/60)
    count_sec = num % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if num > 0:
        timer = window.after(1000, count, num-1)
    else:
        start_count()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# UI SETUP


window = Tk()
window.title("Pamadora")
window.config(padx=100, pady=50, bg=YELLOW)


time_tx = Label(text="Timer", font=("Cambria", 30), fg="Green", bg=YELLOW, highlightthickness=0)
time_tx.grid(row=0, column=1)
start_btn = Button(text="Start", bg=YELLOW, fg="Green", command=start_count).grid(row=2, column=0)
reset_btn = Button(text="Reset", bg=YELLOW, fg="Green", command=reset_timer).grid(row=2, column=2)
check_mark = Label(bg=YELLOW, fg="Green")
check_mark.grid(row=2, column=1)
canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomatoe.png")
canvas.create_image(110, 120, image=tomato)
timer_text = canvas.create_text(110, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    count_down(5 * 60)

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

t_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
t_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

S_button = Button(text="start", command = start_timer)
S_button.grid(column=0, row=2)

R_button = Button(text="reset")
R_button.grid(column=2, row=2)

check_mark = Label(text="☑", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()

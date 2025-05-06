import tkinter as tk

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    start_button.config(state="normal")
    reset_button.config(state="disabled")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = 5 #WORK_MIN * 60
    short_break_sec = 2 # SHORT_BREAK_MIN * 60
    long_break_sec = 8 # LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        checkmark_label.config(text="")
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        checkmark_label.config(text="")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        checkmark_label.config(text="✔" * (reps // 2))

    start_button.config(state="disabled")
    reset_button.config(state="normal")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count // 60:02}:{count % 60:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button.config(state="normal")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

# Label
title_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# Tomato image / Timer
canvas = tk.Canvas(width=203, height=300)
tomato_img = tk.PhotoImage(file="Days 21-30/Day 28 Pomodoro App/tomato.png")
canvas.create_image(103, 162, image=tomato_img)
timer_text = canvas.create_text(103, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tk.Button(text="Start", command=start_timer, font=(FONT_NAME, 12, "bold"))
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12, "bold"))
reset_button.grid(column=2, row=2)
checkmark_label = tk.Label(text="", fg=GREEN, font=(FONT_NAME, 12, "bold"))
checkmark_label.grid(column=1, row=3)


window.mainloop()
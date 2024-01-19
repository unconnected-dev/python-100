import math
from tkinter import *
from PIL import ImageTk, Image


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0 #Initialize reps before using in the function
window_timer_ref = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_():
    global reps, window_timer_ref
    window.after_cancel(window_timer_ref)
    reps = 0

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global window_timer_ref

    minutes = math.floor(count / 60)
    seconds = count % 60

    # if seconds != 0:
    #     current_time_string = f"{minutes}:{seconds}"
    # else:
    #     current_time_string = f"{minutes}:00"

    #Dynamic typing allows the variable to be changed from int to str
    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    current_time_string = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=current_time_string)
    
    if count > 0:
        window_timer_ref = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        
        checks = ""
        for i in range(math.floor(reps/2)):
            checks += "✔"

        check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=30, bg=YELLOW)


#Timer Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
relative_image_path = "./028_tkinter/pomodoro/tomato.png"
img = ImageTk.PhotoImage(Image.open(relative_image_path))

canvas.create_image(100, 112,image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)


#Start button
start_button = Button(text="Start",highlightthickness=0, padx=10, pady=10, command=start_timer)
start_button.grid(row=2, column=0)


#Reset button
reset_button = Button(text="Reset", highlightthickness=0, padx=10, pady=10, command=reset_)
reset_button.grid(row=2, column=2)


#Checkmarks
# check_marks = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
check_marks.grid(row=3,column=1)


window.mainloop()
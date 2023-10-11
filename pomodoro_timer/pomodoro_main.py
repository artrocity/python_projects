# Import libraries
import math
from tkinter import *
from playsound import playsound

# Define Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 35, "bold")
BUTTON_FONT = ("Courier", 18, "normal")
ROUND_FONT = ("Courier", 25, "bold")
CURRENT_ROUND = 0
TIMER = None

# Initialize classes
window = Tk()
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

# Function to sound the alarm on timers
def sound_alarm() -> None:
    """
    Summary:
        Uses playsound library to sound the alarm during timers
    Returns:
        None
    Called by:
        start_timer()
    """
    playsound("alarm.mp3")

# Set up timer mechanism
def start_timer() -> None:
    """
    Summary:
        Sets Round to 1 and runs for 5 rounds total setting a result(break time) to count down 
    Returns:
        None
    Called By: 
        Initially called by pressing the start_button(Tkinter command) on the GUI
        Then to keep it in a "loop" its called by count_down()
    """
    global CURRENT_ROUND
    CURRENT_ROUND += 1
    print(CURRENT_ROUND)
    if CURRENT_ROUND == 5:
        result = 20 # Long break
        heading_label.config(text="Long Break", fg=RED)
        timer_round.config(text=f"Round: {CURRENT_ROUND}/8")
        sound_alarm()
        count_down(result * 60)
    elif CURRENT_ROUND % 2 == 1:
        result = 25 # Work Time
        heading_label.config(text="Work", fg=GREEN)
        timer_round.config(text=f"Round: {CURRENT_ROUND}/8")
        sound_alarm()
        count_down(result * 60)
    elif CURRENT_ROUND % 2 == 0:
        result = 5 # Short break Time
        heading_label.config(text="Short Break", fg=PINK)
        timer_round.config(text=f"Round: {CURRENT_ROUND}/8")
        sound_alarm()
        count_down(result * 60)

# Set up countdown mechanism
def count_down(count: int) -> None:
    """
    Summary:
        Takes the return value from Start Time and counts down 1 second formatting the time
        to be ##:##
    Args:
        count (int): Time to count down from
    Returns:
        None
    Called by:
        start_timer and a self-loop inside of this function
    """
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    timer_time = f"0{count_min}:{count_seconds}"

    canvas.itemconfig(timer_text, text=timer_time)
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count -1)
    else:
        start_timer()

# Timer reset
def reset_timer() -> None:
    global CURRENT_ROUND
    canvas.itemconfig(timer_text, text="00:00")
    heading_label.config(text="Timer")
    window.after_cancel(TIMER)
    CURRENT_ROUND = 0
    timer_round.config(text=f"Round: {CURRENT_ROUND}/8")

# Screen setup
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)

heading_label = Label(text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
heading_label.config(pady=20)
heading_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, font=BUTTON_FONT, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, font=BUTTON_FONT, command=reset_timer)
reset_button.grid(row=2, column=2)

timer_round = Label(text=f"Round: {CURRENT_ROUND}/8", font=ROUND_FONT, bg=YELLOW, fg=GREEN)
timer_round.grid(row=3, column=1)

# Keep window open until closed
window.mainloop()
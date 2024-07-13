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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text ="00:00")
    timer_text.config(text="Timer") 
    checkmarks.config(text = "")
    global reps
    reps = 0
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    
    # increases reps
    reps +=1
    
    if reps % 8 == 0:
        timer_text.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED) 
        count_down(long_break)
    elif reps % 2 == 0:
        timer_text.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK) 
        count_down(short_break)
    else:
        count_down(work_sec)
        timer_text.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN) 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    canvas.itemconfig(text_timer, text = f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        # checkmark
        mark = ""
        work_session = math.floor(reps/2)
        for rep in range(work_session):
            mark += "✅"
        checkmarks.config(text=mark)
             
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

# timer-text
timer_text = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN) 
timer_text.grid(column=2, row=1)

# Create a canvas
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(column=2, row=2)

# Buttons
start_button = Button(text="Start", bg="white", command= start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=3, row=3)

# checkmark
checkmarks = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=2, row=4)

# opens our window
window.mainloop()
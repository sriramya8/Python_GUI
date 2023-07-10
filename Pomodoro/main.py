import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_fun():
    global rep
    rep=0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    label.config(text="Timer")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_click():
    global rep
    rep=rep+1
    if(rep%2!=0):
        label.config(text="💼 Work Time 💼")
        count_down(WORK_MIN*60)
    elif(rep==8):
        label.config(text="🤩 Long Break 🤩",fg=RED)
        count_down(LONG_BREAK_MIN*60)
        rep=0
    else:
        label.config( text="🙂 Short Break 🙂",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(numb):
    if(numb>=0):
        min=math.floor(numb/60)
        sec=numb%60
        if(sec<10):
            sec=f"0{sec}"
        canvas.itemconfig(canvas_text,text=f"{min}:{sec}")
        global timer
        timer=window.after(1000,count_down,numb-1)
    else:
        if(rep%2!=0):
            variab=""
            for i in range(1,rep+1,2):
                variab=variab+"✔  "

            check_label.config(text=variab)


        button_click()
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=tkinter.Canvas(width=200,height=224, bg=YELLOW,highlightthickness=0)
image_tom=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_tom)
canvas_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,18,"bold"))
canvas.grid(row=1,column=1)
label=tkinter.Label(text="Timer")
label.config(font=(FONT_NAME,20,"bold"),bg=YELLOW)
label.config(fg=GREEN)
label.grid(row=0,column=1)
start_button=tkinter.Button(text="Start",highlightthickness=0,command=button_click)
start_button.grid(row=2,column=0)
reset_button=tkinter.Button(text="Reset",highlightthickness=0,command=reset_fun)
reset_button.grid(row=2,column=2)
check_label=tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check_label.grid(row=3,column=1)
window.mainloop()

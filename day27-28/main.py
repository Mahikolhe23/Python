from tkinter import * 
import math
#----------------------------- CONSTANTS ------------------------------------------#
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME  = 'Courier'
WORK_MIN = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
resp = 0 
timer = None
#----------------------------- TIME RESET ------------------------------------------#
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = '00:00')
    title_lable.config(text='Timer')
    check_marks.config(text='')
    global resp
    resp = 0 
    
#----------------------------- TIMER MECHANISM ------------------------------------------#
def start_timer():
    global resp
    resp += 1 

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_TIME * 60 
    long_break_sec = LONG_BREAK_TIME * 60 
    
    if resp % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text='break',fg=RED)
    elif resp % 2 == 0:
        count_down(short_break_sec) 
        title_lable.config(text='break',fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text='work',fg=GREEN)        

#----------------------------- COUNTDOWN MECHANISM ------------------------------------------#
def count_down(count):
    count_min  = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10 :
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text = f'{count_min}:{count_sec}')
    if count > 0 :
        global timer
        timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(resp/2)):
            mark += "✔"
        check_marks.config(text=mark)    


#----------------------------- UI SETUP ------------------------------------------#

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


title_lable = Label(text='Timer',fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50))
title_lable.grid(column=1, row= 0)

canvas  = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(103, 130, text='00:00', fill='black',font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg= YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()

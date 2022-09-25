'''
This program use the 'Pomodoro' Technique which set a time of 25 minutes for work ,and
5 minutes or 20 minutes for breaks. At each interval, the main window will pop up and
tell you to take a break or go back to work
 '''
from tkinter import Tk, Label, Button, Canvas, PhotoImage
from math import ceil


PEACH = '#fa7070'
YELLOW = '#fbf2cf'
LIGHT_GREEN = '#9bdeac'
DARK_GREEN = '#a1c298'

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

count =0
timer = ''

def focus_window(option):
    '''Function used to show window when is required'''
    if option:
        #Put window on top and stay on top but can be minimize.
        window.deiconify()
        window.attributes('-topmost', True)
        window.focus_force()
    elif not option:
        #Allow window to be places behide other windows.
        window.attributes('-topmost', False)


def reset_timer():
    '''Reset the timer and other variables to their default vaules when fuction is called'''
    global count
    window.after_cancel(timer)
    title_label.configure(text='Pomodoro')
    canvas.itemconfigure(time_countdown_text, text='00:00')
    markers_label.configure(text='')
    start_button.configure(state='active')
    count = 0


def start_timer():
    '''Start the timer when fuction is called'''
    global count
    count+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    #Start button is disable so that it's isn't button is press again and causes errors
    start_button.configure(state='disabled')

    focus_window(False)
    #Breaks are trigger after every work session,
    #Long breaks are every 4th breaks and the rest are short breaks.
    if count % 2 == 0 and count % 8 != 0:
        count_down(short_break_sec)
        title_label.configure(text='Break Time', foreground= LIGHT_GREEN)
    elif count % 8 == 0:
        count_down(long_break_sec)
        title_label.configure(text='Break Time', foreground= DARK_GREEN)
    else:
        count_down(work_sec)
        title_label.configure(text='Work Time', foreground= PEACH)


def count_down(time_in_sec):
    '''Function that count down the time it's given which is in seconds'''
    global timer

    #Return marker in groups of 100, 10, and 1
    def markers_text():
        markers_count =ceil(count/2)
        time_100 = markers_count//100
        time_10 = (markers_count-time_100*100)//10
        time_1 = markers_count%10
        if time_100>0:
            return f"{'✘ˣ¹⁰⁰'*time_100}\n{'✘ˣ¹⁰'*time_10}\n{'✘'*time_1}"
        if time_10>0:
            return f"{'✘ˣ¹⁰'*time_10}\n{'✘'*time_1}"
        return '✘'*time_1

    #Convert time from seconds to minutes and seconds format to display
    minute= time_in_sec//60
    second = time_in_sec%60
    if second < 10:
        second = f'0{second}'
    if minute < 10:
        minute = f'0{minute}'
    canvas.itemconfigure(time_countdown_text, text=f'{minute}:{second}')

    #After evey one second, 1 is subtracted from time_in_sec and called its self to simlate a count down
    if  time_in_sec>0 :
        timer = window.after(1000, count_down, time_in_sec-1)

    else: #When time is up, the start button is actived, title is changed and check mark is added
        focus_window(True)
        start_button.configure(state='active')
        if count%2 == 1:
            markers_label.configure(text=markers_text())
            title_label.configure(text='Time for a break')
        else:
            title_label.configure(text='Now back to work', foreground=PEACH)


#Window
window = Tk()
window.title('Pomodoro')
window.configure(padx=60,pady=40, background=YELLOW)
icon = PhotoImage(file='PixelTomato.png')
window.iconphoto(True, icon)


#Label
title_label = Label(text='Pomodoro', foreground=PEACH,background=YELLOW, font=(FONT_NAME,30,''))
title_label.grid(column=1,row=0)

#Markers are used to show how many a work session has be completed 
markers_label = Label(foreground=PEACH, background=YELLOW,pady=15 ,font=('',20,''))
markers_label.grid(column=1,row=3)


#Button
start_button = Button(text='Start',command=start_timer,foreground=DARK_GREEN, background=YELLOW,
                    activeforeground=DARK_GREEN, activebackground= YELLOW, relief='flat',
                    highlightcolor=PEACH, highlightthickness=2, font=(FONT_NAME,15,'bold'),
                    default='active')
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',command=reset_timer,foreground=DARK_GREEN, background=YELLOW,
                    activeforeground=DARK_GREEN,activebackground= YELLOW, relief='flat',
                    highlightcolor=PEACH,highlightthickness=2, font=(FONT_NAME,15,'bold'),
                    default='active')
reset_button.grid(column=2,row=2)


#canvas  Which is the image that is shown on background
canvas = Canvas(width=390, height=224, background=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(195, 112, image=img)
#Text that is shown on the iamge
time_countdown_text = canvas.create_text(195, 130, text='00:00', fill='white',
                                        font=(FONT_NAME, 27, 'bold'))
canvas.grid(column=1, row=1)


window.mainloop()

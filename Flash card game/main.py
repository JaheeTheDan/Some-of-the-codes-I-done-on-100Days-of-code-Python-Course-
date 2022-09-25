'''A fun way to learn french, a card with a french word is shown. 3 seconds is pass to
let the user guess the english translated version of the french word. If the user guesses right,
the user can press the checkbox. If not right, user press the X button.
For each word the user guesses right, it's remove from a list of french words to learn'''
from tkinter import Tk, PhotoImage, Canvas, Button
from tkinter import messagebox
from random import choice
from os import remove
import pandas

BACKGROUND_COLOR = "#B1DDC6"

word = ''

#Check for if words_to_learn exist and  if not, french_words.csv file is used as data
try:
    data = pandas.read_csv('data\\words_to_learn.csv')
    print(0)
except FileNotFoundError:
    data = pandas.read_csv('data\\french_words.csv')
    print(1)
finally:
    data_list = [{'French':row['French'],'English':row['English']} for (_,row) in data.iterrows()]


def show_back():
    '''Show the back of the card which have english translated word'''
    global word
    wrong_button.configure(state='active')
    right_button.configure(state='active')

    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')


def next_card():
    '''Show the next card with a new french word'''
    global word
    #The button are disabled so the user doesn't break the program
    wrong_button.configure(state='disabled')
    right_button.configure(state='disabled')

    #French word and its english translated word is randomly choosen
    word = choice(data_list)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=word['French'], fill='black')
    #3 seconds is allowed to user to guess
    window.after(3000, show_back)


def is_known():
    '''function called when the presses the checkbox,
    which remove the learned word from word_to_learn.csv file and new card is shown'''
    data_list.remove(word)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv('data\\words_to_learn.csv')

    #If words_to_learn list is empty, then program will exit out and remove the words_to_learn.csv
    if len(data_list) == 0:
        messagebox.showinfo(title='GOOD JOB!!',
                            message='There are no more words to learn\nGOOD JOB!!')
        remove('data\\words_to_learn.csv')
        exit()

    next_card()


#Window
window = Tk()
window.title('Flash Card')
window.configure(background=BACKGROUND_COLOR, padx=45, pady= 45)

#Canvas
card_front_image = PhotoImage(file='images\\card_front.png')
card_back_image = PhotoImage(file='images\\card_back.png')

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

canvas_image = canvas.create_image(400, 263, image=card_front_image)

title_text = canvas.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', fill='black', font=('Arial', 60, 'bold'))

#Button
image_1 = PhotoImage(file='images\\wrong.png')
wrong_button = Button(image=image_1, command=next_card, relief='flat',
                      background=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

image_2 = PhotoImage(file='images\\right.png')
right_button = Button(image=image_2, command=is_known, relief='flat',
                      background=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR)
right_button.grid(column=1,row=1)

#Ask user if they are ready to go, if not ready the program is exit out
if messagebox.askyesno(title='Ready?', message='Are you ready to start?'):
    next_card()
else:
    exit()

window.mainloop()

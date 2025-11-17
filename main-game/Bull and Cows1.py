import tkinter as tk
import random
import time
from pygame import mixer
import os # работа с файловой системой

mixer.init()

def play_music():
    try:
        mixer.music.load('C:\\Users\\Егор\\Downloads\\Отдыхаем.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(1)
        print("Музыка играет")
    except Exception as e:
        print(f"Ошибка: {e}")
play_music()


window = tk.Tk()
window.title('Bull and Cows')
window.geometry('800x600')

priglas = tk.Label(
    window,
    text = 'Добро пожаловать в игру!',
    font = ('Times New Roman', 30, 'bold'),
    fg='black',
    bg='white',
)
priglas.pack(pady=(50,0))

name = tk.Label(
    window,
    text = 'Bull and Cows',
    font = ('Times New Roman', 30, 'bold'),
    fg = 'red',
    bg = 'white',
)
name.pack(pady=(0,100))

def Knopka_nachalo():
    status.config(text='Игра началась!')
    Anigilacia()

def Anigilacia():
    for widget in window.winfo_children():
        widget.destroy()

    zagolovok = tk.Label(
        window,
        text='Выбери уровень сложности',
        fg='blue',
        bg='white',
        font=('Times New Roman', 30)
    )
    zagolovok.pack(pady=(50,0))

    easy_button = tk.Button(window, text='Лёгкий (3 цифры)', bg='green', font=('Times New Roman', 30, 'bold'), command=lambda: pusk(3))
    easy_button.pack(pady=(100,40))

    medium_button = tk.Button(window, text='Средний (4 цифры)', bg='yellow', font=('Times New Roman', 30, 'bold'), command=lambda: pusk(4))
    medium_button.pack(pady=40)

    hard_button = tk.Button(window, text='Сложный (5 цифр)', bg='red', font=('Times New Roman', 30, 'bold'), command=lambda: pusk(5))
    hard_button.pack(pady=40)

    back_button = tk.Button(window, text='Назад', command=Yroven)
    back_button.pack(pady=10)

def Yroven():
    for widget in window.winfo_children():
        widget.destroy()

    priglas = tk.Label(
        window,
        text='Добро пожаловать в игру!',
        font=('Times New Roman', 30, 'bold'),
        fg='black',
        bg='white',
    )
    priglas.pack(pady=(50, 0))

    name = tk.Label(
        window,
        text='Bull and Cows',
        font=('Times New Roman', 30, 'bold'),
        fg='red',
        bg='white',
    )
    name.pack(pady=(0, 100))

    start = tk.Button(
        window,
        text='Начать игру',
        command=Knopka_nachalo,
        font=('Times New Roman', 50, 'bold'),
        fg='green',
        bg='white',
    )

    start.pack(pady=(50,0))

    global status
    status = tk.Label(
        window,
        text='Нажмите кнопку чтобы начать',
        font=('Times New Roman', 10, 'bold'),
    )
    status.pack(pady=(0,0))

start = tk.Button(
    window,
    text = 'Начать игру',
    command = Knopka_nachalo,
    font = ('Times New Roman', 50, 'bold'),
    fg = 'green',
    bg = 'white',
)

start.pack(pady = 20)

status= tk.Label(
    window,
    text = 'Нажмите кнопку чтобы начать',
    font = ('Times New Roman', 12, 'bold'),
)
status.pack()

def pusk(level):

    for widget in window.winfo_children():
        widget.destroy()

    if level == 3:
        text1 = 'Лёгкий уровень'
        max_cifr = 15
    elif level == 4:
        text2 = 'Средний уровень'
        max_cifr = 10
    else:
        text3 = 'Сложный уровень'
        max_cifr = 7

    uga = tk.Label(
    window,
    text = 'Угадай число!',
    font = ('Times New Roman', 30, 'bold'),
    fg = 'black',
    bg = 'white',
    )
    uga.pack(pady=(50,0))

    LvL=tk.Label(
        window,
        text = text,
        font = ('Times New Roman', 20, 'bold'),
        fg = 'black',
        bg = 'white',
    )
    LvL.pack()

    Vvod = tk.Entry(
        width=level+2,
        justify = 'center',

    )
    Vvod.pack()

    instruction = tk.Label(
        text=f"Введите {level}-значное число..."
    )

window.mainloop()

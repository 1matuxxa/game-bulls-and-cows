import tkinter as tk

from pygame import mixer

# Инициализация музыки
mixer.init()

def play_background_music():
    try:
        mixer.music.load("По ресторанам.mp3")  # или music.wav
        mixer.music.play(-1)  # зациклить
        mixer.music.set_volume(1)
    except:
        print("Музыкальный файл не найден")

def stop_music():
    mixer.music.stop()

window = tk.Tk()
window.title('Bull and Cows')
window.geometry('1920x1080')

priglas = tk.Label(
    window,
    text = 'Добро пожаловать в игру!',
    font = ('Times New Roman', 20, 'bold'),
    fg='black',
    bg='white',
)

priglas.pack()

name = tk.Label(
    window,
    text = 'Bull and Cows',
    font = ('Times New Roman', 18, 'bold'),
    fg='red',
    bg='white',
)
name.pack()
def Knopka():
    status.config(text='Игра началась!')
    start_game()

def start_game():
    for widget in window.winfo_children():
        widget.destroy()
    new_game()

def new_game():
    zagolovok_game = tk.Label(
        window,
        text = 'Выбери уровень сложности',
        fg = 'blue',
        bg = 'white',
    )

    zagolovok_game.pack()

    easy_button = tk.Button(window, text = 'Лёгкий', font=('Times New Roman', 50, 'bold'), fg = 'black', bg = 'blue', command = Knopka)
    easy_button.pack(pady=10)

    medium_button = tk.Button(window, text = 'Средний', font=('Times New Roman', 50, 'bold'), fg = 'yellow', bg = 'blue', command = Knopka)
    medium_button.pack(pady=10)

    hard_button = tk.Button(window, text = 'Сложный', font=('Times New Roman', 50, 'bold'), fg = 'red', bg = 'blue', command = Knopka)
    hard_button.pack(pady=10)

start = tk.Button(
    window,
    text = 'Начать игру',
    command = Knopka,
    font = ('Times New Roman', 30, 'bold'),
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

window.mainloop()

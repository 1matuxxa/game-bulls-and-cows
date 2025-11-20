import tkinter as tk
from pygame import mixer

mixer.init()

def play_music():
    try:
        mixer.music.load('C:\\Users\\Егор\\Downloads\\Пикник.mp3')
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
    zagolovok.pack(pady=(50, 0))

    easy_button = tk.Button(window, text='Лёгкий (3 цифры)', bg='green', font=('Times New Roman', 30, 'bold'), command=lambda: pusk(3))
    easy_button.pack(pady=(100, 40))

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
    start.pack(pady=(50, 0))

    global status
    status = tk.Label(
        window,
        text='Нажмите кнопку чтобы начать',
        font=('Times New Roman', 10, 'bold'),
    )
    status.pack(pady=(0, 0))

def pusk(level):
    for widget in window.winfo_children():
        widget.destroy()

    if level == 3:
        text1 = 'Лёгкий уровень'
    elif level == 4:
        text1 = 'Средний уровень'
    else:
        text1 = 'Сложный уровень'

    uga = tk.Label(
        window,
        text='Угадай число!',
        font=('Times New Roman', 28, 'bold'),
        fg='black',
        bg='white',
    )
    uga.pack(pady=(30, 10))

    LvL = tk.Label(
        window,
        text=text1,
        font=('Times New Roman', 25),
        fg='black',
        bg='white',
    )
    LvL.pack(pady=(0, 20))

    instruction = tk.Label(
        window,
        text=f"Введите {level}-значное число c неповторяющимися цифрами:",
        font=('Times New Roman', 16),
        fg='black',
        bg='white',
    )
    instruction.pack(pady=(0, 10))

    Vvod = tk.Entry(
        window,
        font=('Times New Roman', 20),
        width=level + 2,
        justify='center',
    )
    Vvod.pack(pady=20)
    Vvod.focus()

    resultat = tk.Text(
        window,
        width=60,
        height=10,
        font=('Times New Roman', 12),
    )
    resultat.pack(pady=20, padx=20)

    def proverit_chislo():
        chislo = Vvod.get()
        Vvod.delete(0, tk.END)
        resultat.insert(tk.END, f"Введено: {chislo}\n")
        resultat.see(tk.END)

    Proverit = tk.Button(
        window,
        text='Проверить',
        font=('Times New Roman', 20),
        bg='lightgreen',
        command=proverit_chislo
    )
    Proverit.pack(pady=10)

    nazad = tk.Button(
        window,
        text='Назад к выбору уровня',
        font=('Times New Roman', 14, 'bold'),
        fg='green',
        bg='white',
        command=Anigilacia
    )
    nazad.pack(pady=10)

start = tk.Button(
    window,
    text='Начать игру',
    command=Knopka_nachalo,
    font=('Times New Roman', 50, 'bold'),
    fg='green',
    bg='white',
)
start.pack(pady=20)

status = tk.Label(
    window,
    text='Нажмите кнопку чтобы начать',
    font=('Times New Roman', 12, 'bold'),
)
status.pack()

window.mainloop()
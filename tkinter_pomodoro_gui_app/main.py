import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.config(timer_text, text='00:00')
    pomo_label.config(text='Timer')
    checks_label.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 10
    short_break_sec = SHORT_BREAK_MIN * 10
    long_break = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        pomo_label.config(text='Study Timer')
        count_down(work_sec)

    elif reps == 8:
        pomo_label.config(text='Long Break Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=RED)
        count_down(long_break)

    else:
        pomo_label.config(text='Short break Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)# primeiro é o tempo, dps a função que vai chamar, e dps os argumentso que irão para a função
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        checks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# adicionando uma imagem na tela do tkinter
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

# TEXTO TIMER
pomo_label = tkinter.Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
pomo_label.grid(column=3, row=1)


# criando um texto no tomate da  tela do tkinter
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold')) # os primeiros valores sao a posição que ficará o texto
canvas.grid(column=3, row=2)


checks_label = tkinter.Label(bg=YELLOW, fg=GREEN)
checks_label.grid(column=3, row=5)


# BOTÕES
start_button = tkinter.Button(text='START', highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=4)

reset_button = tkinter.Button(text='RESET', highlightthickness=0, command=reset_timer)
reset_button.grid(column=5, row=4)

window.mainloop()
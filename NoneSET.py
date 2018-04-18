# -*- coding utf-8 -*-

import tkinter, json, requests, bs4, time
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

time.sleep(2)

FILE_NAME = tkinter.NONE

def new_file(event):
    global FILE_NAME
    FILE_NAME = 'Untitled'
    text.delete('1.0', tkinter.END)

def save_file(event):
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as(event):
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Опаньки!", message='Не удалось сохранить файл...')

def open_file(event):
    global FILE_NAME
    inp = askopenfile(mode='r')
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def new_file_static():
    global FILE_NAME
    FILE_NAME = 'Untitled'
    text.delete('1.0', tkinter.END)

def save_file_static():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def caption_static():
     t = ent.get()
     lbl.configure(text = t)

def save_as_static():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title='Опаньки!', message='Не получилось сохранить файл...')

def open_file_static():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def caption(event):
     t = ent.get()
     lbl.configure(text = t)

def select_all(event):
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')

def phelp():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(win, text='Добро пожаловать в NoneSET!\nNoneSET- быстрый редактор текста. Всё время мы перерабатываем, изменяем или добавляем новые функции в эту программу.\nНа данный момент, вы можете открывать, сохранять, редактирвоать и создавать новые файлы. Также вы можете создавать плагины, если вы знаете язык Python')
    lab.pack()

def about():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(win, text='Название программы: NoneSET\nВерсия: 1.0.3\nАвтор: Елисей Шаров\nКомпания: SharovCompanyGroup\nСайт: scgofficial.esy.es\nЛичный сайт автора: scgofficial.esy.es/workers/')
    lab.pack()

def settings():
	win = tkinter.Toplevel(root)
	lab = tkinter.Label(text)

def bgW():
    text.config(bg='white')

def bgB():
    text.config(bg='black')

def bgG():
	text.config(bg='grey')

def textW():
    text.config(fg='white')

def textB():
    text.config(fg='black')

def textG():
	text.config(fg='grey')

def width5():
	text.config(font='Verdana 5')

def width10():
	text.config(font='Verdana 10')

def width15():
	text.config(font='Verdana 15')

def width20():
	text.config(font='Verdana 20')

root = tkinter.Tk()
root.title('NoneSET')
root.geometry('1320x640')
root.minsize(width=200, height=100)

scrollbar_y = Scrollbar(root)
scrollbar_y.pack(side = RIGHT, fill=Y)
text = Text(root, yscrollcommand = scrollbar_y.set, width=1320, height=640, fg='white', bg='black', font='Verdana 15')
text.pack(side = LEFT, fill=BOTH)
scrollbar_y.config(command = text.yview)

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
infoMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
settingsMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
bgcolor = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
textcolor = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
fsize = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
ffam = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
fileMenu.add_command(label='Новый файл [Ctrl+N]', command=new_file_static)
fileMenu.add_command(label='Открыть... [Ctrl+O]', command=open_file_static)
fileMenu.add_command(label='Созранить... [Ctrl+S]', command=save_file_static)
fileMenu.add_command(label='Сохранить как... [Ctrl+D]', command=save_as_static)
fileMenu.add_command(label='Отменить... [Ctrl+Z]', command=caption_static)
fileMenu.add_separator()
fileMenu.add_command(label='Выход', command=quit)
menuBar.add_cascade(label='Файл', menu=fileMenu)
menuBar.add_cascade(label='Информация', menu=infoMenu)
menuBar.add_cascade(label='Настройки', menu=settingsMenu)
infoMenu.add_command(label='Помощь', command=phelp)
infoMenu.add_command(label='О программе', command=about)
settingsMenu.add_cascade(label='Цвет фона', menu=bgcolor)
bgcolor.add_command(label='Белый', command=bgW)
bgcolor.add_command(label='Чёрный', command=bgB)
bgcolor.add_command(label='Серый', command=bgG)
settingsMenu.add_cascade(label='Цвет текста', menu=textcolor)
textcolor.add_command(label='Белый', command=textW)
textcolor.add_command(label='Чёрный', command=textB)
textcolor.add_command(label='Серый', command=textG)
settingsMenu.add_cascade(label='Размер шрифта', menu=fsize)
fsize.add_command(label='5', command=width5)
fsize.add_command(label='10', command=width10)
fsize.add_command(label='15', command=width15)
fsize.add_command(label='20', command=width20)

root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-d>', save_as)
root.bind('<Control-a>', select_all)

root.config(menu=menuBar)
root.mainloop()

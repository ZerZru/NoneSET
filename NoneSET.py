# -*- coding: utf-8 -*-

#import packages for program
import tkinter, time, json
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

try:
    import requests, bs4
except:
    print("У вас не установлены пакеты requests и BeautifulSoup4. Чтобы использовать все функции программы, пожалуйста, установите эти пакеты.\nУстановка requests:\n1) Откройте командную строку\n2) Прописать pip install requests\nУстановка bs4:\n1) Откройте командную строку\n2) Прописать pip install BeautifulSoup4", error)

def tracking(command):
    if command == 'start':
        print('$ NoneSET Tracking: запуск программы...')
        time.sleep(1)
    elif command == 'verification':
        print('$ NoneSET Tracking: верификация продукта...')
        time.sleep(2)
        __author__ = 'Elisey Sharov'
        print('Автор: ',  __author__)
        time.sleep(1)
        print('Лицензия: MIT')
        time.sleep(1)
        print('Страна: Russian Federation')
        time.sleep(1)
    elif command == 'checking':
        print('$ NoneSET Tracking: проверка установки пакетов...')
        time.sleep(2)
    elif command == 'check_version':
        print('$ NoneSET Tracking: проверка версии...')
        time.sleep(2)
        try:
            def check_version():
                s = requests.get('http://scgofficial.esy.es/version.html')
                b = bs4.BeautifulSoup(s.text, "html.parser")
                p1 = b.select('.version .ns')
                result_ver = p1[0].getText()
                #print(result_ver)
                version = 'beta'
                if version == 'beta':
                    print('У вас установлена бета-версия NoneSET. Мы не гарантируем стабильную работу программы.')
                elif result_ver != version:
                    print('Вы используете старую версию NoneSET.Последня версия: {}; У вас установлена: {}; Для получения новых функций и возможности программы, пожалуйста, обновите версию NoneSET'.format(result_ver, version))
                elif result_ver == version:
                    print('Вы используете последнюю версию NoneSET. ')
            check_version()
        except Exception as error:
            print("Не удалось проверить версию программы. Возможные причины:\n1) Отсутствует Интернет-подключение\n2) Программе закрыт доступ в сеть\n3) Технические работы на сервере\n4) Установлена нестабильная версия программы или она установлена неправильно")
            print('$ NoneSET Tracking: ', error)
    elif command == 'start_optimization':
        print('$ NoneSET Tracking: запуск оптимизации...')
        time.sleep(3)
    elif command == 'new':
        print('$ NoneSET Tracking: Создан новый файл')
    elif command == 'save':
        print('$ NoneSET Tracking: Сохранён файл {}'.format(FILE_NAME))
    elif command == 'save_as':
        print('$ NoneSET Tracking: создан файл {} с новым расширением'.format(FILE_NAME))
    elif command == 'open':
        print('$ NoneSET Tracking: открыт файл {}'.format(FILE_NAME))
    elif command == 'help':
        print('$ NoneSET Tracking: Открыто окно "Помощь"')
    elif command == 'about':
        print('$ NoneSET Tracking: Открыто окно "Информация"')
    elif command == 'all_text':
        print('$ NoneSET Tracking: В файле {} выделен весь текст'.format(FILE_NAME))

tracking('start')
tracking('verification')
tracking('checking')
tracking('check_version')
tracking('start_optimization')

global installed_packages
installed_packages = False

#create constant
FILE_NAME = tkinter.NONE

#create functions
def new_file(event):
    global FILE_NAME
    tracking('new')
    FILE_NAME = 'Untitled'
    text.delete('1.0', tkinter.END)

def save_file(event):
    global FILE_NAME
    tracking('save')
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as(event):
    global FILE_NAME
    tracking('save_as')
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)

#try:
#    out.write(data.rstrip())
#except Exception:
#    showerror(title="Опаньки!", message='Не удалось сохранить файл...')

def open_file(event):
    global FILE_NAME
    tracking('open')
    inp = askopenfile(mode='r')
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def new_file_static():
    global FILE_NAME
    tracking('new')
    FILE_NAME = 'Untitled'
    text.delete('1.0', tkinter.END)

def save_file_static():
    global FILE_NAME
    tracking('save')
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def caption_static():
    t = ent.get()
    lbl.configure(text = t)

def save_as_static():
    global FILE_NAME
    tracking('save_as')
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)

#try:
#    out.write(data.rstrip())
#except Exception:
#    showerror(title='Опаньки!', message='Не получилось сохранить файл...')
#    print('$ NoneSET Tracking: ошибка сохранение файла {}'.format(FILE_NAME))

def open_file_static():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)
    tracking('open')

def caption(event):
    t = ent.get()
    lbl.configure(text = t)

def select_all(event):
    #select text
    widget.select_range(0, 'end')
    #move cursor to the end
    widget.icursor('end')
    tracking('all_text')

def phelp():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(win, text='Добро пожаловать в NoneSET!\nNoneSET- быстрый редактор текста. Всё время мы перерабатываем, изменяем или добавляем новые функции в эту программу.\nНа данный момент, вы можете открывать, сохранять, редактирвоать и создавать новые файлы. Также вы можете создавать плагины, если вы знаете язык Python')
    lab.pack()
    tracking('help')

def about():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(win, text='Название программы: NoneSET\nВерсия: 1.0.4\nАвтор: Елисей Шаров\nКомпания: SharovCompanyGroup\nСайт: scgofficial.esy.es\nЛичный сайт автора: scgofficial.esy.es/workers/')
    lab.pack()
    tracking('about')

def settings():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(text)

def save_font(font):
    from saving_settings import dict as dict
    dict['f'] = font
    with open('settings.json', mode='w') as f:
        json.dump(dict, f)

def save_bg(bg):
    from saving_settings import dict as dict
    dict['f'] = bg
    with open('settings.json', mode='w') as f:
        json.dump(dict, f)

def save_text(text):
    from saving_settings import dict as dict
    dict['t'] = text
    with open('settings.json', mode='w') as f:
        json.dump(dict, f)

def bgW():
    text.config(bg='white')
    save_bg('white')
    print('$ NoneSET Tracking: фон изменён на белый')

def bgB():
    text.config(bg='black')
    save_bg('black')
    print('$ NoneSET Tracking: фон изменён на чёрный')

def bgG():
    text.config(bg='grey')
    save_bg('grey')
    print('$ NoneSET Tracking: фон изменён на серый')

def textW():
    text.config(fg='white')
    save_text('white')
    print('$ NoneSET Tracking: цвет текста изменён на белый')

def textB():
    text.config(fg='black')
    save_text('black')
    print('$ NoneSET Tracking: цвет текста изменён на чёрный')

def textG():
    text.config(fg='grey')
    save_text('grey')
    print('$ NoneSET Tracking: цвет текста изменён на серый')

def width5():
    text.config(font='Verdana 5')
    save_font('Verdana 5')
    print('$ NoneSET Tracking: размер шрифта изменён на значение 5')

def width10():
    text.config(font='Verdana 10')
    save_font('Verdana 10')
    print('$ NoneSET Tracking: размер шрифта изменён на значение 10')

def width15():
    text.config(font='Verdana 15')
    save_font('Verdana 15')
    print('$ NoneSET Tracking: размер шрифта изменён на значение 15')

def width20():
    text.config(font='Verdana 20')
    save_font('Verdana 20')
    print('$ NoneSET Tracking: размер шрифта изменён на значение 20')

def callback():
    print('$ NoneSET Tracking: функция заблокирована. Причина: нестабильная работа')

#window title and size
root = tkinter.Tk()
root.title('NoneSET')
root.geometry('1920x1080')
root.minsize(width=400, height=300)

#scrollbar settings
scrollbar_y = Scrollbar(root)
scrollbar_y.pack(side = RIGHT, fill=Y)
try:
    with open('settings.json', 'r') as fh:
        data = json.load(fh)
        background_color = data['bg']
        text_color = data['t']
        font_size = data['f']
        text = Text(root, yscrollcommand = scrollbar_y.set, width=1320, height=640, fg=text_color, bg=background_color, font=font_size)
        text.pack(side = LEFT, fill=BOTH)
        scrollbar_y.config(command = text.yview)
except Exception as error:
    text = Text(root, yscrollcommand = scrollbar_y.set, width=1320, height=640, fg='white', bg='black', font='Verdana 15')
    text.pack(side = LEFT, fill=BOTH)
    scrollbar_y.config(command = text.yview)
    print('$ NoneSET Tracking: {}'.format(error))

#all menus and his submenus
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
infoMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
settingsMenu = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
fasterScripts = tkinter.Menu(menuBar, bg='black', fg='white', bd='3')
whileScripts = tkinter.Menu(fasterScripts, bg='black', fg='white', bd='3')
bgcolor = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
textcolor = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
fsize = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
ffam = tkinter.Menu(settingsMenu, bg='black', fg='white', bd='3')
fileMenu.add_command(label='Новый файл [Ctrl+N]', command=new_file_static)
fileMenu.add_command(label='Открыть... [Ctrl+O]', command=open_file_static)
fileMenu.add_command(label='Сохранить... [Ctrl+S]', command=save_file_static)
fileMenu.add_command(label='Сохранить как... [Ctrl+D]', command=save_as_static)
fileMenu.add_command(label='Отменить... [Ctrl+Z]', command=caption_static)
fileMenu.add_separator()
fileMenu.add_command(label='Выход', command=quit)
menuBar.add_cascade(label='Файл', menu=fileMenu)
menuBar.add_cascade(label='Информация', menu=infoMenu)
menuBar.add_cascade(label='Настройки', menu=settingsMenu)
menuBar.add_cascade(label='Код', menu=fasterScripts)
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
fasterScripts.add_cascade(label='Быстрая вставка', menu=whileScripts)
whileScripts.add_command(label='Цикл while', command=callback)

#hotkeys
root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-d>', save_as)
root.bind('<Control-a>', select_all)

root.config(menu=menuBar)
root.mainloop()
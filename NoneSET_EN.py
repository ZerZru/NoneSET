# -*- coding: utf-8 -*-

#import packages for program
import tkinter, time, json
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

try:
    import requests, bs4
except Exception as error:
    print("You don't have packages requests and BeautifulSoup4. For use all program functions, please, install this packages.\n(pip install requests)(pip install BeautifulSoup4)", error)

def tracking(command):
    if command == 'start':
        print('$ NoneSET Tracking: launch program...')
        time.sleep(1)
    elif command == 'verification':
        print('$ NoneSET Tracking: verification...')
        time.sleep(2)
        __author__ = 'Elisey Sharov'
        print('Author: ',  __author__)
        time.sleep(1)
        print('License: MIT')
        time.sleep(1)
        print('Country: Russian Federation')
        time.sleep(1)
    elif command == 'checking':
        print('$ NoneSET Tracking: try to import packages...')
        time.sleep(2)
    elif command == 'check_version':
        print('$ NoneSET Tracking: checking version...')
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
                    print("You have a beta-version of NoneSET. We don't guaranted stability working of program.")
                elif result_ver != version:
                    print('You use old version of NoneSET. Last version: {}; You have: {}; Please, update NoneSET'.format(result_ver, version))
                elif result_ver == version:
                    print('You use last version of NoneSET. ')
            check_version()
        except Exception as error:
            print("1) No Internet-connection\n2) Working on server\n")
            print('$ NoneSET Tracking: ', error)
    elif command == 'start_optimization':
        print('$ NoneSET Tracking: launch optimization...')
        time.sleep(3)
    elif command == 'new':
        print('$ NoneSET Tracking: Created a new file')
    elif command == 'save':
        print('$ NoneSET Tracking: File {} saved'.format(FILE_NAME))
    elif command == 'save_as':
        print('$ NoneSET Tracking: created file {} with new expansion'.format(FILE_NAME))
    elif command == 'open':
        print('$ NoneSET Tracking: opened file {}'.format(FILE_NAME))
    elif command == 'help':
        print('$ NoneSET Tracking: Opened window "Help"')
    elif command == 'about':
        print('$ NoneSET Tracking: Opened window "Info"')

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
    lab = tkinter.Label(win, text='Welceome to NoneSET!\nNoneSET- fastest text editor. All time we change and add new functions!.\nAt this moment, You can open, create, edit files and change settings in program. Also you can create plugins, if you have knowlange of Python')
    lab.pack()
    tracking('help')

def about():
    win = tkinter.Toplevel(root)
    lab = tkinter.Label(win, text='Title: NoneSET\nVersion: 1.0.4\nAuthor: Elisey Sharov\nCompany: SharovCompanyGroup\nSite: scgofficial.esy.es')
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
    print('$ NoneSET Tracking: background changed to white')

def bgB():
    text.config(bg='black')
    save_bg('black')
    print('$ NoneSET Tracking: background changed to black')

def bgG():
    text.config(bg='grey')
    save_bg('grey')
    print('$ NoneSET Tracking: background changed to grey')

def textW():
    text.config(fg='white')
    save_text('white')
    print('$ NoneSET Tracking: text color changed to white')

def textB():
    text.config(fg='black')
    save_text('black')
    print('$ NoneSET Tracking: text color changed to black')

def textG():
    text.config(fg='grey')
    save_text('grey')
    print('$ NoneSET Tracking: text color changed to grey')

def width5():
    text.config(font='Verdana 5')
    save_font('Verdana 5')
    print('$ NoneSET Tracking: font size changed to 5')

def width10():
    text.config(font='Verdana 10')
    save_font('Verdana 10')
    print('$ NoneSET Tracking: font size changed to 10')

def width15():
    text.config(font='Verdana 15')
    save_font('Verdana 15')
    print('$ NoneSET Tracking: font size changed to 15')

def width20():
    text.config(font='Verdana 20')
    save_font('Verdana 20')
    print('$ NoneSET Tracking: font size changed to 20')

def callback():
    print('$ NoneSET Tracking: function is blocked')

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
fileMenu.add_command(label='New file [Ctrl+N]', command=new_file_static)
fileMenu.add_command(label='Open... [Ctrl+O]', command=open_file_static)
fileMenu.add_command(label='Save... [Ctrl+S]', command=save_file_static)
fileMenu.add_command(label='Save as... [Ctrl+D]', command=save_as_static)
fileMenu.add_command(label='Undo... [Ctrl+Z]', command=caption_static)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)
menuBar.add_cascade(label='File', menu=fileMenu)
menuBar.add_cascade(label='Info', menu=infoMenu)
menuBar.add_cascade(label='Settings', menu=settingsMenu)
menuBar.add_cascade(label='Code', menu=fasterScripts)
infoMenu.add_command(label='Help', command=phelp)
infoMenu.add_command(label='About', command=about)
settingsMenu.add_cascade(label='Background color', menu=bgcolor)
bgcolor.add_command(label='White', command=bgW)
bgcolor.add_command(label='Black', command=bgB)
bgcolor.add_command(label='Grey', command=bgG)
settingsMenu.add_cascade(label='Text color', menu=textcolor)
textcolor.add_command(label='White', command=textW)
textcolor.add_command(label='Black', command=textB)
textcolor.add_command(label='Grey', command=textG)
settingsMenu.add_cascade(label='Font size', menu=fsize)
fsize.add_command(label='5', command=width5)
fsize.add_command(label='10', command=width10)
fsize.add_command(label='15', command=width15)
fsize.add_command(label='20', command=width20)
fasterScripts.add_cascade(label='Fast code', menu=whileScripts)
whileScripts.add_command(label='While loop', command=callback)

#hotkeys
root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-d>', save_as)
root.bind('<Control-a>', select_all)

root.config(menu=menuBar)
root.mainloop()
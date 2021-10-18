from tkinter import *


def btn_press(x):
    if x == 'Quit':
        root.destroy()
    elif x == '+':
        label['text'] = float(my_entry1.get()) + \
                        float(my_entry2.get())
    elif x == '-':
        label['text'] = float(my_entry1.get()) - \
                        float(my_entry2.get())
    elif x == '*':
        label['text'] = float(my_entry1.get()) * \
                        float(my_entry2.get())
    elif x == '/':
        label['text'] = float(my_entry1.get()) / \
                        float(my_entry2.get())
    elif x == '//':
        label['text'] = float(my_entry1.get()) // \
                        float(my_entry2.get())
    elif x == '**':
        label['text'] = float(my_entry1.get()) ** \
                        float(my_entry2.get())


root = Tk()
my_version = 'Calc v1.0'    # programm version
my_geometry = '250x400'     # window size
my_title = root.title(my_version)
root.geometry(my_geometry)

my_menu = Menu(root)

# Menu Files
files_menu = Menu(my_menu, tearoff=0)
files_menu.add_command(label="Open")
files_menu.add_command(label="Save")
files_menu.add_separator()
files_menu.add_command(label="Exit", command=root.destroy)
my_menu.add_cascade(label="Files", menu=files_menu)

my_menu.add_command(label="Settings")

root.config(menu=my_menu)

my_entry1 = Entry(width=30)
my_entry2 = Entry(width=30)
my_entry1.pack()
my_entry2.pack()

label = Label(text='Answer',
              width=25,
              height=1,
              bg='#0000ff',
              fg='white')
label.pack()

btn_plus = Button(root, text='+',
                  command=lambda y='+': btn_press(y))
btn_minus = Button(root, text='-')
btn_mult = Button(root, text='*')
btn_div = Button(root, text=':')
btn_div_int = Button(root, text='//')
btn_div_rem = Button(root, text='%')
btn_pow = Button(root, text='**')
btn_exit = Button(root, text='Quit',
                  command=lambda y='Quit': btn_press(y))

btn_plus.pack()
btn_minus.pack()
btn_mult.pack()
btn_div.pack()
btn_div_int.pack()
btn_div_rem.pack()
btn_pow.pack()
btn_exit.pack()

root.mainloop()
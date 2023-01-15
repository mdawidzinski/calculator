from tkinter import *
from tkinter import messagebox

# creating window
main = Tk()
main.resizable(None, None)  # resizing window disabled
main.title('Calculator')
main.iconbitmap('calculator_general_icon.ico')


but_font = ('Cambria', '14', 'bold')  # font for buttons

# creating entry widget
entry_init = StringVar()
entry_init.set('0')
entry = Entry(main, textvariable=entry_init, width=30, borderwidth=10, font=but_font, justify=RIGHT)
entry.grid(row=0, columnspan=4)

proces = [] 


def click(val):  
    if val == '.':  
        if val not in entry.get():
            entry.insert(END, val)
    elif entry.get() == '0':  
        entry.delete(0, END)
        entry.insert(0, val)
    else:
        entry.insert(END, val)


def clear():
    entry.delete(0, END)
    entry.insert(0, '0')
    proces[:] = []


def math(mark):
    if len(proces) < 2:
        proces.append(entry.get())
        proces.append(mark)
        entry.delete(0, END)
        entry.insert(0, '0')
    elif len(proces) == 2:
        proces.append(entry.get())
        try:
            res = eval(''.join(proces))
            proces[0] = str(res)
            proces[1] = mark
            proces[:] = proces[:2]
            entry.delete(0, END)
            entry.insert(0, '0')
        except ZeroDivisionError:
            messagebox.showerror('Division Error', 'Cannot divide by zero')
            clear()


def eq():
    if not proces:
        pass
    else:
        proces.append(entry.get())
        try:
            res = eval(''.join(proces))
            entry.delete(0, END)
            if res == int(res):  # cuts additional zeros eg. 1.000 -> 1
                entry.insert(0, str(int(res)))
            else:
                entry.insert(0, res)
            proces[:] = []
        except ZeroDivisionError:
            messagebox.showerror('Division Error', 'Cannot divide by zero')
            clear()


# creating buttons
button_eq = Button(main, text='=', width=30, font=but_font, fg='#0064C8', activeforeground='red', command=eq)
button_eq.grid(row=5, columnspan=4)

button0 = Button(main, text='0', width=6, height=3, font=but_font, command=lambda: click('0'))
button0.grid(row=4, column=0)

button_sep = Button(main, text='.', width=6, height=3, font=but_font, command=lambda: click('.'))
button_sep.grid(row=4, column=1)

button_clear = Button(main, text='Clear', width=6, height=3, font=but_font, command=clear)
button_clear.grid(row=4, column=2)

button1 = Button(main, text='1', width=6, height=3, font=but_font, command=lambda: click('1'))
button1.grid(row=3, column=0)

button2 = Button(main, text='2', width=6, height=3, font=but_font, command=lambda: click('2'))
button2.grid(row=3, column=1)

button3 = Button(main, text='3', width=6, height=3, font=but_font, command=lambda: click('3'))
button3.grid(row=3, column=2)

button4 = Button(main, text='4', width=6, height=3, font=but_font, command=lambda: click('4'))
button4.grid(row=2, column=0)

button5 = Button(main, text='5', width=6, height=3, font=but_font, command=lambda: click('5'))
button5.grid(row=2, column=1)

button6 = Button(main, text='6', width=6, height=3, font=but_font, command=lambda: click('6'))
button6.grid(row=2, column=2)

button7 = Button(main, text='7', width=6, height=3, font=but_font, command=lambda: click('7'))
button7.grid(row=1, column=0)

button8 = Button(main, text='8', width=6, height=3, font=but_font, command=lambda: click('8'))
button8.grid(row=1, column=1)

button9 = Button(main, text='9', width=6, height=3, font=but_font, command=lambda: click('9'))
button9.grid(row=1, column=2)

button_add = Button(main, text='+', width=6, height=3, font=but_font, command=lambda: math('+'))
button_add.grid(row=4, column=3)

button_sub = Button(main, text='-', width=6, height=3, font=but_font, command=lambda: math('-'))
button_sub.grid(row=3, column=3)

button_div = Button(main, text='/', width=6, height=3, font=but_font, command=lambda: math('/'))
button_div.grid(row=2, column=3)

button_pow = Button(main, text='*', width=6, height=3, font=but_font, command=lambda: math('*'))
button_pow.grid(row=1, column=3)

main.mainloop()

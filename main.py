from tkinter import *

expression = ""

def press(num):
    global expression

    if (expression != ""):
        if ((num == "+" or num == "-" or num == "/" or num == "*") and (
                expression[-1] == "+" or expression[-1] == "-")):
            pass
        elif ((num == "/" or num == "*") and (expression[-1] == "/" or expression[-1] == "*")):
            pass
        else:
            expression = expression + str(num)
    else:
        if (num == "/" or num == "*"):
            pass
        else:
            expression = expression + str(num)

    equation.set(expression)


def equalpress():
    try:

        global expression

        total = str(eval(expression))

        expression = expression + "=" + str(total)
        equation.set(expression)

        expression = ""

    except:

        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set(expression)


def clear_single():
    global expression
    expression = expression[:-1]
    equation.set(expression)


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="white")

    gui.title("Calculator")

    gui.geometry("300x360")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('arial', 18, 'bold'), bg="white", borderwidth=5)

    expression_field.grid(columnspan=4, padx=(5, 5), pady=(5, 5))

    btn1 = Button(gui, text=' 1 ', fg='white', bg='dark blue',
                  command=lambda: press(1), height=2, width=7, borderwidth=5)
    btn1.grid(row=3, column=0, padx=(5, 5), pady=(5, 5))

    btn2 = Button(gui, text=' 2 ', fg='white', bg='dark blue',
                  command=lambda: press(2), height=2, width=7, borderwidth=5)
    btn2.grid(row=3, column=1, padx=(5, 5), pady=(5, 5))

    btn3 = Button(gui, text=' 3 ', fg='white', bg='dark blue',
                  command=lambda: press(3), height=2, width=7, borderwidth=5)
    btn3.grid(row=3, column=2, padx=(5, 5), pady=(5, 5))

    btn4 = Button(gui, text=' 4 ', fg='white', bg='dark blue',
                  command=lambda: press(4), height=2, width=7, borderwidth=5)
    btn4.grid(row=4, column=0, padx=(5, 5), pady=(5, 5))

    btn5 = Button(gui, text=' 5 ', fg='white', bg='dark blue',
                  command=lambda: press(5), height=2, width=7, borderwidth=5)
    btn5.grid(row=4, column=1, padx=(5, 5), pady=(5, 5))

    btn6 = Button(gui, text=' 6 ', fg='white', bg='dark blue',
                  command=lambda: press(6), height=2, width=7, borderwidth=5)
    btn6.grid(row=4, column=2, padx=(5, 5), pady=(5, 5))

    btn7 = Button(gui, text=' 7 ', fg='white', bg='dark blue',
                  command=lambda: press(7), height=2, width=7, borderwidth=5)
    btn7.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))

    btn8 = Button(gui, text=' 8 ', fg='white', bg='dark blue',
                  command=lambda: press(8), height=2, width=7, borderwidth=5)
    btn8.grid(row=5, column=1, padx=(5, 5), pady=(5, 5))

    btn9 = Button(gui, text=' 9 ', fg='white', bg='dark blue',
                  command=lambda: press(9), height=2, width=7, borderwidth=5)
    btn9.grid(row=5, column=2, padx=(5, 5), pady=(5, 5))

    btn0 = Button(gui, text=' 0 ', fg='white', bg='dark blue',
                  command=lambda: press(0), height=2, width=7, borderwidth=5)
    btn0.grid(row=6, column=1, padx=(5, 5), pady=(5, 5))

    plus = Button(gui, text=' + ', fg='black', bg='light green',
                  command=lambda: press("+"), height=2, width=7, borderwidth=5)
    plus.grid(row=3, column=3, padx=(5, 5), pady=(5, 5))

    minus = Button(gui, text=' - ', fg='black', bg='light green',
                   command=lambda: press("-"), height=2, width=7, borderwidth=5)
    minus.grid(row=4, column=3, padx=(5, 5), pady=(5, 5))

    multiply = Button(gui, text=' * ', fg='black', bg='light green',
                      command=lambda: press("*"), height=2, width=7, borderwidth=5)
    multiply.grid(row=5, column=3, padx=(5, 5), pady=(5, 5))

    divide = Button(gui, text=' / ', fg='black', bg='light green',
                    command=lambda: press("/"), height=2, width=7, borderwidth=5)
    divide.grid(row=6, column=3, padx=(5, 5), pady=(5, 5))

    equal = Button(gui, text=' = ', fg='black', bg='light green',
                   command=equalpress, height=2, width=7, borderwidth=5)
    equal.grid(row=6, column=2, padx=(5, 5), pady=(5, 5))

    clear = Button(gui, text='Clear', fg='white', bg='red',
                   command=clear, height=2, width=7, borderwidth=5)
    clear.grid(row=7, column='2', padx=(5, 5), pady=(5, 5))

    clear_s = Button(gui, text='<--', fg='white', bg='red',
                     command=clear_single, height=2, width=7, borderwidth=5)
    clear_s.grid(row=7, column='1', padx=(5, 5), pady=(5, 5))

    dec = Button(gui, text='.', fg='black', bg='light green',
                 command=lambda: press('.'), height=2, width=7, borderwidth=5)
    dec.grid(row=6, column=0, padx=(5, 5), pady=(5, 5))

    gui.mainloop()
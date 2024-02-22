from tkinter import *


# Records Buttons Pressed
def buttonPress(num):
    global equationText

    equationText = equationText + str(num)
    equationLabel.set(equationText)


# Evaluated The Equation Typed 
def equals():
    global equationText

    try:
        total = str(eval(equationText))
        equationLabel.set(total)
        equationText = total
        
    except SyntaxError:
        equationLabel.set("Syntax ERROR")
        equationText = ""

    except ZeroDivisionError:
        equationLabel.set("Zero Div ERROR")
        equationText = ""


# Clears the Output Label
def clear():
    global equationText

    equationLabel.set("")
    equationText = ""


window = Tk()
window.title("Calculator")
window.geometry("225x300")

equationText = ""

equationLabel = StringVar()

# Output Label
label = Label(window, textvariable=equationLabel, font=("consolas", 20), fg="#18a8eb",bg="#ebeceb", width=20, height=2)
label.pack()

# Platform to Hold The Buttons
frame = Frame(window)
frame.pack()

clear = Button(frame, text="C", height=1, width=4, fg="#797ef6", font=("Bold", 30), command=clear)
clear.grid(row=0, column=0, columnspan=2)

deci = Button(frame, text=".", height=1, width=1, fg="#797ef6", font=("Bold", 30), command=lambda: buttonPress("."))
deci.grid(row=0, column=2)

button7 = Button(frame, text=7, height=1, width=1, fg="#4bdedd",font=("Bold", 30), command=lambda: buttonPress(7))
button7.grid(row=1, column=0)

button8 = Button(frame, text=8, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(8))
button8.grid(row=1, column=1)

button9 = Button(frame, text=9, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(9))
button9.grid(row=1, column=2)

button4 = Button(frame, text=4, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(6))
button6.grid(row=2, column=2)

button1 = Button(frame, text=1, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(1))
button1.grid(row=3, column=0)

button2 = Button(frame, text=2, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(2))
button2.grid(row=3, column=1)

button3 = Button(frame, text=3, height=1, width=1, fg="#4bdedd", font=("Bold", 30), command=lambda: buttonPress(3))
button3.grid(row=3, column=2)

button0 = Button(frame, text=0, height=1, width=4, fg="#003EFF", font=("Bold", 30), command=lambda: buttonPress(0))
button0.grid(row=4, column=0, columnspan=2)

equal = Button(frame, text="=", height=1, width=4, fg="#797ef6", font=("Bold", 30), command=equals)
equal.grid(row=4, column=2, columnspan=2)

divide = Button(frame, text="/", height=1, width=1, fg="#797ef6", font=("Bold", 30), command=lambda: buttonPress("/"))
divide.grid(row=0, column=3)

multiply = Button(frame, text="*", height=1, width=1, fg="#797ef6", font=("Bold", 30), command=lambda: buttonPress("*"))
multiply.grid(row=1, column=3)

minus = Button(frame, text="-", height=1, width=1, fg="#797ef6", font=("Bold", 30), command=lambda: buttonPress("-"))
minus.grid(row=2, column=3)

plus = Button(frame, text="+", height=1, width=1, fg="#797ef6", font=("Bold", 30), command=lambda: buttonPress("+"))
plus.grid(row=3, column=3)


window.mainloop()

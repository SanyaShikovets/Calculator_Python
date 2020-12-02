from tkinter import *
from decimal import *
from tkinter import messagebox
from math import trunc

calculator = Tk()
calculator.title('Calculator')
calculator.geometry("520x650")

firstNumberString = StringVar()
secondNumberString = StringVar()
thirdNumberString = StringVar()
fourthNumberString = StringVar()
firstActionString = StringVar()
secondActionString = StringVar()
thirdActionString = StringVar()
result = StringVar()

def Is_num(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def sout(x):
    return '{0:,}'.format(x).replace(',', ' ')

def count():
    textResult1.delete(0, END)
    input1 = firstNumber.get().replace(',', '.').replace(' ', '')
    input2 = secondNumber.get().replace(',', '.').replace(' ', '')
    input3 = thirdNumber.get().replace(',', '.').replace(' ', '')
    input4 = fourthNumber.get().replace(',', '.').replace(' ', '')

    actionOne = firstAction.get()
    actionTwo = secondAction.get()
    actionThree = thirdAction.get()

    if actionOne == "+" or actionOne == "-" or actionOne == "*" or actionOne == "/" or not actionOne:
        action1 = actionOne
        if not actionOne:
            action1 = "+"
        if actionTwo == "+" or actionTwo == "-" or actionTwo == "*" or actionTwo == "/" or not actionTwo:
            action2 = actionTwo
            if not actionTwo:
                action2 = "+"
            if actionThree == "+" or actionThree == "-" or actionThree == "*" or actionThree == "/" or not actionThree:
                action3 = actionThree
                if not actionThree:
                    action3 = "+"
            else:
                messagebox.showerror("Calculator", "third action is invalid")
                return
        else:
            messagebox.showerror("Calculator", "second action is invalid")
            return
    else:
        messagebox.showerror("Calculator", "first action is invalid")
        return

    if not input1:
        first = 0
    else:
        if 'e' in input1 or 'E' in input1:
            messagebox.showerror("Calculator", "first number is invalid11")
            return
        else:
            if Is_num(input1):
                first = Decimal(input1)
            else:
                messagebox.showerror("Calculator", "first number is invalid")
                return
    if not input2:
        second = 0
    else:
        if 'e' in input2 or 'E' in input2:
            messagebox.showerror("Calculator", "second number is invalid")
            return
        else:
            if Is_num(input2):
                second = Decimal(input2)
            else:
                messagebox.showerror("Calculator", "second number is invalid")
                return

    if not input3:
        third = 0
    else:
        if 'e' in input3 or 'E' in input3:
            messagebox.showerror("Calculator", "third number is invalid")
            return
        else:
            if Is_num(input3):
                third = Decimal(input3)
            else:
                messagebox.showerror("Calculator", "third number is invalid")
                return

    if not input4:
        fourth = 0
    else:
        if 'e' in input4 or 'E' in input4:
            messagebox.showerror("Calculator", "fourth number is invalid")
            return
        else:
            if Is_num(input4):
                fourth = Decimal(input4)
            else:
                messagebox.showerror("Calculator", "fourth number is invalid")
                return

    bufResult = round(second + third, 10)
    if action2 == "-":
        bufResult = round(second - third, 10)
    if action2 == "*":
        bufResult = round(second * third, 10)
    if action2 == "/":
        bufResult = round(second / third, 10)
    flag = False
    if action3 == "*":
        flag = True
        bufResult2 = round(bufResult * fourth, 10)
    if action3 == "/":
        flag = True
        bufResult2 = round(bufResult / fourth, 10)
    if flag:
        result = round(first + bufResult2, 10)
        if action1 == "-":
            result = round(first - bufResult2, 10)
        if action1 == "*":
            result = round(first * bufResult2, 10)
        if action1 == "/":
            result = round(first / bufResult2, 10)
    else:
        bufResult2 = round(first + bufResult, 10)
        if action1 == "-":
            bufResult2 = round(first - bufResult, 10)
        if action1 == "*":
            bufResult2 = round(first * bufResult, 10)
        if action1 == "/":
            bufResult2 = round(first / bufResult, 10)
        result = round(bufResult2 + fourth, 10)
        if action3 == "-":
            result = round(bufResult2 - fourth, 10)
        if action3 == "*":
            result = round(bufResult2 * fourth, 10)
        if action3 == "/":
            result = round(bufResult2 / fourth, 10)
    textResult1.insert(INSERT, str(result))
    textResult.insert(INSERT,
                      str(sout(first)) + " " + action1 + " (" + str(sout(second)) + " " + action2 + " " +  str(sout(third)) + ") "
                      + action3 + " " + str(sout(fourth)) + " = " + str(sout(result)) + "\n")

def r(num):
    num = float(num)
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

def math():
    res = result.get()
    textResult1.delete(0, END)
    textResult1.insert(INSERT, str(r(Decimal(res))))

def accountant():
    res = result.get()
    textResult1.delete(0, END)
    textResult1.insert(INSERT, str(round(Decimal(res))))

def truncation():
    res = result.get()
    textResult1.delete(0, END)
    textResult1.insert(INSERT, str(trunc(Decimal(res))))

labelName = Label(calculator, text="Шиковец Александр Дмитриевич 3 курс 12 группа 2020", font=("Times New Roman", 14))
labelName.place(x=10, y=10)

labelFirstNumber = Label(calculator, text="Введите 1 число:", font=("Times New Roman", 14))
labelFirstNumber.place(x=10, y=50)

labelSecondNumber = Label(calculator, text="Введите 2 число:", font=("Times New Roman", 14))
labelSecondNumber.place(x=10, y=130)

labelFirstNumber = Label(calculator, text="Введите 3 число:", font=("Times New Roman", 14))
labelFirstNumber.place(x=10, y=210)

labelFirstNumber = Label(calculator, text="Введите 4 число:", font=("Times New Roman", 14))
labelFirstNumber.place(x=10, y=290)

firstNumber = Entry(calculator, width=35, bd=3, font=("Times New Roman", 14), textvariable=firstNumberString)
firstNumber.place(x=180, y=50)

firstAction = Entry(calculator, width=5, bd=3, font=("Times New Roman", 14), textvariable=firstActionString)
firstAction.place(x=310, y=90)

secondNumber = Entry(calculator, width=35, bd=3, font=("Times New Roman", 14), textvariable=secondNumberString)
secondNumber.place(x=180, y=130)

secondAction = Entry(calculator, width=5, bd=3, font=("Times New Roman", 14), textvariable=secondActionString)
secondAction.place(x=310, y=170)

thirdNumber = Entry(calculator, width=35, bd=3, font=("Times New Roman", 14), textvariable=thirdNumberString)
thirdNumber.place(x=180, y=210)

thirdAction = Entry(calculator, width=5, bd=3, font=("Times New Roman", 14), textvariable=thirdActionString)
thirdAction.place(x=310, y=250)

fourthNumber = Entry(calculator, width=35, bd=3, font=("Times New Roman", 14), textvariable=fourthNumberString)
fourthNumber.place(x=180, y=290)

sumButton = Button(calculator, text="count", font=("Times New Roman", 14), bd=10, command=count)
sumButton.place(x=400, y=350)

mathButton = Button(calculator, text="математическое", font=("Times New Roman", 14), bd=4, command=math)
mathButton.place(x=10, y=330)

accountantButton = Button(calculator, text="бухгалтерское", font=("Times New Roman", 14), bd=4, command=accountant)
accountantButton.place(x=10, y=370)

truncationButton = Button(calculator, text="усечение", font=("Times New Roman", 14), bd=4, command=truncation)
truncationButton.place(x=10, y=410)

labelResult1 = Label(calculator, text="Результат округления:", font=("Times New Roman", 14))
labelResult1.place(x=10, y=470)

textResult1 = Entry(calculator, width=30, bd=4, font=("Times New Roman", 14), textvariable=result)
textResult1.place(x=200, y=470)

labelResult = Label(calculator, text="Результат:", font=("Times New Roman", 14))
labelResult.place(x=10, y=520)

textResult = Text(calculator, height=5, width=43, bd=5, font=("Times New Roman", 14))
textResult.place(x=120, y=520)

calculator.mainloop()

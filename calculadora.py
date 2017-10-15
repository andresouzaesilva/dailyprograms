from tkinter import *
from tkinter import ttk

janela=Tk()

# função soma
def soma():
    num1=float(num1Entry.get())
    num2=float(num2Entry.get())
    lb["text"] = num1 + num2

#função subtração
def sub():
    num1=float(num1Entry.get())
    num2=float(num2Entry.get())
    lb["text"] = num1 - num2

#função multiplicação
def multi():
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    lb["text"] = num1 * num2

#função divisão
def divi():
    num1=float(num1Entry.get())
    num2=float(num2Entry.get())
    lb["text"] = num1 / num2

#Label observação
Label(janela, text="Digite os numeros primeiros e depois a operação!").place(x=10, y=10)

#Label e caixa do número 1
Label(janela, text="Digite o primeiro número").place(x=50, y=40)
num1Entry = Entry(janela)
num1Entry.place(x=50, y=60)

#Label e caixa do número 2
Label(janela, text="Digite o segundo número").place(x=50, y=80)
num2Entry = Entry(janela)
num2Entry.place(x=50, y=100)

#botão soma
b1= Button(janela, width=7, text="+", command=soma)
b1.place(x=180, y=60)

#botão subtração
b2= Button(janela, width=7, text="-", command=sub)
b2.place(x=180, y=100)

#botão multiplicação
b3= Button(janela, width=7, text="*", command=multi)
b3.place(x=180, y=140)

#botão divisão
b4= Button(janela, width=7, text="/", command=divi)
b4.place(x=180, y=180)

#label e caixa resultado
Label(janela, text="Resultado =").place(x=50, y=180)
lb=Label(janela, text="")
lb.place(x=120, y=180)


janela.title("Calculadora")
janela.geometry("280x280")
janela.mainloop()
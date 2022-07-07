from tkinter import *

csa = Tk()
csa.title("Ticker System")
csa.geometry("1200x50")
csa.config(bg="#549")

mili_seconds = 300
variable = StringVar()
label = Label(csa, textvariable=variable, height=10)


def ticker_system():
    ticker_system.msg = ticker_system.msg[1:] + ticker_system.msg[0]
    variable.set(ticker_system.msg)
    csa.after(mili_seconds, ticker_system)


ticker_system.msg = " THIS IS AKHTAR ALI & THANKS FOR VISITING AND SUPPORTING ME, DO NOT FORGET TO HIT LIKE AND DO SUBSCRIBE MY CHANNEL"
ticker_system()
label.pack()
csa.mainloop()

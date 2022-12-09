# import numpy as np
# import pandas as pd
# from tkinter import *
# from tkinter import ttk
#
# clicks = 0
#
# def changetext():
#     btn['text'] = 'Ну и хуйня'
#
#
# df = pd.read_csv('annual_deaths_by_causes.csv')
# df=df.dropna()
# col = list(df)
# col.remove('country')
# col.remove('year')
# col.remove('code')
# window = Tk()
# window.title("You choose:")
# window.geometry('1000x1000')
# lbl = Label(window, text="Выбирай сука", font=("Arial Bold", 50))
# a = 2
# for i in col:
#     btn = Button(window, text=i, font=("Arial Bold", 1), command=changetext)
#     btn.grid(column=a, row=0)
#     a += 100
# window.mainloop()

import tkinter as tk
import random

windows = tk.Tk()

def random1():
    s1 = ['kk','aa','cc']
    s = random.choice(s1)
    return s
def random2():
    s2 = ['oy','xw','yccd ']
    s = random.choice(s2)
    return s
def button_click():
    name = nameEntry.get()
    verb = random1()
    noun = random2()
    sentence = name +"" + verb +""+noun
    result.delete(0,tk.END)
    result.insert(0,sentence)
namelabel = tk.Label(windows,text="name:")
nameEntry = tk.Entry(windows)
button = tk.Button(windows,text="生成随机",command=button_click)
result =tk.Entry(windows)
namelabel.pack()
nameEntry.pack()
button.pack()
result.pack()
windows.mainloop()
from tkinter import *
root = Tk()
root.geometry('260x380')
root.title("YANG")
frame_show = Frame(width=300,height=150,bg='red')
frame_show.pack()
sv = StringVar()
sv.set('0')
show_label=Label(frame_show,textvariable=sv,bg='green',width=12,height=1,font=('黑体',20,'bold'),justify=LEFT,anchor='e')
show_label.pack(padx=10,pady=10)

def delete():
    print("删除")
def fanhui():
    print("返回")
def clear():
    print("清除")
frame_bord = Frame(width=400,height=350,bg='#cccccc')
b_del= Button(frame_bord,text='删除',width=5,height=1,command=delete)
b_del.grid(row=0,column=0)
b_clear = Button(frame_bord,text='C',width=5,height=1,command=clear).grid(row=0,column=1)
def change(num):
    print(num)
b_1 = Button(frame_bord,text='1',width=5,height=2,command=lambda:change('1'))
b_1.grid(row=1,column=0)
frame_bord.pack(padx=10,pady=10)
root.mainloop()
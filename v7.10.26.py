import tkinter as tk

window = tk.Tk()
def check_password():
    password = "110"
    entryword_pass = passwordentry.get()
    if password == entryword_pass:
        confirmlabel.config(text='正确')
    else:
        confirmlabel.config(text='错误')

password_label = tk.Label(window,text="密码")
passwordentry = tk.Entry(window,show="*")
button = tk.Button(window,text="校验",command=check_password)
confirmlabel = tk.Label(window,text='结果')
password_label.pack()
passwordentry.pack()
button.pack()
confirmlabel.pack()
window.mainloop()
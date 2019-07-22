import tkinter

if __name__=="__main__":
    root_window = tkinter.Tk()
    root_window.title('飞机大战')
    root_window.resizable(width=False,height=False)
    window_canvas = tkinter.Canvas(root_window,width=480,height=600)
    window_canvas.pack()
    bg_img_name = 'D:\\pycharm\\dnf.png'
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    window_canvas.create_image(240,300,anchor=tkinter.CENTER,image=bg_img,tags='bg')
    bee_img_name = "D:\\pycharm\\h2u.png"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    window_canvas.create_image(120,150,anchor=tkinter.CENTER,image=bee_img,tags='bee')
    root_window.mainloop()
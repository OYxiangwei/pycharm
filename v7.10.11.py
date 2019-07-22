file_name = input("请输入文件名：")
def file_write(file_name):
    f = open(file_name,"w+")
    print("请输入内容 或者 按w退出")
    while True:
        write_something = input()
        if write_something != 'w':
            f.write(write_something)
        else:
            break
    f.close()

file_write('7.10.txt')
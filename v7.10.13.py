file_name = input("请输入要打开的文件名:")
rep_word = input("请输入要替换的：")
new_word = input("请输入替换的新字符串：")

def r_p(file_name,rep_word,new_word):
    f = open(file_name)
    content = []
    for eachline in f:
        if rep_word in eachline:
            eachline = eachline.replace(rep_word,new_word)
        content.append(eachline)
    decide = input("你确定替换吗：")
    if decide in ['yes','YES']:
        f_write = open(file_name,"w+")
        f_write.write("".join(content))
        f_write.close()

r_p(file_name,rep_word,new_word)
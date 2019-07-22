import os
start_dir = input("请输入目录:")
target = input("请输入搜索的文件名：")
backbu = []
def search_file(start_dir,target):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print("找到了")
            backbu.append(each_file)

        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)
    return backbu

rd = search_file(start_dir,target)
f = open(os.getcwd()+os.sep + 'backup.txt','wb' )
f.write('\n'.join(rd).encode('utf-8'))
f.close()
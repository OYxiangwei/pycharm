file1 = input("输入第一个要比较的文件:")
file2 = input("请输入第二个要比较的文件:")
def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0
    differ = []
    for line1 in f1:
        line2 = f2.readline()
        count +=1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
differ = file_compare(file1,file2)
if len(differ) == 0:
    print("相同")
else:
    print(len(differ))
    for each in differ:
        print(each)
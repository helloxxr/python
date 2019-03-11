#案例：读取stu_info.txt文件内容，并将所有文件中学生名称显示出来
f=open('stu_info.txt','r')
'''以只读方式打开txt文件'''
#readlines()一次性读取文件所有行 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理
lines=f.readlines()
print(lines)
for line in lines:
    print(line.split(',')[0])
    print(line.split(',')[1])
    print(line.split(',')[2])

#每次读取整个文件read()，read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。
# line0=f.read()
# print(line0)
#readline() 每次只读取一行
# line1=f.readline()
# print(line1)
f.close()



#异常学习
# try:
#     filename=input("please input filename:")
#     open("%r.txt"%filename)
# except FileNotFoundError:
#     print("%r文件未找到"%filename)
'''
#异常学习
try:
    print(stu)
except NameError:
    print("变量未定义")
#异常学习
try:
    print(stu)
except BaseException:
    print("变量未定义")

#异常学习
try:
    stu='Jack'
    print(stu)
#只有发生异常时打印except信息
except BaseException as msg:
    print(msg)
#只有当正确时处理else的信息,等于另起一分支
else:
    print("Test end!")
#异常学习
try:
    stu='Jack'
    print(stu)
#只有发生异常时打印except信息
except BaseException as msg:
    print(msg)
#以下finally语句都处理
finally:
    print("Test end!")
'''

#异常学习
def division(x,y):
    if y==0:
       raise ZeroDivisionError("zero is not allow!")
    return x/y
try:
    k=division(8,2)
except BaseException as msg:
    print(msg)
else:
    print("%r" %k)
finally:
    print("The end!")
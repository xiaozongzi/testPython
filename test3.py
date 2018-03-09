# for i in range(10):
#     print(i)
#
# print('\n')
# print(R'\n')
from Tools.scripts.treesync import raw_input

globvar = 0


def set_globvar_to_one():
    global globvar  # 使用 global 声明全局变量
    globvar = 1


def print_globvar():
    print(globvar)  # 没有使用 global


set_globvar_to_one()
print(globvar)  # 输出 1
print_globvar()  # 输出 1，函数内的 globvar 已经是全局变量


def reverse(li):
    print(5 // 2)
    for i in range(0, len(li) // 2):
        temp = li[i]
        li[i] = li[-i - 1]
        li[-i - 1] = temp
        # print(locals())


l = [1, 2, 3, 4, 5]
reverse(l)
print(l)

str = raw_input("请输入：")
print("你输入的内容是: ", str)

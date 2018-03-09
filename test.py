# -*- coding: UTF-8 -*-
# print("Hello, World!")
# count = 1
# name = """whil
# e i"""
# print(name)
# list = ['12', 'ff', 'dfd', 'eee', "ddf"]
# tinylist = [2.23, 'john']
# print(list)
# print(list[1])
# print(list.__len__())
# # print(list.index('john'))
# print(list[1:])
# print(list.__contains__('joh'))
# print(list.__contains__('john'))
# print('john' not in list)
# # print(list.insert(1,"222"))
# # print(list+tinylist)
# # print(list.pop())
# # print(list.pop())
# list.sort()
# # list=tinylist
# print(list)
#
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
# # tuple[1] = "222" 元组不能赋值
# print(tuple + tinytuple)
# print(tuple[2])
# print(tuple.__class__)
#
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
# print(dict)
# print(dict['one'])
# print(dict.__contains__(2))
# print(dict.__contains__(3))
# # 合并2个 字典
# d = dict.copy()
# d.update(tinydict)
# print(d)
#
# print(dict.items())
#
# a = 21
# b = 10
# c = 0
# c = a // b
# print(a / b)
#
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
# c = 0
#
# c = a & b;  # 12 = 0000 1100
# print("1 - c 的值为：", c)
#
# c = a | b;  # 61 = 0011 1101
# print("2 - c 的值为：", c)
#
# c = a ^ b;  # 49 = 0011 0001
# print("3 - c 的值为：", c)
#
# c = ~a;  # -61 = 1100 0011
# print("4 - c 的值为：", c)
#
# c = a << 2;  # 240 = 1111 0000
# print("5 - c 的值为：", c)
#
# c = a >> 2;  # 15 = 0000 1111
# print("6 - c 的值为：", c)
#
# a = 20.0
# b = 20
# print(a and b)  # a为false 才返回false 不然返回b的值
# print(a or b)
# print(not 0)
# print(a.__eq__(b))
# print(a is b)
# print(id(a) is id(b))
#
# a = 2
# b = 4
# c = 6
# print(a + b * c)
# print(c is a + b)
#
# if 0:
#     print(a)
#     print(b)
# print(c)
# var = 1
# # while var:  # 该条件永远为true，循环将无限执行下去
# #     num = int(input("Enter a number  :"))
# #     var = num
# #     print("You entered: ", var)
# #
# # print("Good bye!")
# index = 1
# for index in range(1, 10):
#     print(index)
#
# sequence = [12, 34, 34, 23, 45, 76, 89]
# # print(enumerate(sequence).__str__())
# for i, j in enumerate(sequence):  # 循环读
#     print(i, j)
#
# i = 2
# while (i < 100):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j): print(i, " 是素数")
#     i = i + 1
#
# print("Good bye!")
#
# print(complex(11.2, 5.26))


# def check(name, age):
#     print(str(age) + name)
#
#
# check("ff", 50)
#
# cast = ["dfdf", "eeeee", 0]
# cast.remove(0)
# sd = "aaaadf"
# a = sd.split("d")
# print(a)

file = open("D:\logcat.txt")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.seek(0)
print(file.readlines())
s = set({"2", "3", "4", 5})
print(s)
# for name in file:
#     print(name)
# file.close()
#
# string = "221"
# string = string.replace("2", "1")
# print(string)
#
# clean = []
# # clean = [each for each in file]
# dist = set({10, 11, 22})  # set 方法创建集合
# print(dist)

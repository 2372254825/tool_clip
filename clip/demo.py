# # import sys
# # list = (1, 2, 3, 4)
# # it = iter(list)
# # while True:
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         sys.exit()
# class MyNumberas:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# myclass = MyNumberas()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)

# class Numbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
# myclass = Numbers()
# it = iter(myclass)
# for x in myclass:
#     print(x)

# import sys
#
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b, = b, a + b
#         counter += 1
# f = fibonacci(10)
#
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# def area(width, height):
#     return width*height
#
# def print_welcome(name):
#     print("Welcome", name)
#
# print_welcome("aaa")
# w = 4
# h = 5
# print("width=", w, "height = ", h, "area =", area(w, h))

# def printme( str ):
#     print(str)
#     return
# printme("Hello World")
#
#
# def printinfo(arg1, *vartuple):
#     print("打印:")
#     print(arg1)
#     # for var in vartuple:
#     #     print(var)
#     # return
#     print(vartuple)
#
#
# # printinfo(1, a=70, b=60, c=50)
# # printinfo(1)
# printinfo(1, 2, 3, 4, 5)
#
#
# # sum = lambda arg1, arg2 : arg1+arg2
# #
# # print("输出后的和为：", sum(10, 20))
# # print("输出后的和为：", sum(20, 20))
#
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数体：", total)
#     return total
#
#
# total = sum(10, 20)
#
# print(total)
#
# # vec = [2, 4, 6]
# # # print([3*x for x in vec])
# # print(3*x for x in vec if x < 2)
# import sys
#
# print('命令参数如下：')
# for i in sys.argv:
#     print(i)
# print('\n\npython 路径为：', sys.path, '\n')

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print("我来自另一个模块")

# import sys
# dir(sys)
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    print(repr(x*x*x).rjust(4))
# def Foo(x):
# #     if (x==4):
# #         # print(1)
# #         print(x+Foo(x-1))
# #
# #
# # print(Foo(4))

print('{}网址："{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))

print('{name}网址: {site}'.format(name='菜鸟教程', site='www.runoob.com'))



import math
print('常量 PI 的值近似为：{}。'.format(math.pi))
print('常量 PI 的值近似为：{!s}。'.format(math.pi))
print('常量 PI 的值近似为：{!r}。'.format(math.pi))
print('常量 PI 的值近似为：{!a}。'.format(math.pi))
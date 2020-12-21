# file1 = open('spam.txt')
# list1 = file1.readlines()
# print(list1)
# file2 = open('spam-message.txt','w')
# # "sales" , #back to work" , "help,"sos",
#
# for line in list1:
#     if 'sales' in line or 'back to work' in line or 'help' in line or 'sos' in line:
#         file2.write(line)

# with open('rock.txt') as file1:
#     list1 =file1.readlines()
#     print(len(list1))
#     i = 1
#     for line in list1:
#
#         print(f'B {i} строке - {len(line)})- символов')


# def write(filename,mode):
#     if mode == 'read':
#         file1 = open(filename)
#         print(file1.read())
#     elif mode == 'write':
#         file1 = open(filename,'w')
#         text = input("Введите текст:")
#         file1.write(text)
# write('spam.txt','write')



# socks = list(map(int,input().split()))
# a = socks[0]
# b = socks[1]
# count_fash = 0
# count_notfash = 0
# if a > b:
#     a = a - b
#     if a > 1:
#         count_notfash = a // 2
#     print(b, count_notfash)
# elif a < b:
#     b = b - a
#     if b > 1:
#         count_notfash = b // 2
#         print(a, count_notfash)
#     else:
#         b = 0


# red = socks[0]
# blue = socks [1]
#
# count_fashion = min (red,blue)
# count_not_fashion = (red - min(red,blue) + blue - min(red,blue))//2
#
# print(count_fashion,int(count_not_fashion))
# print(min(red,blue),(max(red,blue))-min(red,blue)//2)


# import random
# n = int(input())
# list1 = list(map(int,input()))
# print(list1)
# ser = 0
# dim = 0
# i = 0
# while i < len(list1):
#     scales = max(list1[0],list1[-1])
#     if i % 2 == 0:
#         ser += scales
#     else:
#         dim += scales
#     i += 1
#     list1.remove(scales)
# print(ser,dim)


# list1 = [1,2,3,4,5,6,7,8,9,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4]
# list2 = [1,2,3,4,5,6,7,8,9]
# dict1 = {}
#
# def unique (list2):
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
# print(list2)
#
# for i in range (len(list1)):
#     dict1 = {list1[i]:list1.count(list1[i])}
#     print(dict1)

# string = 'lAla'
#
# if not string[0].istitle() and string[1:].isupper():
#     print(string.swapcase())
# elif string.isupper():
#     print(string.swapcase())
# elif len(string)>1 and string.islower():
#     print(string)
# elif len(string)==1 and string.islower():
#     print(string.swapcase())
# else:
#     print(string)


class Car:

    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
        self.fuel = 100
        self.run = 0
        self.color = 'orange'
        self.no2 = False

    def move(self,distance):
        if distance > 0:
            result = 20/100
            result = distance * result
            self.fuel -= result
            self.run += distance

car1 =  Car('tesla','XS',90000)
print(car1.run)
car1.move(240)
print(car1.run)

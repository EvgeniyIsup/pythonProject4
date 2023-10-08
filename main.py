# 1 задача
# radius = int(input("радиус "))
# duga = int(input("дуга "))
# def ploshadSect(radius, duga):
#      return duga*(radius/2)
# print(f"Площадь сектора = {ploshadSect(radius, duga)}")


# # 2 задача
# choice = int(input("выберите метод через дугу(1) или количество секторов(2) "))
# if choice == 1:
#     radius = int(input("радиус "))
#     duga = int(input("дуга "))
#     def ploshadSect(radius, duga):
#      return duga*(radius/2)
#     print(f"Площадь сектора = {ploshadSect(radius, duga)}")
#
# elif choice == 2:
#
#     import math
#     def ploshad (r):
#          return math.pi * r**2
#
#     r = int(input("Введите радиус "))
#     kolSec = int(input("Количество секторов "))
#     print(f"{ploshad(r) / kolSec}")



# 3 задача
# start = int(input("число"))
# end = int(input("второе число"))
# #
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#
#     sum = 0
#     for i in range(start, end + 1):
#         sum += i
#     return sum
# print(sum_range(start, end))
#
#
# 4 задача
price = 35800
procent = 20/100
newPrice = price * procent + price
print(newPrice)

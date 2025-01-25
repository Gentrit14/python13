# class Shape:
#     def __init__(self, width, length):
#         self.__width = width
#         self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def set_length(self, length):
#         self.__length = length
#
#
# square1 = Shape(20 , 20)
# print("Width:", square1.get_width())
# square1.set_width(40)
# print("Updatet width:", square1.get_width())


import datetime

current_time = datetime.datetime.now()

print("Year:" ,current_time.year)
print("Month:" , current_time.month)
print("Day:", current_time.day)
print("Time", current_time.hour)

current1_time = datetime.datetime.now().date()

print(current1_time)



settime = datetime.datetime.now()

specific_time = datetime.datetime(2020, 10,22)

print(specific_time.year)
print(specific_time.month)
print(specific_time.day)

future_time = current_time + datetime.timedelta(days= 100)

print(future_time.year)

teksti1 = "Hello world this is the world hahahahhaahah"

with open("example.txt", "w") as file:
    file.write(teksti1)

file_path = "example.txt"
file = open(file_path, "r")

content = file.read()
print(content)
file.close()

with open ("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open ("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
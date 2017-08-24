# string = "1234567890"

# for char in string:
#     print(char)
# my_interator = iter(string)
# print(my_interator)
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))
# print(next(my_interator))

# for char in string:
#     print(char)

# for char in iter(string):
#     print(char)

my_list = ["monday", "tuesday", "wednesday",
           "thursday", "friday", "saturday", "sunday"]

my_interator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_interator)
    print(next_item)

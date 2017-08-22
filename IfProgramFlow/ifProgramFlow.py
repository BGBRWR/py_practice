# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))
# print("Please guess a number betweenn 1 and 10: ")
# guess = int(input())

# if guess != 5:
#     if guess < 5:
#         print("Pleae guess higher")
#     else: # guess must be greater than 5
#         print("Please guess lower")

#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly.")
# else:
#     print("You got it the first time")

# age = int(input("How old are you? "))
# # if (age >=16) and (age <=65):
# # if 16 <= age <= 65:
# # if 15 < age < 66:
# #     print("Have a good day at work")
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# x = "false"
# if (x):
#     print("x is true")

# x = input("Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# print(not False)
# print(not True)

# age = int(input("how old are you? "))
# if not(age < 18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")
name = input('What is your name? ')
age = int(input('What is your age, {0}? '.format(name)))

if (18 <= age <= 30):
    print('Welcome to the Party, {0}'.format(name))
elif age < 18:
    print('You are too young to party, {0}'.format(name))
else:
    print('You are too old to party, {0}'.format(name))

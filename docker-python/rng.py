from random import randint

min_number = int(input('Min number: '))
max_number = int(input('Max number: '))

if min_number > max_number:
    print("Invalid input")
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number) 
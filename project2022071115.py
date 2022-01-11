# write by number int dari 0 - 75
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(75):
	value = randint(0,75)
	print(value)
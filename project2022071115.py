# write by number int dari 0 - 98
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(98):
	value = randint(0,98)
	print(value)
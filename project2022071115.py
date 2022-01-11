# write by number int dari 0 - 61
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(61):
	value = randint(0,61)
	print(value)
# write by number int dari 0 - 96
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(96):
	value = randint(0,96)
	print(value)
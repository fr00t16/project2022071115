# write by number int dari 0 - 285
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(285):
	value = randint(0,285)
	print(value)
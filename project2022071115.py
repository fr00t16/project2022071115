# write by number int dari 0 - 76
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(76):
	value = randint(0,76)
	print(value)
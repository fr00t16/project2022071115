# write by number int dari 0 - 253
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(253):
	value = randint(0,253)
	print(value)
# write by number int dari 0 - 37
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(37):
	value = randint(0,37)
	print(value)
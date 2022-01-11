# write by number int dari 0 - 473
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(473):
	value = randint(0,473)
	print(value)
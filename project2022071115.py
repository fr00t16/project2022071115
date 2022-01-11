# write by number int dari 0 - 36
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(36):
	value = randint(0,36)
	print(value)
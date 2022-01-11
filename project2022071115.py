# write by number int dari 0 - 10
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(10):
	value = randint(0,10)
	print(value)
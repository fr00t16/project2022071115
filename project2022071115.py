# write by number int dari 0 - 28
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(28):
	value = randint(0,28)
	print(value)
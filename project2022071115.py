# write by number int dari 0 - 263
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(263):
	value = randint(0,263)
	print(value)
# write by number int dari 0 - 361
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(361):
	value = randint(0,361)
	print(value)
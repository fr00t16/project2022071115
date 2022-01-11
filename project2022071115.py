# write by number int dari 0 - 481
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(481):
	value = randint(0,481)
	print(value)
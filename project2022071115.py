# write by number int dari 0 - 631
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(631):
	value = randint(0,631)
	print(value)
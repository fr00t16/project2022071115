# write by number int dari 0 - 730
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(730):
	value = randint(0,730)
	print(value)
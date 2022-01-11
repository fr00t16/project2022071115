# write by number int dari 0 - 701
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(701):
	value = randint(0,701)
	print(value)
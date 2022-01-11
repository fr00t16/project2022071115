# write by number int dari 0 - 675
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(675):
	value = randint(0,675)
	print(value)
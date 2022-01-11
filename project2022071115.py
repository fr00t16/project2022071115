# write by number int dari 0 - 365
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(365):
	value = randint(0,365)
	print(value)
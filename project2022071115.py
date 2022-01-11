# write by number int dari 0 - 59
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(59):
	value = randint(0,59)
	print(value)
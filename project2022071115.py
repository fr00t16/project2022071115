# write by number int dari 0 - 13
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(13):
	value = randint(0,13)
	print(value)
# write by number int dari 0 - 650
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(650):
	value = randint(0,650)
	print(value)
# write by number int dari 0 - 563
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(563):
	value = randint(0,563)
	print(value)
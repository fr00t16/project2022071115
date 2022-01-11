# write by number int dari 0 - 241
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(241):
	value = randint(0,241)
	print(value)
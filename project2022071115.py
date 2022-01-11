# write by number int dari 0 - 609
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(609):
	value = randint(0,609)
	print(value)
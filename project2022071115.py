# write by number int dari 0 - 987
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(987):
	value = randint(0,987)
	print(value)
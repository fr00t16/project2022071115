# write by number int dari 0 - 991
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(991):
	value = randint(0,991)
	print(value)
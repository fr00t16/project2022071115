# write by number int dari 0 - 940
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(940):
	value = randint(0,940)
	print(value)
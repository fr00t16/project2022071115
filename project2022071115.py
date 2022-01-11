# write by number int dari 0 - 655
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(655):
	value = randint(0,655)
	print(value)
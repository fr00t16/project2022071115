# write by number int dari 0 - 953
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(953):
	value = randint(0,953)
	print(value)
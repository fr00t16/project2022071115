# write by number int dari 0 - 843
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(843):
	value = randint(0,843)
	print(value)
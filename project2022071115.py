# write by number int dari 0 - 970
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(970):
	value = randint(0,970)
	print(value)
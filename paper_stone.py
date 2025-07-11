import itertools as it
import random as random
x = ["paper","stone","scissors"]
re =list( it.combinations_with_replacement(x,2))
for each in range(10):
    number = random.randint(0,5)
    print(re[number])
    if number==0 or number==3 or number==5:
        print("agin")
    elif number==1:
        print("win paper")
    elif number==2:
        print("win scissors")
    else:
        print("win stone")
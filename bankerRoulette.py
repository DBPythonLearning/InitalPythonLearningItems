names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
import random
names2 = names[:]
bankers = []
banklen = len(bankers) 
nameslen = len(names2) 
a = 0
b = 0
while a < nameslen:
    bankers.append(names2[b])
    a  += 1
    b  += 1
payer = random.choice(bankers)
print(payer+" is going to buy the meal today!")
 
 
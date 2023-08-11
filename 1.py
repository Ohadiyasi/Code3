import random as r
import sys

rollCount = 0

def rollDice():
    global rollCount
    rollCount += 1
    i = r.randint(1, 6)
    print(f'Rolled number is {i}')
    if i == 6:
        print('Two more roll allowed')
        rollDice()
        rollDice()


for i in range(1):
    rollDice()

print(rollCount)
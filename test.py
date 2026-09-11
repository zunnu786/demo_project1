from numpy import random

x = random.choice([5, 2, 7], p=[0.1, 0.3, 0.6], size=100)
print(x)
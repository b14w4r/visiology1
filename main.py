import os
import random

if not os.path.exists('./test.xlsx'):
    os.mknod('./test.xlsx')
a = {}
names = ["Ivan", "Oleg", "Gennadiy", "Oksana", "Olga", "Elena"]
for i in range(10):
    a[random.choice(names)] = random.randint(1, 10)
print(a)
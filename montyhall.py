import random
sim = int(input('''how many times do you want to run the simulation?
'''))
switch = 0
stay = 0
for i in range(sim):
    car = random.randint(1, 3)
    choice_1 = random.randint(1, 3)
    zonk = random.randint(1, 3)
    while choice_1 == zonk or car == zonk:
        zonk = random.randint(1, 3)
    choice_2 = random.randint(1, 3)
    while choice_2 == choice_1 or choice_2 == zonk:
        choice_2 = random.randint(1, 3)
    if choice_2 == car:
        switch = switch + 1
    if choice_1 == car:
        stay = stay + 1
switch_percent = (switch/sim)*100
stay_percent = (stay/sim)*100
print('''Your chance of winning if you switch is''', switch_percent, '''%.
Your chance of winning if you stay is''', stay_percent, '''%.''')

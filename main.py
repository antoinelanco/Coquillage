bc = []
# mvt 1
move = [1,2,100]
bc.append (move)
# mvt 2
move = [1,2,100]
bc.append (move)
# mvt 3
move = [3,1,500]
bc.append(move)


# amount user1
amount = 0
for value in bc:
    if value[0] == 1:
        amount -= value[2]
    elif value[1] == 1:
        amount += value[2]
print amount
# amount user2
amount = 0
for value in bc:
    if value[0] == 2:
        amount -= value[2]
    elif value[1] == 2:
        amount += value[2]
print amount
# amount user3
amount = 0
for value in bc:
    if value[0] == 3:
        amount -= value[2]
    elif value[1] == 3:
        amount += value[2]
print amount

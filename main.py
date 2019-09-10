bc = []
users = {"user0":1000}

move = ["user0","user1",100]
bc.append (move)

move = ["user0","user2",50]
bc.append (move)

move = ["user0","user3",300]
bc.append (move)

move = ["user3","user4",250]
bc.append (move)

print bc

for value in bc:
    list = (0,1)
    for i in list:
        if not users.get(value[i]):
            print "On genere le " + value[i]
            users[value[i]] = 0
    # effectue la transaction
    users[value[0]] -= value[2]
    users[value[1]] += value[2]
    print users

for key, value in users.items():
    print key + " get " + str(value) + " coquillages"

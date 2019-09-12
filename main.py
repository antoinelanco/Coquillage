#! /usr/bin/env python3
import block

def add_dict(dict,key,value):
    if not key in dict:
        dict[key] = 0
    dict[key] += value

def sub_dict(dict,key,value):
    if not key in dict:
        dict[key] = 0
    dict[key] -= value

def amount(bc):
    users = {}
    for v in bc:
        add_dict(users,v[1],v[2])
        sub_dict(users,v[0],v[2])
    print(users)

bc = []

move = ["user0","user1",10000]
bc.append (move)

move = ["user1","user2",100]
bc.append (move)

move = ["user1","user3",50]
bc.append (move)

move = ["user1","user4",300]
bc.append (move)

move = ["user4","user5",250]
bc.append (move)

print(bc)
amount(bc)

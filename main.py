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
        #     print ("On genere le " + value[i])
        #     users[value[i]] = 0
        #
        # users[v[1]] +=
        # print(value)


# for value in bc:
#     list = (0,1)
#     for i in list:
#         if not users.get(value[i]):
#             print ("On genere le " + value[i])
#             users[value[i]] = 0
#     # effectue la transaction
#     users[value[0]] -= value[2]
#     users[value[1]] += value[2]
#     print(users)



#
# for key, value in users.items():
#     print (key + " get " + str(value) + " coquillages")



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

# print(bc)
amount(bc)

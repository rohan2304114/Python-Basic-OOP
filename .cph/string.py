# """ list  """

# number =[1,2,3,4,5,6,7,8,8,9,0]

# print(number[3])
# print(number[-8])


# name = 'Asikur Rahman Rohan'
# print(name[0])
# print(name[1])

# for char in name:
#     print(char)
#  tuples 

# def multiple():
#     return 3,4

# things = 'pen','book','laptop','charger','mouse',
# # print(things[0])
# # print(things[-2])
# # print(things[2:5])

# if 'pen' in things:
#         print('yes')
#         print(len(things))

        # tupple is immutable

#  set and sets

# about=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,1.0,1.0]
# print(about)
# numbers = set(about)
# print(numbers)


# A ={1,2,3,4,5,6,7,8,9}
# B={1,3,5,7,0}
# print(A&B)
# print(A|B)


# Dictionary python

# person ={'name':'Asikur Rahman Rohan','age':25,'city':'Dhaka'}
# # print(person)
# # print(person['name'])
# # print(person['age'])

# print(person.keys())
# print(person.values())




# for item in person:
#     print(item)

# numbers =[1,2,3,4,5,6,7,8,9]
# for i, num in enumerate(numbers):
#     print(i,)


# python built in modules


# from math import * 
# result = ceil(4.5)


# import pyautogui
# from time import sleep
# sleep(5)

# for i in range(0,3):
#     pyautogui.write('Hi')
#     pyautogui.press('enter')


# Exception in python

# try:

# result =45/0

# except :
# print('error happened')
# finally:
# print('finsih')


# with open('message.txt','r') as file:
#     text = file.read()
#     print(text)

# lamda expression
# doubled =lambda num :num *2
# squared =lambda num: num *num
# result =doubled(4)
# output = squared(4)
# print(result , output)

# add = lambda x,y : x+y
# result =add(1,5)
# print(result)

# lambda funtions are used in to shprten the code 

# number = [1,2,3,4,5,6,7,8,9]
# doubled = list(map(lambda x: x*2, number))
# print(doubled)


roomMates = [

    {
        'name':'Rohan',
        'age':23
    },
     {
        'name':'masud',
        'age':24
    },
     {
        'name':'nehal',
        'age':25
    },
     {
        'name':'sowkot',
        'age':26
    }
]

jnior = filter(lambda x: x ['age']<25, roomMates)
print(list(jnior))

























'''
A028 DoorDoorDoor
Problem : https://www.acmicpc.net/problem/17210
Date : 20220919
'''

door = int(input())
first = int(input())
if door >= 6:
    print("Love is open door")
else:
    if first == 0:
        for i in range(1, door):
            if i % 2 == 0:
                print(0)
            else:
                print(1)
    else:
        for i in range(1, door):
            if i % 2 == 0:
                print(1)
            else:
                print(0)
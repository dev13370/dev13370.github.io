import random

def list_ran():
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890-.'
    userlen = int(input("enter your user length: "))
    usercount = int(input("How many users would you like: "))

    for n in range(0, usercount):
        users = ""

        for n in range(0, userlen):
            
            userschar = random.choice(chars)
            users = users + userschar

        with open("list.txt", "a") as na :
            na.write(f"{users}\n")
            na.close()

list_ran()
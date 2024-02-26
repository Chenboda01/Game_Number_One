#!/usr/bin/env python3
# By chenboda01@gmail.com
# Created at Mon Feb 26 10:59:43 AM EST 2024
#

from random import randint
from time import sleep

boda = randint(1, 100)
daddy = randint(1, 100)

print("Are you ready to play a game?")
input = input("Press Enter to continue...")

print("Boda is drawing a number now....")
sleep(2)

print("Daddy is drawing a number now...")
sleep(2)

if boda > daddy:
    print("Boda wins! because boda is", boda, "and daddy is", daddy)
elif boda < daddy:
    print("Daddy wins! because boda is", boda, "and daddy is", daddy)
else:
    print("It's a tie! because boda is", boda, "and daddy is", daddy)

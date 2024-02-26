#!/usr/bin/env python3
# By chenboda01@gmail.com
# Created at Mon Feb 26 10:59:43 AM EST 2024
#

from random import randint
from time import sleep

boda_number = randint(1, 100)
daddy_number = randint(1, 100)

print("Are you ready to play a game?")
sleep(2)
# input = input("Press Enter to continue...")

print("Let's do it now.\n")

print("Boda is drawing a number now....")
sleep(2)

print("Daddy is drawing a number now...\n\n")
sleep(2)

if boda_number > daddy_number:
    print("Boda wins, because boda gets", boda_number, "and daddy gets", daddy_number, ".\n")
elif boda_number < daddy_number:
    print("Daddy wins, because boda gets", boda_number, "and daddy gets", daddy_number, ".\n")
else:
    print("It's a tie, because both boda and daddy get", boda_nubmer, ".\n")


print("Thanks for playing the game! See you next time!")

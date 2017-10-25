#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
guess = 0
secret = randint(0, 20)

while guess != secret:
    guess = int(raw_input("ugani skrito število "))
    if  guess == secret:
        print "ćestitam"
        break
    elif guess < secret:
        print "število je večje"
    elif guess > secret:
        print  "število je manjše"
    else:
        print  str(guess)+ " je napačno število  "

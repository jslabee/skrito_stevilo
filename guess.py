from random import randint

secret = randint(0, 20)
guess = 0
while guess != secret:
    guess = int(raw_input("ugani skrito stevilo "))

    if  guess == secret:
            print "cestitam {0}".format(guess)
            break

    elif guess > secret:
        print "Your guess is not correct... try something smaller"
    elif guess < secret:
        print "Your guess is not correct... try something bigger"
    else:
        print " je napacno stevilo %s " % (guess)
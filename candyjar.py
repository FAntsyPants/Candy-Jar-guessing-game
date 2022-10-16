# inspired to make a candy jar in order to emulate real world objects

from time import sleep

import random

#define the jar and its qualities


candy_jar = {

    "number of pieces": random.randint(10,100),

    "jar size": "32 oz.",

    "number of turns": random.randint(1, 10),

    "candy type": ["M&Ms", "Skittles", "Jelly Beans"],

}

number = candy_jar["number of pieces"]
candy_type = candy_jar["candy type"]
turns = candy_jar["number of turns"]
jar_size = candy_jar["jar size"]
pick_candy = candy_jar["candy type"][random.randint(0, 2)]

def remove_lid():
    #for however many turns the jar takes, print "turning..." wait, and then loop again
    for i in range(turns):
        print("turning...")
        sleep(1)
    print("*Pop!*")
    sleep(1)

def describe_jar():
    #expressing commas in the number of pieces
    comma_number = "{:,}".format(number)
    print(f"This {jar_size} jar has {comma_number} {pick_candy}.")

def guess_count():
    while True:
        try:
            #taking input from the user and removing the comma if needed.
            guess = input(f"How many {pick_candy} pieces are in the jar?")
            intguess = guess.replace(",","")
            #get a positive integer representing the difference between the total and the user's guess
            difference = number-int(intguess)
            #condition statements
            if difference == 0:
                print("congratulations!")
                break
            elif difference > 0:
                print("Too low!")
            elif difference < 0:
                print("too high!")
                #backup code:
                #print(f"you underestimated by {difference} pieces, there were {number} in total!")
        except ValueError as error:
                print("You can't do that!")
                break

def get_random_candy():
    #this is to get a random color of a random candy
    print(pick_candy)


remove_lid()
guess_count()
describe_jar()
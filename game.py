##this is the adventure game (very short)

def game(): 
    q1 = input("Welcome to the World of Helirma!!!! Would you like to start your new fantasy adventure? (y/n) ").lower()        

    if q1 == "y":
        print("Great!! Let's us begin!!")
    elif q1 == "n":
        print("TOO BAD, YOU FUCKING PUSSY!!!!")
        return game()

    q2 = input("You have spawn in front of a dungeon. Do you want to go in? (y/n) ").lower()

    if q2 == "y":
        print("It is too dark for you to see. You steped onto a trap and fell into a endless deep hole. YOU DIED!!!")
        return game()
    elif q2 == "n":
        print("You chose to look around ... (15 min later) ... you saw a castle.")

    q3 = input("Do you go toward the castle? (y/n) ").lower()

    if q3 == "y":
        print("The guards outside of the castle saw you and start to yell at you but with a language you never heard of from Earth.")
    elif q3 == "n":
        print("Couple of gobins with daggers saw you and jumped on you and stabbed you to death!!!")
        return game()

    q4 = input("You saw couple of gobins running toward you. Do you run toward the castle as fast as you can? (y/n) ").lower()

    if q4 == "y":
        print("Guards run toward the gobins with their spears and swords. They killed all the gobins and YOU because you look ugly as FUCK and SHORT as FUCK!!! LOL!!!")
    elif q4 == "n":
        print("You started running but you are too slow. Gobins with daggers jumped on you and stabbed you to death!!!")
        return game()


game()


#Библиотека для настоящих Boss of this GYM
print("Библиотека успешно импортирована")
#Ван - лезерман
Van = "Leatherman"

#Билли, небеса тебе пухом...
Billy = "Boss of this gym"

#Все те, кто находится в Gym
Gym = ["Billy Herrighton", "Slave", "Slave", "Slave", "Slave", "Fucking Slave"]

#Все те, кто находится в Dungeon
Dungeon = ["Van Darkholme", "Fucking Slave", "Fucking Slave", "LeatherMan"]

Gachi = print

fuckyou = input

#Mini-game ################
def Yes_Sir():
    Ready = input("You ready to start game? ('Oh, Yes Sir!' or 'Fuck You') \n")
    if Ready == "Oh, Yes Sir!":
        zzz = input("Ok, first question. When Billy died? (number year) \n")
        if zzz == "2018":
            Gachi("You are right!")
            zzzz = input("Next question. Van have twitch account? (Yes or No)")
            if zzzz == "Yes":
                Gachi("You are right!")
                Gachi("This is all.")
            else:
                Gachi("Nope, Van played Minecraft in twitch")
        else:
            Gachi("Nope.")
    elif Ready == "Fuck You":
        Gachi("Fuck you too")
    else:
        Gachi("You are not.")
        Yes_Sir()
###########################

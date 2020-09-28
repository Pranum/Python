# #snake water gun


import random
list=["s","w","g"]

chance=10
no_of_chance=0
user_point=0
bot_point=0


print("\t\t\t\t\t\t\t Snake Water and Gun game\n")
print("s for snake\nw for water\ng for gun\n")

while no_of_chance < chance:
    user=input('Snake, Water, gun:')
    _random=random.choice(list)
    if user==_random:
        print("Tie 0 point to both\n")
    elif user=="s" and _random=="w":
        user_point=user_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("user wins 1 point\n")
        print(f"user point:{user_point} and bot point:{bot_point}")
    elif user=="s" and _random=="g":
        bot_point=bot_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("bot wins 1 point\n")
        print(f"user point:{user_point} and bot point{bot_point}\n")
    elif user=="w" and _random=="g":
        user_point=user_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("user wins a point")
        print(f"user point:{user_point} and bot point:{bot_point}")
    elif user=="w" and _random=="s":
        bot_point=bot_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("bot wins 1 point")
        print(f"user point:{user_point} and bot point:{bot_point}")
    elif user=="g" and _random=="s":
        user_point=user_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("user wins 1 point")
        print(f"user point:{user_point} and bot point{bot_point}")
    elif user=="g" and _random=="w":
        bot_point=bot_point+1
        print(f"user guess {user} and bot guess {_random}\n")
        print("bot wins 1 point")
        print(f"user point:{user_point} and bot point:{bot_point}")

    else:
        print("invalid input\n")
        continue



    no_of_chance = no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

print("Game Over")
if user_point==bot_point:
    print("TIE")

elif user_point>bot_point:
    print("user wins")
else:
    print("bot wins")

# else:
#     print("draw")

print(f"user point is{user_point} and bot point is{bot_point}")




name = input("type your name: ")
print("Welcome",name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?"  ).lower()
if answer == "left":
   answer == input("You come to a river, you can walk around it or you can swim across? Type walk to walk around amd swim to swim across: ").lower()

   if answer == "swim":
       print("You swim across and were eaten by an alligator")
   elif answer == "walk":
       print("You walked for many meters , ran out of water and you lost the game")
   else:
       print('not a valid option.You lose.')
elif answer == "right":
     answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back?")
     
     if answer == "back":
       print("You go back to main road and lose")
     elif answer == "cross":
       answer = input("You cross the bridge and talk to a gatekeeper(yes/no)")
       
       if answer == "yes":
           print("You ask permission to gatekeeper and he allowed and you win")
       elif answer == "no":
          print("You cant enter as if gatekeeper not allowed and you lost")
       else:
          print('not a valid option.You lose.')

     
     else:
       print('not a valid option.You lose.')
else:
    print('Not a valid option, You loss.')

print("Thankyou for trying",name )
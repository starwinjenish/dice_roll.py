import random
while True:
 user_choice = input("Roll The Dice? (y/n): ").lower()
 if user_choice == "y":
      roll1 = random.randint(1,6)
      roll2 = random.randint(1,6)
      print(f"{roll1} , {roll2}")   
 elif user_choice in "n" == "n":
         print("thank for playing".capitalize())
         break
 else:
         print("invalid choice!".capitalize())


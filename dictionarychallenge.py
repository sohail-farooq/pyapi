#!/usr/bin/env python3
  
superhero= {"batman": {"superpower": "I am Rich", "strength": "batmobile"}}

answer= " "

while answer != "q":
        try:
                char_name= input("Which is your favorite character? (Batman)")
                char_stat= input("What would you like to know? (Superpower or Strength)")

                print(f"{char_name} {char_stat} is: {superhero[char_name][char_stat]}")
                print("correct!!")

#answer= input("choose another superhero?")

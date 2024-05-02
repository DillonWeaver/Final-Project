import turtle
import random
from time import sleep

def printspeed(text):
   for e in text:
      print(e, end="", flush=True)
      sleep(0.05)
   print()
   
def main():
    printspeed("Welcome to the Digital Art Museum presneted by Turtle!")
    printspeed("Here you will see beautiful recreations of the world's most iconic paintings.")
    while True:
       art = int(input("Pick which painting you wish to see (1, 2 ,3 ,4, 5, 6 for a random painting or 7 to quit!): "))

       if art == 1:
          printspeed("Mona Lisa function called")
       elif art == 2:
          printspeed("Starry Night function called")
       elif art == 3: 
          printspeed("Girl with a Pearl Earring function called")
       elif art == 4:
          printspeed("Scream function called")
       elif art == 5:
          printspeed("American Gothic function called")
       elif art == 6:
          printspeed("Random function called")
       elif art == 7:
          printspeed("Thanks for visiting the Digital Art Museum,")
          printspeed("Hope to see you again soon!")
          break
       else:
          printspeed("Whoops! Invalid pick, chose again!")

#Next time add more information and set up functions for the paintings. also add the random system

if __name__ == "__main__":
    main()
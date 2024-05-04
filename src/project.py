import turtle
import random
from time import sleep

def randomart(number):
   idx = random.randrange(len(number))
   return number[idx]

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
       numbers = (1, 2, 3, 4, 5)

       if art == 1:
          printspeed("The Mona Lisa, the world's most famous painting!")
          printspeed("10 Million people a year travel to see this iconic artwork.")
          printspeed("The lady in the painting was a real woman named Lisa del Giocondo.")
          printspeed("Although Leonardo da Vinci is most known for the Mona Lisa, it one of a very few amount of paintings he ever made.")
       elif art == 2:
          printspeed("Van Gogh's classic work, The Starry Night!")
          printspeed("The famous artist painted this masterpiece from a room in the Saint-Paul Asylum in 1889.")
          printspeed("The giant black triangle in the center of the painting is actually a stylized cyprus tree.")
          printspeed("Van Gogh could barely afford to paint at the time, but now The Starry Night is valued at almost 100 million dollars.")
       elif art == 3: 
          printspeed("The Girl with a Pearl Earring, a classic dutch work by painter Johannes Vermeer.")
          printspeed("Before becomming a classic, this painting was once lost for over 200 years!")
          printspeed("The painting is a style of dutch painting called a Tronie, where human facial expressions are the primary focus.")
          printspeed("Unlike the Mona Lisa, nobody knows who the girl in the painting is.")
       elif art == 4:
          printspeed("Edvard's Munch's iconic yet unsettling artwork, The Scream!")
          printspeed("This painting is inspired by actual anxiety and panic attacks Munch had at the time.")
          printspeed("Munch made multiple versions of The Scream that are on display in multiple museums.")
          printspeed("The original Scream painting has been stolen twice! Once in 1994 and again in 2004.")
       elif art == 5:
          printspeed("American Gothic, the defining work of Grant Wood.")
          printspeed("Wood was inspired to create this painting after seeing a house in Iowa that looked almost like a church.")
          printspeed("Relative of Wood say he intended the people in the painting not to be husband and wife, but a father and daughter.")
          printspeed("This painting is known for being a commentary on the preservation of the old culture of the midwest clashing with the new image of Modern America.")
       elif art == 6:
          printspeed("Random selected, generating random painting.....")
          randomart(numbers)
       elif art == 7:
          printspeed("Thanks for visiting the Digital Art Museum,")
          printspeed("Hope to see you again soon!")
          break
       else:
          printspeed("Whoops! Invalid input, choose again!")


if __name__ == "__main__":
    main()
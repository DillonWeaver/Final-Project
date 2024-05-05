import random
from time import sleep
from PIL import Image

def monalisa():
   filename = "emojilisa.png"
   img = Image.open(filename)
   img.show()
   printspeed("The Mona Lisa, the world's most famous painting!")
   printspeed("10 Million people a year travel to see this iconic artwork.")
   printspeed("The lady in the painting was a real woman named Lisa del Giocondo.")
   printspeed("Although Leonardo da Vinci is most known for the Mona Lisa, it one of a very few amount of paintings he ever made.")
   printspeed("👩‍🦱")
   img.close()

def starrynight():
   filename = "emojinight.png"
   img = Image.open(filename)
   img.show()
   printspeed("Van Gogh's classic work, The Starry Night!")
   printspeed("The famous artist painted this masterpiece from a room in the Saint-Paul Asylum in 1889.")
   printspeed("The giant black triangle in the center of the painting is actually a stylized cyprus tree.")
   printspeed("Van Gogh could barely afford to paint at the time, but now The Starry Night is valued at almost 100 million dollars.")
   printspeed("🌠🌙")
   img.close()

def pearlearring():
   filename = "emojiearring.png"
   img = Image.open(filename)
   img.show()
   printspeed("The Girl with a Pearl Earring, a classic dutch work by painter Johannes Vermeer.")
   printspeed("Before becomming a classic, this painting was once lost for over 200 years!")
   printspeed("The painting is a style of dutch painting called a Tronie, where human facial expressions are the primary focus.")
   printspeed("Unlike the Mona Lisa, nobody knows who the girl in the painting is.")
   printspeed("👩‍🦳◽")
   img.close()

def scream():
   filename = "emojiscream.png"
   img = Image.open(filename)
   img.show()
   printspeed("Edvard's Munch's iconic yet unsettling artwork, The Scream!")
   printspeed("This painting is inspired by actual anxiety and panic attacks Munch had at the time.")
   printspeed("Munch made multiple versions of The Scream that are on display in multiple museums.")
   printspeed("The original Scream painting has been stolen twice! Once in 1994 and again in 2004.")
   printspeed("😱")
   img.close()

def gothic():
   filename = "emojigothic.png"
   img = Image.open(filename)
   img.show()
   printspeed("American Gothic, the defining work of Grant Wood.")
   printspeed("Wood was inspired to create this painting after seeing a house in Iowa that looked almost like a church.")
   printspeed("Relative of Wood say he intended the people in the painting not to be husband and wife, but a father and daughter.")
   printspeed("This painting is known for being a commentary on the preservation of the old culture of the midwest clashing with the new image of Modern America.")
   printspeed("🧓👴")
   img.close()


def randomart(painting):
   painting = [monalisa, starrynight, pearlearring, scream, gothic]
   idx = random.randrange(len(painting))
   return painting[idx]

def printspeed(text):
   for e in text:
      print(e, end="", flush=True)
      sleep(0.05)
   print()
   
def main():
    printspeed("Welcome to the 🖌🖼🖋 EMOJI ART MUSEUM! 🖌🖼🖋")
    printspeed("Here you will see some of the world's most iconic paintings recreated entirely through emojis! 😀")
    while True:
       art = int(input("Pick which painting you wish to see (1, 2 ,3 ,4, 5, 6 for a random painting or 7 to quit!): "))

       if art == 1:
          monalisa()
       elif art == 2:
          starrynight()
       elif art == 3: 
          pearlearring()
       elif art == 4:
          scream()
       elif art == 5:
          gothic()
       elif art == 6:
          printspeed("Random selected, generating random painting 😎 .....")
          randomart()
       elif art == 7:
          printspeed("Thanks for visiting the Digital Art Museum,")
          printspeed("Hope to see you again soon! 😄✋")
          break
       else:
          printspeed("Whoops! Invalid input 😯 choose again!")


if __name__ == "__main__":
    main()
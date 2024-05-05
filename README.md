# The Digital Emoji Art Museum

## Demo
Demo Video: https://youtu.be/LqlrU1SbjMk

## GitHub Repository
GitHub Repo: https://github.com/DillonWeaver/Final-Project

## Description

The Digital Emoji Art Museum is an interactive experience entirely within python that allows the user to explore through recreations of class artwork re-made entirely through emojis!
This program utilizes images, custom string operations, and detailed input systems to give the user full control over being immersed in this stage of creativity.
Other than just python itself, all one would need to fully operate this program are importing random, time and pillow with necessary installations along with each image file used in the museum.

Running the program greets you with a joyful introduction and explanation to the Digital Emoji Art Museum along with asking for an input of a number 1 through 7.
The paintings in the program are identified through numbers, 1 is the Mona Lisa, 2 is The Starry Night, 3 is Girl with a Peal Earring, 4 is The Scream and 5 is American Gothic, all recreated entirely with emojis.
Option 6 allows for you to randomly choose any of the paintings, with a string announcing the randomizer before you get your result. 7 closes the program with a proper sign off message.
Any other input in the program will result in a response telling the user they had an invalid input and to try again. 
Once a painting is generated, it is accompained by strings detailing the real life painting and artist along with three interesting facts regarding each piece.
The combination of user control over what they see along with special information regarding each artwork transforms this program into an earnest recreation of an actual museum.

The project file contains the PNG files for each artwork so they tie to their place in the program.
The requirements.txt file lists the required libraries needed for importing or installation in order for the project to work.
The main file is the project.py, which contains all the code which operates the program itself.
The Artworks class contains the function tied to each emoji painting, opening the image along with printing the strings additional information.
Option six's randomizer is stored in the randomart function, and the printspeed function controls the speed at which every printed line in the museum is segmented to. 
Finally, the main function of the program stores the strings for the opening, closing, random and invalid input statements along with storing and delivering the user inputs to call for each painting in Artworks. 

Potential additions to this program would focus whole heartedly on improving the flair and cohesion of the user experience, such as a more vibrant terminal display of information or an improved way of presenting each artwork.
Hope you enjoy exploring and learning through the wonders of classical art reframed in a unique, emoji-fied way!

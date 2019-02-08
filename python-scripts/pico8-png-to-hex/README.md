# Pico-8 Png-to-Hex Converter <img src="https://github.com/bretlinne/Linne-Dev-Prod/blob/master/resources/pico8.png" alt="drawing" width="64"/> 


[Pico-8 Website](https://www.lexaloffle.com/pico-8.php "Go get Pico-8--only $15!")

<!---alternative way to display image using github markdown:--->

<!---![pico8](https://github.com/bretlinne/Linne-Dev-Prod/blob/master/resources/pico8.png)--->

## Purpose
This script stretches the limits of the Pico-8's graphic capabilities.  
Only 256 8x8 pixel sprite tiles can be created and stored in the IDE.  This is 
what we must use to contstruct **EVERYTHING** in the game.  

However, the draw function of the Pico-8 can also draw directly from string data
in the right format if kajiggered properly.  

**That's what this project does.**

## Usage
1) Download the repo
2) Test it using 'python pico8-png-to-hex.py ./p8Test.png'
3) it should spit out a string like so: '0123456789abcdef'
4) this would be copied and then pasted into the Pico-8 for usage in 
...a draw function.  I've included an example draw function in the HELP
...and an example of how to build a data structure to store this data.

The executable: 
## Background
The Pico-8 is a fantasy console and IDE.  It emulates a console like a GameBoy 
color which **_could_** have existed in the 90's or so, but was never actually 
created.  This system is **very** restrained in its capabilities.  

* only 16 colors
* only 256 8x8 tiles of sprite storage
* only 7 input buttons (d-pad, buttonX, button Z, and a start button)
* whole thing is restrained to 32Kb of memory per game!

Within these limits, a great deal can be done and it's a fantastic little game engine
to learn to build games or prototype ideas.

## Palette - **IMPORTANT!**
To convert a .png file to a string of hex characters the Pico-8 can understand, 
you must author it using the EXACT hexadecimal color codes which correspond to
the system's 16-color palette.  

As long as the png is authored in these specific 16 colors, this script will work.

## Why?
Using this, you can start embedding larger graphics into the pico-8's code
which don't use up the very limited sprite real estate.  For instance a title
image which might be 8 tiles wide and 6 tiles high would take up 48 of your 
256 total tiles!  If you encode the png into a data string, you just drop it 
into a data struct within the code and create a draw function to parse it.

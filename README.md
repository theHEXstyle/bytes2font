# bytes2font
This small python scripts takes a .cpp binary that contains a font (usually required for rendering text on a screen for microcontrollers such as arduino, esp32, etc...) and creates a image of all the fonts
---
The concept is to assess a priory how a binary font file is rendered before using it in your project.

Opposite of this project can be found with [font2bytes](https://github.com/theHEXstyle/font2bytes) to create a .cpp file from a font one.

---
## Usage:
1. Simply put the .cpp file in the input folder
2. update the code with:
    * your file name 
    * font width (not size): how many pixels is each font line composed of (should be written in the .cpp file)
3. run, and get the .png file in the output foler


# Title: Project1.py
# Abstract: Reads the path of a few images, than offers the possibility to remove the
#           unwanted object from it using the median and the average method. Morover,
#           offers the grayscale and the evil red filter.
# PS: to successfully update the path, you need to choose a valid path.
# Author: Leticia Domingues
# GitHub Repo: https://github.com/leticiaDomingues/CST205Proj1
# Group E -  Team 21


#imports Java Swing and Awt, to make the GUI
from javax.swing import JButton, JFrame, JPanel, JLabel
from java.awt import Component, GridLayout, FlowLayout

#creates a list of pictures, with the path to all 9 pictures
path = "/Users/leticiadomingues/Documents/CSUMB/MultimediaDesignAndProgramming/CST205Proj1/Images/"
pics = [makePicture(path+"1.png"),makePicture(path+"2.png"),makePicture(path+"3.png"),
        makePicture(path+"4.png"),makePicture(path+"5.png"),makePicture(path+"6.png"),
        makePicture(path+"7.png"),makePicture(path+"8.png"),makePicture(path+"9.png")]

#get the width and height from the pictures
width = getWidth(pics[0])
height = getHeight(pics[0])

#create an empty picture to be the final one
finalPic = makeEmptyPicture(width, height)


#action for the click in the "median method" button
class MedianAction(awt.event.ActionListener):
    def actionPerformed(self,event):
      #runs through the pixels of the picture
      for y in range(0,height):
        for x in range(0,width):
          #gets the pixel in the coordinate (x,y) from the 9 pictures and creates a list with all of them
          pixels = [getPixel(pics[0],x,y),getPixel(pics[1],x,y), getPixel(pics[2],x,y),getPixel(pics[3],x,y),
                    getPixel(pics[4],x,y),getPixel(pics[5],x,y), getPixel(pics[6],x,y),getPixel(pics[7],x,y),
                    getPixel(pics[8],x,y)]
          
          #creates a list with the blue values of the pixels in the pixels list
          bluePixels = [getBlue(pixels[0]),getBlue(pixels[1]), getBlue(pixels[2]),getBlue(pixels[3]),
                        getBlue(pixels[4]),getBlue(pixels[5]), getBlue(pixels[6]),getBlue(pixels[7]),
                        getBlue(pixels[8])]
                        
          #creates a list with the red values of the pixels in the pixels list
          redPixels = [getRed(pixels[0]),getRed(pixels[1]), getRed(pixels[2]),getRed(pixels[3]),
                       getRed(pixels[4]),getRed(pixels[5]), getRed(pixels[6]),getRed(pixels[7]),
                       getRed(pixels[8])]

          #creates a list with the green values of the pixels in the pixels list
          greenPixels = [getGreen(pixels[0]),getGreen(pixels[1]), getGreen(pixels[2]),getGreen(pixels[3]),
                         getGreen(pixels[4]),getGreen(pixels[5]), getGreen(pixels[6]),getGreen(pixels[7]),
                         getGreen(pixels[8])]
    
          #sorts all 3 lists of colors, so we can take the median value
          bluePixels = sorted(bluePixels)
          redPixels = sorted(redPixels)
          greenPixels = sorted(greenPixels)

          
          #creates a new empty pixel in the coordinate (x,y) in the final picture
          pixel = getPixel(finalPic,x,y)
          #creates a new color for the pixel, using the median value for red, green and blue
          newColor = makeColor(redPixels[4], greenPixels[4], bluePixels[4])
          setColor(pixel,newColor)
      #show the final picture to the user    
      show(finalPic)
      repaint(finalPic)

#action for the click in the "average method" button
class AverageAction(awt.event.ActionListener):
    def actionPerformed(self,event):
      #runs through the pixels of the picture
      for y in range(0,height):
        for x in range(0,width):
          #gets the pixel in the coordinate (x,y) from the 9 pictures and creates a list with all of them
          pixels = [getPixel(pics[0],x,y),getPixel(pics[1],x,y), getPixel(pics[2],x,y),getPixel(pics[3],x,y),
                    getPixel(pics[4],x,y),getPixel(pics[5],x,y), getPixel(pics[6],x,y),getPixel(pics[7],x,y),
                    getPixel(pics[8],x,y)]
          
          #calculates the average value of the blue pixels from the pixels list
          avgBluePixels = (getBlue(pixels[0]) + getBlue(pixels[1]) + getBlue(pixels[2]) + getBlue(pixels[3]) +
                           getBlue(pixels[4]) + getBlue(pixels[5]) + getBlue(pixels[6]) + getBlue(pixels[7]) +
                           getBlue(pixels[8]))/9
                        
          #calculates the average value of the red pixels from the pixels list
          avgRedPixels = (getRed(pixels[0]) + getRed(pixels[1]) + getRed(pixels[2]) + getRed(pixels[3]) +
                          getRed(pixels[4]) + getRed(pixels[5]) + getRed(pixels[6]) + getRed(pixels[7]) +
                          getRed(pixels[8]))/9

          #calculates the average value of the green pixels from the pixels list
          avgGreenPixels = (getGreen(pixels[0]) + getGreen(pixels[1]) + getGreen(pixels[2]) + getGreen(pixels[3]) +
                            getGreen(pixels[4]) + getGreen(pixels[5]) + getGreen(pixels[6]) + getGreen(pixels[7]) +
                            getGreen(pixels[8]))/9
    
          #creates a new empty pixel in the coordinate (x,y) in the final picture
          pixel = getPixel(finalPic,x,y)
          #creates a new color for the pixel, using the average value for red, green and blue
          newColor = makeColor(avgRedPixels, avgGreenPixels, avgBluePixels)
          setColor(pixel,newColor)
      #show the final picture to the user    
      show(finalPic)
      repaint(finalPic)

#action for the click in the "grayscale" button, which executes the median method and then the grayscale
class GrayscaleAction(awt.event.ActionListener):
    def actionPerformed(self,event):
      #runs through the pixels of the picture
      for y in range(0,height):
        for x in range(0,width):
          #gets the pixel in the coordinate (x,y) from the 9 pictures and creates a list with all of them
          pixels = [getPixel(pics[0],x,y),getPixel(pics[1],x,y), getPixel(pics[2],x,y),getPixel(pics[3],x,y),
                    getPixel(pics[4],x,y),getPixel(pics[5],x,y), getPixel(pics[6],x,y),getPixel(pics[7],x,y),
                    getPixel(pics[8],x,y)]
          
          #creates a list with the blue values of the pixels in the pixels list
          bluePixels = [getBlue(pixels[0]),getBlue(pixels[1]), getBlue(pixels[2]),getBlue(pixels[3]),
                        getBlue(pixels[4]),getBlue(pixels[5]), getBlue(pixels[6]),getBlue(pixels[7]),
                        getBlue(pixels[8])]
                        
          #creates a list with the red values of the pixels in the pixels list
          redPixels = [getRed(pixels[0]),getRed(pixels[1]), getRed(pixels[2]),getRed(pixels[3]),
                       getRed(pixels[4]),getRed(pixels[5]), getRed(pixels[6]),getRed(pixels[7]),
                       getRed(pixels[8])]

          #creates a list with the green values of the pixels in the pixels list
          greenPixels = [getGreen(pixels[0]),getGreen(pixels[1]), getGreen(pixels[2]),getGreen(pixels[3]),
                         getGreen(pixels[4]),getGreen(pixels[5]), getGreen(pixels[6]),getGreen(pixels[7]),
                         getGreen(pixels[8])]
    
          #sorts all 3 lists of colors, so we can take the median value
          bluePixels = sorted(bluePixels)
          redPixels = sorted(redPixels)
          greenPixels = sorted(greenPixels)
          
          #calculates the new RGB value
          newValue = (redPixels[4] + greenPixels[4] + bluePixels[4])/3
   
          #creates a new empty pixel in the coordinate (x,y) in the final picture
          pixel = getPixel(finalPic,x,y)
          #creates a new color for the pixel, using the new RGB value
          newColor = makeColor(newValue, newValue, newValue)
          setColor(pixel,newColor)
      #show the final picture to the user    
      show(finalPic)
      repaint(finalPic)

#action for the click in the "Evil Red" button
class EvilRedAction(awt.event.ActionListener):
    def actionPerformed(self,event):
      #runs through the pixels of the picture
      for y in range(0,height):
        for x in range(0,width):
          #gets the pixel in the coordinate (x,y) from the 9 pictures and creates a list with all of them
          pixels = [getPixel(pics[0],x,y),getPixel(pics[1],x,y), getPixel(pics[2],x,y),getPixel(pics[3],x,y),
                    getPixel(pics[4],x,y),getPixel(pics[5],x,y), getPixel(pics[6],x,y),getPixel(pics[7],x,y),
                    getPixel(pics[8],x,y)]
          
          #creates a list with the blue values of the pixels in the pixels list
          bluePixels = [getBlue(pixels[0]),getBlue(pixels[1]), getBlue(pixels[2]),getBlue(pixels[3]),
                        getBlue(pixels[4]),getBlue(pixels[5]), getBlue(pixels[6]),getBlue(pixels[7]),
                        getBlue(pixels[8])]
                        
          #creates a list with the red values of the pixels in the pixels list
          redPixels = [getRed(pixels[0]),getRed(pixels[1]), getRed(pixels[2]),getRed(pixels[3]),
                       getRed(pixels[4]),getRed(pixels[5]), getRed(pixels[6]),getRed(pixels[7]),
                       getRed(pixels[8])]

          #creates a list with the green values of the pixels in the pixels list
          greenPixels = [getGreen(pixels[0]),getGreen(pixels[1]), getGreen(pixels[2]),getGreen(pixels[3]),
                         getGreen(pixels[4]),getGreen(pixels[5]), getGreen(pixels[6]),getGreen(pixels[7]),
                         getGreen(pixels[8])]
    
          #sorts all 3 lists of colors, so we can take the median value
          bluePixels = sorted(bluePixels)
          redPixels = sorted(redPixels)
          greenPixels = sorted(greenPixels)

          
          #creates a new empty pixel in the coordinate (x,y) in the final picture
          pixel = getPixel(finalPic,x,y)
          #creates a new color for the pixel, using the median value for red, green and blue
          newColor = makeColor(redPixels[8], redPixels[4], redPixels[4])
          setColor(pixel,newColor)
      #show the final picture to the user    
      show(finalPic)
      repaint(finalPic)

#action for the click in the "Change Path" button
class ChangePathAction(awt.event.ActionListener):
    def actionPerformed(self,event):
      path = pickAFolder()
      pics = [makePicture(path+"1.png"),makePicture(path+"2.png"),makePicture(path+"3.png"),
              makePicture(path+"4.png"),makePicture(path+"5.png"),makePicture(path+"6.png"),
              makePicture(path+"7.png"),makePicture(path+"8.png"),makePicture(path+"9.png")]
      lblPath.setText("Path:  " + path)
              
#creates the main frame
frame = JFrame("CST205 - Project 1", size = (800, 180))

#creates the button panel, which will have the 4 buttons
buttonPanel = JPanel(GridLayout(1,4))
button1 = JButton('Median Method')
button1.addActionListener(MedianAction())
button2 = JButton('Average Method')
button2.addActionListener(AverageAction())
button3 = JButton('Grayscale')
button3.addActionListener(GrayscaleAction())
button4 = JButton('Evil Red')
button4.addActionListener(EvilRedAction())

#adds the buttons to the button panel
buttonPanel.add(button1)
buttonPanel.add(button2)
buttonPanel.add(button3)
buttonPanel.add(button4)

#creates the part where the user can change the images path
lblPath = JLabel("Path:  " + path)
btnChangePath = JButton('Change')
btnChangePath.addActionListener(ChangePathAction())
pathPanel = JPanel(FlowLayout())
pathPanel.add(lblPath)
pathPanel.add(btnChangePath)

#creates the main panel, which will have the button panel and the path panel
mainPanel = JPanel(GridLayout(2,1))
mainPanel.add(pathPanel)
mainPanel.add(buttonPanel)

#add the panel to the main frame
frame.add(mainPanel)
frame.visible = True
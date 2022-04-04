#evanpark_Cam_Visual.py

#Goal: Dipslay a cam static image that can be saved or display an animation of the cam rotating

#Input: Takes in passedInDataPoints(all of the kinematic values of the follower for each angle), unitString (units),
#rotationalW (angular velocity), and the modeType ("Image" or "Animation")

#Output/Methods: windowSetUp, canvasCreate, staticImage, dynamicImage, playAgain, saveStatic, quitProgram, drawCam

#libaries needed: tkinter, datetime, math, PIL (Pillow - Must be PIP Installed), ghostscript (needed for Pillow - Must be PIP Installed)
#Spefic classes/functions needed: asksaveasfilename, datetime, cos, sin, pi, Image

#Additional Notes: In order to save the static image as a PNG file, the following requirements are needed:
    #Ghostscript (AGPL License) needs to be installed (DL Page: https://www.ghostscript.com/download/gsdnld.html)
    #The gs binary file needs to be added to the PATH/Path Folder in the system's environment variables
        #EXAMPLE DIRECTORY THAT NEEDS TO BE ADDED TO PATH FOLDER: C:\Program Files\gs\gs9.50\bin

#If Ghostscript is not installed and added to the PATH/Path Foler, the PNG file cannot be saved, even with the Pillow
#and Ghostscript libraries installed. The Cam can still be properly displayed without the 3rd Party Libraries

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from datetime import datetime
from math import cos, sin, pi

#Try to import Image from PIL
try: 
    from PIL import Image
    #pillowImport gets True if successful
    pillowImport = True
#If it fails to import, execute the following
except:
    #print message that the import has failed
    print("\nFailed to import Pillow Library. Photos will not be able to be exported")
    #pillowImort gets False if it failed
    pillowImport = False

#Try to import ghostscript
try: 
    import ghostscript
    #ghostImport gets True if successful
    ghostImport = True
#If it fails to import, execute the following
except:
    #print message that the import has failed
    print("\nFailed to import Ghostscript Library. Photos will not be able to be exported")
    #ghostImport gets False if it failed
    ghostImport = False

#Define class CamVisual
class CamVisual:
    #initialize the class with input self, passedInDataPoints, unitString, rotationalW, and modeType
    def __init__(self, passedInDataPoints, unitString, rotationalW, modeType):
        #self.camProfileData gets empty list
        self.camProfileData = []
        #self.units gets unitString
        self.units = unitString
        #self.omega gets value of rotationalW
        self.omega = rotationalW
        #self.maxDisplace gets value of -1
        self.maxDisplace = -1
        #for line in passedInDataPoints, loop through
        for line in passedInDataPoints:
            #angle is equal to the 1st item, displacement is equal to the 3rd item
            angle = line[0]
            displacement = line[2]
            #if displacemnt is more than self.maxDisplace, execute the following
            if displacement > self.maxDisplace:
                #self.maxDisplace gets the value of displacement
                self.maxDisplace = displacement
            #add tuple of angle and displacement to the self.camProfileData List
            self.camProfileData.append((angle, displacement))

        #run method self.windowSetUP
        self.windowSetUp()

        #if modeType is "Image", execute the following
        if modeType == "Image":
            #run method self.staticImage
            self.staticImage()
        #elif modeType is "Animation", execute the following
        elif modeType == "Animation":
            #self.playButton gets button on self.frame with text Play Again and commmand self.playAgain
            self.playButton = Button(self.frame, text = "Play Again", command = self.playAgain, height = 1, width = 10)
            #self.playButton is placed on grid at row 0, column 0
            self.playButton.grid(row = 0, column = 0)
            #run method self.dynamicImage
            self.dynamicImage()

        #self.master.mainloop (Loop unitl self.master is destroyed)
        self.master.mainloop()
        #print closing message
        print("\nClosing Visual Display...")

    #define method windowSetUp with input self
    def windowSetUp(self):
        #self.master gets Class Tk()
        self.master = Tk()
        #make the self.master the main window
        self.master.focus_force()
        #send self.master in front of any other windows
        self.master.attributes("-topmost", True)
        #define self.master size as 800x775
        self.master.geometry("800x775")
        #self.master cannot be resized or maximized
        self.master.resizable(False, False)
        #self.master gets the title "Cam Profile Image"
        self.master.title("Cam Profile Image")

        #self.frame gets Frame with parent self.master
        self.frame = Frame(self.master)
        #self.frame is a grid
        self.frame.grid()
        #place self.frame's botoon right corner at 750, 762.5 
        self.frame.place(x = 750, y= 762.5, anchor = "se")

        #run method self.canvasCreate
        self.canvasCreate()

        #self.pixelsOverDistanceRation gets the value of 200 divided by self.maxDisplace
        self.pixelsOverDistanceRatio = 200.0 / self.maxDisplace

        #self.quitButton gets Button on self.frame with text Quit and command quitProgram
        self.quitButton = Button(self.frame, text = "Quit", command = self.quitProgram, height = 1, width = 10)
        #place self.quitButton on the grid at row 0, column 1
        self.quitButton.grid(row = 0, column = 1)

    #define method canvasCreate with Input self
    def canvasCreate(self):
        #self.canvas gets Canvas on parent self.master with width 750 and height 700
        self.canvas = Canvas(self.master, width = 750, height = 700, background = "white")
        #place the canvas's top left corner at 25,25
        self.canvas.place(x = 25, y = 25, anchor = "nw")
        #create a center dot of cam on self.canvas
        self.canvas.create_oval(372, 478, 378, 472, fill = "black")

        #create the shaft in which the follower moves up and down on self.canvas
        self.canvas.create_line(350, 100, 350, 275, fill = "red", width = 5)
        self.canvas.create_line(400, 100, 400, 275, fill = "red", width = 5)
        self.canvas.create_line(350, 275, 300, 275, fill = "red", width = 5)
        self.canvas.create_line(400, 275, 450, 275, fill = "red", width = 5)

        #create the scale of the cam at the top left of the self.canvas
        self.canvas.create_line(25, 25, 225, 25, fill = "black", width = 3)
        self.canvas.create_line(25, 20, 25, 30, fill = "black", width = 3)
        self.canvas.create_line(225, 20, 225, 30, fill = "black", width = 3)
        self.canvas.create_text(125, 50, fill = "black", font = "Times 20 bold", text = ("{:0.2f} {}") .format(self.maxDisplace, self.units))

    #define staticImage with input self
    def staticImage(self):
        #run method camDraw with input 0
        self.camDraw(0)
        #self.saveButton gets Button on self.frame with text Save and command self.saveStatic
        self.saveButton = Button(self.frame, text = "Save", command = self.saveStatic, height = 1, width = 10)
        #place self.saveButton on grid at row 0, column 0
        self.saveButton.grid(row = 0, column = 0)
        #if pillowImport and ghostImport are both true, execute the following
        if pillowImport and ghostImport:
            #do not execute anything
            pass
        #if either one failed, execute the following
        else:
            #disable the self.saveButton
            self.saveButton.config(state = DISABLED)

    #define method dynamicImage with input self
    def dynamicImage(self):
        #disable both the quitButton and playButton
        self.quitButton.config(state = DISABLED)
        self.playButton.config(state = DISABLED)
        #for degVal in range of 0 to 360 (sentry: degVal)
        for degVal in range(0, 360):
            #run method camDraw with input degVal
            self.camDraw(degVal)
            #update the self.canvas
            self.canvas.update()
            #delete the self.followingBar
            self.canvas.delete(self.followingBar)
            #for lineVal in range 0 to 360 (sentry: lineVal)
            for lineVal in range(0, 360):
                #delete the lineVal th element in list allCamLines
                self.canvas.delete(self.allCamLines[lineVal])
        #run method camDraw with input 0
        self.camDraw(0)
        #Enable both the quitButton and playButton
        self.quitButton.config(state = NORMAL)
        self.playButton.config(state = NORMAL)
        
    #define method playAgain with input self
    def playAgain(self):
        #delete the self.followingBar
        self.canvas.delete(self.followingBar)
        #for lineVal in range 0 to 360 (sentry: lineVal)
        for lineVal in range(0, 360):
            #delete the linVal th element in list allCamLines
            self.canvas.delete(self.allCamLines[lineVal])
        #run method self.dynamicImage
        self.dynamicImage()
    
    #define method quitProgram with input self
    def quitProgram(self):
        #destroy self.master
        self.master.destroy()

    #define method saveStatic with input self
    def saveStatic(self):
        
        #try the following code
        try:
            #dialogBox gets the class Toplevel
            dialogBox = Toplevel()
            #hide the Toplevel box that appears
            dialogBox.withdraw()

            #rawDate gets the current time and date
            rawDate = datetime.now()
            #fileImageDefault gets the string with the date and time in the following format
            fileImageDefault = rawDate.strftime("Cam_Profile_Image_%m-%d-%Y_%H-%M-%S.png")
            #filenamePhoto gets the output of asksaveasfilename with intialfile fileImageDefault and defaultextension .png
            filenamePhoto = asksaveasfilename(defaultextension = '.png', initialfile = fileImageDefault, filetypes=[("PNG files (.png)", "*.png")])

            #destroy the dialogBox
            dialogBox.destroy()

        #try the following code if an error occurs
        except:
            #print an error message
            print("\nAn Error has Occured")
            #destroy the dialogBox
            dialogBox.destroy()

        else:
            #if filenamePhoto is empty, execute the following
            if not filenamePhoto:
                #print the message that the user closed the dialog box
                print("\nUser Closed the Dialog Box")

            #else (filenamePhoto is not empty)
            else:
                #try the following code
                try:
                    #update self.canvas
                    self.canvas.update()
                    #temp.eps is create via postscript method
                    self.canvas.postscript(file = "temp.eps", colormode = 'color')
                    #staticImage gets the image opened with via class Image
                    staticImage = Image.open("temp.eps")
                    #staticImage is saved using the absolute path as a PNG file
                    staticImage.save(filenamePhoto, 'png')

                    #print a message that the photo succesfully saved
                    print("\nSuccesfully Wrote {}" .format(filenamePhoto))
                #if WindowsError occurs, execute the following
                except WindowsError:
                    #print message that the binary file needs to be added to the PATH enviornment variables
                    print("\n{} could not be saved because an error has occured: Ensure the ghostscript binary file has been added to the PATH enviornment variables" .format(filenamePhoto))
                #if another error occurs, execute the following
                except:
                    #print an error message
                    print("\n{} could not be saved because an error has occured." .format(filenamePhoto))

    #define method camDraw with input self and zeroAngleLoc
    def camDraw(self, zeroAngleLoc):
        #followerVal gets the value of zeroAngleLoc
        followerVal = zeroAngleLoc
        #zeroAngleLoc gets 360 minus the zeroAngleLoc
        zeroAngleLoc = 360 - zeroAngleLoc
        #if zeroAngleLoc is 360, convert it to 0
        if zeroAngleLoc == 360:
            zeroAngleLoc = 0

        #currentAngle gets the value of 
        currentAngle = 0
        #followerLoc gets the value of the pixel ratio (self.pixelsOverDistanceRatio) times the diplacement of the angle passed in 
        followerLoc = (self.pixelsOverDistanceRatio * self.camProfileData[followerVal][1])

        #self.followingBar is drawn as a line from the point of the cam currently at angle 0 (90 for traditional coordinates) and drawn to be 225 pixels long
        self.followingBar = self.canvas.create_line(375, 475 - followerLoc, 375, 250 - followerLoc, fill = "grey", width = 5)
        
        #self.allCamLines gets empty list of 360 items
        self.allCamLines = [None] * 360
        #for currentAngle in range of 0 to length of self.camProfileData
        for currentAngle in range(len(self.camProfileData)):
            #prevAngle gets currentAngle minus 1
            prevAngle = currentAngle - 1
            #if prevAngle is -1, convert to 359
            if prevAngle == -1:
                prevAngle = 359
        
            #currentAngle Rad converts the currentAngle plus the zeroAngleLoc shift to radians
            currentAngleRad = pi * (currentAngle + zeroAngleLoc) / 180
            #the currentRadius gets the pixel ratio (self.pixelsOverDistanceRatio) times the length value in self.camProfileData for the currentAngle
            currentRadius = self.camProfileData[currentAngle][1] * self.pixelsOverDistanceRatio
            #prevAngleRad converts the PrevAnlge plus the zeroAngleLoc shift to radians
            prevAngleRad = pi * (prevAngle + zeroAngleLoc) / 180
            #the prevRadius gets the pixel ratio (self.pixelsOverDistanceRatio) times the length value in self.camProfileData for the prevAngle
            prevRadius = self.camProfileData[prevAngle][1] * self.pixelsOverDistanceRatio

            #calculates the x and y for the current point and the previous point (use cos for y and sin for x due to the 90 deg shift)
            yCurr = 475 - (cos(currentAngleRad) * currentRadius)
            yPrev = 475 - (cos(prevAngleRad) * prevRadius)
            xCurr = 375 + (sin(currentAngleRad) * currentRadius)
            xPrev = 375 + (sin(prevAngleRad) * prevRadius)
            
            #self.allCamLines[currentAngle] gets the line drawn from the previous point to the current point
            self.allCamLines[currentAngle] = self.canvas.create_line(xPrev, yPrev, xCurr, yCurr, fill = "black", width = 3)

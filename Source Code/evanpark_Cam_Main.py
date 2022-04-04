#evanpark_Cam_Main.py

#Goal: Serve as the primarly function for the Cam analysis program. This file should probably sort the users input so that cam profiles can 
#be manually created or imported form a .txt file. Once the cam profile is successfully created or imported, the logic within this program uses function
#from other programs to either completely preform the user selected function or return the nessicary data that is then prepared within this file

#Input: User Inputs for the menus, the cam profile (imported and/or manually inputted). If manually inputted, angle intervals, type of motion, overall displacement
#angular velocity

#Output: General Information about the Cam, .txt Profile, .cvs of kinematics of the follower, visual display of the needed cam profile, animation of the cam motion

#libaries needed: tkinter, evanpark_Cam_Properties, evanpark_Utilities, time, datetime, os
#Spefic classes/functions needed: Tk, Toplevel, askopenfilename, asksaveasfile, CamProperties, sleep, datetime
from tkinter import Tk, Toplevel
from tkinter.filedialog import askopenfilename, asksaveasfile
from evanpark_Cam_Properties import CamProperties
from evanpark_Utilities import *
from time import sleep
from datetime import datetime
import os


#Main function (Goals, Inputs, Outputs described above)
def main():
    #keepGoing gets True
    keepGoing = True
    #while loop with sentry keepGoing, changes via quit option
    while keepGoing:
        #display first menu via menu1()
        menu1()
        #get the user's input, store to userResp1
        userResp1 = input(" > ")
        #if userResp is "1", execute the following
        if userResp1 == "1":
            #create new profile via createProfile()
            createProfile()

        #elif userResp is "2", execute the following
        elif userResp1 == "2":
            #import profile via importProfile()
            importProfile()

        #elif userResp is 3, execute the following
        elif userResp1 == "3":
            #quit by setting keepGoing to False
            keepGoing = False
        
        #else, execute the following
        else:
            #invalid input, print error message
            print("Error: Invalid Input")


#define function createProfile(Goal: Create a cam profile from scratch. No Inputs passed in. Outputs a Cam profile in the correct format for a later function)
def createProfile():
    #keepGoing2 gets True
    keepGoing2 = True
    #while loop with sentry keepGoing2, exits via valid input
    while keepGoing2:
        #keepGoing2 gets False, anticipating valid input
        keepGoing2 = False
        #print the second menu via function menu2()
        menu2()
        #get user's input, store to userResp2
        userResp2 = input(" > ")
        #if userResp2 is "1", execute the following
        if userResp2 == "1":
            #units gets "cm"
            units = "cm"
        #if userResp2 is "2", execute the following
        elif userResp2 == "2":
            #units gets "m"
            units = "m"
        #if userResp3 is "3", execute the following
        elif userResp2 == "3":
            #units gets "in"
            units = "in"
        #if userResp3 is "4", execute the following
        elif userResp2 == "4":
            #units gets "ft"
            units = "ft"
        #else, execute the following
        else:
            #invalid input, set keepGoing2 to True to loop back through
            keepGoing2 = True
            #print error message
            print("Error: Invalid Input")

    #keepGoing2 gets True
    keepGoing2 = True
    #prompt user for the starting radius of the cam, store to startRadius
    startRadius = input("\nPlease input a positive starting radius ({}):\n > " .format(units))
    #while loop with sentry keepGoing2, changes via valid input
    while keepGoing2:
        #if startRaius is a number (from function isNumber), execute the following
        if isNumber(startRadius):
            #startRadius is converted to a float
            startRadius = float(startRadius)
            #if startRadius is more than 0, execute the following
            if startRadius > 0:
                #keepGoing2 gets False since the input is valid
                keepGoing2 = False
            #else, execute the following
            else:
                #prompt the user for a valid input, store to startRadius
                startRadius = input("\nError: Please input a valid positive starting radius ({}):\n > " .format(units))
        #else, execute the following
        else:
            #prompt the user for a valid input, store to startRadius
            startRadius = input("\nError: Please input a valid positive starting radius ({}):\n > " .format(units))

    #keepGoing2 gets True
    keepGoing2 = True
    #prompt the user for the angular velocity of the cam, store the input to angularW
    angularW = input("\nPlease input a positive rotational speed (rad/s):\n > ")
    #while loop with sentry keepGoing2
    while keepGoing2:
        #if the angularW is a number (from function isNumber), execute the following
        if isNumber(angularW):
            #convert angularW to float
            angularW = float(angularW)
            #if angularW is more than 0, execute the following
            if angularW > 0:
                #keepGoing2 gets False since this is a valid input
                keepGoing2 = False
            #else, execute the following
            else:
                #prompt the user for a valid input, store to angularW
                angularW = input("\nError: Please input a valid positive rotational speed (rad/s):\n > ")
        #else, execute the following
        else:
            #prompt the user for a valid input, store to angularW
            angularW = input("\nError: Please input a valid positive rotational speed (rad/s):\n > ")

    #keepGoing2 gets True
    keepGoing2 = True
    #camDetails gets empty list
    camDetails = []
    #pastAngle gets initial value of 0
    pastAngle = 0
    #loopNum gets initial value of 1
    loopNum = 1
    #currentPosition gets initial value of startRadius
    currentPosition = startRadius
    #while loop with keepGoing2, exits after 360 is entered subsequent information is entered
    while keepGoing2:
        #[startAngle, endAngle, Type of Movement, Change in R] stored to currentLine
        currentLine = [pastAngle, 0, "Type", currentPosition, 0]
        
        #Print Label for the current interval
        print("\nInterval #{}\nNote: Degree inputs must be integer values" .format(loopNum))
        #keepGoing3 gets True
        keepGoing3 = True
        #prompt the user for the end angle of the current interval, store input to finalAngle
        finalAngle = input("Initial Angle for Interval #{1} (deg): {0}\nFinal Angle for Interval #{1} (deg): " .format(pastAngle, loopNum))
        #while loop with sentry keepGoing3, exits on valid input
        while keepGoing3:
            #if finalAnlge is an integer (via function isInteger), execute the following
            if isInteger(finalAngle):
                #if finalAngle is more than the past angle and less than or equal to 360
                if int(finalAngle) > pastAngle and int(finalAngle) <= 360:
                    #keepGoing3 gets false since input is valid
                    keepGoing3 = False
                    #finalAngle is convert to an integer
                    finalAngle = int(finalAngle)
                    #the second item of currentLine gets the value of finalAngle
                    currentLine[1] = finalAngle
                #else, execute the following
                else:
                    #print an error message
                    print("Error: Invalid Input")
                    #prompt the user again for a valid input, store to finalAngle
                    finalAngle = input("Initial Angle for Interval #{1} (deg): {0}\nFinal Angle for Interval #{1} (deg): " .format(pastAngle, loopNum))
            #else, execute the following
            else:
                #print an error message
                print("Error: Invalid Input")
                #prompt the user again for a valid input, store to finalAngle
                finalAngle = input("Initial Angle for Interval #{1} (deg): {0}\nFinal Angle for Interval #{1} (deg): " .format(pastAngle, loopNum))
        
        #if finalAngle is equal to 360, execute the following
        if finalAngle == 360:
            #if the currentPosition is equal to the startRadius, execute the following
            if currentPosition == startRadius:
                #print message explaining that the motion type must be a dwell
                print("\nIn order to maintain cam continuity, interval {} must be a Dwell" .format(loopNum))
                #change Radius gets value of 0
                changeRadius = 0
                #motionType gets "Dwell"
                motionType = "Dwell"
            #else, execute the following
            else:
                #changeRadius gets the value of the startRadius minus the currentPosition
                changeRadius = startRadius - currentPosition
                #print message explaining that the motion type must have a specific rise or run of a specific displacement
                print("\nIn order to maintain cam continuity, interval {} must have a displacement of {} {}" .format(loopNum, changeRadius, units))
                #keepGoing gets value of True
                keepGoing3 = True
                #while loop with sentry of keepGoing3
                while keepGoing3:
                    #keepGoing gets False, with anticipation of valid input
                    keepGoing3 = False
                    #print the paired down motion type menu via menu4() function
                    menu4()
                    #prompt user for input, store to userResp4
                    userResp4 = input(" > ")
                    #if userResp4 is "1", execute the following
                    if userResp4 == "1":
                        #motionType gets "Uniform"
                        motionType = "Uniform"
                    #elif userResp4 is "2", execute the following
                    elif userResp4 == "2":
                        #motionType gets "Parabolic"
                        motionType = "Parabolic"
                    #elif userResp4 is "3", execute the following
                    elif userResp4 == "3":
                        #motionType gets "Harmonic"
                        motionType = "Harmonic"
                    #elif userResp4 is "4", execute the following
                    elif userResp4 == "4":
                        #motionType gets "Cycloidal"
                        motionType = "Cycloidal"
                    #else, execute the following
                    else:
                        #keepGoing3 gets True so that the input loop runs again
                        keepGoing3 = True
                        #print error message
                        print("Error: Invalid Input")
            #keepGoing2 gets false since the values inputted into currentLine later are now all valid
            keepGoing2 = False

        #else (finalAngle is not 360), execute the following
        else:
            #keepGoing3 gets True
            keepGoing3 = True
            #while loop with sentry keepGoing3, exits via valid input
            while keepGoing3:
                #keepGoing3 gets False, anticipates valid input
                keepGoing3 = False
                #print the full motion type menu via function menu3()
                menu3()
                #prompt user for input, store response to userResp3
                userResp3 = input(" > ")
                #if userResp is "1", execute the following
                if userResp3 == "1":
                    #motionType gets "Dwell"
                    motionType = "Dwell"
                #elif userResp is "2", execute the following
                elif userResp3 == "2":
                    #motionType gets "Uniform"
                    motionType = "Uniform"
                #elif userResp3 is "3", execute the following
                elif userResp3 == "3":
                    #motionType gets "Parabolic"
                    motionType = "Parabolic"
                #elif userResp3 is "4", execute the following
                elif userResp3 == "4":
                    #motionType gets "Harmonic"
                    motionType = "Harmonic"
                #elif userResp3 is 5, execute the following
                elif userResp3 == "5":
                    #motionType gets "Cycloidal"
                    motionType = "Cycloidal"
                #else, execute the following
                else:
                    #keepGoing3 gets True, since input is not valid
                    keepGoing3 = True
                    #print error message
                    print("Error: Invalid Input")

            #if the motionType is "Dwell", execute the following
            if motionType == "Dwell":
                #changeRadius gets 0
                changeRadius = 0

            #else (motionType is not "Dwell"), execute the following
            else:
                #keepGoing3 gets True
                keepGoing3 = True
                #propmt the user for the change in radius, store to changeRadius
                changeRadius = input("Current Radius: {1} {0}\nChange in Cam Radius ({0}): " .format(units, currentPosition))
                #while loop with sentry keepGoing3, exits via valid input
                while keepGoing3:
                    #if changeRadius is a number (via function isNumber), execute the following
                    if isNumber(changeRadius):
                        #if the currentPosition plus the changeRadius is more than 0, execute the following
                        if currentPosition + float(changeRadius) > 0:
                            #keepGoing3 gets False since the input is valid
                            keepGoing3 = False
                            #convert changeRadius to a float
                            changeRadius = float(changeRadius)
                        #else, execute the following
                        else:
                            #print an error message
                            print("Error: Invalid Input")
                            #prompt the user again for a valid input
                            changeRadius = input("Current Radius: {1} {0}\nChange in Cam Radius ({0}): " .format(units, currentPosition))
                    #else, execute the following
                    else:
                        #print an error message
                        print("Error: Invalid Input")
                        #prompt the user again for a valid input
                        changeRadius = input("Current Radius: {1} {0}\nChange in Cam Radius ({0}): " .format(units, currentPosition))
        
        #third item of currentLine gets the value of the motionType
        currentLine[2] = motionType
        #fifth (last) item of currentLine gets the value of the changeRadius plus the currentPosition
        currentLine[4] = changeRadius + currentPosition

        #convert currentLine to tuple called currentLineTup
        currentLineTup = (currentLine[0], currentLine[1], currentLine[2], currentLine[3], currentLine[4])
        #append currentLineTup to camDetails
        camDetails.append(currentLineTup)

        #currentPosition now gets the value of the final position from the previous interval
        currentPosition = currentLine[4]
        #pastAngle now gets the value of the finalAngle from the previous interval
        pastAngle = finalAngle
        #inc loopNum
        loopNum = loopNum + 1

    #camInformation gets list of the units and the angularW
    camInformation = [units, angularW]
    
    #run function camAnalysis with the inputs camInformation and camDetails
    camAnalysis(camInformation, camDetails)
    

#define function importProfile(Goal: Create a cam profile from using the information from the file. No Inputs passed in. Outputs a Cam profile in the correct format for a later function)
def importProfile():
    #dialogBox gets the class Tk()
    dialogBox = Tk()
    #dialogBox is the main window/focus via method focus_force()
    dialogBox.focus_force()
    #dialgoBox is sent to the front, on top of any other windows
    dialogBox.attributes("-topmost", True)
    #Tk box is hidden from the user via method withdraw()
    dialogBox.withdraw()
    #the inputFilename gets the result of askopfilename (This prompts the user to pick a .txt file to load in)
    inputFilename = askopenfilename(parent = dialogBox, filetypes = [("Text file (.txt)", "*.txt")])
    
    #try the following
    try:
        #open inputFilename in read mode, set to inputFile
        with open(inputFilename, 'r') as inputFile:
            #read all of the lines from the inputFile, store to inputData as list
            inputData = inputFile.readlines()
            #print messge saying the inputFilename has succesfully been loaded
            print("\nSuccesfully Loaded {}" .format(inputFilename))
        #strippedData gets empty list
        strippedData = []
        #lineNum gets 0
        lineNum = 0
        #close the inputFile
        inputFile.close()
        #for every line in the inputData list, loop through
        for line in inputData:
            #strip the lines of any newlines
            line = line.rstrip()
            #replace any spaces with nothing
            line = line.replace(" ", "")
            #add the line to the list strippedData
            strippedData.append(line)
            #uppercase the entire current line
            line = line.upper()
            #if UNITS appears in the line, execute the following
            if "UNITS" in line:
                #replace any colons with nothing
                line = line.replace(":", "")
                #replace the UNITS with nothing, then lowercase the line. Value gets set to units
                units = line.replace("UNITS", "").lower()
            #elif ROTATIONALSPEED appears in the line, execute the following
            elif "ROTATIONALSPEED" in line:
                #replace any colons with nothing
                line = line.replace(":", "")
                #replace RAD/S with nothing
                line = line.replace("RAD/S", "")
                #replace the ROTATIONALSPEED with nothing, then convert what is left to float and set to angularW
                angularW = float(line.replace("ROTATIONALSPEED", ""))
            #elif CAMDETAILS appears in the line, execute the following
            elif "CAMDETAILS" in line:
                #lineCamDetails gets the value of lineNum plus 1
                lineCamDetails = lineNum + 1
            #inc lineNum
            lineNum = lineNum + 1

        #for loop from 0 to lineCamDetails (sentry is ival)
        for ival in range(lineCamDetails):
            #delete the first item in list strippedData
            del strippedData[0]

        #camDetails gets empty list        
        camDetails = []

        #for each line in strippedData, loop through
        for line in strippedData:
            #lineValues gets list of the line after all of the values seperated by commas have been extracted
            lineValues = line.split(",")
            #currentLinTup gets the values of the lineValues with the first two being converted to integers, the third being in title format, and the last two being made floats
            currentLineTup = (int(lineValues[0]), int(lineValues[1]), lineValues[2].title(), float(lineValues[3]), float(lineValues[4]))
            #add the currentLineTup to the list camDetails
            camDetails.append(currentLineTup)

        #camInformation gets list of units and angularW
        camInformation = [units, angularW]

        #destroy the dialogBox
        dialogBox.destroy()
        #run function camAnalysis with inputs of camInformation and camDetails
        camAnalysis(camInformation, camDetails)

    #if the error FileNotFoundError occurs, execute the following
    except FileNotFoundError:
        #print a message telling the user that the dialog box had been closed
        print("\nUser Closed the Dialog Box")
        #destroy the dialogBox
        dialogBox.destroy()
    #if any other errors occur, execute the following
    except:
        #print a general error message
        print("\nAn Error has Occured")
        #destroy the dialgoBox
        dialogBox.destroy()


#define function camAnalysis (Goal: Provide the need logic to act as a hub for launching functions/methods to preform the task that the user has selected. 
#Inputs passed in: camMotionInfo (Intervals for each motion, type of motion, start and end locations) and camBasicInformation (units and angular velocity)
#Outputs: Changing information such as the units/angular velocity, creating a .txt file for the profle, .cvs file for the follower kinematics, viusal output
#of the cam's shpae, and an animation of the cam rotating 
def camAnalysis(camBasicInformation, camMotionInfo):
    
    #keepGoing4 gets True
    keepGoing4 = True
    #CamP gets class CamProperties with inputs camMotionInfo (list), camBasicInformation[0] (units), and camBasicInformation[1] (angular velocity)
    CamP = CamProperties(camMotionInfo, camBasicInformation[0], camBasicInformation[1])

    #while loop with sentry keepGoing4, changes with quit option
    while keepGoing4:
        #prints menu of options via function menu5()
        menu5()
        #get input from the user, save input to userResp5
        userResp5 = input(" > ")

        #if userResp is "1", execute the following
        if userResp5 == "1":
            #Display Cam Data and Information via method displayInformation in class CamP
            CamP.displayInformation()
            #wait for the user to hit enter to continue 
            try:
                input("Press Enter to Continue: ")
            except:
                pass
        
        #elif userResp5 is "2", execute the following
        elif userResp5 == "2":
            #Update Rotational Speed
            #keepGoing5 gets True
            keepGoing5 = True
            #print newline
            print("\n")
            #while loop with sentry keepGoing5, change via valid input
            while keepGoing5:
                #prompt user for a rotational velocity, store input to rotationalInput
                rotationalInput = input("Input a new valid positive rotational speed (rad/s):\n > ")
                #if rotationalInput is a number (via funciton isNumber), execute the following
                if isNumber(rotationalInput):
                    #set CamP.rotatioalSpeed to float of rotatioalInput
                    CamP.rotationalSpeed = float(rotationalInput)
                    #keepGoing5 gets False since the user's input is valid
                    keepGoing5 = False
                #else, execute the following
                else:
                    #print an error message
                    print("\nError: Invalid Input")

        #elif userResp5 is "3", execute the following
        elif userResp5 == "3":
            #Update Units
            #keepGoing5 gets True
            keepGoing5 = True
            #while loop with sentry keepGoing5, exits with valid input
            while keepGoing5:
                #keepGoing5 gets False for anticipation for valid input
                keepGoing5 = False
                #print menu for units via function menu2()
                menu2()
                #prompt the user for their input, store to unitsInput
                unitsInput = input("Note: This is not a conversion (ie: 1 m changes to 1 cm, not 100 cm)\n > ")
                #if unitsInput is "1", execute the following
                if unitsInput == "1":
                    #CamP.unitsType gets "cm"
                    CamP.unitsType = "cm"
                #elif unitsInput is "2", execute the following
                elif unitsInput == "2":
                    #CamP.unitsType get "m"
                    CamP.unitsType = "m"
                #elif unitsInput is "3", execute the following
                elif unitsInput == "3":
                    #CamP.unitsType gets "in"
                    CamP.unitsType = "in"
                #elif unitsInput is "4", execute the following
                elif unitsInput == "4":
                    #CamP.unitsType gets "ft"
                    CamP.unitsType = "ft"
                #else, execute the following
                else:
                    #keepGoing gets True since the user input was not valid
                    keepGoing5 = True
                    #print an error message to the user
                    print("Error: Invalid Input")

        #elif userResp5 is "4", execute the following
        elif userResp5 == "4":
            #Generate and Save Cam Profile File
            #rawDate gets the current date and time
            rawDate = datetime.now()
            #fileDefault gets the following string containing the date and time
            fileDefault = rawDate.strftime("Cam_Profile_%m-%d-%Y_%H-%M-%S.txt")
            #inFileData gets the following string containing the date and time
            inFileDate = rawDate.now().strftime("Cam Profile: %D %H:%M:%S")
            #textFileBody gets the strings of inFileDate plus CamP.getCamInformation()
            textFileBody = inFileDate + CamP.getCamInformation()
            #dialogBox gets class Tk()
            dialogBox = Tk()
            #dialogBox becomes the main window via method focus_force()
            dialogBox.focus_force()
            #dialogBox is sent to the front of any other windows
            dialogBox.attributes("-topmost", True)
            #hide the Tk box via method withdraw()
            dialogBox.withdraw()
            #try the following
            try:
                #outputFile gets the output of asksaveasfile in write mode, with the intialfile of fileDefault and defaultextension of .txt
                outputFile = asksaveasfile(mode = 'w', initialfile = fileDefault, defaultextension = ".txt", filetypes=[("Text file (.txt)", "*.txt")])
                #write the textFileBody to outputFile
                outputFile.write(textFileBody)
                #close the outputFile
                outputFile.close()
                #print message of succesfully writing the filename to the directory's path
                print("\nSuccesfully Wrote {} to {}" .format(os.path.basename(outputFile.name), os.path.dirname(outputFile.name)))
            #if the error AttributeError occurs, execute the following
            except AttributeError:
                #print message explaining that the user closed the Dialog Box
                print("\nUser Closed the Dialog Box")
            #if another error occurs, execute the following
            except:
                #print message explaining that the file failed to write
                print("\nFailed to Write to File")
            #destroy the dialogBox
            dialogBox.destroy()

        #elif userResp5 is "5", execute the following
        elif userResp5 == "5":
            #Generate and Save Cam Analysis File
            #rawDate gets the current time and date
            rawDate = datetime.now()
            #fileDefault gets the string with the date and time in the following format
            fileDefault = rawDate.strftime("Cam_Analysis_%m-%d-%Y_%H-%M-%S.csv")
            #dialogBox gets class Tk()
            dialogBox = Tk()
            #dialogBox becomes the main window via method focus_force()
            dialogBox.focus_force()
            #send dialogBox to front of any other windows
            dialogBox.attributes("-topmost", True)
            #hide the Tk box from the user
            dialogBox.withdraw()
            #try the following code
            try:
                #outputFile puts the output of asksaveasfile in mode write with initialfile of fileDefault and defaultextension of .csv
                outputFile = asksaveasfile(mode = 'w', initialfile = fileDefault, defaultextension = ".csv", filetypes=[("CSV file (.csv)", "*.csv")])
                #write return of CamP.getAngularDataPointsCSV to outputFile
                outputFile.write(CamP.getAngularDataPointsCSV())
                #close the outputFile
                outputFile.close()
                #print message that the filename was written the to the file directory
                print("\nSuccesfully Wrote {} to {}" .format(os.path.basename(outputFile.name), os.path.dirname(outputFile.name)))
            #if error AttributeError occurs, execute the following
            except AttributeError:
                #print message explaining that the user closed the DialogBox
                print("\nUser Closed the Dialog Box")
            #if any other error occurs, execute the following
            except:
                #print an error message that the file failed to write
                print("\nFailed to Write to File")
            #destroy the dialogBox
            dialogBox.destroy()

        #elif userResp5 is "6", execute the following
        elif userResp5 == "6":
            #Display Mock Cam Profile via method CamP.displayCamVisual()
            CamP.displayCamVisual()

        #elif userResp5 is "7", execute the following
        elif userResp5 == "7":
            #Display Mock Cam animation via method CamP.displayCamVisual()
            CamP.displayCamAnimation()

        #elif userResp5 is "8", execute the following
        elif userResp5 == "8":
            #quit
            #print message that the user is quitting to the main menu
            print("\nQuitting to the main menu...")
            #keepGoing4 gets False so that the loop is exitted
            keepGoing4 = False

        #else, execute the following
        else:
            #print invalid input message
            print("Error: Invalid Input")

        #wait for 0.25 seconds
        sleep(0.25)

#if the file is the main file being run
if __name__ == "__main__":
    #run the main function
    main()
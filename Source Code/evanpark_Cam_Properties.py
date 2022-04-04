#evanpark_Cam_Properties.py

#Goal: Create a class with methods that can set/get the angular velocity and units, get the values needed for the .csv file,
#update the values for each angle from 0 to 359 given changes in angular velcotiy, show the static cam profile, and show an
#animation of the cam rotating

#Input: Takes in camDataAnalysis (motion intervals), unitString (units), and rotatinalW (angular speed)

#Output/Methods: set/get Rotational Speed, set/get Units, get cam basic info, display basic info, get the points for each of the 
#angle points in a format compatible to writing a .csv file, update the angular points value, display the static cam profile, and 
#show an animation of the cam rotating

#libaries needed: math, evanpark_Cam_Visual
#Spefic classes/functions needed: pi, sin, cos, pow, CamVisual
from math import pi, sin, cos, pow
from evanpark_Cam_Visual import CamVisual

#Define Class CamProperties, inherits CamVisual (Info for Class Above)
class CamProperties(CamVisual):
    #initialize the class with inputs self, camDataAnalysis, unitString, rotationalW
    def __init__(self, camDataAnalysis, unitString, rotationalW):
        #self.camData gets the list camDataAnalysis
        self.camData = camDataAnalysis
        #use method self.setRotationalSpeed with input rotationalW
        self.setRotationalSpeed(rotationalW)
        #use method self.setUnits with input unitsString
        self.setUnits(unitString)

    #define method setRotationalSpeed with inputs self, rotSpeed
    def setRotationalSpeed(self, rotSpeed):
        #if the rotSpeed is more than 0, execute the followig
        if rotSpeed > 0:
            #self.__rotationalW gets rotSpeed
            self.__rotationalW = rotSpeed
            #run method self.updateCamData()
            self.updateCamData()
        #elif rotSpeed is equal to 0
        elif rotSpeed == 0:
            #if return of method self.getRotationalSpeed is 0, execute the following
            if self.getRotationalSpeed() == 0:
                #print message explaing that the angular velocity will be set to a different value
                print("\nError: Rotational speed cannot be 0. Setting to 1.0 rad/s" )
                #self.__rotationalW gets 1
                self.__rotationalW = 1
                #run method self.updateCamData()
                self.updateCamData()
            #else, execute the following
            else:
                #print error message
                print("\nError: Rotational speed cannot be 0. Reverting back to {:0.4f} rad/s" .format(self.getRotationalSpeed()))
        #elif rotSpeed is negative, execute the following
        elif rotSpeed < 0:
            #explain that negative rotational speeds cannot be used, value will be made positive
            print("\nError: Rotational speed cannot be negative. Setting Rotational speed to {:0.4f} rad/s" .format((-1.0) * rotSpeed))
            #self.__rotationalW gets -1 times the rotSpeed
            self.__rotationalW = (-1.0) * rotSpeed
            #run method self.updateCamData()
            self.updateCamData()

    #define method getRotatinalSpeed with input self
    def getRotationalSpeed(self):
        #return value of self.__rotationalW
        return self.__rotationalW

    #define method setUnits with input self and units
    def setUnits(self, units):
        #self.__units gets units
        self.__units = units

    #define method getUnits with input self
    def getUnits(self):
        #return value of self.__units
        return self.__units

    #define method getCamInformation with input self
    def getCamInformation(self):
        #camInfoLong gets the string with the labels for units, rotational speed, and CamDetails and units and rotatinal speed value
        camInfoLong = ("\nUnits: {}\nRotational Speed: {} rad/s\n\nCam Details:\n" . format(self.getUnits(), self.getRotationalSpeed()))
        #for 0 to length of self.camData, sentry mVal
        for mVal in range(len(self.camData)):
            #camInfoLong gets camInfoLong plus each of the items in self.camData for line mVal
            camInfoLong = camInfoLong + ("{}, {}, {}, {}, {}\n" .format(self.camData[mVal][0], self.camData[mVal][1], self.camData[mVal][2], self.camData[mVal][3], self.camData[mVal][4]))
        #return the string camInfoLong
        return camInfoLong

    #define method getAngularDataPointsCSV with input self
    def getAngularDataPointsCSV(self):
        #textCSV gets the string for each of the column labels
        textCSV = "Degree, Time, Follower Position, Follower Velocity, Follower Acceleration, Follower Jerk\n"
        #for every line in self.angleDataPoints, loop through
        for line in self.angleDataPoints:
            #itemFirst gets defined as True
            itemFirst = True
            #for each item in line, loop through
            for item in line:
                #if itemFirst is True, execute the following
                if itemFirst:
                    #add value to textCSV
                    textCSV = textCSV + ("{}" .format(str(item)))
                    #itemFirst gets False
                    itemFirst = False
                #else, execute the following
                else:
                    #add value to textCSV with comma in front of it
                    textCSV = textCSV + (", {}" .format(str(item)))
            #add newline to textCSV
            textCSV = textCSV + "\n"

        #return textCSV string
        return textCSV

    #define displayInformation with input self
    def displayInformation(self):
        #print the output of method self.getCamInformation
        print(self.getCamInformation())

    #define updateCamData with input self
    def updateCamData(self):
        #numberMotions gets length of self.camData
        numberMotions = len(self.camData)
        #currentAngle gets value of zero
        currentAngle = 0
        #self.angleDataPoints gets empty list
        self.angleDataPoints = []
        #for mValue in range of 0 to numberMotions (sentry mValue)
        for mValue in range (0, numberMotions):
            #lVal gets value of self.camData[mValue][4] (interval end displacement) minus self.camData[mValue][3] (interval start displacement)
            lVal = float(self.camData[mValue][4]) - float(self.camData[mValue][3])
            #intervalValue gets self.camData[mValue][1] (interval end angle) minus self.camData[mValue][0] (interval start angle)
            intervalValueDeg = float(self.camData[mValue][1] - self.camData[mValue][0])
            #convert intervalValueDeg to radians, set to intervalValueRad
            intervalValueRad = intervalValueDeg * pi / 180.0
            #for currentAngle in range of start angle to final angle of interval (sentry: currentAngle)
            for currentAngle in range (self.camData[mValue][0], self.camData[mValue][1]):
                #thetaOverB gets the currentAngle minus the start Angle divided by the intervalValueDeg
                thetaOverB = float(currentAngle - self.camData[mValue][0])  / intervalValueDeg
                #multiple thetaOverB by Pi, set to thetaOverBPI
                thetaOverBPI = pi * thetaOverB
                #if self.camData[mValue][2] (motion type) in uppercase is "DWELL"
                if self.camData[mValue][2].upper() == "DWELL":
                    #see documentation for formulas for position, velocity, acceleration, and jerk
                    currentPosition = self.camData[mValue][3]
                    currentVelocity = 0
                    currentAcceleration = 0
                    currentJerk = 0
                #elif self.camData[mValue][2] (motion type) in uppercase is "UNIFORM"
                elif self.camData[mValue][2].upper() == "UNIFORM":
                    #see documentation for formulas for position, velocity, acceleration, and jerk
                    currentPosition = ((float(currentAngle) - float(self.camData[mValue][0]))* (self.camData[mValue][4] - self.camData[mValue][3]) / (float(self.camData[mValue][1]) - float(self.camData[mValue][0]))) + self.camData[mValue][3]
                    currentVelocity = self.getRotationalSpeed() * (self.camData[mValue][4] - self.camData[mValue][3]) / ((pi / 180.0) * (float(self.camData[mValue][1]) - float(self.camData[mValue][0])))
                    currentAcceleration = 0
                    currentJerk = 0
                #elif self.camData[mValue][2] (motion type) in uppercase is "HARMONIC"
                elif self.camData[mValue][2].upper() == "HARMONIC":
                    #see documentation for formulas for position, velocity, acceleration, and jerk
                    currentPosition = (lVal * 0.5) * (1 - cos(thetaOverBPI)) + self.camData[mValue][3]
                    currentVelocity = (pi * self.getRotationalSpeed()/ intervalValueRad) * (lVal * 0.5) * (sin(thetaOverBPI))
                    currentAcceleration = pow((pi * self.getRotationalSpeed() / intervalValueRad), 2) * (lVal * 0.5) * (cos(thetaOverBPI))
                    currentJerk = (-1.0) * pow((pi * self.getRotationalSpeed() /  intervalValueRad), 3) * (lVal * 0.5) * (sin(thetaOverBPI))
                #elif self.camData[mValue][2] (motion type) in uppercase is "PARABOLIC"
                elif self.camData[mValue][2].upper() == "PARABOLIC":
                    #if thetaOverB is less than 0.5, use this set of formulas found in documentation for position, velocity, and acceleration
                    if thetaOverB <= 0.5:
                        currentPosition = 2 * lVal * pow(thetaOverB, 2) + self.camData[mValue][3]
                        currentVelocity = self.getRotationalSpeed() * (4 * lVal * thetaOverB / intervalValueRad)
                        currentAcceleration = pow(self.getRotationalSpeed(), 2) * (4 * lVal / pow(intervalValueRad, 2))
                    #elif thetaOverB is more than 0.5, use this set of formulas found in documentation for position, velocity, and acceleration
                    else:
                        currentPosition = lVal * (-1 + (4 * thetaOverB) - (2 * pow(thetaOverB, 2))) + self.camData[mValue][3]
                        currentVelocity = self.getRotationalSpeed() * (4 * lVal * (1 - thetaOverB) / intervalValueRad)
                        currentAcceleration = pow(self.getRotationalSpeed(), 2) * (-4 * lVal / pow(intervalValueRad, 2))
                    currentJerk = 0
                elif self.camData[mValue][2].upper() == "CYCLOIDAL":
                    #see documentation for formulas for position, velocity, acceleration, and jerk
                    currentPosition = lVal * (thetaOverB - ((1 / (2 *pi)) * sin(2 * thetaOverBPI))) + self.camData[mValue][3]
                    currentVelocity = (lVal * self.getRotationalSpeed() / intervalValueRad) * (1 - cos(2 * thetaOverBPI))
                    currentAcceleration = (2 * pi * lVal * pow(self.getRotationalSpeed() / intervalValueRad, 2)) * (sin(2 * thetaOverBPI))
                    currentJerk = (pow(2 * pi, 2) * lVal * pow(self.getRotationalSpeed() / intervalValueRad, 3)) * (cos(2 * thetaOverBPI))

                #add list of currentAngle, time (calculated in line), currentPosition, currentVelocity, currenAcceleration, and currentJerk
                self.angleDataPoints.append([currentAngle, float(pi * currentAngle / (180.0 * self.getRotationalSpeed())) ,currentPosition, currentVelocity, currentAcceleration, currentJerk])

    #define method displayCamVisual with input self
    def displayCamVisual(self):
        #print message explaining how to exit mainloop in master
        print("\nClose out of the cam window to continue")
        #class camVisual with inputs of self.angleDataPoints, self.getUnits, self.getRotationalSpeed, and "Image"
        cv = CamVisual(self.angleDataPoints, self.getUnits(), self.getRotationalSpeed(), "Image")

    #define method displayCamAnimation with input self
    def displayCamAnimation(self):
        #print message explaining how to exit mainloop in master
        print("\nClose out of the cam window to continue")
        #class camVisual with inputs of self.angleDataPoints, self.getUnits, self.getRotationalSpeed, and "Animation"
        cv = CamVisual(self.angleDataPoints, self.getUnits(), self.getRotationalSpeed(), "Animation")

    #define property rotationalSpeed with fget of getRotationalSpeed and fset of setRotationalSpeed
    rotationalSpeed = property(fget = getRotationalSpeed, fset = setRotationalSpeed)
    #define property unitsType with fget of getUints and fset of setUnits
    unitsType = property(fget = getUnits, fset = setUnits)
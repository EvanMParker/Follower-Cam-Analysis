#evanpark_Utilities.py
#This file is a collection of functions that are utilized throughout the main python file. The functions include printing menus
#and determining if a passed through value is a number or not and if a passed through value is an integer or not


#function menu1() prints the main menu for the program. It takes no input and outputs the menu via print
def menu1():
    print("""
Please Select One of the Following Options:
[1] Generate New Cam Profile
[2] Import Existing Cam Profile File
[3] Quit Program
    """)

#function menu2() prints the units menu for the program. It takes no inputs and outputs the menu via print
def menu2():
    print("""
Please Select One of the Following Units:
[1] Centimeters (cm)
[2] Meters (m)
[3] Inches (in)
[4] Foot (ft)
    """)

#function menu3() prints the menu for selecting a motion types. It takes no inputs and outputs the menu via print
def menu3():
    print("""
Please Select One of the Following Interval Motion Types:
[1] Dwell
[2] Uniform
[3] Parabolic
[4] Harmonic
[5] Cycloidal""")

#function menu4() prints the menu for selecting a motinon type given that it cannot be a dwell. It takes no inputs and outputs the menu via print
def menu4():
    print("""Please Select One of the Following Interval Motion Types:
[1] Uniform
[2] Parabolic
[3] Harmonic
[4] Cycloidal""")

#function menu5() prints the menu for once the cam has been created or successfully imported. It takes no inputs and outputs the menu via print
def menu5():
    print("""
Please Select One of the Following Options:
[1] Display Cam Information
[2] Update Rotational Velocity
[3] Update Units
[4] Generate and Save Cam Profile File (.txt file)
[5] Generate and Save Cam Analysis File (.csv file)
[6] Display Mock Cam Profile
[7] Display Mock Cam Animation
[8] Quit to Main Menu
    """)

#funtion isNumber() retruns a T/F value for whether an inputted variable is a number or not. It takes a single input and outputs either True or False
def isNumber(testNumber):
    #try to convert the input to a float. If successful, return True. Otherwise, return False
    try:
        float(testNumber)
        return True
    except:
        return False

#funtion isNumber() retruns a T/F value for whether an inputted variable is an integer or not. It takes a single input and outputs either True or False
def isInteger(testInteger):
    #Ensure the input is a number. If the float of the input is equal to the int of the input, the value is an integer and True is returned. Otherwise, return False
    try:
        isNumber(testInteger)
        if float(testInteger) == int(testInteger):
            return True
        else:
            return False
    except:
        return False
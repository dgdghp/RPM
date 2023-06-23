# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.
# Allowable libraries are Python 3.8, Pillow 8.1.0, np 1.19.1, and OpenCV4.2.0
# OpenCV 4.2.0, opencv-contrib-python-headless. Non-headless versions of OpenCV will work,
# but the contrib modules of OpenCV like imshow() will not work.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageOps
import numpy as np
import cv2 as cv

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    # Remember to return the answer [Key], not the name, as the ANSWERS ARE SHUFFLED.
    # np.invert(Use var = problem.figures["A"].visualFilename) to open files
    # Do not use Absolute pathing to open files.

    # 
    def Solve(self,problem):

            # Create a tolerance variable for the MSE function shown later, just for ease of access
            global tolerance
            tolerance = 0.04

            # pretty much we are just getting this variable from the Intake() function
            images = self.Intake(problem)
            # Use the checkEquivalence() function to make a final guess
            guessKey = self.checkEquivalence(problem, images)

        

            #       ~~ BEGIN DEBUGGING TESTS ~~
            # print(self.matchKey(problem,images,images["B"]))
            # print(self.checkSimilarity(images["B"], images["A"]))
            # print(type(images["A"]))
            # print(self.checkSymmetry(images["A"], images["B"]))
            # print(self.getSimilarity(np.fliplr(im2),im1))
            print(guessKey)
            #       ~~ END DEBUGGING TESTS ~~


            # This is the final return statement that will submit the answers
            return guessKey


    # Intake all the images and put them in a dictionary for easy access
    # Two separate functions for 2x2 and 3x3 matrices

    def Intake(self,problem):

        # first check if the matrix is a 2x2 or 3x3
        # next import the image with opencv and assign it to a dictionary
        # during the import, the image is converted to grayscale, inverted, and the array is clipped from 0-255 to 0-1
        # NOTE put this stuff in a separate file later possible

        if problem.problemType == "2x2":
            images = {
            "A": np.invert(cv.cvtColor(cv.imread(problem.figures["A"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "B": np.invert(cv.cvtColor(cv.imread(problem.figures["B"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "C": np.invert(cv.cvtColor(cv.imread(problem.figures["C"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "1": np.invert(cv.cvtColor(cv.imread(problem.figures["1"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "2": np.invert(cv.cvtColor(cv.imread(problem.figures["2"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "3": np.invert(cv.cvtColor(cv.imread(problem.figures["3"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "4": np.invert(cv.cvtColor(cv.imread(problem.figures["4"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "5": np.invert(cv.cvtColor(cv.imread(problem.figures["5"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)), 
            "6": np.invert(cv.cvtColor(cv.imread(problem.figures["6"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1))
            }
        elif problem.problemType == "3x3":
            images = {
            "A": np.invert(cv.cvtColor(cv.imread(problem.figures["A"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "B": np.invert(cv.cvtColor(cv.imread(problem.figures["B"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "C": np.invert(cv.cvtColor(cv.imread(problem.figures["C"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "D": np.invert(cv.cvtColor(cv.imread(problem.figures["D"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "E": np.invert(cv.cvtColor(cv.imread(problem.figures["E"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "F": np.invert(cv.cvtColor(cv.imread(problem.figures["F"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "G": np.invert(cv.cvtColor(cv.imread(problem.figures["G"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "H": np.invert(cv.cvtColor(cv.imread(problem.figures["H"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "1": np.invert(cv.cvtColor(cv.imread(problem.figures["1"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "2": np.invert(cv.cvtColor(cv.imread(problem.figures["2"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "3": np.invert(cv.cvtColor(cv.imread(problem.figures["3"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "4": np.invert(cv.cvtColor(cv.imread(problem.figures["4"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "5": np.invert(cv.cvtColor(cv.imread(problem.figures["5"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "6": np.invert(cv.cvtColor(cv.imread(problem.figures["6"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "7": np.invert(cv.cvtColor(cv.imread(problem.figures["7"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1)),
            "8": np.invert(cv.cvtColor(cv.imread(problem.figures["8"].visualFilename), cv.COLOR_BGR2GRAY).clip(max=1))
            }

        # Return the variable images, which is an array of uint8 values
        return images


    



    # Return the Mean Squared Error, or basically how similar images are
    def checkSimilarity(self, arr1, arr2):
        err = np.sum((arr1.astype("float") - arr2.astype("float")) ** 2)
        err /= float(arr1.shape[0] * arr2.shape[1])
        return err
        
    

    # Using the previous MSE function, return the most similar image under the threshold, "tolerance"
    def matchKey(self,problem,images,im):
        sim_array = []
        if problem.problemType == "2x2":
            for i in range(6):
                sim_array.append(self.checkSimilarity(im, images[f"{i+1}"]))
        else:
            for i in range(8):
                sim_array.append(self.checkSimilarity(im, images[f"{i+1}"]))

        return np.argmin(sim_array)+1



    # Combines checkSimilarity and matchKey in order to return a guess of the image that the input image matches
    def checkEquivalence(self, problem, images):
        if self.checkSimilarity(images["A"], images["B"]) < 0.04:
            return self.matchKey(problem, images, images["C"])
        elif self.checkSimilarity(images["A"], images["C"]) < 0.04:
            return self.matchKey(problem, images, images["B"])
        else:
            return 0

    # returns which type of symmetry (vertical or horizontal) the image has, if any
    # 0 = no symmetry detected
    # 1 = horizontal symmetry
    # 2 = vertical symmetry
    def getSymmetry(self, im1, im2):
        if self.getSimilarity(np.fliplr(im2), im1) < tolerance:
            return 1
        if self.getSimilarity(np.flipud(im2), im1) < tolerance:
            return 2
        else:
            return 0
        
    # Compares symetry from A -> B and A -> C
    def checkSymmetry(self, problem, images):
        # checks for a - b symmetry and applies to c
        if (self.getSymmetry(images["A"], images["B"]) == 1):
            return self.matchKey(problem,images,np.fliplr(images["C"]))
        if (self.getSymmetry(images["A"], images["B"]) == 2):
            return self.matchKey(problem, images, np.flipud(images["C"]))
        
        # checks for a - c symmetry and applies to b
        if (self.getSymmetry(images["A"], images["C"] == 1)):
            return self.matchKey(problem, images, np.fliplr(images["B"]))
        if (self.getSymmetry(images["A"], images["C"] == 2)):
            return self.matchKey(problem, images, np.flipud(images["B"]))
        return 0


    def checkFill():
        pass

    def shapeSubtraction():
        pass

    
    
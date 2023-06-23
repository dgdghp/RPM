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


    # Intake all the images and put them in a dictionary for easy access
    # Two separate functions for 2x2 and 3x3 matrices

    def Intake(self,problem):

        # first check if the matrix is a 2x2 or 3x3
        # next import the image with opencv and assign it to a dictionary
        # during the import, the image is converted to grayscale, and the array is clipped from 0-255 to 0-1
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

        return images


    def Solve(self,problem):
        global tolerance
        tolerance = 0.04
        images = self.Intake(problem)


        #       ~~DEBUGGING TESTS~~
        # print(self.matchKey(problem,images,images["B"]))
        # print(self.checkSimilarity(images["B"], images["2"]))
        # print(images["A"])

        guessKey = self.checkEquivalence(problem, images)
        #if guessKey != 0:
        #    return guessKey
        
        print(guessKey)
        return guessKey

    # Return the Mean Squared Error
    def checkSimilarity(self, arr1, arr2):
        err = np.sum((arr1.astype("float") - arr2.astype("float")) ** 2)
        err /= float(arr1.shape[0] * arr2.shape[1])
        return err
        
    
    # Neal's function to return the matched image
    def matchKey(self,problem,images,im):
        sim_array = []
        if problem.problemType == "2x2":
            for i in range(6):
                sim_array.append(self.checkSimilarity(im, images[f"{i+1}"]))
        else:
            for i in range(8):
                sim_array.append(self.checkSimilarity(im, images[f"{i+1}"]))

        # print(sim_array)
        return np.argmin(sim_array)+1


    def checkEquivalence(self, problem, images):
        if self.checkSimilarity(images["A"], images["B"]) < 0.04:
            return self.matchKey(problem, images, images["C"])
        elif self.checkSimilarity(images["A"], images["C"]) < 0.04:
            return self.matchKey(problem, images, images["B"])
        else:
            return 0


    def checkSymmetry(self, problem, images):
        if self.checkSimilarity(np.fliplr(images["B"]), images["A"]) < tolerance:
            return problem.figures["A"].visualFilename + " -> symmetrical"

    def checkFill():
        pass

    def shapeSubtraction():
        pass

    
    
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
from PIL import Image
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
    # Use var = problem.figures["A"].visualFilename to open files
    # Do not use Absolute pathing to open files.


    # Intake all the images and put them in a dictionary for easy access
    # Two separate functions for 2x2 and 3x3 matrices

    def Intake(self,problem):

        if problem.problemType == "2x2":
            images = {
            "A": cv.IMREAD_GRAYSCALE(problem.figures["A"].visualFilename), 
            "B": cv.IMREAD_GRAYSCALE(problem.figures["B"].visualFilename), 
            "C": cv.IMREAD_GRAYSCALE(problem.figures["C"].visualFilename), 
            "1": cv.IMREAD_GRAYSCALE(problem.figures["1"].visualFilename), 
            "2": cv.IMREAD_GRAYSCALE(problem.figures["2"].visualFilename), 
            "3": cv.IMREAD_GRAYSCALE(problem.figures["3"].visualFilename), 
            "4": cv.IMREAD_GRAYSCALE(problem.figures["4"].visualFilename), 
            "5": cv.IMREAD_GRAYSCALE(problem.figures["5"].visualFilename), 
            "6": cv.IMREAD_GRAYSCALE(problem.figures["6"].visualFilename)
            }
        elif problem.problemType == "3x3":
            images = {
            "A": cv.IMREAD_GRAYSCALE(problem.figures["A"].visualFilename),
            "B": cv.IMREAD_GRAYSCALE(problem.figures["B"].visualFilename),
            "C": cv.IMREAD_GRAYSCALE(problem.figures["C"].visualFilename),
            "D": cv.IMREAD_GRAYSCALE(problem.figures["D"].visualFilename),
            "E": cv.IMREAD_GRAYSCALE(problem.figures["E"].visualFilename),
            "F": cv.IMREAD_GRAYSCALE(problem.figures["F"].visualFilename),
            "G": cv.IMREAD_GRAYSCALE(problem.figures["G"].visualFilename),
            "H": cv.IMREAD_GRAYSCALE(problem.figures["H"].visualFilename),
            "1": cv.IMREAD_GRAYSCALE(problem.figures["1"].visualFilename),
            "2": cv.IMREAD_GRAYSCALE(problem.figures["2"].visualFilename),
            "3": cv.IMREAD_GRAYSCALE(problem.figures["3"].visualFilename),
            "4": cv.IMREAD_GRAYSCALE(problem.figures["4"].visualFilename),
            "5": cv.IMREAD_GRAYSCALE(problem.figures["5"].visualFilename),
            "6": cv.IMREAD_GRAYSCALE(problem.figures["6"].visualFilename),
            "7": cv.IMREAD_GRAYSCALE(problem.figures["7"].visualFilename),
            "8": cv.IMREAD_GRAYSCALE(problem.figures["8"].visualFilename)
            }

        return images

    def Solve(self,problem):

        images = self.Intake(problem)


        # DEBUGGING TESTS
        # print(self.matchKey(problem,images,images["B"]))
        # print(self.checkSimilarity(images["B"], images["6"]))
        print(images["A"])
        
        return 2

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
        return np.argmin(sim_array)+1


    
    
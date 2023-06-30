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

            # TEST code for later            
            # testSingle, testName = 1, "Problem B-06"
            # if testSingle == True:
            #     if problem.problemName != testName:



            # Create a tolerance variable for the MSE function shown later, just for ease of access
            global tolerance
            tolerance = 0.025 # 0.0283

            # pretty much we are just getting this variable from the Intake() function
            images = self.Intake(problem)

            # Use the checkEquivalence() function to make a final guess
            guessKey = self.checkSymmetry(problem, images)

        

            #       ~~ BEGIN DEBUGGING TESTS ~~

            # print(self.matchKey(problem,images,images["B"]))
            # print(self.mse(images["B"], images["A"]))
            # print(images["A"])
            # print(self.checkSymmetry(images["A"], images["1"]))
            # print(self.getSimilarity(np.fliplr(im2),im1))
            # print(guessKey)
            # self.saveAsCSV(images["B"], "B")
            # print(self.isIdentical(images["A"], images["B"]))
            # self.checkDifference(images["A"], images["B"], images["C"])

            #       ~~ END DEBUGGING TESTS ~~



            # This is the final return statement that will submit the answers
            # return guessKey
            if guessKey != 0:
                return guessKey
            else:
                return self.checkDifference(problem, images, images["A"], images["B"], images["C"])


    # Intake all the images and put them in a dictionary for easy access
    # Two separate functions for 2x2 and 3x3 matrices
    def Intake(self,problem):

        # first check if the matrix is a 2x2 or 3x3
        # next import the image with opencv and assign it to a dictionary
        # during the import, the image is converted to grayscale, inverted, and the array is clipped from 0-255 to 0-1
        # NOTE put this stuff in a separate file later possible

        if problem.problemType == "2x2":
            images = {
            "A": np.invert(cv.cvtColor(cv.imread(problem.figures["A"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "B": np.invert(cv.cvtColor(cv.imread(problem.figures["B"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "C": np.invert(cv.cvtColor(cv.imread(problem.figures["C"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "1": np.invert(cv.cvtColor(cv.imread(problem.figures["1"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "2": np.invert(cv.cvtColor(cv.imread(problem.figures["2"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "3": np.invert(cv.cvtColor(cv.imread(problem.figures["3"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "4": np.invert(cv.cvtColor(cv.imread(problem.figures["4"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "5": np.invert(cv.cvtColor(cv.imread(problem.figures["5"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1), 
            "6": np.invert(cv.cvtColor(cv.imread(problem.figures["6"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1)
            }
        elif problem.problemType == "3x3":
            images = {
            "A": np.invert(cv.cvtColor(cv.imread(problem.figures["A"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "B": np.invert(cv.cvtColor(cv.imread(problem.figures["B"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "C": np.invert(cv.cvtColor(cv.imread(problem.figures["C"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "D": np.invert(cv.cvtColor(cv.imread(problem.figures["D"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "E": np.invert(cv.cvtColor(cv.imread(problem.figures["E"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "F": np.invert(cv.cvtColor(cv.imread(problem.figures["F"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "G": np.invert(cv.cvtColor(cv.imread(problem.figures["G"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "H": np.invert(cv.cvtColor(cv.imread(problem.figures["H"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "1": np.invert(cv.cvtColor(cv.imread(problem.figures["1"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "2": np.invert(cv.cvtColor(cv.imread(problem.figures["2"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "3": np.invert(cv.cvtColor(cv.imread(problem.figures["3"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "4": np.invert(cv.cvtColor(cv.imread(problem.figures["4"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "5": np.invert(cv.cvtColor(cv.imread(problem.figures["5"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "6": np.invert(cv.cvtColor(cv.imread(problem.figures["6"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "7": np.invert(cv.cvtColor(cv.imread(problem.figures["7"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1),
            "8": np.invert(cv.cvtColor(cv.imread(problem.figures["8"].visualFilename), cv.COLOR_BGR2GRAY)).clip(max=1)
            }

        # Return the variable images, which is an array of uint8 values
        return images


    



    # Return the Mean Squared Error, or basically how similar images are
    def mse(self, arr1, arr2):
        err = np.sum((arr1.astype("float") - arr2.astype("float")) ** 2)
        err /= float(arr1.shape[0] * arr2.shape[1])
        return err
    
    # Just return if the two input images are "identical", or if they are under the tolerance
    def isIdentical(self, im1, im2):
        return self.mse(im1, im2) < tolerance   
    

    # Using the previous MSE function, return the most similar image under the threshold, "tolerance"
    def matchKey(self, problem, images, im):

        # Benchmark error level
        minError = self.mse(im, images["1"])
        minErrorindex = 0

        if problem.problemType == "2x2":
            for i in range(1, 6):
                if self.mse(im, images[f"{i+1}"]) < minError:
                    minError = self.mse(im, images[f"{i+1}"])
                    minErrorindex = i
                
        elif problem.problemType == "3x3":
            for i in range(1, 8):
                if self.mse(im, images[f"{i+1}"]) < minError:
                    minError = self.mse(im, images[f"{i+1}"])
                    minErrorindex = i

        if problem.name == "Basic Problem B-11":
            print(self.mse(im, images["1"]))
            print(minError, minErrorindex)

        return minErrorindex + 1



    # Combines mse and matchKey in order to return a guess of the image that the input image matches
    def checkEquivalence(self, problem, images):
        if self.mse(images["A"], images["B"]) < tolerance:
            return self.matchKey(problem, images, images["C"])
        elif self.mse(images["A"], images["C"]) < tolerance:
            return self.matchKey(problem, images, images["B"])
        else:
            return 0

    # returns which type of symmetry (vertical or horizontal) the image has, if any
    # 0 = no symmetry detected
    # 1 = horizontal symmetry
    # 2 = vertical symmetry
    def getSymmetry(self, im1, im2):
        if self.isIdentical(np.fliplr(im2), im1):
            return 1
        if self.isIdentical(np.flipud(im2), im1):
            return 2
        else:
            return 0
        
    # Compares symetry from A -> B and A -> C
    # This function combines all the previous ones
    def checkSymmetry(self, problem, images):
        # print(images["A"])
        # print(type(images["A"]))
        # print(images["B"])
        # print(type(images["B"]))
        abSim = self.getSymmetry(images["A"], images["B"])
        

        # checks for a - b symmetry and applies to c
        if (abSim == 1):
            return self.matchKey(problem, images, np.fliplr(images["C"]))    
        if (abSim == 2):
            return self.matchKey(problem, images, np.flipud(images["C"]))
        
        
        acSim = self.getSymmetry(images["A"], images["C"])


        # checks for a - c symmetry and applies to b
        if (acSim == 1):
            return self.matchKey(problem, images, np.fliplr(images["B"]))
        if (acSim == 2):
            return self.matchKey(problem, images, np.flipud(images["B"]))
        

        # Return 0 if no symmetry
        return 0
    
    def checkDifference(self, problem, images, im1, im2, im3):
        # combinedArray = ((im2 - im1) + (im3 - im1))
        combinedArray = (im1 + im2 + im3 - 2)
        # combinedArray = combinedArray[combinedArray != 2]


        if problem.name == "Basic Problem B-11":
            # print(self.mse(combinedArray, images["5"]))
            self.saveAsCSV(combinedArray[combinedArray != 2], "B-11")
            print("ok")


        return self.matchKey(problem, images, combinedArray)


    def pixelCount(self, im):
        pass
    # def checkFill():
    #     pass

    # def shapeSubtraction():
    #     pass

    def saveAsCSV(self, im, letter):
        np.savetxt(f"img_{letter}.csv", im, fmt='%d', delimiter=",")

    
    
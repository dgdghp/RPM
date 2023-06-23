file = open('ProblemResults.csv', 'rt')
data = file.read()
words = data.split(',')
print(str(round(((words.count('Correct') - 2) / (words.count("Incorrect") + (words.count("Correct") -2)) * 100), 2)) + "%")
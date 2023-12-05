import os;
import re;

def getFilePath(filename):
  return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def extractNumbers(s):
    fullNumber = 0
    numList = re.findall('\d', s)
    fullNumber = int(numList[0] + numList[-1])
    return fullNumber

allNums = [0]

with open(getFilePath("input1.txt")) as file:
    while line := file.readline():
        allNums.append(extractNumbers(line.rstrip()))
        
print(sum(allNums))
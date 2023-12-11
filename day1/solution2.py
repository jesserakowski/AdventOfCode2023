import os;
import re;

NUMBER_MAP = {"one" : "1",
              "two" : "2",
              "three" : "3",
              "four" : "4",
              "five" : "5",
              "six" : "6",
              "seven" : "7",
              "eight" : "8",
              "nine" : "9"
              }

def getFilePath(filename):
  return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def extractNumbers(s):
    numList = re.findall("(one|two|three|four|five|six|seven|eight|nine|[1-9])", s, re.IGNORECASE)
    
    if len(numList) == 0:
        return 0
    
    if len(numList) == 1:
        return convertWordToDigit(numList[0])
    
    return convertWordToDigit(numList[0]) + convertWordToDigit(numList[len(numList)-1])
    
def convertWordToDigit(number):
    if re.match('\d', number):
        return str(number)
    
    return NUMBER_MAP.get(number)

allNums = []
runningTotal = 0
    
with open(getFilePath("test_input2.txt")) as file:
    while line := file.readline():
        n = int(extractNumbers(line.rstrip()))
        allNums.append(n)
        
print(sum(allNums))
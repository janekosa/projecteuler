

def solution():
  maxMultiplier = 6
  maxMultiplierFound = 1
  length = 1
  while(length < 50):
    min = lowerBound(length)
    max = upperBound(length)
    for i in range (min, max):
      maxMultiplierFoundThisTime = maxMultiplierContainingSameDigits(i, 6)
      if (maxMultiplierFoundThisTime >= maxMultiplier):
        return i
      if (maxMultiplierFoundThisTime > maxMultiplierFound):
        maxMultiplierFound = maxMultiplierFoundThisTime
    print("no success for length " + str(length))
    length += 1


def lowerBound(length):
  result = "1"
  for i in range(1,length):
    result = result + "0"
  return int(result)

def upperBound(length): # slight optimisation. if a number is bigger than 16666.. it will have more digits when multiplied by 6
  result = "1"
  for i in range(1,length):
    result = result + "6"
  return int(result)

def maxMultiplierContainingSameDigits(number, maxMultiplier):
  for i in range(1, maxMultiplier):
    if not containsSameDigitsWhenMultiplied(number, i+1):
      return i
  return maxMultiplier

def containsSameDigitsWhenMultiplied(number, multiplier):
  number2 = number*multiplier
  return digits(number) == digits(number2)

def digits(number):
  result = dict()
  for char in str(number):
    result[char] = result.get(char, 0) + 1
  return result

def prettyDict(input):
  result = dict()
  for i in range(10):
    if str(i) in input:
      result[i] = input.get(str(i), 0)
  return result


def useSolutionAndVerify():
  result = solution()
  print("found result " + str(result))
  for i in range (6):
    multipliedResult = result * (i+1)
    print("result multiplied by " + str(i+1) + " equals " + str(multipliedResult) + " and has digits " + str(prettyDict(digits(multipliedResult))))


useSolutionAndVerify()
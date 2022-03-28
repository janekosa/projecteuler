from copy import deepcopy

def solution():
  sudokus = loadSudokus()
  result = 0
  for sudoku in sudokus:
    solvedSudoku = solveSudoku(sudoku)
    result += getSudokuHashNumber(solvedSudoku)
  return result

def getSudokuHashNumber(sudoku):
  return int(100*sudoku[0][0] + 10*sudoku[0][1] + sudoku[0][2])


def solveSudoku(sudoku):
  fillTrivial(sudoku)
  if isFinished(sudoku):
    return sudoku
  for x in range(9):
    for y in range(9):
      if sudoku[x][y] == 0:
        for option in getLegalOptions(sudoku, x, y):
          node = guess(sudoku, x, y, option)
          if node:
            return node
  return 0


def guess(sudoku, x, y, val):
  guessNode = deepcopy(sudoku)
  guessNode[x][y] = val
  fillTrivial(guessNode)
  if isFinished(guessNode):
    return guessNode
  if canContinue(guessNode):
    bestPoint = findBestGuessingPoint(guessNode)
    for option in getLegalOptions(guessNode, bestPoint[0], bestPoint[1]):
      deeperNode = guess(guessNode, bestPoint[0], bestPoint[1], option)
      if deeperNode:
        return deeperNode
  return 0


def findBestGuessingPoint(sudoku):
  minimumOptions = 10
  bestPoint = (-1,-1)
  for x in range(9):
    for y in range(9):
      if sudoku[x][y] == 0:
        localOptions = getLegalOptions(sudoku, x, y)
        if len(localOptions) < minimumOptions:
          minimumOptions = len(localOptions)
          bestPoint = (x,y)
  return bestPoint



def canContinue(sudoku):
  for x in range(9):
    for y in range(9):
      if sudoku[x][y] == 0 and len(getLegalOptions(sudoku, x, y)) == 0:
        return 0
  return 1


def isFinished(sudoku):
  finished = 1
  for xIter in range(9):
    for yIter in range(9):
      if sudoku[xIter][yIter] == 0:
        finished = 0
  return finished


def fillTrivial(sudoku):
  progress = 1
  while(progress):
    progress = 0
    for xIter in range(9):
      for yIter in range(9):
        if sudoku[xIter][yIter] == 0:
          options = getLegalOptions(sudoku, xIter, yIter)
          if len(options) == 1:
            progress = 1
            sudoku[xIter][yIter] = list(options)[0]


def loadSudokus():
  file = open("sudoku.txt", 'r')
  lines = file.readlines()
  numberOfSudokus = int(len(lines)/10)
  sudokus = list()
  for i in range(numberOfSudokus):
    sudoku = list()
    for j in range(1,10):
      sudoku.append(list())
      for k in range(9):
        sudoku[j-1].append(int(lines[(10*i) + j][k]))
    sudokus.append(sudoku)
  return sudokus


def getLegalOptions(sudoku, x, y):
  options = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  for i in range(9):
    options.discard(sudoku[x][i])
    options.discard(sudoku[i][y])
  squareRanges = getRangesForSubSquare(x, y)
  for xIter in squareRanges["x"]:
    for yIter in squareRanges["y"]:
      options.discard(sudoku[xIter][yIter])
  return options


def getRangesForSubSquare(x,y):
  xSquare = int(x/3)
  ySquare = int(y/3)
  xRange = range(3*xSquare, 3*xSquare + 3)
  yRange = range(3*ySquare, 3*ySquare + 3)
  return {"x" : xRange, "y": yRange}

print(solution())
def solution():
  file1 = open('poker.txt', 'r')
  lines = file1.readlines()
  cardDegs = cardDesignations()
  p1wins = 0
  p2wins = 0
  for line in lines:
    p1Cards = computeHand1(line, cardDegs)
    p2Cards = computeHand2(line, cardDegs)
    res = whoWins(p1Cards, p2Cards)
    if res == 1:
      p1wins += 1
    else:
      p2wins += 1
  return p1wins

def whoWins(p1Cards, p2Cards):
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasStraightFlush(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasFourOfAKind(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasFullHouse(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasFlush(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasStraight(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasThreeOfAKind(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasTwoPairs(x))
  if (win != 0):
    return win
  win = whoWinsForFunc(p1Cards, p2Cards, lambda x: hasPair(x))
  if (win != 0):
    return win
  p1Cards.reverse()
  p2Cards.reverse()
  p1CardValues = [c["value"] for c in p1Cards]
  p2CardValues = [c["value"] for c in p2Cards]
  return compareResults(p1CardValues, p2CardValues)

def whoWinsForFunc(p1cards, p2cards, func):
  if (func(p1cards)):
    if not (func(p2cards)):
      return 1
    return compareResults(func(p1cards), func(p2cards))
  else:
    if func(p2cards):
      return 2
  return 0


def compareResults(p1res, p2res):
  for i in range(len(p1res)):
    if p1res[i] > p2res[i]:
      return 1
    if p1res[i] < p2res[i]:
      return 2
  return 0

def hasPair(cards):
  pairIndex = -1
  for i in range(1,5):
    if (cards[i-1]["value"] == cards[i]["value"]):
      pairIndex = i
      break
  if pairIndex == -1:
    return 0;
  result = [cards[pairIndex]["value"]]
  for i in range(5):
    index = 4-i
    if (not index == pairIndex) and (not index+1 == pairIndex):
      result.append(cards[index]["value"])
  return result

def hasTwoPairs(cards):
  topPair = cards[3]["value"] == cards[4]["value"]
  bottomPair = cards[0]["value"] == cards[1]["value"]
  if (topPair and bottomPair):
    return [cards[3]["value"], cards[0]["value"], cards[2]["value"]]
  if (topPair and cards[1]["value"] == cards[2]["value"]):
    return [cards[3]["value"], cards[1]["value"], cards[0]["value"]]
  if (bottomPair and cards[2]["value"] == cards[3]["value"]):
    return [cards[2]["value"], cards[0]["value"], cards[4]["value"]]
  return 0

def hasThreeOfAKind(cards):
  bottom3 = cards[0]["value"] == cards[1]["value"] and cards[1]["value"] == cards[2]["value"]
  middle3 = cards[1]["value"] == cards[2]["value"] and cards[2]["value"] == cards[3]["value"]
  top3 = cards[2]["value"] == cards[3]["value"] and cards[3]["value"] == cards[4]["value"]
  if bottom3:
    return [cards[0]["value"], cards[4]["value"], cards[3]["value"]]
  if middle3:
    return [cards[1]["value"], cards[4]["value"], cards[0]["value"]]
  if top3:
    return [cards[2]["value"], cards[1]["value"], cards[0]["value"]]
  return 0

def hasStraight(cards):
  for i in range(1,5):
    if (cards[i-1]["value"] + 1 != cards[i]["value"]):
      return 0
  return [cards[0]]

def hasFlush(cards):
  color = cards[0]["color"]
  for i in cards:
    if i["color"] != color:
      return 0
  return [cards[4]["value"],cards[3]["value"],cards[2]["value"],cards[1]["value"],cards[0]["value"]]

def hasFullHouse(cards):
  lowPair = cards[1]["value"] != cards[2]["value"]
  if (lowPair):
    expectedIndiciesForThree = range(2,5)
    expectedIndiciesForTwo = range(0,2)
    expectedValueForThree = cards[2]["value"]
    expectedValueForTwo = cards[0]["value"]
  else:
    expectedIndiciesForThree = range(0,3)
    expectedIndiciesForTwo = range(3,5)
    expectedValueForThree = cards[0]["value"]
    expectedValueForTwo = cards[3]["value"]
  for i in expectedIndiciesForThree:
    if cards[i]["value"] != expectedValueForThree:
      return 0
  for i in expectedIndiciesForTwo:
    if cards[i]["value"] != expectedValueForTwo:
      return 0
  return [expectedValueForThree, expectedValueForTwo]


def hasFourOfAKind(cards):
  lowKicker = cards[0]["value"] != cards[1]["value"]
  if (lowKicker):
    expectedIndicies = range(1,5)
    expectedValue = cards[1]["value"]
    expectedKicker = cards[0]["value"]
  else:
    expectedIndicies = range(0,4)
    expectedValue = cards[0]["value"]
    expectedKicker = cards[4]["value"]
  for i in expectedIndicies:
    if cards[i]["value"] != expectedValue:
      return 0
  return [expectedValue, expectedKicker]

def hasStraightFlush(cards):
  color = cards[0]["color"]
  for i in cards:
    if i["color"] != color:
      return 0
  for i in range(1, len(cards)):
    if cards[i-1]["value"] + 1 != cards[i]["value"]:
      return 0
  return [cards[0]["value"]]

def cardDesignations():
  result = dict()
  result["2"]=2
  result["3"]=3
  result["4"]=4
  result["5"]=5
  result["6"]=6
  result["7"]=7
  result["8"]=8
  result["9"]=9
  result["T"]=10
  result["J"]=11
  result["Q"]=12
  result["K"]=13
  result["A"]=14
  return result

def computeCard(string, cardDesignations):
  result = dict()
  result["value"] = cardDesignations[string[0]]
  result["color"] = string[1]
  return result

def computeHand1(string, cardDesignations):
  result = list()
  for i in range(5):
    cardString = (string[3* i :3*i + 2])
    result.append(computeCard(cardString, cardDesignations))
  result.sort(key=getCardValue)
  return result

def computeHand2(string, cardDesignations):
  result = list()
  for i in range(5, 10):
    cardString = (string[3* i :3*i + 2])
    result.append(computeCard(cardString, cardDesignations))
  result.sort(key=getCardValue)
  return result

def getCardValue(card):
  return card['value']

print(solution())
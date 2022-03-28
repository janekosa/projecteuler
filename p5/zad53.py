def solution(maxN, threshold):
  result = 0
  triangle = pascalTriangle(maxN, threshold)
  for line in triangle:
    for number in line:
      if number>1000000:
        result += 1
  return result

def pascalTriangle(maxN, threshold):
  result = list()
  firstline = [1]
  result.append(firstline)
  for i in range(1, maxN + 1):
    line = list()
    line.append(1)
    for j in range(1,i):
      val = result[i-1][j-1] + result[i-1][j]
      if val > threshold:
        val = threshold + 1
      line.append(val)
    line.append(1)
    result.append(line)
  return result

print("answer: " + str(solution(100, 1000000)))

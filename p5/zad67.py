

def solution():
  tree = loadTree()
  for i in range(1, len(tree)):
    tree[i][0] = tree[i][0] + tree[i-1][0]
    tree[i][i] = tree[i][i] + tree[i-1][i-1]
    for j in range(1,i):
      tree[i][j] = tree[i][j] + max(tree[i-1][j-1], tree[i-1][j])
  return max(tree[len(tree)-1])

def loadTree():
  file1 = open("triangle.txt", 'r')
  lines = file1.readlines()
  tree = list()
  for i in range(len(lines)):
    nums = [int(j) for j in lines[i].split()]
    tree.append(nums)
  return tree

print(solution())
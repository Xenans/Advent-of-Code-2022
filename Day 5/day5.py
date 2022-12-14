import re

file = open('./Day 5/input.txt', 'r')
input = [line for line in file]

numcols = 9
# Start by parsing the crates input
crates = [[] for i in range(numcols)]
crates2 = [[] for i in range(numcols)]

def parseCrates(line):
  for i in range(numcols):
    char = line[4*i + 1]
    if char != " " and not char.isdigit():
      crates[i].insert(0, char)
      crates2[i].insert(0, char)

def parseMove(line):
  nums = re.match(r'move (\d+) from (\d+) to (\d+)', line)
  count = int(nums[1])
  stack1 = int(nums[2]) - 1
  stack2 = int(nums[3]) - 1
  temp = []
  for i in range(count):
    crates[stack2].append(crates[stack1].pop())
    temp.append(crates2[stack1].pop())
  for i in range(count):
    crates2[stack2].append(temp.pop())

for line in input:
  if len(line) <= 3:
    continue
  elif line[0] == 'm':
    parseMove(line)
  else:
    parseCrates(line)

print(crates)
ans1 = ""
ans2 = ""
for i in range(numcols):
  ans1 = ans1 + crates[i][-1]
  ans2 = ans2 + crates2[i][-1]
print(ans1)
print(ans2)
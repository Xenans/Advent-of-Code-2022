file = open('./Day 3/input.txt', 'r')
input = [line.strip() for line in file]

sum1 = 0
sum2 = 0

linecount = 0
set1 = set()
set2 = set()
set3 = set()
for line in input:
  linecount += 1
  if linecount == 1:
    set1 = set(line)
  if linecount == 2:
    set2 = set(line)
  if linecount == 3:
    set3 = set(line)
    linecount = 0
    badge = set1.intersection(set2.intersection(set3)).pop()
    ascii = ord(badge)
    priority = ascii - 38 if ascii <= 96 else ascii - 96
    sum2 += priority
  num = len(line) // 2
  firsthalf = line[:num]
  firstset = set(firsthalf) 
  secondhalf = line[num:]
  secondset = set(secondhalf)

  dupe = firstset.intersection(secondset)
  ascii = ord(dupe.pop())
  priority = ascii - 38 if ascii <= 96 else ascii - 96
  sum1 += priority
  

print(sum1)
print(sum2)
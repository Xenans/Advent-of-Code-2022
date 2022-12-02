file = open('./Day 2/input.txt', 'r')
input = [line.strip() for line in file]

col1 = ['A', 'B', 'C']
col2 = ['K', 'Y', 'Z', 'X']

score = 0
score2 = 0
for line in input:  
  played = line[0]
  response = line[2]
  i = col1.index(played)
  j = col2.index(response)

  score +=  1 + j % 3
  if j == i + 1:
    score += 6
  elif j == i or j == i + 3:
    score += 3
  
  score2 += 1 + (i + j - 1) % 3
  if j == 1:
    score2 += 3
  elif j == 2:
    score2 += 6
  
print(score)
print(score2)
file = open('./Day 1/input.txt', 'r')
input = [line.strip() for line in file]

print(input)

sums = []
sum = 0
for line in input:
  if line:
    sum = sum + int(line)
  else:
    sums.append(sum)
    sum = 0

sums.sort()
print(sums[-1])
print(sums[-3] + sums[-2] + sums[-1])
import re

file = open('./Day 4/input.txt', 'r')
input = [line.strip() for line in file]

count1 = 0
count2 = 0
for line in input:
  nums = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)

  start1 = int(nums[1])
  end1 = int(nums[2])
  start2 = int(nums[3])
  end2 = int(nums[4])

  if (start1 <= start2) and (end2 <= end1):
    count1 += 1
    count2 += 1
    # print("2 is contained", line, start1, end1, start2, end2)
  elif (start2 <= start1) and (end1 <= end2):
    count1 += 1
    count2 += 1
    # print("1 is contained", line, start1, end1, start2, end2)
  elif (start2 <= end1) and (start1 <= end2):
    count2 += 1
  elif (start1 <= end2) and (start2 <= end1):
    count2 += 1


print(count1)
print(count2)
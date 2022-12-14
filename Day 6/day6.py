file = open('./Day 6/input.txt', 'r')
input = [line.strip() for line in file]

packet = 0
message = 0

for line in input:
  for i in range(len(line)):
    # print(line[i:i+4])
    chars = set(line[i:i+4])
    chars2 = set(line[i:i+14])
    if len(chars) >= 4 and not packet:
      packet = i+4
    if len(chars2) >= 14 and not message:
      message = i+14
print(packet)
print(message)
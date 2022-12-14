import re

file = open('./Day 7/input.txt', 'r')
input = [line.strip() for line in file]

class Directory:
  def __init__(self, name, parent = None):
    self.parent = parent
    self.name = name
    self.children = {}
    self.files = []
  

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size
  def __repr__(self) -> str:
    return f'{self.name}, (size={self.size})'

curdir = root = Directory('/')
curdir.parent = root

for line in input:
  # print('currently in', curdir.name, line)
  if line == r'$ cd /':
    continue
  if line[0] == '$':
    cmd = line[2:4]
    if cmd == 'cd':
      dir = line[5:]
      if dir == '..':
        curdir = curdir.parent
      elif curdir.children.get(dir):
        curdir = curdir.children.get(dir)
      else:
        # print('making a dir', dir)
        curdir.children[dir] = Directory(dir, curdir)
        curdir = curdir.children.get(dir)
    elif cmd == 'ls':
      pass

  else:
    parse = re.match(r'(.+) (.+)', line)
    # print(parse[1], parse[2])
    if parse[1] == 'dir':
      continue
    else:
      curdir.files.append(File(parse[2], int(parse[1])))

running_size = 0
maxsize = 100_000
sizes = {}

def recurse(directory: Directory):
  size = 0
  for file in directory.files:
    size += file.size
  for dir in directory.children.values():
    size += recurse(dir)
  if size <= maxsize:
    global running_size 
    running_size += size
  sizes[directory.name] = int(size)
  return size

recurse(root)
print(running_size)
small_size = sizes['/']
small_dir = '/'
unused_needed = 30000000 - (70000000 - sizes['/'])
for dir, size in sizes.items():
  if size >= unused_needed and size < small_size:
    small_dir = dir
    small_size = size
print(unused_needed)
print(small_size)
import os

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day3/data.txt", 'r') as file:
    data = file.readline()

  print(data)
  return data

def solve_p1(data):
  x,y = 0,0
  grid = dict()
  grid[(x,y)] = 1
  for ch in data:
    if ch == '^':
      y -= 1
    elif ch == ">":
      x += 1
    elif ch == "v":
      y += 1
    elif ch == "<":
      x -= 1
    if (x,y) not in grid:
      grid[(x,y)] = 0
    grid[(x,y)] += 1
  
  count = 0
  for k,v in grid.items():
    if v > 0:
      count += 1
  print(count)
  return count

def solve_p2(data):
  x,y = 0,0
  u,v = 0,0
  grid = dict()
  grid[(x,y)] = 2
  for i,ch in enumerate(data):
    if i % 2 == 0:
      if ch == '^':
        y -= 1
      elif ch == ">":
        x += 1
      elif ch == "v":
        y += 1
      elif ch == "<":
        x -= 1
      if (x,y) not in grid:
        grid[(x,y)] = 0
      grid[(x,y)] += 1
    else:
      if ch == '^':
        v -= 1
      elif ch == ">":
        u += 1
      elif ch == "v":
        v += 1
      elif ch == "<":
        u -= 1
      if (u,v) not in grid:
        grid[(u,v)] = 0
      grid[(u,v)] += 1
  
  count = 0
  for k,v in grid.items():
    if v > 0:
      count += 1
  print(count)
  return count

def main():
  data = get_data()
  solve_p1(data)
  solve_p2(data)

if __name__ == "__main__":
  main()
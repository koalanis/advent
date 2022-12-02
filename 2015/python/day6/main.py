import os

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day6/data.txt", 'r') as file:
    data = [line.strip() for line in file.readlines()]
  return data


def pair_to_tuple(pair):
  d = pair.split(",")
  return (int(d[0]),int(d[1]))

def instruction_to_tuple(inst):
  tokens = inst.split(" ")
  if inst.startswith("turn on"):
    return ("turnon", pair_to_tuple(tokens[2]), pair_to_tuple(tokens[4]))
  elif inst.startswith("turn off"):
    return ("turnoff", pair_to_tuple(tokens[2]), pair_to_tuple(tokens[4]))
  elif inst.startswith("toggle"):
    return ("toggle", pair_to_tuple(tokens[1]), pair_to_tuple(tokens[3]))

def get_instructions(data):
  return [instruction_to_tuple(st) for st in data]


def get_grid():
  grid = []
  for i in range(1000):
    grid.append([0]*1000)
  return grid

def solve_1(data):
  grid = get_grid()
  for inst in data:
    action, start, end = inst
    if action == "turnon":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] = 1
    elif action == "turnoff":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] = 0
    elif action == "toggle":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] = (grid[i][j] + 1) % 2
  
  count = 0
  for r in grid:
    for cell in r:
      if cell == 1:
        count += 1
  
  print(count)
  return count

def solve_2(data):
  grid = get_grid()
  for inst in data:
    action, start, end = inst
    if action == "turnon":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] += 1
    elif action == "turnoff":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] = max(0, grid[i][j]-1)
    elif action == "toggle":
      x1, y1 = start
      x2, y2 = end
      for i in range(x1, x2+1):
        for j in range(y1, y2+1):
          grid[i][j] += 2
  
  count = 0
  for r in grid:
    for cell in r:
        count += cell
  
  print(count)
  return count

def main():
  data = get_data()
  data = get_instructions(data)
  solve_1(data)
  solve_2(data)

if __name__ == "__main__":
  main()
import os

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day1/data.txt", 'r') as file:
    data = file.readline()
  return data

def solve_p1(data):
  floor = 0
  for ch in data:
    if ch == '(':
      floor += 1
    elif ch == ')':
      floor -= 1
  
  print(floor)
  return floor

def solve_p2(data):
  floor = 0
  step_in_basement = 0
  for ch in data:
    step_in_basement += 1
    if ch == '(':
      floor += 1
    elif ch == ')':
      floor -= 1
    if floor == -1:
      break
  print(step_in_basement)
  return step_in_basement

def main():
  data = get_data()
  solve_p1(data)
  solve_p2(data)


if __name__ == "__main__":
  main()
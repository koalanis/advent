import os

def dim_str_to_tuple(dim_str):
  vals = dim_str.split("x")
  return (int(vals[0]), int(vals[1]), int(vals[2]))

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day2/data.txt", 'r') as file:
    data = (line.strip() for line in file.readlines())
  
  data = [dim_str_to_tuple(dim) for dim in data]
  return data

def solve_p1(data):
  total = 0
  for box in data:
    l,w,h = box[0],box[1],box[2]
    sf_area = (2*l*w) + (2*w*h) + (2*h*l)
    extra = min([l*w, w*h, h*l])
    total += sf_area + extra
  
  print(total)
  return total

def solve_p2(data):
  total = 0
  for box in data:
    l,w,h = box[0],box[1],box[2]
    ribbon = min([2*(l+w), 2*(w+h), 2*(h+l)])
    bow = l*w*h
    total += ribbon + bow
  
  print(total)
  return total

def main():
  data = get_data()
  solve_p1(data)
  solve_p2(data)

if __name__ == "__main__":
  main()
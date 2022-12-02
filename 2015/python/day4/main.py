import os
import hashlib  

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day4/data.txt", 'r') as file:
    data = file.readline()

  print(data)
  return data

def to_hash_hex(s_val):
  out =  hashlib.md5(s_val.encode()).hexdigest()
  # print(out)
  return out

def has_starting_five_zeros(s_val):
  return s_val[:5] == "00000"

def has_starting_six_zeros(s_val):
  return s_val[:6] == "000000"

def solve_p1(data):
  i = 0

  def create_key(num):
    return f"{data}{num}"
  
  
  key = create_key(i)
  while not has_starting_five_zeros(to_hash_hex(key)):
    i += 1
    key = create_key(i)
  
  print(i)
  return i

def solve_p2(data):
  i = 0

  def create_key(num):
    return f"{data}{num}"
  
  
  key = create_key(i)
  while not has_starting_six_zeros(to_hash_hex(key)):
    i += 1
    key = create_key(i)
  
  print(i)
  return i

def main():
  data = get_data()
  solve_p1(data)
  solve_p2(data)

if __name__ == "__main__":
  main()
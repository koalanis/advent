import os

def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day5/data.txt", 'r') as file:
    data = [line.strip() for line in file.readlines()]
  return data

vowels = 'aeiou'
def three_vowels(st):
  count = 0
  for ch in st:
    if ch in vowels:
      count += 1
  return count >= 3

def twice_in_row(st):
  for i in range(1,len(st)):
    if st[i-1] == st[i]:
      return True
  return False

illegal = ["ab", "cd", "pq", "xy"]
def doesnt_contain_illegal_pairs(st):
    for i in range(1,len(st)):
      if st[i-1: i+1] in illegal:
        return False
    return True

def pair_appears_twice(st):
  m = dict()
  for i in range(1,len(st)):
    pair = st[i-1: i+1] 
    if pair not in m:
      m[pair] = []
    m[pair].append(i)
  print(m)
  for k,v in m.items():
    if max(v) - min(v) >= 2:
      return True
  return False

def one_letter_between(st):
  for i in range(2,len(st)):
    if st[i-2] == st[i]:
      print(st[i-2: i+1])
      return True
  return False

def solve_1(data):
  count = 0

  for st in data:
    if three_vowels(st) and twice_in_row(st) and doesnt_contain_illegal_pairs(st):
      count += 1
  print(count)
  return count

def solve_2(data):
  count = 0

  for st in data:
    if one_letter_between(st) and pair_appears_twice(st) :
      count += 1
      print(st)
  print(count)
  return count

def main():
  data = get_data()
  solve_1(data)
  solve_2(data)

if __name__ == "__main__":
  main()
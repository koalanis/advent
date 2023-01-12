import functools
import random
def get_partitions_rec(data, target, curr, acc, index):
  if target == 0:
    acc.append(curr)
  elif target > 0 and index < len(data):
    consider = data[index]
    if target - consider >= 0 and len(curr) < len(data) - 2:
      next_curr = [c for c in curr]
      next_curr.append(consider)
      get_partitions_rec(data, target-consider, next_curr, acc, index+1) 
    get_partitions_rec(data, target, curr, acc, index+1)
  else:
    pass

def get_partitions(data, target):
  possible_partitions = []
  get_partitions_rec(data, target, [], possible_partitions, 0)
  possible_partitions.sort(key=lambda x: len(x))
  return possible_partitions

def solve_for_bucket_size(data, bucket_size):
  data = [i for i in data]
  data_size = len(data)
  total_sum = sum(data)


  buckets = bucket_size

  bin_size = total_sum//buckets
  data = sorted(data, reverse=True)  

  # we can assume the following from the data:
  #   - the sum of the total weight tw of packages is divisible by three
  #   - there exists a partition of data such that each partition has a sum of tw/3
  #   - the max size of a partition is t-2 where t is the total number of values
  # thus, this problem can be solved by finding the smallest partition that has the sum tw/3
  # if there are multiple partitions of the same size, 
  # the answer is the one which has the smallest product

  partitions = get_partitions(data, bin_size)
  smallest_size = len(partitions[0])
  filtered = filter(lambda x: len(x) == smallest_size, partitions)
  mapped = sorted(map(lambda x: functools.reduce(lambda a,b: a*b, x), filtered))

  print(mapped[0])

def solve_part_1(data):
  solve_for_bucket_size(data, 3)

def solve_part_2(data):
  solve_for_bucket_size(data, 4)

def main():
  data = []
  with open("../../data/day24/data.txt", 'r') as file:
    data = [int(lines.strip()) for lines in file.readlines()]
  
  solve_part_1(data)
  solve_part_2(data)


if __name__ == "__main__":
  main()
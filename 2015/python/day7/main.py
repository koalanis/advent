import os
import queue

import numpy as np

# NOTE: this is a graph traversal problem
# a graph can be made in terms of a a wiring instruction and its dependencies



def get_data():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day7/data.txt", 'r') as file:
    data = [line.strip() for line in file.readlines()]
  return data


def get_data_two():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day7/data2.txt", 'r') as file:
    data = [line.strip() for line in file.readlines()]
  return data


def wiring(txt):
  tokens = txt.split("->")
  return (tokens[0].strip(), tokens[1].strip())

def to_wirings(data):
  wirings = [wiring(t) for t in data]
  return wirings

def define_ops():
  ops = dict()
  
  ops["ASSIGN"] = lambda x : x
  ops["AND"] = lambda x, y : x & y
  ops["OR"] = lambda x, y : x | y
  ops["LSHIFT"] = lambda x, y : x << y
  ops["RSHIFT"] = lambda x, y : x >> y
  ops["NOT"] = lambda x : ~x 
  return ops

OPS = define_ops()

def handle_op(op, data):
  if op in ["ASSIGN", "NOT"]:
    return OPS[op](np.ushort(data[0]))
  else:
    return OPS[op](np.ushort(data[0]), np.ushort(data[1]))

def count_deps(deps):
  i = 0
  for item in deps:
    if not item.isnumeric():
      i += 1
  return i

def parse_atom(atom):
  tokens = atom.split(" ")
  if len(tokens) == 1:
    deps = (atom,)
    return (deps, "ASSIGN")
  elif len(tokens) == 2:
    op = tokens[0]
    val = tokens[1]
    deps = (val,)
    return (deps, op)
  elif len(tokens) == 3:
    val_l = tokens[0]
    op = tokens[1]
    val_r = tokens[2]
    deps = (val_l, val_r)
    return (deps, op)

def to_graph(data):
  dest_map = dict()
  dep_map = dict()
  data_map = dict()
  for tpl in data:
    atom, dest = tpl
    if dest not in dest_map:
      i = parse_atom(atom)
      deps, op = i
      dest_map[dest] = i
      for d in deps:
        if not d.isnumeric():
          if d not in dep_map:
            dep_map[d] = []
          dep_map[d].append(dest)

  data_map = dict()

  q = queue.PriorityQueue()
  for key, val in dest_map.items():
    deps, op = val
    q.put((count_deps(deps), (key,val)))



  to_resolve = 'a'

  while to_resolve not in data_map:
    # print("go")
    to_collapse = []
    while not q.empty():
      # print("gogo")
      pri, data = q.get()
      # print(pri, data)
      if pri == 0:
        # print('gogogog')
        dest, tpl = data
        deps, op = tpl
        value = handle_op(op, deps)
        data_map[dest] = value
        # print(dest, data_map[dest])
        to_collapse.append(dest)
      else: 
        q.put((pri, data))
        break
    
    # print("collapsing")
    for i in to_collapse:
      dest_map.pop(i)
      if i in dep_map:
        # print(f"dep {i} with value {data_map[i]} and is a dep of {dep_map[i]}")
        for to_update in dep_map[i]:
          # print(f"{to_update} {dest_map[to_update]}")
          dest_data = dest_map[to_update]
          deps, op = dest_data
          deps_2 = []
          for d in deps:
            if d == i:
              # print("swapping")
              deps_2.append(str(data_map[d]))
            else:
              deps_2.append(d)
          dest_map[to_update] = (tuple(deps_2), op)
      
    q = queue.PriorityQueue()
    for key, val in dest_map.items():
      deps, op = val
      q.put((count_deps(deps), (key,val)))
    # print(data_map)

    
    
  print(data_map[to_resolve])
  return dest_map

def solve_1(data):
  dest_map = dict()
  dep_map = dict()
  data_map = dict()
  for tpl in data:
    atom, dest = tpl
    if dest not in dest_map:
      i = parse_atom(atom)
      deps, op = i
      dest_map[dest] = i
      for d in deps:
        if not d.isnumeric():
          if d not in dep_map:
            dep_map[d] = []
          dep_map[d].append(dest)

  data_map = dict()

  q = queue.PriorityQueue()
  for key, val in dest_map.items():
    deps, op = val
    q.put((count_deps(deps), (key,val)))



  to_resolve = 'a'

  while to_resolve not in data_map:
    # print("go")
    to_collapse = []
    while not q.empty():
      # print("gogo")
      pri, data = q.get()
      # print(pri, data)
      if pri == 0:
        # print('gogogog')
        dest, tpl = data
        deps, op = tpl
        value = handle_op(op, deps)
        data_map[dest] = value
        # print(dest, data_map[dest])
        to_collapse.append(dest)
      else: 
        q.put((pri, data))
        break
    
    # print("collapsing")
    for i in to_collapse:
      dest_map.pop(i)
      if i in dep_map:
        # print(f"dep {i} with value {data_map[i]} and is a dep of {dep_map[i]}")
        for to_update in dep_map[i]:
          # print(f"{to_update} {dest_map[to_update]}")
          dest_data = dest_map[to_update]
          deps, op = dest_data
          deps_2 = []
          for d in deps:
            if d == i:
              # print("swapping")
              deps_2.append(str(data_map[d]))
            else:
              deps_2.append(d)
          dest_map[to_update] = (tuple(deps_2), op)
      
    q = queue.PriorityQueue()
    for key, val in dest_map.items():
      deps, op = val
      q.put((count_deps(deps), (key,val)))
    # print(data_map)

    
    
  print(data_map[to_resolve])
  return dest_map

def solve_2(data):
  dest_map = dict()
  dep_map = dict()
  data_map = dict()
  for tpl in data:
    atom, dest = tpl
    if dest not in dest_map:
      i = parse_atom(atom)
      deps, op = i
      dest_map[dest] = i
      for d in deps:
        if not d.isnumeric():
          if d not in dep_map:
            dep_map[d] = []
          dep_map[d].append(dest)

  data_map = dict()

  q = queue.PriorityQueue()
  for key, val in dest_map.items():
    deps, op = val
    q.put((count_deps(deps), (key,val)))



  to_resolve = 'a'

  while to_resolve not in data_map:
    # print("go")
    to_collapse = []
    while not q.empty():
      # print("gogo")
      pri, data = q.get()
      # print(pri, data)
      if pri == 0:
        # print('gogogog')
        dest, tpl = data
        deps, op = tpl
        value = handle_op(op, deps)
        data_map[dest] = value
        # print(dest, data_map[dest])
        to_collapse.append(dest)
      else: 
        q.put((pri, data))
        break
    
    # print("collapsing")
    for i in to_collapse:
      dest_map.pop(i)
      if i in dep_map:
        # print(f"dep {i} with value {data_map[i]} and is a dep of {dep_map[i]}")
        for to_update in dep_map[i]:
          # print(f"{to_update} {dest_map[to_update]}")
          dest_data = dest_map[to_update]
          deps, op = dest_data
          deps_2 = []
          for d in deps:
            if d == i:
              # print("swapping")
              deps_2.append(str(data_map[d]))
            else:
              deps_2.append(d)
          dest_map[to_update] = (tuple(deps_2), op)
      
    q = queue.PriorityQueue()
    for key, val in dest_map.items():
      deps, op = val
      q.put((count_deps(deps), (key,val)))
    # print(data_map)

  
  
  print(data_map[to_resolve])
  return dest_map

def main():
  data = get_data()
  data = to_wirings(data)
  solve_1(data)

  data = get_data_two()
  data = to_wirings(data)
  solve_2(data)

if __name__ == "__main__":
  main()

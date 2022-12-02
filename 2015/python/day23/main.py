


import os


def instruction_str_to_tuple(inst_val):
  tokens = inst_val.split(" ")
  instruction = tokens[0]
  if instruction in ["hlf", "tpl", "inc"]:
    return (instruction, tokens[1])
  elif instruction == "jmp":
    return (instruction, int(tokens[1]))
  elif instruction in ["jie", "jio"]:
    return (instruction, tokens[1][:1], int(tokens[2]))


def get_instructions():
  data = []
  with open(f"{os.environ['ADVENT_HOME']}/2015/data/day23/data.txt", 'r') as file:
    data = (line.strip() for line in file.readlines())
  

  return [instruction_str_to_tuple(k) for k in data]


def get_initial_state_p1():
  return {"a": 0, "b": 0, "i_ptr": 0}

def get_initial_state_p2():
  return {"a": 1, "b": 0, "i_ptr": 0}

def handle_instruction(cpu, instruction):
  cpu_next = {k:v for k,v in cpu.items()}
  
  if instruction[0] == "hlf":
    register = instruction[1]
    cpu_next[register] = cpu_next[register] // 2
    cpu_next["i_ptr"] = cpu_next["i_ptr"] + 1
  elif instruction[0] == "tpl":
    register = instruction[1]
    cpu_next[register] = cpu_next[register] * 3
    cpu_next["i_ptr"] = cpu_next["i_ptr"] + 1
  elif instruction[0] == "inc":
    register = instruction[1]
    cpu_next[register] = cpu_next[register] + 1
    cpu_next["i_ptr"] = cpu_next["i_ptr"] + 1
  elif instruction[0] == "jmp":
    register = instruction[1]
    cpu_next["i_ptr"] = cpu_next["i_ptr"] + instruction[1]
  elif instruction[0] == "jie":
    register = instruction[1]
    if cpu_next[register] % 2 == 0:
      cpu_next["i_ptr"] = cpu_next["i_ptr"] + instruction[2]
    else:
      cpu_next["i_ptr"] = cpu_next["i_ptr"] + 1
  elif instruction[0] == "jio":
    register = instruction[1]
    if cpu_next[register] == 1:
      cpu_next["i_ptr"] = cpu_next["i_ptr"] + instruction[2]
    else:
      cpu_next["i_ptr"] = cpu_next["i_ptr"] + 1
  else:
    print("unicorns")

  return cpu_next

def solve_part1(instructions):
  cpu_state = get_initial_state_p1()
  while 0 <= cpu_state["i_ptr"] < len(instructions):
    instr_tuple = instructions[cpu_state["i_ptr"]]
    cpu_state = handle_instruction(cpu_state, instr_tuple)

  print(cpu_state["b"])
  return cpu_state["b"]

def solve_part2(instructions):
  cpu_state = get_initial_state_p2()
  while 0 <= cpu_state["i_ptr"] < len(instructions):
    instr_tuple = instructions[cpu_state["i_ptr"]]
    cpu_state = handle_instruction(cpu_state, instr_tuple)

  print(cpu_state["b"])
  return cpu_state["b"]

def main():
  instructions = get_instructions()
  
  solve_part1(instructions)
  solve_part2(instructions)


if __name__ == "__main__":
  main()

  
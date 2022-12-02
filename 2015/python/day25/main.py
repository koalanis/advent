

multiply_by = 252533
divide_by = 33554393

def to_index(row, col):
    diagonal_line = 0
    r,c = row,col
    distance = 0
    print(f"r={r},c={c}")
    while c > 1:
        r = r+1
        c = c-1
        distance += 1
    diagonal_line = r
    diagonal_start = 1
    sum_inc = 0

    for i in range(diagonal_line):
        diagonal_start += sum_inc
        sum_inc += 1
    
    code_at = diagonal_start + distance
    return code_at

problem_row, problem_col = 3010, 3019

problem_idx = to_index(problem_row, problem_col)

first_num = 20151125


def find_code(idx):
    acc = 1
    for i in range(1,idx+1):
        if i == 1:
            acc = first_num
        else:
            acc = (acc * multiply_by) % divide_by

    return acc


def main():
    print(find_code(problem_idx))

if __name__ == "__main__":
    main()



# 8997277
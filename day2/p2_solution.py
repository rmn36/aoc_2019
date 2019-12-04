def op(pos, arr):
    opcode = arr[pos]
    in_pos_1 = arr[pos+1]
    in_pos_2 = arr[pos+2]
    out_pos = arr[pos+3]
        
    if opcode == 1:
        arr[out_pos] = arr[in_pos_1] + arr[in_pos_2]
    elif opcode == 2:
        arr[out_pos] = arr[in_pos_1] * arr[in_pos_2]
    elif opcode == 99:
        pass
    else:
        print(f'Opcode# {opcode} at Position# {pos}')
        exit(1)
    
    return arr

def run(noun, verb):
    arr = list(map(lambda x: int(x),open('input.csv').readline().split(',')))
    arr[1] = noun
    arr[2] = verb
    pos = 0
    while arr[pos] != 99:
        op(pos, arr)
        pos += 4

    return arr[0]

for i in range(0, 99):
    for j in range(0, 99):
        out = run(i, j)
        if out == 19690720:
            print(100 * i + j)
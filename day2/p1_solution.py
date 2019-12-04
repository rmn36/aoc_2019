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

arr = list(map(lambda x: int(x),open('input_1202.csv').readline().split(',')))
pos = 0
while arr[pos] != 99:
    op(pos, arr)
    pos += 4

print(arr[0])
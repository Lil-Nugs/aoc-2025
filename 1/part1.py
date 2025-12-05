input_file = 'input.txt'

start_num = 50
zero_counts = 0

with open(input_file, 'r') as file:
    rotations = [line.strip() for line in file]

for rotation in rotations:
    direction, rotation_count = rotation[0], int(rotation[1:])
    rotation_count = rotation_count % 100

    if direction == 'L':
        start_num = (start_num - rotation_count) % 100
    if direction == 'R':
        start_num = (start_num + rotation_count) % 100
    if start_num == 0:
        zero_counts += 1

print(zero_counts)

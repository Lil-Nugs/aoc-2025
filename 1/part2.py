input_file = 'input.txt'
rotations = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
start_num = 50
zero_counts = 0

with open(input_file, 'r') as file:
    rotations = [line.strip() for line in file]

for rotation in rotations:
    direction, rotation_count = rotation[0], int(rotation[1:])
    zero_counts += rotation_count // 100
    rotation_count = rotation_count % 100

    if direction == 'L':
        end_num = (start_num - rotation_count) % 100
        if end_num != 0 and start_num != 0 and end_num > start_num:
            zero_counts += 1
    if direction == 'R':
        end_num = (start_num + rotation_count) % 100
        if end_num != 0 and start_num != 0 and end_num < start_num:
            zero_counts += 1

    if end_num == 0:
        zero_counts += 1

    print(f"Rotation: {rotation}\nStarted at: {start_num}\nEnded at: {end_num}")
    print(f"Zero counts: {zero_counts}")
    print("==================")

    start_num = end_num
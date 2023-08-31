# Read input file
with open('input.txt') as f:
    lines = f.readlines()

current_sum_of_calories = 0
max_calories = 0

for line in lines:
    if line.strip() == '':
        if current_sum_of_calories > max_calories:
            max_calories = current_sum_of_calories
        current_sum_of_calories = 0
    else:
        current_sum_of_calories += int(line)

print('# of Calories it Contains: ', max_calories)
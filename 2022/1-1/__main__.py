# Read input file
with open('input.txt') as f:
    lines = f.readlines()

current_sum_of_calories = 0
max_calories = 0
calories = []

for line in lines:
    if line.strip() == '':
        if current_sum_of_calories > max_calories:
            max_calories = current_sum_of_calories
        calories.append(current_sum_of_calories)
        current_sum_of_calories = 0
    else:
        current_sum_of_calories += int(line)

calories.sort(reverse=True)
print("# of Calories from top 3 elves: ", sum(calories[:3]))
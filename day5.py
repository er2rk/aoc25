#Part1
list_food = []
with open("day5input") as data:
    for line in data:
        line = line.strip()
        list_food.append(line)

bool_fresh = True

list_fresh = []
list_fridge = []

for item in list_food:
    if item == '':
        bool_fresh = False
    else:
        if bool_fresh:
            list_fresh.append(item)
        else:
            list_fridge.append(item)

count = 0
for food in list_fridge:
    food_number = int(food)
    for fresh_range in list_fresh:
        range_numbers = fresh_range.split("-")
        start = int(range_numbers[0])
        end = int(range_numbers[1])
        if start <= food_number and end >= food_number:
            count += 1
            break

"""
Part 2
Todays problems are quite easy. Except this one has to worry about overlapping.
If the ranges weren't so large we could just keep them in a list but they are huge. ie 526859759527027-530903630595569
Maybe i can use a little set theory. I'll take the union of the sets. AuB = A+B - AnB
Couldn't figure the implementation of this one on my own. Credits to this post: 
https://old.reddit.com/r/adventofcode/comments/1penqq2/2025_day_5_part_2_visualization_for_the_sample/
"""
#Constructing the interval sets.
pois = []
for fresh_range in list_fresh:
    range_numbers = fresh_range.split("-")
    pois.append((int(range_numbers[0]), int(range_numbers[1])+1))

#This solution wouldn't work without sorting the sets. 
intervals = sorted(pois)

merged = []
current_start, current_end = intervals[0]

#Handle the union of sets.
for start, end in intervals[1:]:
     # The start of the 2nd set, end of the first set
    if start <= current_end:    
        current_end = max(current_end, end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))

#Finally count all set intervals.
total = 0
for start, end in merged:
    total += end - start #Don't need to add one as we already did it in the construction of the sets.

print(total)

    

        
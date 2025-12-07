from collections import defaultdict

lines = []
with open("day7input") as data:
    for line in data:
        line = line.strip()
        lines.append(line)

#141
length = len(lines[0])
#70, right in the middle.
starting_position = 0
for i in range(length):
    if lines[0][i]=="S":
        starting_position = i
        break

#Could work with lists and check for duplicates but python's sets eliminates this issue.
beams = set()
beams.add(starting_position)

#Check one line.
def helper(beams, string):
    new_beams = set()
    splitter_count = 0
    for beam in beams:
        #first check if the beam is in the right range
        if 0 <= beam < len(string):
            #if it hits a beam split it
            if string[beam] == "^":
                splitter_count += 1
                new_beams.add(beam-1)
                new_beams.add(beam+1)
            #if not let it continue.
            else:
                new_beams.add(beam)  
    return new_beams, splitter_count

#We don't have to check every line, start at index 2 then increment by 2 until index > length-1
i = 2
tree_length = len(lines)
hit_splitter = 0
while i < tree_length-1:
    #just a simple illustration for myself
    pretty_line = ""
    for x in range(tree_length-1):
        if x in beams:
            pretty_line += "|"
        else:
            pretty_line +="."
    print(pretty_line)
    #the actual counter part 1
    new_beams, splitter_count= helper(beams, lines[i])
    beams = new_beams
    hit_splitter += splitter_count
    i += 2

print(hit_splitter)

#Trying to find the easiest solution for part 2.
#Keeping the amount of timelines at each position in the string
timelines = defaultdict(int)
timelines[starting_position] = 1

#resetting i for the loop
i = 2

#Same loop structure as part 1.
while i < tree_length:
    next_timelines = defaultdict(int)
    
    # Iterate through all positions where timelines currently exist
    for pos, count in timelines.items():
        if 0 <= pos < len(lines[i]):
            char = lines[i][pos]   
            if char == "^":
                next_timelines[pos - 1] += count
                next_timelines[pos + 1] += count
            else:
                next_timelines[pos] += count

    timelines = next_timelines
    i += 2

total_timelines = sum(timelines.values())
print(total_timelines)








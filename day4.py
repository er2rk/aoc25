shelves = []

with open("day4input") as data:
    for line in data:
        line = line.strip()
        shelves.append(line)

#Each end up being 140.
width = max(len(s) for s in shelves)
length = len(shelves)
#So for the sake of brevity.
size = 140

#Helper function so see if a given point is accessible
#ri is the string index in the list, ci is the char index in the string.
def helper(shelves, ri, ci):
    neighbours = [
        #The upper neighbours
        (-1, -1), (-1, 0), (-1,1),
        #Same line neighbours
        (0, -1), (0, 1),
        #Downstairs neighbours
        (1, -1), (1,0), (1,1)
    ]
    adj_count = 0
    
    #This is the hard part for the general solution. Checking for middle positions is easy because they exist.
    #But the edges require an implementation where if there is no neighbour it must be count as empty.
    for rdelta, cdelta in neighbours:
        neighbour_row = ri + rdelta
        neighbour_column = ci + cdelta

        #If the position we find is out of bounds either at row index or col index we'll consider it empty.
        if 0 <= neighbour_row < size and 0 <= neighbour_column < size:
            if shelves[neighbour_row][neighbour_column] == '@':
                adj_count += 1
    
    #finally return boolean. the incrementation will happen in main function.
    return adj_count < 4

def countAccessible(shelves):

    #Starting with 0
    accessibleCount = 0
    #Adding this for part 2.
    positions = []
    #I don't know how python behaves when it's given an index out bounds. We'll see.
    for ri in range(size):
        for ci in range(size):
            if shelves[ri][ci] == '@':
                if helper(shelves, ri, ci):
                    accessibleCount += 1
                    positions.append((ri,ci))
    return accessibleCount, positions

#Jesus that was hard. Big jump from day three.

#Part 2
#Seemed really hard at first but looking at the example i am supposed to un the function once, replace @ with dots.
#Then run the function again until we can't remove anything.
# Let's change the function above to keep positions of paper removed.

accessibleSum = 0

while True:

    count, positions = countAccessible(shelves)
    print(count)

    if count == 0:
        break
    else:
        accessibleSum += count
        for(ri, ci) in positions:
            string = shelves[ri]
            new_string = string[:ci] + "." + string[ci+1:]
            shelves[ri] = new_string

print(accessibleSum)

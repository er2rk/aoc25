nums = []
with open("day6input") as data:
    for line in data:
        line = line.strip()
        ints = list(line.split())
        nums.append(ints)

"""
Part1
We have a list of lists of strings.
We're going to iterate over the length (1000) of each list (5).
There doesn't seem to be any empty space, all lists are equally sized so no need to check that either.
"""

total = 0
line_length = len(nums[0])
line_count = len(nums)
for index in range(line_length):
    #Two operations, addition or multiplication.
    if nums[-1][index] == "+":
        result = 0
        #not counting the first one.
        for index2 in range(line_count-1):
            result += int(nums[index2][index])

    #multiplication
    else:
        result = 1
        for index2 in range(line_count-1):
            result *= int(nums[index2][index])

    total += result


#Part2
#A little hard to construct the numbers as they are of different lengths.
#I know it's a bad solution but i've got an exam at noon and i gotta get this finished.
total = 0
line_length = len(nums[0])
line_count = len(nums)
for index in range(line_length):
    #This time we'll get the string on each line and construct the numbers on a different list first.
    #cephalopod list, we'll keep them as strings to be able to use [index]
    c_list=[]
    for index2 in range(line_count-1):
        c_list.append(nums[index2][index])
    #i know i should find it here but the data shows us the longest integer is 4 digits.
    max_length = 4
    new_list = []
    for c in c_list:
        string_size = len(c)
        while string_size < max_length:
            c = c + " "
            string_size += 1
        new_list.append(c)
    new_list.append(nums[-1][index])

    print(new_list)


    



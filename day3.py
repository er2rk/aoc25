banks = []

with open("day3input") as data:
    for line in data:
        line = line.strip()
        banks.append(line)

#We have the banks stored as a string now.

#Let's use a helper function. Make the code a little cleaner.
def voltageHelper(bank):
    max = int(bank[0])
    max_pointer = 0
    size = len(bank)
    #first we're going to find the largest integer.
    for i in range(size):
        max_candidate = int(bank[i])
        if max_candidate > max:
            max = max_candidate
            max_pointer = i
    #We have two cases. If the max is in the last index we have to find the largest one before it.
    #If it's at any other place we look for indexes after it.
    
    if max_pointer == size-1:
        second_max = int(bank[0])
        for i in range(size-1):
            max_candidate = int(bank[i])
            if max_candidate > second_max:
                second_max = max_candidate
                #no need for a pointer change here.
        result = second_max * 10 + max
        return result
    else:
        #Same logic as the first for loop. Except we start it at the pointer.
        second_max = int(bank[max_pointer+1])
        for i in range(max_pointer+1, size):
            max_candidate = int(bank[i])
            if max_candidate > second_max:
                second_max = max_candidate
                #Again no need for a pointer
        result = max*10 + second_max
        return result

#part1
total_voltage = 0
for bank in banks:
    voltage = voltageHelper(bank)
    total_voltage += voltage

print(total_voltage)



        






        
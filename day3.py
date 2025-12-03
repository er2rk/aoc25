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
"""
total_voltage = 0
for bank in banks:
    voltage = voltageHelper(bank)
    total_voltage += voltage

print(total_voltage)
"""
#part 2
#VIP VERY GOOD PROBLEM! A GENERAL SOLUTION IS MADE FOR THIS.
#using the same banks array.
#will also go through the same logic iterating through them. except we'll use a second helper function.

#This is a much harder problem which needs a general solution.
#At first i thought about a recursive solution but because we need to keep the order it was going to get very complex very fast.
#So instead of taking something and attaching it to another let's use two pointer logic one from left one from right.
#If the one on the right is smaller than the one on the left we remove it.  
def voltageHelper2(bank):
        #Going with this logic we'll only remove as many as we need. 
        remove = len(bank) - 12
        #We'll keep the values in stack. 
        stack = []

        #Iterating through each character.
        for d in bank:
            #If we have to remove more, stack has element and the last one is smaller than what we currently have.
            #Then we remove the last one and put what we currently have in.
            #Would have to implement the stack from scratch if this was Java but we can use python's list which kind of acts like a stack.
            while remove > 0 and stack and stack[-1] < d:
                stack.pop()
                remove -= 1
            stack.append(d)

        # In case we didn't remove enough we get the first 12 characters.
        result_digits = stack[:12]
        return int("".join(result_digits))









total_voltage = 0
for bank in banks:
    voltage = voltageHelper2(bank)
    total_voltage += voltage

print(total_voltage)



        






        
pos = 50
count = 0
N = 100

#Part 1.
with open("day1input") as data:
    for line in data:
        line = line.strip()
        direction = line[0]
        value = int(line[1:])

        if direction == "R":
            pos += value
        else:
            pos -= value

        #Got this trick from GPT. The previous version had %N for numbers greater than 99 and N+pos for the negatives.
        pos %= N

        if pos == 0:
            count += 1

print(count)


#Let's set these to the initial positions again.
pos = 50
count = 0
N = 100

#Part 2
#The processing part is the same.
with open("day1input") as data:
    for line in data:
        line = line.strip()  
        direction = line[0]
        value = int(line[1:])

        start_pos = pos
        clicks = 0

        #The positive case is simple enough.
        if direction == "R":
            end_pos = start_pos + value
            #Get the clicks
            clicks = end_pos // N

            #Update the actual position
            pos = end_pos % N

        #The negative case is very tricky. 
        #The start position is always [0,99] so we have two cases.     
        else:
            
            #We start at 0.
            if start_pos == 0:
                clicks = value // N

            #We start at any other number till 99.   
            else:
                #For there to be a click the value must be greater than the starting position. For example: start_pos 50, value: 80 --> 70. One click.
                if value >= start_pos:
                    #Kind of like the queue logic for findings it's element count. Not it's size.
                    clicks = (value - start_pos + N) // N
                #Value is smaller than start_pos. No click.
                else:
                    clicks = 0

            #Update position
            pos = (start_pos - value) % N
            
        #Finally add the clicks to the total count.
        count += clicks

print (count)



        


    
    




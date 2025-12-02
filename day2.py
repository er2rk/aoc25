#renamed range in work_data to data.
#don't use reserved names for python. While it will work if you don't call the function python has, if you do you'll have to change all occurences.
#part1
#Get the line --> Process range (Seperate them and get the start-end ints from them.) 
# --> Put em in an array. --> Go through each range with iteration.
#Normally we wouldn't even check the starting 0 requirement if not for that last range 1-19.
#Let's first work on checking if the id contains two of the same number. Might be one digit, two digit .... etc.

work_data = []

#This is why i love python man. 2 lines to process a file. Don't even need to import anything.
with open("day2input") as data:
    #We have 1 line in the file but whatever. Just copy paste from day one.
    for line in data:
        #Gets rid of the \n at the end of the file.
        line = line.strip()
        #First split the ranges, identified with the comma.
        ranges = line.split(",")
        #Then put the ranges in an array. Again, gotta love python and it's standard library.
        work_data = [range.split('-') for range in ranges]

#Alright now we have data to work with.
#I thought maybe i would add everything to a list then sum it up but no need.
sum = 0
#Again we must work with the string but iterate with an integer.
for data in work_data:
    start = int(data[0])
    end = int(data[1])
    while start <= end:
        #String version of start to work with.
        work_start = str(start)
        size = len(work_start)
        #First check, see if the number starts with 0.
        if work_start[0] == "0":
            #Add the number to the sum.
            sum += start
        #Using elif so we don't double count the faulty ids. Also we'll go with an easy check before the important one first.
        #If the number size is not even then it cannot have two of the same thing only. example: 22, 654654 etc.
        elif size % 2 != 0:
            pass
        #finally the important part.
        else:
            #The string size must be even. If it is even we can divide it by half and check if they are equal.
            middle =size//2
            half1 = work_start[:middle]
            half2 = work_start[middle:]
            if half1 == half2:
                sum += start
        start += 1

print(sum)

#No need to reset anything for part2. We're going to work with work_data which is unchanged. Except sum i guess.
sum = 0

#part2 
#Same logic applies for iteration except the checking part.
#I think we can apply a similar logic to this one as we did on part one.
#We can start at two, use boolean logic to stop if we get a bad id. Else continue until we are at size-1
for data in work_data:
    start = int(data[0])
    end = int(data[1])
    while start <= end:
        work_start = str(start)
        size = len(work_start)
        invalid_id = False
        if work_start[0] == '0':
            is_invalid = True
        #Bad part about python? Can't put ! before a boolean like we do in java etc. gotta use keywords.
        if not invalid_id:
            #Just like how the string size need to have a 0 remainder from 2 in part 1, here also it must do the same for integers bigger than that.
            #VIP!!! IF YOU GOTTA USE RANGE FUNCTION, YOU CANNOT HAVE A VARIABLE CALLED RANGE YOU BIG DUMMY!
            for temp_size in range(1, size):
                if size % temp_size == 0:
                    repeat = work_start[:temp_size]
                    slices = size // temp_size
                    #Had to get help from GPT for this one. Turns out in python you can mulitply strings. How lovely!
                    if repeat * slices == work_start:
                        invalid_id = True
                        break
        if invalid_id:
            sum += start
            
        start += 1

print(sum)



        

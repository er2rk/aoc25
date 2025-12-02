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
for range in work_data:
    start = int(range[0])
    end = int(range[1])
    while start <= end:
        #String version of start to work with.
        work_start = str(start)
        size = len(work_start)
        #First check, see if the number starts with 0.
        if work_start[0] == "0":
            #Add the number to the sum.
            sum += start
        #Using elif so we don't double count the faulty ids. Also we'll go with an easy check before the important one first.
        #If the number length is not even then it cannot have two of the same thing only. example: 22, 654654 etc.
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




        

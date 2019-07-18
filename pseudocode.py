#Make the list
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

#Add all the numbers together
sum = 0
for num in ages:
        sum += num
        #or use sum = sum(ages)
#sum = sum(ages)
        #is easier

#Find the Length of the lists
length = len(ages)

#divide the sum by the Length
average = sum/length

#print the average
print(average)

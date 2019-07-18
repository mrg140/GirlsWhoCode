#Picking Highest Number
a = [5, 3 , 7, 1 ,8]
print (sorted(a)) #sorts list from lowest to highest, meaning you automatically know that the last number is the highest number
    #print list a from lowest to highest values
print (a[len(a)-1]) #prints last number, as the value in the square brackets = index/place number, but since index starts from 0 and length considers length of list, to get index, index= length-1
    #print list a, but pick the last number using [index], where index = length of list a - 1.

#Multiply all the numbers in the list
b = [5, 6, 2, 9, 8]
product =1
for num in b:
    product *= num

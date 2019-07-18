Closet = ["shirt", "pants", 25]
Numbers = [0.2, 13, 2.5, 22]
#Must use square brackets for lists, otherwise it will not be considered a list
# len() = The amount of things in the list
# len is index plus 1
    #index considers 0 as a number (EX: Range of 5 is 0, 1, 2, 3, 4)
    #index is the placement number of the thing in a list
print(len(Closet))
print(Closet[1])
print(25 in Closet) #true
print("shoe" in Closet) #false
for item in Closet:
    print (item) #prints shirt, pants, 25
#print(len(numbers))
#print(numbers[0])
print ("yes")
for num in range(len(Closet)):
    print (Closet[num])
print ("no")
Closet.append("socks") #to add socks at the end of the list
print (Closet)
#put brackets around Closet so it knows to print the LIST Closet not the word Closet
Letters = ["G", "A", "H", "F", Numbers, Closet]
print (Letters)
#Able to put lists in lists but they must be identified first, such as number and Closet

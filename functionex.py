def is_even(sum):
    if sum % 2 == 0:
        return True
    else:
        return False
def add(num1, num2):
    sum = num1 + num2
    is_even(sum)
    return is_even(sum)

list = [1, 4, 9 , 2, 5]

def calc_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum
        #add all of the numbers in the list
print (add(1,2))

print (calc_total(list))

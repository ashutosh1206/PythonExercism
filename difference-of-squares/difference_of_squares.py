def sum_of_squares(lim):
    i=1
    sumnum=0
    while i <= lim:
        sumnum = sumnum + i**2
        i = i + 1
    return sumnum

def square_of_sum(lim):
    i=1
    sum2 = 0
    while i <= lim:
        sum2 = sum2 + i
        i = i + 1
    square = sum2**2
    return square

lim = input("Enter the count of numbers to be used to calculate the difference between the sum of squares and the square of sum: ")
d1 = sum_of_squares(lim)
d2 = square_of_sum(lim)
print "The difference between the square of sum and the sum of squares is",d2-d1
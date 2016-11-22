x1 = input("Enter the x-coordinate of queen 1: ")
y1 = input("Enter the y-coordinate of queen 1: ")
x2 = input("Enter the x-coordinate of queen 2: ")
y2 = input("Enter the y-coordinate of queen 2: ")
if y1 == y2: 
    print "The queens can attack vertically"
    fl = 1
elif x1 == x2:
    print "The queens can attack horizontally"
    fl = 1
else:
    c = abs(x2 - x1)
    y3 = y1 - c 
    y4 = y1 + c
    if (y2 == y3) or (y2 == y4):
        print "The queens can attack diagonally!"
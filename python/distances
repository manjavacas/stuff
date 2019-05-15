import math

x1 = input('Point 1, x = ')
y1 = input('Point 1, y = ')
x2 = input('Point 2, x = ')
y2 = input('Point 2, y = ')

""" Points """
p1 = (int(x1), int(y1))
p2 = (int(x2), int(y2))

""" Chebyshev distance """
cd = max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

""" Euclidean distance """
ed = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

""" Manhattan distance """
md = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print('\nPoints: ' + str(p1) + ', ' + str(p2) + '\n* Chebyshev distance: ' + str(cd) + 
      '\n* Euclidean distance: ' + str(ed) + '\n* Manhattan distance: ' + str(md))


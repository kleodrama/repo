from visual import *

import csv


with open('test.csv', 'rU') as f:
    reader = csv.reader(f)
    sailpoints = list(reader)
    


print sailpoints

points(pos=[(1,0),
	    (0,1),
	    (1,1),
	    (1,2)], size=1, color=color.red)




#for x in sailpoints:
#points(pos=x, size=1, color=color.red)

#for x in sailpoints:
#points(pos=x, size=1, color=color.red)

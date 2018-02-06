import csv
import numpy
from scipy import stats
class makeObject:
    name = ""
    age = 0
    hobbies = []
    def __init__(self, var1, var2, var3):
    	self.count = var1
        self.speed= var2
        self.dist= var3

my_list = []

with open('CARS.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(makeObject(row[0], row[1], row[2:]))
my_list.pop(0)
speed=[]
dist=[]

	
for obj  in my_list:
	speed.append(float(obj.speed))
	dist.append(float(obj.dist[0]))
print "---------------Speed-----------------"	
print "\tMean:%f" %numpy.mean(speed)
print "\tHarmonic mean:%f" % stats.hmean(speed)
print "\tGeometric mean:%f" % stats.gmean(speed)
print "\n---------------Distance-----------"	
print "\tMean:%f" %numpy.mean(dist)
print "\tHarmonic mean:%f" % stats.hmean(dist)
print "\tGeometric mean:%f\n" % stats.gmean(dist)
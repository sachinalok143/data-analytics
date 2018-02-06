# NOMINAL:symboling, city-mpg,highway-mpg

# ORDINAL:normalized-losses,engine-size, bore  ,stroke ,horsepower ,peak-rpm ,price , horsepower 


# INTERVAL:wheel-base,length,width,height,curb-weight


# RATIO:num-of-doors,num-of-cylinders,compression-ratio 



# make,fuel-type,aspiration,body-style,drive-wheels,engine-location,engine-type,fuel-system 



import pandas as pd
import numpy as np
from statistics import mode
from statistics import median
data = pd.read_csv("AUTOMOBILES.csv")
# for i in xrange(0,len(data)):
# 	print "%s \t %s " % (data['peak-rpm'][i],data['city-mpg'][i])

cityMpg=[]
engineSize=[]
curbWeight=[]
compressionRatio =[]
for i in xrange(0,len(data)):
	cityMpg.append(float(data['city-mpg'][i]))
	engineSize.append(float(data['engine-size'][i]))
	curbWeight.append(float(data['curb-weight'][i]))
	compressionRatio.append(float(data['compression-ratio'][i]))
print "+++++++++++City Mapping++++++++++"
print	"+\tMean:%d\t\t\t+" % np.mean(cityMpg)
print	"+\tMode:%d\t\t\t+" % mode(cityMpg)
print	"+\tMedian:%d\t\t+" % median(cityMpg)
print "+++++++++++++++++++++++++++++++++\n"


print "+++++++++++Engine Size ++++++++++"
print	"+\tMean:%d\t\t+" % np.mean(engineSize)
try:
	print	"+\tMode:%d\t\t\t+" % mode(engineSize)
except Exception as e:
	print "+\tNo unique mode found\t+"
print	"+\tMedian:%d\t\t+" % median(engineSize)
print "+++++++++++++++++++++++++++++++++\n"

print "+++++++++++Curb Weight++++++++++"
print	"+\tMean:%d\t\t+" % np.mean(curbWeight)
print	"+\tMode:%d\t\t+" % mode(curbWeight)
print	"+\tMedian:%d\t\t+" % median(curbWeight)
print "+++++++++++++++++++++++++++++++++\n"

print "+++++++++Compression Rati++++++++"
print	"+\tMean:%d\t\t\t+" % np.mean(compressionRatio)
print	"+\tMode:%d\t\t\t+" % mode(compressionRatio)
print	"+\tMedian:%d\t\t+" % median(compressionRatio)
print "+++++++++++++++++++++++++++++++++\n"
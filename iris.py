import random
import pandas as pd
import numpy as np
# from scipy import stats

data = pd.read_excel("IRIS.xlsx",sheat='sheat1')
# print data
ran=random.randint(0,100)   
# print ran
SepalLengthCm=[]
PetalLengthCm=[]
SepalWidthCm=[]
PetalWidthCm=[]
for i in xrange(0,len(data)):
    SepalLengthCm.append(float(data['SepalLengthCm'][i]))
    SepalWidthCm.append(float(data['SepalWidthCm'][i]))
    PetalLengthCm.append(float(data['PetalLengthCm'][i]))
    PetalWidthCm.append(float(data['PetalWidthCm'][i]))
print "+++++++++++++++++++MEAN++++++++++++++++++"
print	"+\tSepal Length:%d\t\t\t+" % np.mean(SepalLengthCm)
print	"+\tSepal Width:%d\t\t\t+" % np.mean(SepalWidthCm)
print	"+\tPetal Length:%d\t\t\t+" % np.mean(PetalLengthCm)
print	"+\tPetal Width:%d\t\t\t+" % np.mean(PetalWidthCm)
print "+++++++++++++++++++++++++++++++++++++++++\n"
SepalWidthCmFullVar=np.var(SepalWidthCm)
SepalLengthCmFullVar=np.var(SepalLengthCm)
PetalWidthCmFullVar=np.var(PetalWidthCm)
PetalLengthCmFullVar=np.var(PetalLengthCm)

for i in xrange(ran,ran+50):
	SepalLengthCm.append(float(data['SepalLengthCm'][i]))
	SepalWidthCm.append(float(data['SepalWidthCm'][i]))
	PetalLengthCm.append(float(data['PetalLengthCm'][i]))
	PetalWidthCm.append(float(data['PetalWidthCm'][i]))

SepalWidthCm50Var=np.var(SepalWidthCm)
SepalLengthCm50Var=np.var(SepalLengthCm)
PetalWidthCm50Var=np.var(PetalWidthCm)
PetalLengthCm50Var=np.var(PetalLengthCm)

print "-------------------Sepal Length------------------------"
print	"\t \tall data :%f" %SepalLengthCmFullVar
print	"\t random 50 data :%f" %SepalLengthCm50Var

print "\n-------------------Sepal Width------------------------"
print	"\t \tall data :%f" %SepalWidthCmFullVar
print	"\t random 50 data :%f" %SepalWidthCm50Var

print "\n-------------------Petal Length------------------------"
print	"\t \tall data :%f" %PetalLengthCmFullVar
print	"\t random 50 data :%f" %PetalLengthCm50Var

print "\n-------------------Petal Width------------------------"
print	"\t \tall data :%f" %PetalWidthCmFullVar
print	"\t random 50 data :%f" %PetalWidthCm50Var
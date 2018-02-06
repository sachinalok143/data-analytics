import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel("EARTHQUAKE.xlsx",sheat='sheat1')
# print data    
Latitude=[]
Longitude =[]
DepthPerKm=[]
Magnitude=[]
for i in xrange(0,len(data)):
    Latitude.append(float(data['Latitude'][i]))
    Longitude.append(float(data['Longitude'][i]))
    DepthPerKm.append(float(data['Depth/Km'][i]))
    Magnitude.append(float(data['Magnitude'][i]))

def fivenum(v): 
    import numpy as np
    from scipy.stats import scoreatpercentile
    try:
        np.sum(v)
    except TypeError:
        print('Error: you must provide a list or array of only numbers')
    q1 = scoreatpercentile(v,25)
    q3 = scoreatpercentile(v,75)
    iqd = q3-q1
    md = np.median(v)
    whisker = 1.5*iqd
    return np.min(v), md-whisker, md, md+whisker, np.max(v),


def plot(data1,data2,data3,data4):
    import matplotlib.pyplot as plt
    import numpy as np
    data=[data1,data2,data3,data4]
    plt.figure()
    plt.boxplot(data,0)
    plt.show()
def plot1(data1,data2,data3,data4):
    import matplotlib.pyplot as plt
    import numpy as np
    data=[data1,data2,data3,data4]
    plt.figure()
    plt.boxplot(data,0)
    plt.show()
# print(fivenum( Latitude))
Latitude_points=fivenum(Latitude)
Longitude_points=fivenum(Longitude)
DepthPerKm_points=fivenum(DepthPerKm)
Magnitude_points=fivenum(Magnitude)
plot (Latitude_points,Longitude_points,DepthPerKm_points,Magnitude_points)

# def reject_outliers(data):
#     m=2
#     return data[abs(data - np.mean(data)) < m * np.std(data)]

def reject_outliers(data):
    m = 2
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

Longitude=reject_outliers(Longitude)
Latitude=reject_outliers(Latitude)
DepthPerKm=reject_outliers(DepthPerKm)
Magnitude=reject_outliers(Magnitude)

Latitude_points=fivenum(Latitude)
Longitude_points=fivenum(Longitude)
DepthPerKm_points=fivenum(DepthPerKm)
Magnitude_points=fivenum(Magnitude)
plot1 (Latitude_points,Longitude_points,DepthPerKm_points,Magnitude_points)

from datetime import datetime
from datetime import timedelta
from random import randrange
from random import uniform
import numpy as np



def populate_sources_by_group():
    f = open("sources.csv", "a")         
    f.write("House A,Termostate A1,\"{'Model number':'EB-STATE5-01','Min temperature':'45F','Max temperature':'92F','Temperature sensitivity':'1F','Min humidity':'5%','Max humidity':'95%','Humidity sensitivity':'1%'}\",primary residence")
    f.write("\n")
    f.write("House A,Termostate A2,\"{'Model number':'EB-STATE5-01','Min temperature':'45F','Max temperature':'92F','Temperature sensitivity':'1F','Min humidity':'5%','Max humidity':'95%','Humidity sensitivity':'1%'}\",primary residence")       
    f.write("\n")
    f.write("House A,Refrigerator A1,\"{'Model number':'RF28R7551SG','Capacity':'15.6 cubic feet'}\",primary residence")
    f.write("\n")
    f.write("House A,Freezer A1,\"{'Model number':'RF28R7551SG','Capacity':'8.3 cubic feet'}\",primary residence")
    f.write("\n")
    f.write("House B,Termostate B1,\"{'Model number':'EB-STATE5-01','Min temperature':'45F','Max temperature':'92F','Temperature sensitivity':'1F','Min humidity':'5%','Max humidity':'95%','Humidity sensitivity':'1%'}\",vacation home")
    f.write("\n")
    f.write("House B,SmartSensor B1,\"{'Model number':'EB-RSHM2PK-01'}\",vacation home")
    f.write("\n")
    f.write("House B,SmartSensor B2,\"{'Model number':'EB-RSHM2PK-01'}\",vacation home")
    f.write("\n")
    f.close()


def populate_metrics():
    f = open("metrics.csv", "a")         
    f.write("all,temperature,Fahrenheit")
    f.write("\n")    
    f.write("all,humidity,% Relative Humidity")
    f.write("\n")
    f.write("all,occupancy,True/False or 1/0")                                  
    f.write("\n")
    f.close()

    

def populate_time_series(group,source,metric,min_value,max_value):
    # Open files
    f1 = open("series_high_resolution.csv", "a")     
    f2 = open("series_low_resolution.csv", "a")     
    f3 = open("statistics_by_source_metric.csv", "a")     
    
    # Time series parameters
    latest_timestamp = datetime.now().replace(second=0, microsecond=0)
    midnight_timestamp = latest_timestamp.replace(minute=0, hour=0)
    resolution_60s = timedelta(seconds=60) # High resolution - every 60 seconds
    resolution_60m = timedelta(minutes=60) # Low resolution - every 60 minutes
    num_points_high = 10 * 24 * 60  # Minutes in 10 days - number of high resolution points        
    num_points_low = 2 * 365 * 24 # Hours in 2 years - number of low resolution points
    points_60s = []
    points_60m = []
    
    # Compute high resolution points
    for i in range(0,num_points_high):
        point = randrange(min_value, max_value + 1, 1)
        points_60s.append( point )
        if ((i + 1) % 60) == 0:
            points_60m.append( round( np.mean( points_60s[i - 60 + 1 : i + 1] ), 2 ) )
            
    # Compute low resolution points        
    for i in range(len(points_60m),num_points_low):
        point = round( uniform(min_value, max_value), 2 )
        points_60m.append( point )            
        
    # Populate high resolution tables
    for i in range(0,num_points_high):
        point = points_60s[i]      
        timestamp = latest_timestamp - i * resolution_60s      
        f1.write(group + "," + source + "," + str(timestamp) + "," + metric + "," + str(point))
        f1.write("\n")

    # Populate low resolution tables
    for i in range(0,num_points_low):
        point = points_60m[i]     
        timestamp = latest_timestamp - i * resolution_60m       
        f2.write(group + "," + str(timestamp.year) + "," + source + "," + str(latest_timestamp.replace(minute=0) - i * resolution_60m) + "," + metric + "," + str(point))
        f2.write("\n")

    # Populate the table with statistics
    num_points_ignore = int((latest_timestamp - midnight_timestamp).total_seconds()) / int(resolution_60m.total_seconds())
    for i in range(num_points_ignore,num_points_low,24):
        if (i+24) > num_points_low:
            break;
        points = points_60m[i : i + 24]
        points.sort()
        min = points[0]
        max = points[23]
        median = points[12]
        mean = round( np.mean( points ), 2 )
        std = round( np.std( points ), 2 )
        timestamp = latest_timestamp.replace(minute=0) - i * resolution_60m      
        date = str(timestamp.date()) 
        f3.write(source + "," + metric + "," + date + "," + str(min) + "," + str(max) + "," + str(median) + "," + str(mean) + "," + str(std))
        f3.write("\n")

    # Close files
    f1.close()
    f2.close()
    f3.close()

    
    
# Create and populate CSV files

f = open("sources.csv", "w")     
f.write("group,source,characteristics,description")
f.write("\n")
f.close()    
populate_sources_by_group()

f = open("metrics.csv", "w")     
f.write("bucket,metric,unit")
f.write("\n")
f.close()          
populate_metrics()        

f = open("series_high_resolution.csv", "w")     
f.write("group,source,timestamp,metric,value")
f.write("\n")
f.close()    
f = open("series_low_resolution.csv", "w")     
f.write("group,year,source,timestamp,metric,value")
f.write("\n")
f.close()
f = open("statistics_by_source_metric.csv", "w")     
f.write("source,metric,date,min,max,median,mean,stdev")
f.write("\n")
f.close()

populate_time_series('House A','Termostate A1','temperature',74,76)
populate_time_series('House A','Termostate A1','humidity',40,50)
populate_time_series('House A','Termostate A2','temperature',74,76)  
populate_time_series('House A','Termostate A2','humidity',40,50)  
populate_time_series('House A','Refrigerator A1','temperature',30,50)
populate_time_series('House A','Refrigerator A1','humidity',45,75)   
populate_time_series('House A','Freezer A1','temperature',-20,5)

populate_time_series('House B','Termostate B1','temperature',80,82)
populate_time_series('House B','SmartSensor B1','temperature',79,82)
populate_time_series('House B','SmartSensor B2','temperature',82,85)

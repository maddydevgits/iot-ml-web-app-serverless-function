from iotapp import *
from time import sleep
import pandas as pd

data=[]
result=0
count=0
while True:
    count+=1
    h,t=iotSensoryData()
    if(h>20 and h<40):
        result=1
    elif(h>40 and h<60):
        result=2
    elif(h>60 and h<80):
        result=3
    elif(h>80 and h<100):
        result=4
    dummy=[]
    dummy.append(h)
    dummy.append(t)
    dummy.append(result)
    data.append(dummy)
    print(count)
    if(count==20):
        count=0
        df=pd.DataFrame(data)
        df.to_csv('iot.csv')

    sleep(2)
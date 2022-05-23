import pandas as pd
import numpy as nm
import datetime

el=['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
x=pd.Series(nm.random.randint(0,10000,10),index=el)
y=pd.Series(nm.random.randint(0,10000,10),index=el)


sh=nm.random.randint(9,18,10)
sm=nm.random.randint(0,60,10)
ss=nm.random.randint(0,60,10)

eh=nm.random.randint(sh,18,10)
em=nm.random.randint(0,60,10)
es=nm.random.randint(0,60,10)

s1=[]
e1=[]

for i in range(10):
    s1.append(datetime.datetime(2016, 2, 2, sh[i], sm[i], ss[i]))
    e1.append(datetime.datetime(2016, 2, 2, eh[i], em[i], es[i]))

s=pd.Series(s1,index=el)
e=pd.Series(e1,index=el)

df=pd.DataFrame({"Start_time":s,"End_time":e,"x":x,"y":y})
print(df)
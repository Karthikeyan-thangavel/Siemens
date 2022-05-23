import pandas as pd
import numpy as nm

el=['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
x=pd.Series(nm.random.randint(0,10000,10),index=el)
y=pd.Series(nm.random.randint(0,10000,10),index=el)

df=pd.DataFrame({"x":x,"y":y})
print(df)
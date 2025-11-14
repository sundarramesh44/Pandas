#first panda
import pandas as pd
import numpy as np
a=np.array([11,99,303,44,55,6])
b=np.array([1,2,3,4,5,6])
c=a+b
d=np.array(["Abi","Bala","Coulins","Dinesh","Elger","Ganesh"])
#print(a)
#print(b)
#print(c)
#print(d)
convert_to_excel_format = {"Name":d, "A":a, "B":b, "C":c}
#print(convert_to_excel_format)
new = pd.DataFrame(convert_to_excel_format)
print(new)
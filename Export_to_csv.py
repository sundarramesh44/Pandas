#export to excel and csv
import pandas as pd
import numpy as np
a=np.array([11,99,303,44,55,7])
b=np.array([1,2,3,4,5,7])
c=a+b
d=np.array(["Abi","Bala","Coulins","Dinesh","Elger","Ganesh"])
convert_to_excel_format = {"Name":d, "A":a, "B":b, "C":c}
new = pd.DataFrame(convert_to_excel_format)
print(new)
new.to_csv("Data_in_csv.csv",index=True)
new.to_json("Data_in_json.json")
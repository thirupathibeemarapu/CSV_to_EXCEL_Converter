import pandas as pd
#Reading CSV File
df=pd.read_csv("Data.csv")
#Handling Missing Value
df=df.fillna("Not Available")
#save data to Excel
df.to_excel("output.xlsx",index=False)
#print Success message
print("CSV to Excel Conversion Completed")
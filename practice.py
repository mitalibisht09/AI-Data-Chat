
import pandas as pd
print(pd.__version__)

import pandas as pd

# Dictionary se DataFrame banate hain
data = {
    "Name": ["Aman", "Priya", "Rohit", "Simran"],
    "Age": [21, 22, 20, 23],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)

print(df)
print("\nColumns:", df.columns.tolist())
print("\naverage of age:", df["Age"].mean())
print("\nstudents lives in delhi:\n", df[df["City"] == "Delhi"])


import pandas as pd
data =[10,20,30,40,50]
s=pd.Series(data)
print(s)


import pandas as pd
data =[100,50,80,60]
fruits=["Apple","Banana","Mango","Orange"]
s=pd.Series(data,index=fruits)
print(s)




import pandas as pd
data = {
"Name":["Rahul","priya","Aman"],
"Age":[20,21,19],
"Marks":[85,92,78]

}
df =pd.DataFrame(data)
print(df)



#1.Number of rows and columns
print(df.shape)

#2.Column names
print(df.columns)

#3.Data types
print(df.dtypes)

#4.First 2 rows
print(df.head(2))


import pandas as pd
df = pd.DataFrame({
 "Name":["Rahul","priya","Aman"],
 "Age":[20,21,19],
"Marks":[85,92,78]
})

df["Marks"]

df[["Name","Marks"]]

#selecting first row
df.iloc[0]

df.iloc[1,2]
df.loc[1,"Marks"]

df = pd.DataFrame({
     "Name":["Rahul","Priya,"Aman","Neha"],
     "Aman":[20,21,19,22],
    "Marks":[85,92,78,95]
})

#write a pandas code to select students whose Marks are greater than 85
df[df["Marks"]>85]

df[(df["Age"]>=21) & (df["Marks"]>85)]
df[(df["Marks"]>90)] | 9(df["Age"]<20)]

df[df["Name"]].isin(["Rahul","Neha"])]

df[df["Marks"].between(80,95)]

#Sorting
df.sort_values("Marks",ascending=False)

#TOP 2 students
df.sort_values("Marks",ascending=False).head(2)

#data transformation
df["Passed"]=df["Marks"].apply(lambda x : "Yes" if x>=80 
        else "No")

#how to know missing value
df.isnull.sum()

#if i want to replace null value with 80
df["Marks"]=df["Marks"].fillna(80)

#which function would you use to remove duplicates rows?
df.drop_duplicates()


#which command shows he data type of every column?
df.dtypes

#which command gives a summary of the DataFrame,including;
df.info()

#==================================================
#GroupBy begins

#you want to find the average salary of each department
df.groupby("Department")["salary"].mean()

df.groupby("Department")["Salary"].sum()

df.groupby("Department")["salary"].agg(["min","max","mean"])


df.groupby(["Department", "Gender"])["Salary"].mean()

df["Departments"].value_counts()

df["Depatment"].unique()


#===================================================================================================================
#common data-cleaning task
df.rename(columns={"Marks":"Score"})

df.dropna()

#changing datatype
df["Age"]=df["Age"].astype(int)

#string cleaning
df["Name"] = df["Name"].str.strip()


#string strandalization
df["Name"]=df["Name"].str.upper()

df[df["Name"].str.contains("Ra")]

df["Revenue"]=df["Price"]*df["Quantity"]

df["Total_With_Tax"] =df["Revenue"]+(df["Revenue"]*0.18)


#how to combine dataframes
pd.concat([df1,df2])

df=pd.merge(employees,salary,on="Employee_ID")

df=pd.merge(df1,df2,on="ID",how="Outer")

#Date Time
df=pd.DataFrame({
    "Date":["2026-01-15","2026-02-20","2026-03-10"]
})

df["Data"] = pd.to_datetime(df["Date"])

df["Date"].dt.year


df["End"] - df["start"]


df["Date"].dt.day_name()

df["Date"].dt.month_name()
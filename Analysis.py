import pandas as pd

Data_One = pd.read_csv("Dataset/glassdoor job posting Part I.csv")
Data_One.columns = [i.strip().lower() for i in Data_One.columns]

Data_Two = pd.read_csv("Dataset/glassdoor job posting Part II.csv")
Data_Two.columns = [i.strip().lower() for i in Data_Two.columns]

# Comparing columns
Difference = set(Data_One.columns) ^ set(Data_Two.columns)

if len(Difference) == 0:
    Data = pd.concat([Data_One,Data_Two],ignore_index=True)
else:
    print("Data holds different values")
    
# Data Analysis
Job = ", ".join(Data["job title"].value_counts().head().index)
print("The Top 5 Jobs Are: {}".format(Job))
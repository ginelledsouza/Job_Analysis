from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import pandas as pd
import re

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
result = ", ".join(Data["job title"].value_counts().head().index)
print("The Top 5 Jobs Are: {}".format(result))

result = ", ".join([i.split("\n")[0] for i in Data["company name"].value_counts().head().index])
print("The Top 5 Companies Are: {}".format(result))

result = ", ".join(Data["location"].value_counts().head().index)
print("The Top 5 Location Are: {}".format(result))

AvgWord = round(Data["job description"].apply(lambda x : len(x)).mean())
Data["isEng"] = Data["job description"].apply(lambda x: "English" if (re.sub('[^A-Za-z0-9]+', '', x).lower().isalnum()) and len(re.sub('[^A-Za-z0-9]+', '', x).lower())>AvgWord else "Not English")

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

Text = " ".join(Data["job description"].apply(lambda x : re.sub('[^A-Za-z]+', ' ', x)))
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(Text)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
TopRequirement = word_count(Text)
TopRequirement = sorted(TopRequirement.items(), key=lambda x:x[1],reverse=True)[:10]
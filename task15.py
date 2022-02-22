import numpy as np
import pandas as pd
import random
# df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('CS56'))



# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(10, 3)),
                  columns=['CS 5000', 'CS 5110', 'CS 5600'],
                  index=['Alice', 'Mark', 'Bill', 'Tony', 'Jason', 'Ravi','Sandeep','Mounika','John','Curtis'])

df2 = pd.DataFrame(np.random.randint(30,100,size=(1, 3)),
                  columns=['CS 5000', 'CS 5110', 'CS 5600'],
                  index=['Denis'])


df=pd.concat([df,df2])

df['Average'] = df.mean(axis=1)

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}

gpa={
  3.5:"Honor Roll",
  3.0:"Normal",
  0: "In Probation",
}

def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter

def gpa_mapping(value):
    for key, letter in gpa.items():
        if value >= key:
            return letter


letter_grades = df["Average"].map(grade_mapping)
df["CS5000 Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)

# df["GPA"] =random.uniform(0.0, 3.5).unique()

unique_idx = df.index[~df.index.str.isdigit()].unique()
s = pd.Series(np.random.uniform(0,3.5,len(unique_idx)) , index =unique_idx)
df['GPA'] = s

gpa_grades = df["GPA"].map(gpa_mapping)
df["Status"] = pd.Categorical(
    gpa_grades, categories=gpa.values(), ordered=True
)

del df['CS5000 Grade']


print(df)
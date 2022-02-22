import numpy as np
import pandas as pd

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

def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


letter_grades = df["Average"].map(grade_mapping)
df["CS5000Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)

data_a=df[df.CS5000Grade == 'A'].count() ["CS5000Grade"]
data_b=df[df.CS5000Grade == 'B'].count() ["CS5000Grade"]
data_c=df[df.CS5000Grade == 'C'].count() ["CS5000Grade"]
data_d=df[df.CS5000Grade == 'D'].count() ["CS5000Grade"]
data_f=df[df.CS5000Grade == 'F'].count() ["CS5000Grade"]

print("A  ",data_a)
print("B  ",data_b)
print("C  ",data_c)
print("D  ",data_d)
print("F  ",data_f)


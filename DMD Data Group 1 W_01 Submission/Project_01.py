'''
A Python script that reads in a CSV file of student grades to:
1. Calculating averages, 
2. Finding maximum and minimum values, and 
3. Generating simple summaries.

'''

#Importing Libraries
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Impact-Insights/Group-Project/refs/heads/main/class_grades_2c.csv')

print(df.head(), "\n\n")

print('Calculating the averages of the assignment, Tutorial, Midterm, TakeHome and Final columns')
averages = {}
columns = ['Assignment', 'Tutorial', 'Midterm', 'TakeHome', 'Final']

for column in columns:
    averages[column] = round(df[column].mean(), 2)
    print(f"The {column} average is: {averages[column]}")


print('\n\n Calculating Minimum and Maximum Values for each column')
min_max_values = {}

for column in columns:
    min_value = df[column].min()
    max_value = df[column].max()
    min_max_values[column] = {'min': min_value, 'max': max_value}
    print(f"The {column} minimum mark is: {min_value}")
    print(f"The {column} maximum mark is: {max_value}\n")

print('Calculating Learner Average (Adding a New Column \n)')
df['Learner_Average'] = round(df[['Assignment', 'Tutorial', 'Midterm', 'TakeHome']].mean(axis=1), 2)
print("\n", df, "\n\n")

print('Generating Simple Summaries \n')
df_summary = df[['Assignment', 'Tutorial', 'Midterm', 'TakeHome', 'Final',
       'Learner_Average']].describe()
print("\n", df_summary)
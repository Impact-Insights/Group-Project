import pandas as pd
import numpy as np


#Understanding the Data.
#messy_data = pd.read_csv('https://raw.githubusercontent.com/Impact-Insights/Group-Project/refs/heads/main/DMD%20Data%20Group%201%20W_02%20Submission/messy_dataset.csv?token=GHSAT0AAAAAAC7CHSQJ5GDAFSWU6MYQ2L2YZ5W2RFA')
messy_data = pd.read_csv('messy_data.csv')

print("Messy Data\n\n")
print(messy_data.head(), "\n\n")

print(messy_data.info(), "\n\n")

(messy_data.describe(), "\n\n")

print(messy_data.columns, "\n\n")


# WORKING WITH THE Age COLUMN [Filling Nulls with the Mean of the column, Data Type Change]
messy_data['Age'] = messy_data['Age'].fillna(0)

for column in messy_data.columns:
    messy_data['Age'] = np.where(messy_data['Age'] == 0, messy_data['Age'].mean(), messy_data['Age'])

messy_data['Age'] = round(pd.to_numeric(messy_data['Age'], downcast='integer', errors='coerce'), 0)


# WORKING ON THE Email COLUMN [Dropping Duplicates, Dropping Nulls, Standardization] 
messy_data['Email'] = messy_data['Email'].drop_duplicates()

messy_data = messy_data.dropna()

messy_data.loc[0, 'Email'] = "eve@example.com"
messy_data.loc[3, 'Email'] = "david@example.com"

messy_data['Email'] = messy_data['Email'].str.lower()


#WORKING ON THE Salary ($) COLUMN. [Striping and Replacing Unwanted characters and symbols]
messy_data.loc[:, 'Salary ($)'] = messy_data['Salary ($)'].str.strip(',.$')
messy_data.loc[:, 'Salary ($)'] = messy_data['Salary ($)'].str.replace(',', "")

messy_data['Salary ($)'] = messy_data['Salary ($)'].astype('float64')



#WORKING ON THE Joining Date COLUMN [Standardization]
messy_data.loc[:, 'Joining Date'] = messy_data.loc[:,'Joining Date'].str.replace('-', "")
messy_data.loc[:4, 'Joining Date'] = messy_data.loc[:,'Joining Date'].str.replace('-', "")
 
messy_data.at[0, 'Joining Date'] = pd.to_datetime(messy_data.at[0, 'Joining Date'], format='%d/%m/%Y').strftime('%d-%m-%Y')
messy_data.at[1, 'Joining Date'] = pd.to_datetime(messy_data.at[1, 'Joining Date'], format='%Y%m%d').strftime('%d-%m-%Y')
messy_data.at[2, 'Joining Date'] = pd.to_datetime(messy_data.at[2, 'Joining Date'], format='%d%m%Y').strftime('%d-%m-%Y')
messy_data.at[3, 'Joining Date'] = pd.to_datetime(messy_data.at[3, 'Joining Date'], format='%Y%m%d').strftime('%d-%m-%Y')
messy_data.at[7, 'Joining Date'] = pd.to_datetime(messy_data.at[7, 'Joining Date'], format='%B %d, %Y').strftime('%d-%m-%Y')
 
print(messy_data, "\n\n")
messy_data['Age'] = messy_data['Age'].astype('Int64')
sorted_data = messy_data.sort_values(by='ID', ascending=True)

#SAVING THE CLEANED DATA TO A CSV FILE.
print("The Cleaned Data \n\n")
print(messy_data)
cleaned_data = sorted_data.to_csv('cleaned_data.csv', index = False)
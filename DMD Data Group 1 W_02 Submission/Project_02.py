import pandas as pd
import numpy as np

messy_data = pd.read_csv('https://raw.githubusercontent.com/Impact-Insights/Group-Project/refs/heads/main/DMD%20Data%20Group%201%20W_02%20Submission/messy_dataset.csv?token=GHSAT0AAAAAAC7CHSQIGOJKJD3LRGAQ4SQGZ5V3SNA')

print(messy_data.head(), "\n\n")

print(messy_data.info(), "\n\n")

(messy_data.describe(), "\n\n")

print(messy_data.columns, "\n\n")



messy_data['Age'] = messy_data['Age'].fillna(0)
#messy_data['Age'] = messy_data['Age'].fillna(messy_data['Age'].mean())

for column in messy_data.columns:
    messy_data['Age'] = np.where(messy_data['Age'] == 0, messy_data['Age'].mean(), messy_data['Age'])


#messy_data['Age'] = messy_data['Age'].astype('Int64')
messy_data['Age'] = round(pd.to_numeric(messy_data['Age'], downcast='integer', errors='coerce'), 0) #errors='coerce' will turn non-numeric values to NaN



messy_data['Email'] = messy_data['Email'].drop_duplicates()


messy_data = messy_data.dropna()


messy_data.loc[0, 'Email'] = "eve@example.com"
messy_data.loc[3, 'Email'] = "david@example.com"

messy_data['Email'] = messy_data['Email'].str.lower()


messy_data.loc[:, 'Salary ($)'] = messy_data['Salary ($)'].str.strip(',.$')
messy_data.loc[:, 'Salary ($)'] = messy_data['Salary ($)'].str.replace(',', "")


messy_data.loc[:, 'Joining Date'] = messy_data.loc[:,'Joining Date'].str.replace('-', "")
messy_data.loc[:4, 'Joining Date'] = messy_data.loc[:,'Joining Date'].str.replace('-', "")



 
messy_data.at[0, 'Joining Date'] = pd.to_datetime(messy_data.at[0, 'Joining Date'], format='%d%m%Y').strftime('%d-%m-%Y')
messy_data.at[1, 'Joining Date'] = pd.to_datetime(messy_data.at[1, 'Joining Date'], format='%Y%m%d').strftime('%d-%m-%Y')
messy_data.at[2, 'Joining Date'] = pd.to_datetime(messy_data.at[2, 'Joining Date'], format='%d%m%Y').strftime('%d-%m-%Y')
messy_data.at[3, 'Joining Date'] = pd.to_datetime(messy_data.at[3, 'Joining Date'], format='%Y%m%d').strftime('%d-%m-%Y')
messy_data.at[7, 'Joining Date'] = pd.to_datetime(messy_data.at[7, 'Joining Date'], format='%B %d, %Y').strftime('%d-%m-%Y')
 
 
print(messy_data)

messy_data['Age'] = messy_data['Age'].astype('Int64')

print("The Cleaned Data \n\n")
print(messy_data)
cleaned_data = messy_data.to_csv('cleaned_data.csv', index = False)
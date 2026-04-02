import pandas as pd
df = pd.read_csv('titanic.csv')
#print(df) # this will print the DataFrame but it may be truncated if it's too large

# print(df.to_string()) # to print the entire DataFrame without truncation

#data inspection
# print('first five : \n', df.head()) # prints the first 5 rows of the DataFrame

# print('last five : \n', df.tail()) # prints the last 5 rows of the DataFrame
# print('DataFrame Info : \n', df.info()) # provides a concise summary of the DataFrame, including data types and non
# # -null counts    
# print(df.describe()) # generates descriptive statistics for numerical columns in the DataFrame


# data cleaning
# print('Missing values : \n', df.isnull().sum()) # checks for missing values in each column
# print(df.dropna()) # drops rows with any missing values
# print(df.fillna(0)) # fills missing values with 0
# print(df['Age'].fillna(df['Age'].mean())) # fills missing values in the 'Age' column with the mean age 
# # print(df['Age']) 
# new_df = df['Age'].fillna(df['Age'].median()) # fills missing values in the 'Age' column with the median age and updates the DataFrame

# print(new_df.to_string()) # prints the updated 'Age' column without truncation
# print(df['Age'].fillna(df['Age'].median(),inplace=True).to_string()) # checks for missing values in the updated 'Age' column to confirm that they have been filled

# df.fillna({'Age': df['Age'].median()},inplace=True) # fills missing values in the 'Age' column
# print(df['Age']) # checks for missing values in the updated 'Age' column to confirm that they have been filled

# df.drop(columns=['Cabin'],inplace=True) # drops the 'Cabin' column from the DataFrame
# print(df.to_string()) # prints the remaining columns in the DataFrame to confirm that 'Cabin' has been dropped


# df['sex'] = df['Sex'].map({'male': 0,'female': 1}) # maps the 'Sex' column to numerical values (0 for male and 1 for female)
# print(df['sex'].to_string()) # prints the updated ' 

# df.rename(columns={'Sex': 'Gender'}, inplace=True) # renames the '      
# print(df['Gender']) # prints the DataFrame to confirm that the '          


#filtering 

# print(df[df['Age'] > 30]) # filters the DataFrame to show only rows where the 'Age' column is greater than 30
# print(df[df[' Sex'] == 'female']) # filters the DataFrame to show only rows where the 'Sex' column is equal to '      
# print(df[df['Pclass'] == 1]) # filters the DataFrame to show only rows where the 'Pclass' column is equal to 1 (first class passengers)           
df[(df['Gender'] == '1') & (df['Age'] > 30)] # filters the DataFrame to show only rows where the 'Gender' column is equal to '1' (female passengers) and the 'Age' column is greater than 30            

#groupby
# print(df.groupby('Pclass')['Age'].mean()) # groups the DataFrame by the 'Pclass' column and calculates the mean age for each class
# print(df.groupby('Pclass')['Survived'].sum()) # groups the DataFrame by the 'Pclass' column and calculates the total number of survivors for each class
# print(df.groupby('Pclass')['Fare'].max()) # groups the DataFrame by the 'Pclass' column and calculates the maximum fare for each class            



import pandas as pd
df = pd.read_csv("titanic-dataset.csv")
# print(df) #truncate
# print(df.to_string()) #show all

# #data inspection
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())

#data cleaning
# NAN  = not a number]
# print(df["Age"])
# df_new = (df["Age"].fillna(df["Age"].median()))# shows age index only
# print(df_new)
# print(df["Age"].fillna(df["Age"].median(), inplace = True).to_string())
# df.fillna({"Age":df["Age"].median()}, inplace = True)
# print(df["Age"])


# # mapping categories

# df["Sex"] = df["Sex"].map({"male": 0,"female":1})
# print(df)

# mapping categories
# df.drop(columns = ["Cabin","Ticket"], axis = 1, inplace = True)
# print(df)

# df.rename(columns={"Sex":"Gender"}, inplace = True)
# print(df['Gender'])

#filtering
df[(df['Gender']=='1') & (df['Age']> 30)]

#filtering

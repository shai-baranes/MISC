import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df = pd.read_csv(r'./source/survey_results_public.csv')

# ====================================
# update columns
# ====================================

people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


df = pd.DataFrame(people)


df.columns = ["FIRST NAME", "LAST NAME", "EMAIL"]

df.columns = df.columns.str.replace(' ', '_')

df.rename(columns={'FIRST_NAME': 'FIRST', 'LAST_NAME': 'LAST'}, inplace=True)

df.columns = [x.lower() for x in df.columns]



#   first_name last_name                    email
# 0      Corey   Schafer  CoreyMSchafer@gmail.com
# 1       Jane       Doe        JaneDoe@email.com
# 2       John       Doe        JohnDoe@email.com




# ============================================
# update data
# ============================================


# equivalent actions:
df.loc[2].first = "Smith" # if wanting to rename only the first name of the third row
df.loc[2, 'first'] = "Smith" # if wanting to rename only the first name of the third row
#    first     last                    email
# 0  Corey  Schafer  CoreyMSchafer@gmail.com
# 1   Jane      Doe        JaneDoe@email.com
# 2   Smith      Doe        JohnDoe@email.com



df.loc[2] = ['John', 'Smith', 'JohnSmithDoe@email.com']
#    first     last                    email
# 0  Corey  Schafer  CoreyMSchafer@gmail.com
# 1   Jane      Doe        JaneDoe@email.com
# 2   John    Smith   JohnSmithDoe@email.com



df.loc[2, ['last', 'email']]
# LAST                      Smith
# EMAIL    JohnSmithDoe@email.com


df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']
#    first     last                    email
# 0  Corey  Schafer  CoreyMSchafer@gmail.com
# 1   Jane      Doe        JaneDoe@email.com
# 2   John      Doe        JohnDoe@email.com


df.loc[df['first']=="John", "first"] = "Smith"
# df.loc[df['FIRST']=="John"].FIRST = "Smith" # note that this does not work as issues an error (non equivalent)

#    first     last                    email
# 0  Corey  Schafer  CoreyMSchafer@gmail.com
# 1   Jane      Doe        JaneDoe@email.com
# 2  Smith      Doe        JohnDoe@email.com


df["email"] = df["email"].str.lower()
#    first     last                    email
# 0  Corey  Schafer  coreymschafer@gmail.com
# 1   Jane      Doe        janedoe@email.com
# 2  Smith      Doe        johndoe@email.co




# ================================================
# Practive the: 'apply'   -> calling a function on our values (applies on each of the 'df' Series, on the columns by default)
#               'map'     -> calling a function on each value of the DataFrame (works only on a DataFrame object)
#               'replace' -> along with map, enabling replacement of dictionary mapped values, yet maintains the non-mapped values without NuN it
# ================================================

df['email_length'] = df['email'].apply(len)
#    first     last                    email  email_length
# 0  Corey  Schafer  coreymschafer@gmail.com         23
# 1   Jane      Doe        janedoe@email.com         17
# 2  Smith      Doe        johndoe@email.com         17


# removing the 'email length' since the below (len) function cannot apply on int values
df.drop('email_length', axis = 1, inplace=True)


# applies on each individual value of the 'df'
df.map(len)
# df.applymap(len) # deprecated
#    first  last  email
# 0      5     7     23
# 1      4     3     17
# 2      5     3     17


df.map(str.lower)
#    first     last                    email
# 0  corey  schafer  coreymschafer@gmail.com
# 1   jane      doe        janedoe@email.com
# 2  smith      doe        johndoe@email.com


# map is also used to substitute values (note that it substitutes the non mapped values into NaN; otherwise use 'replace')
df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
# 0    Chris
# 1     Mary
# 2      NaN



df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'}) # without compromising 'Smith' which is not mapped for replacement
# 0    Chris
# 1     Mary
# 2    Smith

df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})
#    first     last                    email
# 0  Chris  Schafer  coreymschafer@gmail.com
# 1   Mary      Doe        janedoe@email.com
# 2  Smith      Doe        johndoe@email.com




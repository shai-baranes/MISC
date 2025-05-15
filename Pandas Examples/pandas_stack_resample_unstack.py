import pandas as pd
import numpy as np

np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=90)
items = ['A', 'B']
data = np.random.randint(1, 10, size=(90, 2))  # array of arrays, each internal array comprised of 3 values.
df = pd.DataFrame(data, index=dates, columns=items)



df
#             A  B
# 2023-01-01  6  1
# 2023-01-02  4  4
# 2023-01-03  8  4
# 2023-01-04  6  3
# 2023-01-05  5  8
# ...        .. ..
# 2023-03-27  7  6
# 2023-03-28  8  1
# 2023-03-29  9  5
# 2023-03-30  7  6
# 2023-03-31  9  3


df.info()
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   A       90 non-null     int32
#  1   B       90 non-null     int32

df.columns
# Index(['A', 'B'], dtype='object')

df.index
# DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
#                '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
#                '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
#                '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16',
#                ...........
#                '2023-03-18', '2023-03-19', '2023-03-20', '2023-03-21',
#                '2023-03-22', '2023-03-23', '2023-03-24', '2023-03-25',
#                '2023-03-26', '2023-03-27', '2023-03-28', '2023-03-29',
#                '2023-03-30', '2023-03-31'],
#               dtype='datetime64[ns]', freq='D')

df.stack().index
# MultiIndex([('2023-01-01', 'A'),    -->  6  (from above randmized values)
#             ('2023-01-01', 'B'),    -->  1
#             ('2023-01-05', 'A'),
#             ('2023-01-05', 'B'),
#             ...
#             ('2023-03-27', 'A'),
#             ('2023-03-31', 'B')],
#            length=180)

df.stack()[('2023-01-01', 'A')] # 6 # note that stack()/unstack() is not 'inplace=True'





# data = (pd.concat([df.unstack('ticker')['dollar_volume'].resample('M').mean().stack('ticker').to_frame('dollar_volume'), # and stack it back into a muti-index and to frame only the 'dollar_volume' columms (TBD what happens if I get only that column? like df[['dollar_volume']])?
#            df.unstack()[last_cols].resample('M').last().stack('ticker')],
#           axis=1)).dropna()




# now with additional value (to be able to unstack by a specific 'key')
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=90)
items = ['A', 'B', 'C']
data = np.random.randint(1, 10, size=(90, 3))  # array of arrays, each internal array comprised of 3 values.
df = pd.DataFrame(data, index=dates, columns=items)

df
#             A  B  C
# 2023-01-01  6  1  4
# 2023-01-02  4  8  4
# 2023-01-03  6  3  5
# 2023-01-04  8  7  9
# 2023-01-05  9  2  7
# ...        .. .. ..
# 2023-03-27  9  9  8
# 2023-03-28  1  4  9
# 2023-03-29  8  8  2
# 2023-03-30  9  5  8
# 2023-03-31  1  5  1



# TBD try this layter using group()
# note that for unstack() you can also use level, either by 
pd.DataFrame(df.unstack(), columns=['values']) # in this case, the ressult is pd.Serier
#               values
# A 2023-01-01       6
#   2023-01-02       4
#   2023-01-03       6
#   2023-01-04       8
#   2023-01-05       9
# ...              ...
# C 2023-03-27       8
#   2023-03-28       9
#   2023-03-29       2
#   2023-03-30       8
#   2023-03-31       1

type(pd.DataFrame(df.unstack(), columns=['values']))


my_df = pd.DataFrame(df.unstack(), columns=['values']) # converting to DF with column name
my_df.index.names = ['letter', 'date'] # adding names to index
my_df

my_df
#                    values
# letter date              
# A      2023-01-01       6
#        2023-01-02       4
#        2023-01-03       6
#        2023-01-04       8
#        2023-01-05       9
# ...                   ...
# C      2023-03-27       8
#        2023-03-28       9
#        2023-03-29       2
#        2023-03-30       8
#        2023-03-31       1


my_df.swaplevel()
#                    values
# date       letter        
# 2023-01-01 A            6
# 2023-01-02 A            4
# 2023-01-03 A            6
# 2023-01-04 A            8
# 2023-01-05 A            9
# ...                   ...
# 2023-03-27 C            8
# 2023-03-28 C            9
# 2023-03-29 C            2
# 2023-03-30 C            8
# 2023-03-31 C            1


my_df = my_df.swaplevel().sort_index()
#                    values
# date       letter        
# 2023-01-01 A            6
#            B            1
#            C            4
# 2023-01-02 A            4
#            B            8
# ...                   ...
# 2023-03-30 B            5
#            C            8
# 2023-03-31 A            1
#            B            5
#            C            1

my_df.index # INAGINE THAT THE LETTER IS THE STOCK TICKER
# MultiIndex([('2023-01-01', 'A'),
#             ('2023-01-01', 'B'),
#             ('2023-01-01', 'C'),
#             ('2023-01-02', 'A'),
#             ('2023-01-02', 'B'),
#             ('2023-01-02', 'C'),
#             ('2023-01-03', 'A'),
#              .........


data = np.random.randint(100, 200, size=(my_df.shape[0], 2))  # array of arrays, each internal array comprised of 3 values.

my_df[['value_2', 'value_3']] = data


my_df
#                    values  value_2  value_3
# date       letter                          
# 2023-01-01 A            6      142      114
#            B            1      186      128
#            C            4      120      182
# 2023-01-02 A            4      168      122
#            B            8      199      183
# ...                   ...      ...      ...
# 2023-03-30 B            5      184      156
#            C            8      162      156
# 2023-03-31 A            1      148      117
#            B            5      157      109
#            C            1      162      179

my_df.loc[('2023-01-01', 'A'), :]
# values       6
# value_2    142
# value_3    114




# note that when using unstack, you apply per index name or level if not named

# both belowo equivalents
my_df.unstack(level=0)
my_df.unstack(level='date')
#            values                        ...    value_3                      
# date   2023-01-01 2023-01-02 2023-01-03  ... 2023-03-29 2023-03-30 2023-03-31
# letter                                   ...                                 
# A               6          4          6  ...        179        173        117
# B               1          8          3  ...        103        156        109
# C               4          4          5  ...        167        156        179



# note that resample works only on a datetime index type
# here we get the montly average (end of each month) on a period of 3 months
my_df.unstack().resample('ME').mean()
#               values                      ...     value_3                        
# letter             A         B         C  ...           A           B           C
# date                                      ...                                    
# 2023-01-31  5.193548  4.548387  4.483871  ...  147.806452  145.225806  154.387097
# 2023-02-28  4.464286  4.964286  6.178571  ...  150.500000  157.642857  156.535714
# 2023-03-31  4.419355  5.225806  5.129032  ...  138.322581  157.451613  144.258065



# here we get the max values on a period of 3 months
my_df.unstack().resample('ME').max()
#            values       value_2           value_3          
# letter          A  B  C       A    B    C       A    B    C
# date                                                       
# 2023-01-31      9  9  9     198  199  192     199  197  194
# 2023-02-28      9  9  9     194  198  193     198  197  198
# 2023-03-31      9  9  9     189  194  196     190  199  199



# here we get the sum of the values over a period of 3 months
my_df.unstack().resample('ME').sum()
#            values           value_2             value_3            
# letter          A    B    C       A     B     C       A     B     C
# date                                                               
# 2023-01-31    161  141  139    4738  4566  4569    4582  4502  4786
# 2023-02-28    125  139  173    4231  4289  4241    4214  4414  4383
# 2023-03-31    137  162  159    4555  4419  4650    4288  4881  4472
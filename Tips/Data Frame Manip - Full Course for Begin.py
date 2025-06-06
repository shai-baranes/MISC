Data Analysis with Python - Full Course for Beginners (Numpy, Pandas, Matplotlib, Seaborn)
https://www.youtube.com/watch?v=r-uOLxNrNk8&t=237s

https://pandas.pydata.org/docs/reference/api/

my google sheet link:
https://docs.google.com/document/d/1CBWE7vvQ-PXCAtkxuC4BG0Jw6XlFSdjBF6JCw-4VSyE/edit?usp=sharing

# pd.set_option('display.max_rows', None) # in such case, df.head() -> retrieves the entire list (maybe need to add; df.head(5) )
# pd.set_option('display.max_rows', 0) # (either rows or columns -  to revert)

basic funcs to get acquaintet with your df:
	df.info() # object type and non-empty cells count per column
	df.columns
	df.describe() # for statistics - works only on the mumeric fields!
	df['Story Points (Hours)'].describe() # works on the specified column
	df.tail()
	df.head()
	df.sample(10)  # gets rando lines
	df.shape # matrix size (rows and columns)
	df.to_csv('file_name.csv') # getting df or manipulated df into a csv file
	df['Reporter'].unique() # list of all unique reporters
	df[0:5] # listing the first 5 rows
	df[-5:] # listing the last  5 rows
	df.iloc[:,:] # listing all rows and all columns
	last row: df2[-1:] # (from -1 to last row); df2.loc[9872] # adding row index; df.loc['K2-1'] # key for the key indexed
	df.drop(['col1', 'col2'], axis=1, inplace=True) # droping columns
	df.drop(columns=['col1', 'col2'], inplace=True) # same as above
	df_basic.drop(df_basic[pd.to_numeric(df_basic['Key'].apply(my_split))>=10000].index)  # find below the implementation on the 'my_split()' function
	df_basic.drop(df_basic[pd.to_numeric(df_basic['Key'].apply(lambda x: x.split('-')[1]))>=10000].index)  # same as above (we cannot use the split inside w/o lambda)
	df_basic.drop(df_basic[df_basic['Key'].apply(lambda x: int(x.split('-')[1]))>=10000].index)  # and the shortest way (using int casting instead of pdnumeric)
	df_basic.drop(df_basic[df_basic['Key'].apply(lambda x: int(x.split('-')[1]))>=10000].index, inplace=True) # if wanting to change the DF itself

	df.dropna() # probably all rows with any nan shall be droped
	df.dropna(subset=['look_@me_column']) #droping rows where the nan is in that specific column

	df[df['Reporter'] == 'Guy.Cohen']['Total Days to Resolve'].mean() ; df.loc[df['Reporter'] == 'Guy.Cohen', 'Total Days to Resolve'].mean() # same results = 327.6
	df_basic[df_basic['Reporter'].isin(['Ortal Avner', 'Svetlana Gordon'])] # instead of: (df['Reporter']== "x") | (df['Reporter']== "y")
	df_basic[df_basic['Reporter'] == "Shai Baranes"][['Key', 'Status']].groupby('Status').count() # grouping by Status on all of my personal jiras
	my_group['percents'] = my_group['Key']/my_group['Key'].sum()*100 # adding column with the percentlie value per unique item in group
	my_group.reset_index() # results with indexing and filling in the assumed info (e.g. all the 2021 year shall now have "2021" explicitly in cells)

	df.drop_duplicates() # By default, it removes duplicate rows based on all columns (meaning less chance to remove something)
	df.drop_duplicates(subset=['look_@me_column']) #droping rows where having already used value in subset column (asking it to be unique)
	df.drop_duplicates(subset=['column1', 'column2'], keep='last') # asking for pair to be unique (and keeping only the last)

	df_sliced = df_main.reset_index(inplace=True, drop=True) # to reset the .loc index for sliced df (starting from 0) and remove the older index

	# getting location by index instead of key (although using the 'loc' and not 'iloc' which not supporting the columns' names)
	df_modified.loc[df_modified.index[0:4], ["Summary", "Status"]]

more advanced:
	df['Story Points (Hours)'].isnull().sum() # 9077 (out of 9871) - count of all the entried with null value under 'Story Points (Hours)'
	df[~pd.isnull(df['Story Points (Hours)'])]['Story Points (Hours)'].sum() # 11384 - sum of all values under story points
	df['Story Points (Hours)'].sum() # 11384 (same value)
	try #1 df[('Story Points (Hours)' < 0)] # not working
	try #2 df[('Story Points (Hours)' < 0.0)] # not working
	df[~pd.isnull(df['Story Points (Hours)'])][(df[~pd.isnull(df['Story Points (Hours)'])]['Story Points (Hours)'].astype('int') < 0)]['Story Points (Hours)'] # by getting only items with values..
	# >> K2-5921   (-1.0)  (1st: subset; 2nd: another filter/condition/converting 5.0 to 5; 3rd: interesting columns to disaplay)

	df['Risk Classification'].value_counts() # Medium: 790, High: 677, Low: 305, No Risk: 249, Pending Risk Assessment: 18  (in a table view) ; note: NULL was ignored for 'Story Points'
	# for df.corr(), you first need to convert DF objects to int (find below section)
	df.corr() # correlation matrix on all mumeric fields (after converting number columns into int/float...)

	df_modified['Reporter'].map({'Guy.Cohen': 'Guy Cohen', 'Ayala.Goldshtein': 'Ayala Goldshtein'}) # we can use ,inplace=True (or df_modified['Reporter'] = this); note that the rest will be Nan
	df_modified['Reporter'].replace({'Guy.Cohen': 'Guy Cohen', 'Ayala.Goldshtein': 'Ayala Goldshtein'}) # the rest shall remain as before!

	# DF for "Kodex-[version]] (p_Detected)" sheet (based on the basic DF with Key = 0.....->n)
	df_sheet8_1 = new_df_basic_1.set_index(['Detected_in_Version', 'Issue Type'])[['Key', 'Summary', 'Status', 'Reporter', 'Sprint', 'Severity', 'Probability', 'Priority', 'Creation Date', 'Resolution', 'Components', 'Regression', 'Fixed in Build', 'Version Found', 'Fix versions']].sort_values(by=['Detected_in_Version', 'Key'], ascending=False)

	# adding a column with percentage change per row (first row value is Nan)
	df['new'] = df['total count'].pct_change()

	# merging 2 DFs on a common column/key
	merged_df = df_main.merge(df_vlookup, left_on='parent_theme', right_on = 'name')


conventional Plots;
	df['Story Points (Hours)'].plot(kind='box', vert=False, figsize=(14,6)) ; plt.show() ; # with quartiles and outliers in a visual formatting
	df['Story Points (Hours)'].plot(kind='density', figsize=(14,6)) ; plt.show() # we ge the distribution of data along the values axis (most values are 8.0 in out case)

	df['Risk Classification'].value_counts().plot(kind='pie', figsize=(6,6)) # simple pie chart
	df['Risk Classification'].value_counts().plot(kind='bar', figsize=(14,6)) # same as above but using the bar chart

	boxplot_cols = ['Story Points (Hours)', 'Days to Resolve from CCB', 'Days to Verify', 'Days to CCB', 'Total Days to Resolve']
	df[(df['Version Found'] == '1.5.1') & (df['Issue Type'] == 'Bug')][boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
	plt.show() # multiple box plos of desired data under condition of 1.5.1 found bugs

	TBD will be interesting to get some plos on the newly added columns (time to resolve ets...)

conventional Plots (with annotations);
	ax = df['Story Points (Hours)'].plot(kind='density', figsize=(14,6)) # density chart
	ax.axvline(df['Story Points (Hours)'].mean(), color='red') # adding vertical red line for the average value (much affected by outliers)
	ax.axvline(df['Story Points (Hours)'].median(), color='green') ; plt.show() # adding vertical green line for the average value (less affected by outliers)

	ax = df['Story Points (Hours)'].plot(kind='hist', figsize=(14,6)) # quick histogram
	ax = df['Story Points (Hours)'].plot(kind='hist', figsize=(14,6), bins=100) # more bins is for better resolution
	ax.set_ylabel('Number of items') # adding the 'Y' axis label
	ax.set_xlabel('effort in hours') ; plt.show() # adding the 'X' axis label

	corr = df.corr()
	fig = plt.figure(figsize=(8,8))
	plt.matshow(corr, cmap='RdBu', fignum=fig.number)
	plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
	plt.yticks(range(len(corr.columns)), corr.columns)
	plt.show() # nice 2D correlation chart (diagonal in blue for high correlation - note that red is for low correlation)






tbd how to get rows with only columns 1 to n ?

tbd need to replace 'Days to CCB' = (-1) with 'Days to CCB' = (0)




convert DF objects to int (or something else):
	# convert a single column of DataFrame
	df["a"] = pd.to_numeric(df["a"])

	# convert all columns of DataFrame
	df = df.apply(pd.to_numeric) # convert all columns of DataFrame

	# You can also use it to convert multiple columns of a DataFrame via the apply() method:
	df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
	df[[ 'Days to Resolve from CCB', 'Days to Verify', 'Days to CCB', 'Total Days to Resolve']] = df[[ 'Days to Resolve from CCB', 'Days to Verify', 'Days to CCB', 'Total Days to Resolve']].apply(pd.to_numeric)
	



Example with lambda function using apply():

	def get_city(address):
		return address.split(', ')[1]

	def get state (address):
		return address.split(', ')[2].split(' ')[1]

	all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) +	' (' + get_state(x) + ')')  # same as before only with the f-string
	all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")




Other Functions used here for .apply()  :
	def my_split(my_str):
		return my_str.split('-')[1]



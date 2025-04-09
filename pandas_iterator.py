# https://www.youtube.com/watch?v=x2DxiL8WOmc

import pandas as pd
import time

start = time.time()
data = pd.read_csv("./Input/data.csv", usecols = ["final_price", "image_url", "url", "title", "categories"], chunksize = 10) # chunksize for preformance
# data = pd.read_csv("data.csv")
print(f"FILE LOADED! this operation took {time.time() - start} in seconds")
# print(f"data shape: {data.shape}") # no longer relevant once using chunks

for i, chunk in enumerate(data):
	if i == 0:
		temp_df = chunk
		# temp_df = pd.DataFrame(chunk) # the way she did it in YouTube  

		temp_df["final_price"][0] = 8.88
		print(temp_df["final_price"][0]) # 8.88
	else:
		break

# note that current chunk is the next chunk in line


# ====================================================================
data = pd.read_csv("./Input/data.csv", usecols = ["final_price", "image_url", "url", "title", "categories"])

data.to_csv("./Output/modified_data.csv", encoding = "utf-8", index = False) # note that you cannot save the data chunks iterator to file
data.to_csv("./Output/modified_data_2.csv")
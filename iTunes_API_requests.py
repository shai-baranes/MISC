# .results.trackName = "Say It Ain't So" (for weezer)

import json
import requests
import sys

# if len(sys.argv)!=2: # we expect only one argument after program name
# 	sys.exit()



response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=beetles")

if response.status_code != 200: # add here raise / raises (user configured exception)
	print("No access to URL")
	sys.exit()


# print(json.dumps(response.json(), indent=2)) # 'dump' dumping to a file, 'dumps' dumping to screen


for item in range(len(response.json()['results'])):  # my stupid loop
# for item in range(50):  # my stupid loop
	print(json.dumps(response.json()["results"][item]["trackName"]))


print()

# a better looop by the teacher

for result in response.json()['results']: # clean and pythonic by the lecturer
	print(result['trackName'])
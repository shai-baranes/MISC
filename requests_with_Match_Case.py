# cases of dictionary results

from enum import Enum, auto
import requests

POSTCODES_IO_URL = "https://api.postcodes.io"


class PoscodeStatus(Enum):
	INVALID = auto()
	LIVE = auto()
	TERMINATED = auto()
	UNKNOWN = auto()



def postcode_status(postcode: str) -> PoscodeStatus:
	with requests.get(f"{POSTCODES_IO_URL}/terminated_postcodes/{postcode}") as resp:
		match resp.json():
			case {"status": 200}: # you can pass only a portion of the dictionary
				return PoscodeStatus.TERMINATED
			case {"status": 404, "error": "Invalid postcode"}:
				return PoscodeStatus.INVALID
			case {"status": 404, "error": "Terminated postcode not found"}:
				return PoscodeStatus.LIVE
			case _:
				return PoscodeStatus.UNKNOWN



if __name__ == "__main__":
	print(postcode_status("EC1A 1BB")) # Live postcode
	print(postcode_status("INVALID"))  # Invalid postcode
	print(postcode_status("W1A 0AA"))  # Terminated postcode
	print(postcode_status(""))  	   # Unknown postcode

# PoscodeStatus.LIVE
# PoscodeStatus.INVALID
# PoscodeStatus.TERMINATED
# PoscodeStatus.UNKNOWN

 
# print(type(postcode_status("")))
# # <enum 'PoscodeStatus'>


# #example of a web result after input:"https://api.postcodes.io/terminated_postcodes/101" :

# {
# "status": 404,
# "error": "Invalid postcode"
# }
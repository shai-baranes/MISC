# match case
# from BroCode: https://www.youtube.com/watch?v=XKHEtdqhLK8

def is_weekend(day):
	match day.lower():
		case "saturday" | "friday":
			return True
		case  "sunday" | "monday" | "tuesday" | "wednesday" | "thursday":
			return False
		case _:
			return False








# instead of this heavy coding: 
def is_weekend2(day):
	if day.lower() == "sunday":
		return False
	elif day.lower() == "monday":
		return False
	elif day.lower() == "tuesday":
		return False
	elif day.lower() == "wednesday":
		return False
	elif day.lower() == "thursday":
		return False
	elif day.lower() == "friday":
		return True
	elif day.lower() == "saturday":
		return True
	else:
		return False


def main():
	print(is_weekend("Sunday"))




if __name__ == "__main__":
	main()





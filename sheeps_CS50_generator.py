# from Harvard CS50 - URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=56421s


def main():
	n = int(input("What's n? "))
	for s in sheeps_gen(n):
	# for s in sheeps(n):
		print(s)



# the conventional way to do it assuming we want to use functions to pass to main
# since it builds-up a massive list at once, insteda of delivering the ouputs chunk by chunk, the computer hangs on huge numbers!
def sheeps(n):
	flock = []
	for i in range(n):
		flock.append("🐏"*i)
	return flock


def sheeps_gen(n):
	for i in range(n):
		yield "🐏"*i




if __name__ == "__main__":
	main()


# for n = 10:
# 🐏
# 🐏🐏
# 🐏🐏🐏
# 🐏🐏🐏🐏
# 🐏🐏🐏🐏🐏
# 🐏🐏🐏🐏🐏🐏
# 🐏🐏🐏🐏🐏🐏🐏
# 🐏🐏🐏🐏🐏🐏🐏🐏
# 🐏🐏🐏🐏🐏🐏🐏🐏🐏




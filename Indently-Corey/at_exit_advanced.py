import atexit
import time



@atexit.register # first decorated function is the last to run upon exit
def func_A() -> None:
    print('Exit function A')


@atexit.register
def func_B() -> None:
    raise Exception('B did something wrong...')
    print('Exit function B')


def main():
    for i in range (3):
        print(i)
        time.sleep(1)


## important!
## also note that if you wcan unregister any atexit function later in the script (can be beneficial dugin debug mode where you want to alter the ending behavior):
# atexit.unregister(func_A) # input = the unregistered func/



if __name__ == "__main__":
    main()

# 0
# 1
# 2
# Exit function B
# Exit function A
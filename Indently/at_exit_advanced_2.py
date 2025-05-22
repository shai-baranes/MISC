# also note that a fatal exception that is not handles by python shall not trigger the atexit functions!
import atexit



def func_A(val: int) -> None:
    print('Exit function A')
    print(val)


def func_B(val: int, val2: int) -> None:
    print('Exit function B')
    print(val, val2)


def main():
    print("shai")


# note that now we register the cuntions after the definition, and TBD
atexit.register(func_A, 10) # passing in the func name and its' arguments!
atexit.register(func_B, val=10, val2=20)




if __name__ == "__main__":
    main()

# shai                                                                                                                                                                      
# Exit function B                                                                                                                                                           
# 10 20                                                                                                                                                                     
# Exit function A                                                                                                                                                           
# 10   
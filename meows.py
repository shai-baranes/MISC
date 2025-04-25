

 ####################################################################################################
 #                                                                                                  #
 #                                         Arguments Parser:                                        #
 #                                                                                                  #
 ####################################################################################################
# CS50 URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=52615s


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", default=1, help="number of times to meow", type=int)

args = parser.parse_args() # args now contain all the cmd arguments

for _ in range(args.n):  # once we define the n-type to be int, we can trust it without having to convert the input!
# for _ in range(int(arg.n)):  # the value for the 'n' argument
	print("meow")


# from cmd line, ask help on the function: > meows.py -h or 'meows.py --help' (if stored in a seperate file)


# parser.add_argument("-n")
# > meows.py -h
##########################################################                                                                                                                                                            
# (URL_Requests) C:\Python_Rust_Removal\MISC>meows.py -h
# usage: meows.py [-h] [-n N]                                                                                                                                 

# options:                                                                                                                                                    
#   -h, --help  show this help message and exit                                                                                                               
#   -n N                                                                                                                                                      
##########################################################                                                                                                                                                            




# parser.add_argument("-n", help="number of times to meow")
# > meows.py -h
##########################################################                                                                                                                                                            
# (URL_Requests) C:\Python_Rust_Removal\MISC>meows.py -h
# usage: meows.py [-h] [-n N]                                                                                                                                 

# options:                                                                                                                                                    
#   -h, --help  show this help message and exit                                                                                                               
#   -n N        number of times to meow 
##########################################################                                                                                                                                                            
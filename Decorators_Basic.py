# decorators.py

# get also the decorators from here: (decorator to calc the remaining time of a lon grunnig program...)
# https://www.youtube.com/watch?v=yf2xznF30-s


def greet():
	print('Hello! ', end='')
	# print('Hello! ')


# not a real pythonic decorator
def mydecorator(fn):
	fn()
	print('How are you?')



mydecorator(greet)



# -----------------------------------



# Decorator!
def mydecorator(fn): # works on any function that doesn't require any argument.
    def inner_function():        
        print('Start') # here you can add TS
        fn()
        print('End!') # here you can add time span from beginnig
    return inner_function




@mydecorator
def greet():
	print('Hello!')



# -----------------------------------



#typical decorator
def mydecoratorfunction(some_function): # decorator function
    def inner_function(): 
        # write code to extend the behavior of some_function()
        some_function() # call some_function
        # write code to extend the behavior of some_function()
    return inner_function # return a wrapper function




# -----------------------------------



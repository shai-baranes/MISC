# https://www.youtube.com/watch?v=DW9YtOytlhE
# note that it works only from cmd line and not from the sublime terminal!


from datetime import datetime
import atexit
# from atexit import register




@atexit.register # decorator to always call a function at the end of the script, even if enconutering Exceptions along the way!
def terminate() -> None:
    now: datetime = datetime.now()
    print(f'The script ended at: {now:%Y-%m-%d %H:%M:%S}')




# if "__name__" == "__main__":

raise Exception # the terminate shall run at the end although encountering this exception!

print("Hello world")




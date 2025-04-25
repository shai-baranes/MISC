

# My Headrt Decorator func:

> def header_creator(text):
> 	print(f" {'#'*100}")	
> 	print(" #", " "*96, "#")
> 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
> 	print(" #", " "*96, "#")
> 	print("", "#"*100)
>

## Example:
	> header_creator("Arguments Parser:")
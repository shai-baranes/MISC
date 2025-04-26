


## My Func/App Header Decorator func:

> def header_creator(text):
> 	print(f" {'#'*100}")	
> 	print(" #", " "*96, "#")
> 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
> 	print(" #", " "*96, "#")
> 	print("", "#"*100)
>

## Example:
	> header_creator("Arguments Parser:")


## 'black' module:
> at the end of the CS50 python basic course, the instructor applied  '>> black app.py' to improve the cosmetics and spaces.
> note that I had to pip install it.


## Useful doc command prompt:

 - dir /ad  (list only directories)
 - dir /b /ad  (a bare '/b' presentation of directories without the noised columns)
 - dir /b /a-d (list only files - excluding directories, hence the "-")
 - tasklist | findstr "python (find all currently running python processes)
 - taskkill /IM python.exe /F (forcefully and immediately killing all active python processes)
 - dir /s /b | findstr /i lambda (finding all files/paths incorporating the "lambda" text, case insensitive '/i' - can be passed into a file)




## Abbreviation:
	'README.md' -> md for Markdown
	



## My Func/App Header Decorator func:

> def header_creator(text):
> 	print(f" {'#'*100}")	
> 	print(" #", " "*96, "#")
> 	print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
> 	print(" #", " "*96, "#")
> 	print("", "#"*100)
>

### 	Example:
		> header_creator("Arguments Parser:")


## 'black' module:
> at the end of the CS50 python basic course, the instructor applied  '>> black app.py' to improve the cosmetics and spaces.
> note that I had to pip install it.


## Useful DOS command prompt:

 - tree     (nice tree representation of all folders/sub folders, hidden exclusive)
 - dir /ad  (list only directories)
 - dir /b /ad  (a bare '/b' presentation of directories without the noised columns)
 - dir /b /a-d (list only files - excluding directories, hence the "-")
 - tasklist | findstr "python (find all currently running python processes)
 - taskkill /IM python.exe /F (forcefully and immediately killing all active python processes)
 - dir /s /b | findstr /i lambda (finding all files/paths incorporating the "lambda" text, case insensitive '/i' - can be passed into a file)
 - type filename (read the file content - the equivalent to cat/touch in Unix)
 - [Current Working Directory] in python runtime: import os; os.getcwd()


## pip/venv related (new to me; note that UV does it better!):
 - pip install --force-reinstall -v "openpyxl==3.0.10" (maybe pip install troubleshooting?)
 - pip freeze > requirements.txt		# get snapshot of all currently installed python packages along with dependencies
 - pip install -r requirements.txt      # to be later installed by someone else or other env
 - python -m venv .venv					# the convention for naming your virtual environment
 - 


## My most useful GIT commands:

 - git config --get-regexp ^alias (check on your pre-configured aliases)
 -- [more tips from:] https://www.youtube.com/watch?v=aolI_Rz0ZqY&t=437s


## Abbreviation:
	'README.md' -> md for Markdown



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
 - dir /o-d  (sorted 'order' by 'date' (-) reversed)
 - tasklist | findstr "python (find all currently running python processes)
 - taskkill /IM python.exe /F (forcefully and immediately killing all active python processes)
 - dir /s /b | findstr /i lambda (finding all files/paths incorporating the "lambda" text, case insensitive '/i' - can be passed into a file)
 - dir /s /b | findstr /i "import pandas as pd" (finding all files/paths incorporating the "lambda" text, case insensitive '/i' - can be passed into a file)
 - type filename (read the file content - the equivalent to cat/touch in Unix)
 - explorer .  (opens the file browser deirectly from where you are in your CMD console directory)
 - curl "https://api.cryptowat.ch/markets/kraken/btceur/price"  (get status/response on web API)
 - python -m notebook (open python notebook from the local repository)
 - [Windows key+R] -> type: "control access.cpl" (you'll get quick access to change mouse behavior, e.g. activation upon mouse hovering)


## pip/venv related (new to me; note that UV does it better!):
 - pip install --force-reinstall -v "openpyxl==3.0.10" (maybe pip install troubleshooting?)
 - pip freeze > requirements.txt		# get snapshot of all currently installed python packages along with dependencies
 - pip show package_name				# getting the specific version of the currently installed package
 - pip install -r requirements.txt      # to be later installed by someone else or other env
 - python -m venv .venv					# the convention for naming your virtual environment (not needed when using the 'uv' framework)


## Extras
 - [Current Working Directory] in python runtime: import os; os.getcwd() # helps to see what is the current working dir of the script
 - [Current Working Directory] in python runtime: import sys; sys.executable # helps to see what python environment (or .venv) you're in...
 - [Sublime] search excluding folders: add '-' (minus sign) and folders to be excluded under 'Where', e.g. -*/venv/, -*/myvenv/, -*/.env/, 
 - python -m notebook (open python notebook from the local repository) 
 - sns.scatterplot.__doc__ (adding doc helps in getting the docstring of a function)
 - import inspect; inspect.signature(func)   --> (this bring the function signature and we see their agrs and their defaults)
 - [Python Debug Mode] 'next', 'continue' (known), 'return' (step-out of the function) ↩️, 'h' (for help), 'h continue' (help on 'continue')
 - [Microsoft Emoji] 'Window KEY' + '.'
 - [executable from your python script]: https://www.youtube.com/watch?v=bqNvkAfTvIc (Indently Channel)




## My most useful GIT commands:

 - git config --get-regexp ^alias (check on your pre-configured aliases)
 	- [more tips from]: https://www.youtube.com/watch?v=aolI_Rz0ZqY&t=437s


## Abbreviation:
	'README.md' -> md for Markdown
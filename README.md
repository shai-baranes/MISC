


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


## Useful DOS command line prompt (bash equivalent):

 - [Windows key+R] -> type: "control access.cpl" (you'll get quick access to change mouse behavior, e.g. activation upon mouse hovering)
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
 - [F7] keyboard key (like unix history, get the list of user prompts to the console - and you can toggle between prompts using the arrows)
 - echo hello world > tmp.txt (create a file with the text "hello world" in it)
 - echo sinderela >> tmp.txt (append the text "sinderela" to the end of the file tmp.txt. note that w/o the >> it replaces the existing content)
 - type tmp.txt (read the content of the file tmp.txt; equivalent to 'cat' in Unix)


## pip/venv related (new to me; note that UV does it better!):
 - pip install --force-reinstall -v "openpyxl==3.0.10" (maybe pip install troubleshooting?)
 - pip freeze > requirements.txt		# get snapshot of all currently installed python packages along with dependencies
 - pip show package_name				# getting the specific version of the currently installed package
 - pip install -r requirements.txt      # to be later installed by someone else or other env
 - python -m venv .venv					# the convention for naming your virtual environment (not needed when using the 'uv' framework)


## Extras
 - [python] in python runtime: import os; os.getcwd() # helps to see what is the current working dir of the script (Current Working Directory)
 - [python] in python runtime: import sys; sys.executable # helps to see what python environment (or .venv) you're in... (.venv)
 - [Sublime] search excluding folders: add '-' (minus sign) and folders to be excluded under 'Where', e.g. -*/venv/, -*/myvenv/, -*/.env/, 
 - python -m notebook (open python notebook from the local repository) 
 - sns.scatterplot.__doc__ (adding doc helps in getting the docstring of a function)
 - [python] import inspect; inspect.signature(func)   --> (this bring the function signature and we see their agrs and their defaults)
 	- you may also get it by: func.__text_signature__   (maybe not true for all inner functios, where the inspect might help much better!)
 - [python] inspect.getmembers(<Class/Func>, inspect.isfunction) --> this will return all functions of the class or module, and you can filter them by their names, e.g.:
 - [python] from pprint import pprint --> use pprint for readability of the above output
 - [python] inspect.getmembers(<Class/Func>, lambda x: inspect.isfunction(x) and x.__name__.startswith('get_'))
 - [Python Debug Mode] 'next', 'continue' (known), 'return' (step-out of the function) ↩️, 'h' (for help), 'h continue' (help on 'continue')
 - [Windows Emoji] 'Window KEY' + '.'
 - Create single-file executable: [Indently Vid](https://www.youtube.com/watch?v=bqNvkAfTvIc)
 -- Ruff related:
 - [Ruff] basic documentation: https://docs.astral.sh/ruff/installation/
 - [Ruff] my general ruff configuration file sits under: 'C:\Users\shaib\AppData\Roaming\ruff\pyproject.toml' (with some added features)
 - [Ruff] from cmd: >> ruff check --show-settings (to see all settings, under: linter.rules.enabled)
 - [Ruff] can also filter rules by cmd: >> ruff check --show-settings | findstr "(\*)"  # tbd without the "\"
 - [Windows] 'Ctrl+Shift+Esc' (to open the task manager directly)
 - [Sublime] 'Ctrl+Alt+/' ("Beyond Compare" diff tool package)
 - [Sublime] 'F10' (quick file name search w/ regex)
 - [Streamlit] 'st.cache_data' (to cache data in Streamlit apps) TBD
 - [Streamlit] streamlit run main.py (to run the Streamlit app) 'Verified'
 - [Streamlit] streamlit config show (to show the current Streamlit configuration)
 - [Streamlit] streamlit config set server.port 8502 (to set the port for the Streamlit app)
 - [Streamlit] streamlit config set server.headless true (to run the Streamlit app in headless mode)
 - [Streamlit] streamlit config set global.developmentMode false (to disable development mode)


## My most useful VIM commands:
 - [linux vim] ':set nu' (to show line numbers)
 - [linux vim] ':set nonu' (to hide line numbers)
 - [linux vim] ':set list' (to show hidden characters like spaces, tabs, etc.)
 - [linux vim] ':set nolist' (to hide the hidden characters)
 - [linux vim] 'dd' (to delete the current line)
 - [linux vim] 'yy' (to copy the current line)
 - [linux vim] 'p' (to paste the copied line below the current line)
 - [linux vim] 'P' (to paste the copied line above the current line)
 - [linux vim] 'u' (to undo the last change)
 - [linux vim] 'Ctrl+r' (to redo the last change)
 - [linux vim] ':wq' (to save and exit the file)
 - [linux vim] ':q!' (to exit the file without saving)
 - [linux vim] ':e filename' (to edit a file)


## My most useful GIT commands:

 - git config --get-regexp ^alias (check on your pre-configured aliases)
 	- [YouTube: More Tips](https://www.youtube.com/watch?v=aolI_Rz0ZqY&t=437s)
 - also find my git aliases under: 'C:\Users\shaib\.gitconfig' (or ~/.gitconfig), also copied to the 'Tips' folder


## Abbreviation:
	'README.md' -> md for Markdown
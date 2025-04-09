import re

with open ('./Input/re_input_file.txt', 'r') as f:
    content = f.read()




date_pattern = r'\d*/\d*/\d*'
# date_pattern = r'([0-9]{4}-[0-9]{2}-[0-9]{2})'
date = re.search(date_pattern, content)
# date = re.search(date_pattern, content).group() # note that w/o the .group() it will be gybrish! (group returns string)

date.group()
#'21/02/2014'


dates = re.findall(date_pattern, content)
# ['21/02/2014', '04/4/2020']


name_pattern = r'(.*my name is )(\w*)(.*)' # this is the important staff: my name is shai end of important staff  # to exxtract "shai"

name = re.search(name_pattern, content).group(2)
# shai


my_text = 'this-is-how-we-do-business'
my_text.replace('-', ' ') 
# 'this is how we do business'

my_text = 'is it true what they say about Shai over and over again?'

# arr_str = re.sub(r"(.*)(2nd)(.*)", r"\1,\2,\3", my_text) # old -> re.sub(r"([-]*\d+[\.]*\d*)\s+([-]\d*[\.]*\d*)", r"\1,\2", arr_str)

re.sub(r"(is it true what they say about) (Shai) (over and over again)", r"\1: Hadas \3?", my_text)
# 'is it true what they say about: Hadas over and over again?'


# -------


print('\nNew Code:\n')


#Find Spider-Man, Spider Man, Spiderman, SPIDER-MAN, etc. (case insensitive)
import re
dailybugle = 'Spider-Man Menaces City!'
pattern = r'spider[- ]?man'
if re.match(pattern, dailybugle, re.IGNORECASE):
    print(dailybugle)


# ----------------------


#Match dates formatted like MM/DD/YYYY, MM-DD-YY,... (data unpack)
import re
date1 = '12/30/1969' # or 12-30-1969
date2 = '12/30/69'
pattern = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(\d\d)?)$')
# pattern = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(?:\d\d)?)$')
# pattern = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(\d\d)+)$') # error
# pattern = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(?:\d\d))$') # error
match = pattern.match(date1)
if match:
    month1 = match.group(1) #12
    day1 = match.group(2) #30
    year1 = match.group(3) #1969

match = pattern.match(date2)
if match:
    month2 = match.group(1) #12
    day2 = match.group(2) #30
    year2 = match.group(3) #69


print(f"\nDate1:")
print(f"month = {month1}\nday = {day1}\nyear = {year1}\n")

print(f"\nDate2:")
print(f"month = {month2}\nday = {day2}\nyear = {year2}\n")



# ----------------------


# Example 19. Simple substitution
# Convert <br> to <br /> for XHTML compliance
import re
text = 'Hello world. <br>'
pattern = re.compile(r'<br>', re.IGNORECASE);
repl = r'<br />'
text = pattern.sub(repl,text)
print(text)
# Hello world. <br />

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


my_text1 = 'this-is-how-we-do-business'
my_text2 = 'this_is_how_we_do_business'
my_text1.replace('_', ' ').replace('-', ' ') # return str -> replacing '_' followed by '-'
my_text2.replace('_', ' ').replace('-', ' ') # return str -> replacing '_' followed by '-'
# 'this is how we do business' (returned, yet source remains the same)

# more powerful
re.sub("[-_]"," ",my_text1) # return str -> replacing '_' followed by '-'
re.sub("[-_]"," ",my_text2) # note that we're using the same patttern!
# 'this is how we do business' (returned, yet source remains the same)



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



# ----------------------------------------------------------------------------------------------
##############################################################################################
# ----------------------------------------------------------------------------------------------


# finding any string that repeats itself right after (with white space between )
import re
my_string = "hello python   python koko smile kneighbor, koko bore bore unmbrella hello"
# my_string = "python     python koko koko smile kneighbor, bore bore unmbrella"
pattern = r'(\w+)\s+\1' # \1 meanin that the first group is repeating itself (followed by)

matches = re.findall(pattern, my_string)



my_string2 = "python     python koko  smile koko kneighbor, bore bore unmbrella"
pattern = r'(\b\w+\b).*\1' # \1 meanin that the first group is repeating itself (anywhere in the text)

matches2 = re.findall(pattern, my_string2)



# -----------------------------


# from harvard, URL: https://www.youtube.com/watch?v=nLRL_NcnK-4&t=35810s

import re
name = input("What's your full name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    # (last, first) = matches.groups() # we return tuple, so it works the same way
    name = f"{first} {last}"
print(f"hello {name}")



    ###
    ###
    ###
###########
 #       #
  #     #
   #   #
    ###


# same as:
import re
name = input("What's your full name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    first = matches.group(1)
    last = matches.group(2)
    name = f"{first} {last}"

print(f"hello {name}")


    ###
    ###
    ###
###########
 #       #
  #     #
   #   #
    ###


# same as:
import re
name = input("What's your full name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name): # Worlog operation?
    first = matches.group(1)
    last = matches.group(2)
    name = f"{first} {last}"

print(f"hello {name}")



# ------------------------------------------
#
# ------------------------------------------


# url = input("URL: ").strip()   # e.g. "https://twitter.com/davidjmalan"
# let's extract the username from the string!

url = "https://twitter.com/davidjmalan" #(instead of inputing the string)

# before moving to the stronger regex tool
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")


    ###
    ###
    ###
###########
 #       #
  #     #
   #   #
    ###


import re
url1 = "https://twitter.com/davidjmalan" #(instead of inputing the string)
url2 = "http://www.twitter.com/davidjmalan" #(instead of inputing the string)
url3 = "twitter.com/davidjmalan" #(instead of inputing the string)
username = re.sub(r"https://twitter\.com/", "", url1) # basic
username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url2) # basic +
username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url3) # basic +
print(f"Username: {username}")



    ###
    ###
    ###
###########
 #       #
  #     #
   #   #
    ###

import re
url1 = "https://twitter.com/davidjmalan" #(instead of inputing the string)
url2 = "http://www.twitter.com/davidjmalan" #(instead of inputing the string)
url3 = "twitter.com/davidjmalan" #(instead of inputing the string)
url4 = "twitter.org/davidjmalan" #(instead of inputing the string)
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.*)$", url1, re.IGNORECASE):
    print(f"Username: {matches.group(3)}") # Username: davidjmalan

# using the non-capturing reg-ex option:
# (?:...)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.*)$", url1, re.IGNORECASE):
    print(f"Username: {matches.group(1)}") # Username: davidjmalan

# now also enabling both options: '.com' & '.org'
# (?:...)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.(?:com|org)/(.*)$", url4, re.IGNORECASE):
    print(f"Username: {matches.group(1)}") # Username: davidjmalan  (note that using the (?:...) operator enables to ignore it as a group and look only for the relevants groups,  (1) in our case)






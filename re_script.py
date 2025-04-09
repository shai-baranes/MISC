import re

with open ('./re_input_file.txt', 'r') as f:
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
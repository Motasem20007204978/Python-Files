
import re

s = 'Hello World!'

print(re.match(r'^Hello', s))
# ^ indicates on that h character must be at the first followed by ello

s = 'X  :'
print(re.search(r'^x*:', s, re.IGNORECASE))#ignore case of letter
# if string starts with X followed by 0 or more characters from any type even white space and ends with :
#the output is as <re.Match object; span=(0, 4), match='X  :'> when using rawstring

s = 'Hello: World!'
result = re.search(r'^H\S+:', s)# if starts with H followed by one or more non white space character and ends with :
print(result.groups())#to return checked string
# ^ means that the line must begin with H
#search stops when pattern checking is done

s = 'search cat or dog'
re.search(r'cat|dog', s)#unless cat is exist, search about dog
re.findall(r'cat|dog', s)#extract oll cat and dog words

s = 'my name is motasem 2000 and age is 22 month 3 day 13'
digits = re.findall('[0-9]+', s)# extract numbers with one ore more digits into list
print(digits)

print(re.findall('[aeoui]', s))# extract all characters in the pattern

email = 'From motasemalmobayyed@gmail.com to medium.com'
print(re.findall('^From\s+(\S+@[a-z.]+com)', email))
#same
print(re.findall('[\w.-]+@[a-z\.]', email))# backward slash for what after it
# \S+@[a-z]+ means that one or more non space chracter before @, and one or more characters in range lettrs from a to z after @, ends with .com
#extract only what matches the pattern between parantheses
#\s+ means one or more space before email

print(re.findall('@([a-z\.]+)', email)[0], 'is the domain of the email')
#[^ ] = \S, \. to search about actual . character
#[^a-zA-Z0-9 ] to avoid the pattern (range a-z, A-Z, 0-9 and whitespaces)

s = 'From : motasem :'
print(re.findall('^F.+:', s))# looks at latest : even if there is white space
print(re.findall('^F.+?:', s))# looks at first :
#? means stopping at the first case that matches next of it in pattern, regardless wether or not what before it matches
#تبحث عن مايطابق اللذي بعدها حتى لو ماقبلها لم يطابق شيء

s = 'moey in my wallet is $10.55'
print(re.search('\$[0-9.]+', s))#\$ to match actual $ character
#as
print(re.search('[0-9.]+$', s))# because the number in the last
# $ means the last character must be as pattern that is before it

#\w search about any alphanumeric character
#\d for digit characters


string = 'hello world abuanwar as motasem'
result = re.search('([a-z]{5})', string, re.I)# repeat pattern 5 times only
result = re.findall('(\b[a-z]{5}\b)', string, re.I)# find only words that have just 5 characters
result = re.findall('(\b[a-z]{5})', string, re.I)# get first 5 characters of each word that specify pattern
result = re.findall('([a-z]{5}\b)', string, re.I)# get last 5 characters of each word that specify pattern
result = re.findall('[a-z]{5,10}', string, re.I)# open ended range, minimum 5 charcters, maximum 10 characters
# if the words consist of 5 or more characters 

#split with re
string = 'hello, everyone. how are you? my name is motasem'
result = re.split(r'[,?.]', string)#split into multiple sentences according to where punctuations
print(result)


s = 'received email for motasem_mobayyed.contact-me@gmail.edu.ps'
pattern = '[\w.-]+@[a-z\.]+'
replaced_string = '[MOTASEM ALMOBAYYED]'
pattern = r'[\w.-]+@[a-z\.]+'
result = re.sub(pattern, replaced_string, s)
#replace the specified string with replaced_string


result = re.sub(r'^([\w.-]*), ([\w.-]*)$', r'\2 \1', 'mobayyed, motasem')
#replace first with second and second with first

def rearranage_name(name:str):
    result = re.search(r'^(\w+), (\w+)$', name)
    if not result:
        return name
    return f'{result[2]}, {result[1]}'


from click import echo,getchar,prompt
from datetime import datetime
from string import digits
from os.path import basename

def generate(arr, lenofpass, pass_string, lenofchoicesrange, listofpass):

	if (lenofpass == 0):
		# store it
		listofpass.append(str(pass_string))
		return
	
	# iterate through the array
	for j in range(0, lenofchoicesrange):
		password = pass_string + arr[j]
		generate(arr, lenofpass - 1, password, lenofchoicesrange, listofpass)

	return

lenofpass = prompt(text='\nenter length of password',type=int)

digitsarray = list(digits)

listofpass = []

print('\nstart generating...')

start_time = datetime.now()
generate(digitsarray, lenofpass, "", len(digitsarray), listofpass)
end_time = datetime.now()

print(f'\nend generating {len(listofpass)} passwords in {(end_time-start_time).microseconds/1000} milliseconds!')

__location__ = __file__.split(basename(__file__))[0]

print('\nstart writing in file....')
with open(__location__+'passwords.txt','w') as wf:
	for ele in listofpass:	
		wf.writelines(ele+'\n')
	wf.flush()

print(f'\nwriting finished and file saved at {__location__}passwords.txt')
print('\n\n-----------------------------------------------')

password = prompt(f'\nenter password from {lenofpass} digits ', type=int)

stime = datetime.now()

with open(__location__+'passwords.txt','r') as of:
	passwordslist = of.read().split('\n')
	of.close()
isexists = str(password) in passwordslist

etime = datetime.now()

searching_time = (etime-stime).microseconds/1000

print(f'\nsearching time is {searching_time} milliseconds!\n')
if isexists:	
    print('entered password is exists')
else:
	print(f'password digits is less or more than {lenofpass}!')


print('\n-------------@copyrights----Author: Motasem Al-Mobayyed  20181931-------------------\n')

echo('\npress any key to exit',nl=False)
getchar();echo()
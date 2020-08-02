import os
from time import sleep
import pyperclip

debugmode=0

def debug(var):
	if debugmode == True:
		print(var)
		input('<>')

tmp_file=open('.tmp_atxt','r')
tmp_info=tmp_file.read()
tmp_info.strip('\n')
tmp_info=tmp_info.split('\n')
debug(tmp_info)
ali_file_name=tmp_info[0]
debug(ali_file_name)
file_seg=0
file_args=0
if len(tmp_info) > 1:
	file_seg=tmp_info[1]
	if len(tmp_info) > 2:
		file_args=tmp_info[2]
ftype = (ali_file_name.split('.'))
debug(ftype)
if ftype[1] == 'aliraw':
	file=open('.'.join(ftype),'r')
	file=file.read().strip().split('\n')
	title=file[0]
	descrip=file[1]
	descrip=descrip[1:]
	print('-----DESCRITPION:-----')
	print(descrip)
	print('----------------------')
	sleep(2)
	file=file[2:]
	if title == '<ALIAS>':
		bash_aliases=open('~/.bash_aliases','a')
		for line in file:
			bash_aliases.write(line)
	elif title == '<COPY>':
		file='\n'.join(file)
		print('--------------COPIED:---------------')
		print(file)
		pyperclip.copy(file)
	elif title == '<RUN>':
		runfile=open('.tmp_runfile','w')
		runfile.write('\n'.join(file))
		os.system('bash .tmp_runfile')
		os.system('rm .tmp_runfile')
elif ftype[1] == 'atxt':
	file=open('.'.join(ftype), 'r')
	file=file.read().srtip().split('\n')
	#More soon!

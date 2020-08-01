import os
from time import sleep
import pyperclip
tmp_file=open('.tmp_atxt','r')
tmp_info=tmp_file.read()
tmp_info.split('\n').strip('\n')
ali_file_name=tmp_info[0]
if len(tmp_info) > 1:
	file_seg=tmp_info[1]
	if len(tmp_info) > 2:
		file_args=tmp_info[2]
		file_args.split(':')
ftype = (ali_file_name.split('.'))
if ftype[1] == 'aliraw':
	file=open(ftype[0],'r')
	file=file.read().strip().split('\n')
	title=file[0]
	descrip=file[1]
	descrip=descrip[1:]
	print(descrip)
	sleep(4)
	file=file[2:]
	if title == '<ALIAS>':
		for line in file:
			os.system('echo \"'+line+'\" >> ~/.bash_aliases')
	elif title == '<COPY>':
		file='\n'.join(file)
		print('--------------COPIED:---------------')
		print(file)
		pyperclip.copy(file)
	elif title == '<RUN>':
		os.system('echo \"'+file+'\" > .tmp_runfile')
		os.system('bash .tmp_runfile')
		os.system('rm .tmp_runfile')
elif ftype[1] == 'atxt':
	#Do everything else

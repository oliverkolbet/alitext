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
	descrip=file[2]
	descrip=descrip[1:]
	print(descrip)
	sleep(4)
	if title == '<ALIAS>':
	elif title == '<COPY>':
	elif title == '<RUN>':

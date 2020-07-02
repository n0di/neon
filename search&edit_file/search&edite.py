
from __future__ import print_function

import os, fnmatch
import io

total_addresses = []
total = []
folder = []
search_file = 'you_file'

for i in os.walk('/dir'):
    folder.append(i)

for address, dirs, files in folder:
    for file in files:
        if search_file in files:
        	total_addresses.append(address+'/'+file)
for i in total_addresses:
	if search_file == i[-13::]:
		total.append(i)

word = u"tex_which_you_need_to_look_for"
with io.open(f'{total[0]}') as file:
    for line in file:
        if word in line:
        	w = open('file.txt', 'w')
        	w.write(f'{total[0]} \n{line}')
        	w.close
        elif word not in line:
        	opf = open(f'{total[0]}', 'a')
        	opf.write(f"you_write_text")
        	opf.close
        	w = open('success.txt', 'w')
        	w.write(f'{total[0]} \n')
        	w.close

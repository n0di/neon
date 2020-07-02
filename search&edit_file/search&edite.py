
from __future__ import print_function

import os, fnmatch
import io

tt = []
ttt = []
folder = []
f = 'wp-config.php'

for i in os.walk('/var/www/'):
    folder.append(i)

for address, dirs, files in folder:
    for file in files:
        if f in files:
        	tt.append(address+'/'+file)
for i in tt:
	if f == i[-13::]:
		ttt.append(i)

# print(ttt[0])

word = u"define('WP_MEMORY_LIMIT', "
with io.open(f'{ttt[0]}') as file:
    for line in file:
        if word in line:
        	w = open('file.txt', 'w')
        	w.write(f'{ttt[0]} \n{line}')
        	w.close
        elif word not in line:
        	opf = open(f'{ttt[0]}', 'a')
        	opf.write(f"define('WP_MEMORY_LIMIT', '128M');")
        	opf.close
        	w = open('success.txt', 'w')
        	w.write(f'{ttt[0]} \n')
        	w.close

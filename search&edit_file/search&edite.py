from __future__ import print_function

import os, fnmatch
import io

total_addresses = []
total = []
text = 'you_write_text'
word = "tex_which"
search_file = 'file'
folder = []
   
for i in os.walk('/dir'):
    folder.append(i)

for address, dirs, files in folder:
    for file in files:
        if search_file in files:
            total_addresses.append(address+'/'+file)

for i in total_addresses:
    if search_file == i[-13::]:
        total.append(i)

t_text = open(f'{total_addresses[0]}').read()
t_text = t_text.split(' \n')

for line in list(t_text):

    if word in line:
        w = open('file.txt', 'w')
        w.write(f'{total_addresses[0]} \n{line}')
        w.close

    elif word not in line:
        opf = open(f'{total_addresses[0]}', 'a')
        opf.write(text)
        opf.close
        w = open('success.txt', 'w')
        w.write(f'{total[0]} \n')
        w.close

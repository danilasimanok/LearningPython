# -*- coding: UTF-8 -*-

import sys

f = open(sys.argv[1], "r")
s = 'Че пялишься?'
while not "-----------------------------------\n" in s:
	s = f.readline()
s = f.readline()
mark = float(s.split(' ')[6].split('/')[0])

sosi = open("sosi", "r")
content = sosi.read().split('\n')
i = -1
if mark == -10.0:
	i = 0
elif mark <= -8.0:
	i = 1
elif mark <= -6.0:
	i = 2
elif mark <= -4.0:
	i = 3
elif mark <= -2.0:
	i = 4
elif mark <= 0.0:
	i = 5
elif mark <= 2.0:
	i = 6
elif mark <= 4.0:
	i = 7
elif mark <= 6.0:
	i = 8
elif mark <= 8.0:
	i = 9
elif mark <= 10.0:
	i = 10
print(content[i])

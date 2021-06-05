from time import sleep
from os import system
micro = 0
sec = 0
min = 0
hour = 0
day = 0
while True:
	system("clear")
	sleep(0.1)
	micro += 1
	print('day: ',day,' hour: ',hour,' min: ',min,' sec: ',sec,' microsec: ',micro)
	if micro == 10:
		micro = 0
		sec += 1
		print('day: ',day,' hour: ',hour,' min: ',min,' sec: ',sec,' microsec: ',micro)
	if sec == 60:
		sec = 0
		min += 1
		print('day: ',day,' hour: ',hour,' min: ',min,' sec: ',sec,' microsec: ',micro)
	if min == 60:
		min = 0
		hour += 1
		print('day: ',day,' hour: ',hour,' min: ',min,' sec: ',sec,' microsec: ',micro)
	if hour == 24:
		hour = 0
		day += 1
		print('day: ',day,' hour: ',hour,' min: ',min,' sec: ',sec,' microsec: ',micro)


#!/usr/bin/python
import random
geheimnis = random.randit(1, 99)
tip = 0
versuche = 0
print "AHOI! Ich bin der berüchtigte Kapitän Hook und habe ein "Geheimnis"!"
print "Es ist eine Zahl zwischen 1 und 99. Du hast 6 Versuche."
while tipp != geheimnis and versuche < 6:
	tipp = input ("Was rätst du?")
	if tipp < geheimnis:
		print "Zu niedrig, du Landratte!"
	elif tipp > geheimnis:
		print "Zu hoch, du Leichtmatrose!"

	versuche = versuche + 1

if tipp == geheimnis:
	print "Ha! Du hast es! Hast mein Geheimnis erraten!"
else:
	print "Alle Versuche verbraucht! Mehr Glück beim nächsten Mal!"
	print "Die Geheimnis war ", geheimnis
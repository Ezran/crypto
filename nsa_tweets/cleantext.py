import fileinput

gramlen = 4

cleantext = ''
quadgram = dict()

for line in fileinput.input():
	line = line.lower()
	cleantext = cleantext + ''.join(e for e in line if e.isalnum() and not e.isdigit())

for i in range(0,len(cleantext)-gramlen):
	q = cleantext[i:i+gramlen]
	if quadgram.has_key(q):
		quadgram[q] += 1
	else:
		quadgram[q] = 1
f = open('latin_quadgrams.txt', 'w')
for x in sorted(quadgram, key=quadgram.get, reverse=True):
	outst = str(x) + ' ' + str(quadgram[x]) + '\n'
	f.write(outst) 

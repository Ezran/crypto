import string
import operator

inp = "NKI 3: S RKFO NOMSNON DY QY RKBNOB YX DRO REWKXC. DRSC CRYEVN KVVYG EC DY PSXN DRO SXDOVVSQOXD CZOMSWOX YP DRO REWKXC. DROI KBO DRO YXOC GO XOON. S RKFO QYXO YEDCSNO DRO LYH K LSD ROBO, PSBCD S ECON MYNSXQ DBKXCVKDYBC, XYG SW ECSXQ DRSXQC DRKD KBO FOBI MYWZVSMKDON."

inp = inp.lower()

def rot(n,inp):
	outp = list()
	for i in inp:
		if i >= 'a' and i <= 'z':
			base = ord('a')
			new = (ord(i) - base + n) % 26 + base
			outp.append(chr(new))
		else:
			outp.append(i)
	return "".join(outp)

inp.lower()
print "=INPUT " + inp + " "
for n in range(1,26):
	print "ROT[" + str(n) + "] " + rot(n,inp)



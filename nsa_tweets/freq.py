from collections import defaultdict

inp = "pjbbfcklerfebjppjjlboumcuppelqpfezbjruoqlerdjbcuddbukulfjojprfebjbjzfrtmloupraublxpepkurtppdbjcbelfrfebkj"

def freq(inp):
	count = defaultdict(int)
	for i in inp:
		if count.has_key(i):
			count[i]+=1
		else:
			count[i] = 1
	return count


print "Letter Frequency"
f_count = freq(inp)
for x in sorted(f_count, key=f_count.get, reverse=True):
	print x,':',f_count[x]
	

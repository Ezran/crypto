import binascii

f = open('201406202100', 'r')
g = open('201406202100_bytes', 'w')
text = ''.join(f.readline().split())
g.write(binascii.unhexlify(text))

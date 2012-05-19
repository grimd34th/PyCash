import time
from blake import BLAKE as BLAKEpy

BLAKE = BLAKEpy

print('')
print('    simple timing test:')

def time_it(hashsize, iter):
	global qq
	qq = 0
	t0 = time.time()
	for i in range(iter):
		digest = BLAKE(hashsize).digest(b'\x00')   # hash a single null byte
		t1 = time.time()
		template = '    %8d iterations of single-block BLAKE-%d took %8.6f seconds'
		#print(template % (iter, hashsize, (t1-t0)))
		qq = qq + (t1-t0)
        
iterations = [10000]
hashsizes  = [256,512]
for hashsize in hashsizes:
	for iter in iterations:
		time_it(hashsize, iter)
		print '    Total Operation Time For {0} bit: {1}'.format(hashsize,(qq/60/60))
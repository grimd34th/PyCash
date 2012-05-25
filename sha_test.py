import time, hash.sha

print('')
print('    simple timing test:')

def time_it(iter):
	global qq
	qq = 0
	t0 = time.time()
	for i in range(iter):
		digest = hash.sha.hash(b'\x00')   # hash a single null byte
		t1 = time.time()
		template = '    %8d iterations of single-block BLAKE-%d took %8.6f seconds'
		#print(template % (iter, hashsize, (t1-t0)))
		qq = qq + (t1-t0)
        
iterations = [10000]
for iter in iterations:
	time_it(iter)
	print '    Total Operation Time For Operation: {0}'.format((qq/60/60))
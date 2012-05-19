import mcrpc
conn = mcrpc.mcrpc('107.21.44.237:8556')

info = conn.getinfo()

print "Block Count: {0}  Difficulty: {1}  Network Hashrate: {2}\nCurrent Network Coincount: {3}".format(info['blocks'],info['difficulty'],(float(info['network_hashrate'])/1000),(float(conn.getinfo()['solidcoins_created'])/10000))
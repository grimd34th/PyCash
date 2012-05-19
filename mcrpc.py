import jsonrpc
Q = []
class mcrpc:
		def __init__(self,details):
			global Q
			Q = details.split(':')
			print "Set Microcash Node: {0}:{1}".format(Q[0],Q[1])
			print "Beta microcash Python connector brought to you by D34TH\nthank jgarzik (Jeff Garzik) for the jsonrpc python authserviceproxy\n"
		def getinfo(self):
			return jsonrpc.ServiceProxy(("http://thin:client@{0}:{1}".format(Q[0],Q[1]))).sc_getinfo()
		def getbalance(self,addr):
			return jsonrpc.ServiceProxy(("http://thin:client@{0}:{1}".format(Q[0],Q[1]))).sc_getbalance(addr)
		def gethistory(self,addr):
			return jsonrpc.ServiceProxy(("http://thin:client@{0}:{1}".format(Q[0],Q[1]))).sc_gethistory(addr,0)
		def sendtransaction(self,params):
			print "Not Yet completed, contact d34th with any transaction params you have"
			#return jsonrpc.ServiceProxy(("http://thin:client@{0}:{1}".format(Q[0],Q[1]))).sc_sendtransaction(params)
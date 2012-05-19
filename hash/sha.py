from Crypto.Hash import SHA256 as sha256

def hash(msg):
	sha = sha256.new()
	sha.update(msg)
	return sha.hexdigest()
from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:4242')
s.twice(2)
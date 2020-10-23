from xmlrpc.server import SimpleXMLRPCServer


s = SimpleXMLRPCServer(("",4242))

def twice(x):
    return x*2

s.register_function(twice)
s.serve_forever()
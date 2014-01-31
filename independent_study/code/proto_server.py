import jsonrpc
from simplejson import loads
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
        jsonrpc.TransportTcpIp(addr=("10.2.4.81", 8080)))

result = loads(server.parse("Hello world.  It is so beautiful"))
print "Result", result

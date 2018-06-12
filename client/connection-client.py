import socket, pickle

def send(data, ip):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.connect((input("IP Address of server: "), 4000))
	data = pickle.dumps(data)
	server.send(data)
	data = server.recv(1024)
	data = pickle.loads(data)
	return data
  	server.close()

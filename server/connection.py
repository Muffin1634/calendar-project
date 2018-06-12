import socket, select, pickle, server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 4000))
server.listen(5)

clients = []
while True:
	Connections, wlist, xlist = select.select([server], [], [], 0.05)

	for Connection in Connections:
		client, Informations = Connection.accept()
		clients.append(client)

	clientsList = []
	try:
		clientsList, wlist, xlist = select.select(clients, [], [], 0.05)
	except select.error:
		pass
	else:
		if __name__ == "__main__":
			for clientInList in clientsList:
				data = clientInList.recv(1024)
				data = pickle.loads(data)
				server.parse(data)
			#data = "Welcome"
			#data = pickle.dumps(data)
			#clientInList.send(data)

clientInList.close()
server.close()

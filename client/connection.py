import socket, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((input("IP Address of server: "), 4000))

def send(data):
	data = pickle.dumps(data)
	server.send(data)
if __name__ == "__main__":
	while True:
		send(input())
		# data = server.recv(1024)
		# data = pickle.loads(data)
		# print(data)

server.close()

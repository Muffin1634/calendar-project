import connection

while True:
  data = input(">> ")
  connection.send(data)

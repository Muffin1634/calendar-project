import connection

commands = ["upload","download","calendar","save","move","rename"]

def returnError():
  pass

while True:
  data = input(">> ")
  testdata = data.split()
  if testdata[0] in commands:
    connection.send(data)
  else:
    returnError()

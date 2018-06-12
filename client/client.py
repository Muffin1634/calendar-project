import connection

commands = ["upload","download","calendar","save","move","rename"]

def sendwithresponse(data):
    testdata = data.split()
    if testdata[0] in commands:
        return connection.send(data)
    else:
        return("error")

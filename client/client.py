import connection_client

commands = ["upload","download","calendar","save","move","rename"]

def sendwithresponse(data, ip):
    testdata = data.split()
    if testdata[0] in commands:
        return connection_client.send(data, ip)
    else:
        return("error")

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((str(input('IP address of server> ')), 1234))

if client.recv(1024).decode() == 'hello':
    # handle handshaking
    client.send('hi'.encode())
    print('finished handshake')

else:
    print('connection failed')
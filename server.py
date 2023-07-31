import socket

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 1234

host.bind((socket.gethostname(), PORT))

print(f'Listening on {socket.gethostbyname(socket.gethostname())}:{PORT}')

while True:
    host.listen(1)
    client, address = host.accept()
    print(f'Connection from {address[0]}')
    client.send('hello'.encode())
    if client.recv(1024).decode() == 'hi':
        # finished handshake
        print(f'Finished handshake with {address[0]}')
    else:
        print(f'Failed handshake with {address[0]}')
        client.close()
        continue
    
    client.close()
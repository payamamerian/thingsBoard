import socket

def create_tcp_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local host and a port
    host = '185.167.96.79'  
    port = 8053
    server_socket.bind((host, port))

    # Start listening for connections
    server_socket.listen(5)

    print("Server listening on", host, ":", port)

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print('Got a connection from', addr)

        try:
            while True:
                # Receive data from client
                data = client_socket.recv(1024)
                if not data:
                    break  # No more data, break out of the loop

                # Print received data
                print('Received:', data.decode())

                # Optionally, you can send a response back to the client
                # client_socket.send('Message received'.encode())

        finally:
            # Close the connection
            client_socket.close()

if __name__ == '__main__':
    create_tcp_server()

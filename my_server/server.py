# server.py
import socket
from df703 import DF703  # Importing the DF703 class

def create_tcp_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local host and a port
    host = '185.167.96.79'  # Specific IP address
    port = 8053
    server_socket.bind((host, port))

    # Start listening for connections
    server_socket.listen(5)
    print("Server listening on", host, ":", port)

    # Accepting a new connection
    client_socket, addr = server_socket.accept()
    print("Got a connection from", addr)

    while True:
        # Receiving data from the client
        data = client_socket.recv(1024)
        if not data:
            break  # Break the loop if no data is received
        print("Received data before decode:", data)

        # Decoding and processing the data
        try:
            decoded_data = DF703.parse_data_DF703(data)
            print("Decoded data:", decoded_data)
        except Exception as e:
            print("Error processing data:", e)

    # Closing the client connection
    client_socket.close()

if __name__ == "__main__":
    create_tcp_server()

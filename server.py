import socket
import subprocess
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

                # Decode the received data using DF703 class
                decoded_data = DF703.parse_data_DF703(data.decode())

                # Prepare the curl command
                curl_command = f'curl -v -X POST http://185.167.96.79:8080/api/v1/l9ollIobraqrDkjy4cEL/telemetry --header Content-Type:application/json --data \'{decoded_data}\''
                subprocess.run(curl_command, shell=True)

        finally:
            # Close the connection
            client_socket.close()

if __name__ == '__main__':
    create_tcp_server()

import subprocess
import json
from df703 import DF703  # Importing the DF703 class
from daemon import DaemonContext
from sys import stdout, stderr

def create_tcp_server():
    while True:  # Outer loop to restart the server on failure
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Add this line
            host = '185.167.96.79'
            port = 8053
            server_socket.bind((host, port))
            server_socket.listen(5)
            print("Server listening on", host, ":", port)

            while True:
                client_socket, addr = server_socket.accept()
                print('Got a connection from', addr)

                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    # Assuming DF703.parse_data_DF703 can handle binary data directly
                    decoded_data = DF703.parse_data_DF703(data)
                    
                    # Convert the decoded data to JSON string if it's a dictionary
                    if isinstance(decoded_data, dict):
                        json_data = json.dumps(decoded_data)
                    else:
                        json_data = str(decoded_data)

                    curl_command = f"curl -v -X POST http://185.167.96.79:8080/api/v1/l9ollIobraqrDkjy4cEL/telemetry --header 'Content-Type:application/json' --data '{json_data}'"
                    subprocess.run(curl_command, shell=True, check=True)

        except Exception as e:
            print(f"An error occurred: {e}")
            server_socket.close()  # Close the server socket before restarting

if __name__ == '__main__':
    with DaemonContext(stdout=stdout, stderr=stderr):
        create_tcp_server()
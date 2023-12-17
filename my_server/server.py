import logging
import socket
import subprocess
import json
import time
from df703 import DF703

# Set up logging to capture both standard output and errors
logging.basicConfig(filename='server.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

def create_tcp_server():
    while True:  # This loop ensures the server is always attempting to run
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            host = '185.167.96.79'
            port = 8053
            server_socket.bind((host, port))
            server_socket.listen(5)
            logging.info("Server listening on %s : %s", host, port)

            while True:  # This loop handles client connections
                try:
                    client_socket, addr = server_socket.accept()
                    logging.info('Got a connection from %s', addr)

                    while True:  # This loop handles data reception
                        data = client_socket.recv(1024)
                        if not data:
                            break

                        decoded_data = DF703.parse_data_DF703(data)
                        logging.debug('Received data: %s', data)
                        logging.debug('Decoded data: %s', decoded_data)

                        if isinstance(decoded_data, dict):
                            json_data = json.dumps(decoded_data)
                        else:
                            json_data = str(decoded_data)

                        curl_command = f"curl -v -X POST http://185.167.96.79:8080/api/v1/l9ollIobraqrDkjy4cEL/telemetry --header 'Content-Type:application/json' --data '{json_data}'"
                        subprocess.run(curl_command, shell=True, check=True)

                except Exception as client_error:
                    logging.error("Client handling error: %s", str(client_error))
                    # Optional: You can also close the client socket here if needed
                    # if client_socket:
                    #     client_socket.close()

        except Exception as server_error:
            logging.error("Server error: %s", str(server_error))
            time.sleep(1)  # Short delay before trying to restart the server

        finally:
            if server_socket:
                server_socket.close()

if __name__ == '__main__':
    create_tcp_server()

# Run Command: nohup python3 server.py >> output.log 2>&1 &

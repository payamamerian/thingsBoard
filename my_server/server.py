import logging

# Set up logging
logging.basicConfig(filename='server.log', level=logging.DEBUG)

import socket
import time
from df703 import DF703
from daemon import DaemonContext
from sys import stdout, stderr

def create_tcp_server():
    server_socket = None
    while True:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            host = '185.167.96.79'
            port = 8053
            server_socket.bind((host, port))
            server_socket.listen(5)
            logging.info("Server listening on %s : %s", host, port)

            while True:
                client_socket, addr = server_socket.accept()
                logging.info('Got a connection from %s', addr)

                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    # Assuming DF703.parse_data_DF703 can handle binary data directly
                    decoded_data = DF703.parse_data_DF703(data)
                    logging.debug('Received data: %s', data)
                    logging.debug('Decoded data: %s', decoded_data)

        except Exception as e:
            logging.error("An error occurred: %s", e)
        finally:
            if server_socket:
                server_socket.close()
            time.sleep(1)

if __name__ == '__main__':
    with DaemonContext(stdout=stdout, stderr=stderr):
        create_tcp_server()